%global _hardened_build 1

# FIXME non-standard directory for storing *.so objects
%{?filter_setup:
%filter_provides_in %{_libdir}/ejabberd/priv/lib/.*\.so$
%filter_setup
}
%{expand: %(NIF_VER=`rpm -q erlang-erts --provides | grep --color=no erl_nif_version` ; if [ "$NIF_VER" != "" ]; then echo %%global __erlang_nif_version $NIF_VER ; fi)}
%{expand: %(DRV_VER=`rpm -q erlang-erts --provides | grep --color=no erl_drv_version` ; if [ "$DRV_VER" != "" ]; then echo %%global __erlang_drv_version $DRV_VER ; fi)}


# Currently, hevea available only in Fedora
%if 0%{?fedora}
%global _with_hevea 1
%endif


Name:           ejabberd
Version:        14.07
Release:        6%{?dist}
Summary:        A distributed, fault-tolerant Jabber/XMPP server

Group:          Applications/Internet
License:        GPLv2+
URL:            http://www.ejabberd.im/
%if 0%{?el7}%{?fedora}
VCS:		scm:git:https://github.com/processone/ejabberd.git
%endif
Source0:	https://github.com/processone/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Source2:        ejabberd.logrotate

# Support for systemd
Source4:	ejabberd.service
Source5:	ejabberd.tmpfiles.conf

# PAM support
Source9:        ejabberdctl.pam
Source11:       ejabberd.pam

# polkit support
Source12:	ejabberdctl.polkit.actions
Source13:	ejabberdctl.polkit.rules

Source14:	ejabberd-src-deps.tar

# Use ejabberd as an example for PAM service name (fedora/epel-specific)
Patch1: ejabberd-0001-Fix-PAM-service-example-name-to-match-actual-one.patch
# Introducing mod_admin_extra
Patch2: ejabberd-0002-Introducing-mod_admin_extra.patch
# BZ# 439583, 452326, 451554, 465196, 502361 (fedora/epel-specific)
Patch3: ejabberd-0003-Fedora-specific-changes-to-ejabberdctl.patch
# Fedora-specific
Patch4: ejabberd-0004-Install-.so-objects-with-0755-permissions.patch
# Fedora-specific
Patch5: ejabberd-0005-Clean-up-false-security-measure.patch
# polkit support
Patch6: ejabberd-0006-Enable-polkit-support.patch
# Fedora-specific
Patch7: ejabberd-0007-Install-into-BINDIR-instead-of-SBINDIR.patch
# Fedora-specific
Patch8:	ejabberd-0008-Disable-Erlang-version-check.patch
# Fedora-specific
Patch9: ejabberd-0009-Fix-permissions-for-captcha-script.patch
# Fedora-specific
Patch10:ejabberd-0010-Enable-systemd-notification-if-available.patch

Patch11: ejabberd-0011-aarch64.patch

BuildRequires:  expat-devel
BuildRequires:  openssl-devel >= 0.9.8
BuildRequires:  pam-devel
BuildRequires:  libyaml-devel
BuildRequires:  erlang
BuildRequires:  erlang-rebar
BuildRequires:  git
# FIXME
#BuildRequires:  erlang-jiffy
#BuildRequires:  erlang-lager
#BuildRequires:  erlang-ibrowse
#BuildRequires:  erlang-xmlrpc
%if 0%{?_with_hevea}
BuildRequires:  hevea
BuildRequires:  texlive-comment
%endif
BuildRequires:	autoconf
BuildRequires:	automake

# For creating user and group
Requires(pre):		shadow-utils

Requires(post): /usr/bin/openssl
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd

Provides: user(%{name})
Provides: group(%{name})

Requires:       erlang
# FIXME see also patch #10
#Requires:       erlang-sd_notify
# for /usr/bin/pkexec
Requires:       polkit
# for flock in ejabberdctl
Requires:	util-linux
%{?__erlang_drv_version:Requires: %{__erlang_drv_version}}
%{?__erlang_nif_version:Requires: %{__erlang_nif_version}}


%description
ejabberd is a Free and Open Source distributed fault-tolerant
Jabber/XMPP server. It is mostly written in Erlang, and runs on many
platforms (tested on Linux, FreeBSD, NetBSD, Solaris, Mac OS X and
Windows NT/2000/XP).

%package doc
Summary: Documentation for ejabberd
BuildArch: noarch
Obsoletes: %{name}-doc < 2.1.4
# docdir owner
Requires: %{name} = %{version}-%{release}
Group: Documentation

%description doc
Documentation for ejabberd.

%prep
%setup -q

%patch1 -p1 -b .pam_name
%patch2 -p1 -b .mod_admin_extra
%patch3 -p1 -b .fedora_specific
%patch4 -p1 -b .so_lib_755
%patch5 -p1 -b .false_security
%patch6 -p1 -b .use_polkit
%patch7 -p1 -b .use_bindir
%patch8 -p1 -b .no_ver_check
%patch9 -p1 -b .captcha_perms
#%patch10 -p1 -b .systemd_notify

tar xvf %{S:14}
%patch11 -p1


%build
autoreconf -ivf

# Disabled: --enable-hipe --enable-roster-gateway-workaround --enable-transient_supervisors --enable-full-xml --enable-mssql --enable-tools --enable-riak --enable-http
%configure --enable-nif --enable-odbc --enable-mysql --enable-pgsql --enable-pam --enable-zlib --enable-json --enable-iconv --enable-debug --enable-lager
make
%if 0%{?_with_hevea}
pushd doc
%ifarch %{power64}
ulimit -a
ulimit -Hs 65536
ulimit -Ss 65536
%endif
# remove pre-built docs
rm -f dev.html features.html
# See this link - http://thread.gmane.org/gmane.linux.redhat.fedora.devel/198954/focus=198957
make release
make html pdf
popd
%endif


%install
make install DESTDIR=%{buildroot}

# fix example SSL certificate path to real one, which we created recently (see above)
%{__perl} -pi -e 's!/path/to/ssl.pem!/etc/ejabberd/ejabberd.pem!g' %{buildroot}/etc/ejabberd/ejabberd.yml

# fix captcha path
%{__perl} -pi -e 's!/lib/ejabberd/priv/bin/captcha.sh!%{_libdir}/%{name}/priv/bin/captcha.sh!g' %{buildroot}/etc/ejabberd/ejabberd.yml

install -D -p -m 0644 %{S:9} %{buildroot}%{_sysconfdir}/pam.d/ejabberdctl
install -D -p -m 0644 %{S:11} %{buildroot}%{_sysconfdir}/pam.d/ejabberd

# install systemd entry
install -D -m 0644 -p %{S:4} %{buildroot}%{_unitdir}/%{name}.service
install -D -m 0644 -p %{S:5} %{buildroot}%{_tmpfilesdir}/%{name}.conf

# install config for logrotate
install -D -p -m 0644  %{S:2} %{buildroot}%{_sysconfdir}/logrotate.d/ejabberd

# create room for additional files (such as SQL schemas)
install -d %{buildroot}%{_datadir}/%{name}
# install sql-scripts for creating db schemes for various RDBMS
install -p -m 0644 sql/mssql2000.sql %{buildroot}%{_datadir}/%{name}
install -p -m 0644 sql/mssql2005.sql %{buildroot}%{_datadir}/%{name}
install -p -m 0644 sql/mssql2012.sql %{buildroot}%{_datadir}/%{name}
install -p -m 0644 sql/mysql.sql %{buildroot}%{_datadir}/%{name}
install -p -m 0644 sql/pg.sql %{buildroot}%{_datadir}/%{name}

# Install polkit-related files
install -D -p -m 0644 %{S:12} %{buildroot}%{_datadir}/polkit-1/actions/ejabberdctl.policy
install -D -p -m 0644 %{S:13} %{buildroot}%{_datadir}/polkit-1/rules.d/51-ejabberdctl.rules


%pre
getent group %{name} >/dev/null || groupadd -r %{name}
getent passwd %{name} >/dev/null || \
useradd -r -g %{name} -d %{_localstatedir}/lib/%{name} -s /sbin/nologin -M \
-c "ejabberd" %{name} 2>/dev/null || :


if [ $1 -gt 1 ]; then
	# we should backup DB in every upgrade
	if ejabberdctl status >/dev/null ; then
		# Use timestamp to make database restoring easier
		TIME=$(date +%%Y-%%m-%%dT%%H:%%M:%%S)
		BACKUPDIR=$(mktemp -d -p /var/tmp/ ejabberd-$TIME.XXXXXX)
		chown ejabberd:ejabberd $BACKUPDIR
		BACKUP=$BACKUPDIR/ejabberd-database
		ejabberdctl backup $BACKUP
		# Change ownership to root:root because ejabberd user might be
		# removed on package removal.
		chown -R root:root $BACKUPDIR
		chmod 700 $BACKUPDIR
		echo
		echo The ejabberd database has been backed up to $BACKUP.
		echo
	fi

	# fix cookie path (since ver. 2.1.0 cookie stored in /var/lib/ejabberd/spool
	# rather than in /var/lib/ejabberd
	if [ -f /var/lib/ejabberd/spool/.erlang.cookie ]; then
		cp -pu /var/lib/ejabberd/{spool/,}.erlang.cookie
		echo
		echo The ejabberd cookie file was moved again.
		echo Please delete old one from /var/lib/ejabberd/spool/.erlang.cookie
		echo
	fi
fi


%post
%systemd_post %{name}.service

# Create SSL certificate with default values if it doesn't exist
(cd /etc/ejabberd
if [ ! -f ejabberd.pem ]
then
    echo "Generating SSL certificate /etc/ejabberd/ejabberd.pem..."
    HOSTNAME=$(hostname -s 2>/dev/null || echo "localhost")
    DOMAINNAME=$(hostname -d 2>/dev/null || echo "localdomain")
    openssl req -new -x509 -days 365 -nodes -out ejabberd.pem \
                -keyout ejabberd.pem > /dev/null 2>&1 <<+++
.
.
.
$DOMAINNAME
$HOSTNAME
ejabberd
root@$HOSTNAME.$DOMAINNAME
+++
chown ejabberd:ejabberd ejabberd.pem
chmod 600 ejabberd.pem
fi)


%preun
%systemd_preun %{name}.service


%postun
%systemd_postun_with_restart %{name}.service


%files
%doc COPYING

%attr(750,ejabberd,ejabberd) %dir %{_sysconfdir}/ejabberd
%attr(640,ejabberd,ejabberd) %config(noreplace) %{_sysconfdir}/ejabberd/ejabberd.yml
%attr(640,ejabberd,ejabberd) %config(noreplace) %{_sysconfdir}/ejabberd/ejabberdctl.cfg
%attr(640,ejabberd,ejabberd) %config(noreplace) %{_sysconfdir}/ejabberd/inetrc

%{_unitdir}/%{name}.service
%{_tmpfilesdir}/%{name}.conf

%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%config(noreplace) %{_sysconfdir}/pam.d/%{name}
%config(noreplace) %{_sysconfdir}/pam.d/ejabberdctl
%{_datadir}/polkit-1/actions/ejabberdctl.policy
%{_datadir}/polkit-1/rules.d/51-ejabberdctl.rules
%{_bindir}/ejabberdctl

%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/ebin
%dir %{_libdir}/%{name}/include
%dir %{_libdir}/%{name}/priv
%dir %{_libdir}/%{name}/priv/bin
%dir %{_libdir}/%{name}/priv/lib
%dir %{_libdir}/%{name}/priv/msgs

%{_libdir}/%{name}/ebin/*.app
%{_libdir}/%{name}/ebin/*.beam
%{_libdir}/%{name}/include/*.hrl
%{_libdir}/%{name}/priv/bin/captcha.sh
%attr(4750,root,ejabberd) %{_libdir}/%{name}/priv/bin/epam
%{_libdir}/%{name}/priv/lib/*.so

%{_libdir}/%{name}/priv/msgs/*.msg

%dir %{_datadir}/%{name}
%{_datadir}/%{name}/mssql2000.sql
%{_datadir}/%{name}/mssql2005.sql
%{_datadir}/%{name}/mssql2012.sql
%{_datadir}/%{name}/mysql.sql
%{_datadir}/%{name}/pg.sql

%attr(750,ejabberd,ejabberd) %dir /var/lib/ejabberd
%attr(750,ejabberd,ejabberd) %dir /var/lock/ejabberdctl
%attr(750,ejabberd,ejabberd) %dir /var/log/ejabberd

%files doc
%doc doc/*.html
%doc doc/*.png
%if 0%{?_with_hevea}
%doc doc/*.pdf
%endif
%doc doc/*.txt


%changelog
* Fri Nov 14 2014 Dan Horák <dan[at]danny.cz> - 14.07-6
- increase stack size for hevea on ppc64* (#1164209)

* Fri Nov 14 2014 Dan Horák <dan[at]danny.cz> - 14.07-5
- hevea exists for all relevant arches, enables build on s390(x) and ppc64(le) (#1161098)

* Wed Nov 12 2014 Marcin Juszkiewicz <mjuszkiewicz@redhat.com> - 14.07-4
- add aarch64 support

* Tue Nov 04 2014 Peter Lemenkov <lemenkov@gmail.com> - 14.07-3
- Rebuild with Erlang 17.3.3

* Sun Aug 31 2014 Peter Lemenkov <lemenkov@gmail.com> - 14.07-2
- Temporarily disable external http support (--with-http)
- Temporarily disable systemd notify
- Add missing BuildRequires: git

* Sat Aug 30 2014 Peter Lemenkov <lemenkov@gmail.com> - 14.07-1
- Ver. 14.07
- Dropped support for EPEL5, EPEL6
- Dropped initial untested support for GSSAPI - nobody is interested in testing
  and further developing this
- Fixed https://bugzilla.redhat.com/1089475
- Fixed https://bugzilla.redhat.com/1117450

* Thu Aug 28 2014 Peter Lemenkov <lemenkov@gmail.com> - 2.1.13-10
- Rebuild with Erlang 17.2.1

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.13-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.13-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Oct 27 2013 Peter Lemenkov <lemenkov@gmail.com> - 2.1.13-7
- Fixed systemd service-file

* Sat Oct 26 2013 Peter Lemenkov <lemenkov@gmail.com> - 2.1.13-6
- Fix polkit again
- Add dependency on Erlang's driver version

* Fri Sep 27 2013 Peter Lemenkov <lemenkov@gmail.com> - 2.1.13-5
- Fix wrong polkit policy (rhbz #1009408)

* Sun Sep 15 2013 Peter Lemenkov <lemenkov@gmail.com> - 2.1.13-4
- Use polkit instead of usermode on modern systems
- Restore user/group provides

* Thu Sep 05 2013 Peter Lemenkov <lemenkov@gmail.com> - 2.1.13-3
- TEMPORARY disable hevea - it's broken in F19+
- Fix building with unversioned docdir
- Move away from fedora-usermgmt

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jun 29 2013 Peter Lemenkov <lemenkov@gmail.com> - 2.1.13-1
- Ver. 2.1.13
- Don't install or use /etc/sysconfig/ejabberd on systemd-enabled systems
- Build with PIE (if available)
- Re-generate configure scripts

* Fri Mar 15 2013 Peter Lemenkov <lemenkov@gmail.com> - 2.1.12-1
- Ver. 2.1.12

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.11-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Oct 28 2012 Peter Lemenkov <lemenkov@gmail.com> - 2.1.11-6
- Fixed rhbz #846856

* Mon Sep 10 2012 Peter Lemenkov <lemenkov@gmail.com> - 2.1.11-5
- Cherry-picked three new patches from upstream trunk

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Jul 15 2012 Peter Lemenkov <lemenkov@gmail.com> - 2.1.11-3
- Fixed rhbz #758601 (no /etc/pam.d/password-auth in EL5)

* Sun Jul 15 2012 Peter Lemenkov <lemenkov@gmail.com> - 2.1.11-2
- Updated mod_admin_extra to work with R15B (see rhbz #840039)
- Updated list of arches where we don't have hevea
- Dropped abandonded and not working modules

* Sun May 06 2012 Peter Lemenkov <lemenkov@gmail.com> - 2.1.11-1
- Ver. 2.1.11
- Fixed systemd installation

* Sun Jan 15 2012 Peter Lemenkov <lemenkov@gmail.com> - 2.1.10-3
- Fixed systemd unit file

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Dec 28 2011 Peter Lemenkov <lemenkov@gmail.com> - 2.1.10-1
- Ver. 2.1.10
- Works with systemd (closes rhbz #767793)

* Sun Dec 18 2011 Dan Horák <dan[at]danny.cz> - 2.1.9-2
- pdf docs require hevea, they are not prebuilt

* Tue Nov 22 2011 Peter Lemenkov <lemenkov@gmail.com> - 2.1.9-1
- Ver. 2.1.9
- Fix for CVE-2011-4320

* Mon Jul 11 2011 Peter Lemenkov <lemenkov@gmail.com> - 2.1.8-3
- Fix for systemd (F15+ only, see rhbz #656581)

* Sat Jun 18 2011 Peter Lemenkov <lemenkov@gmail.com> - 2.1.8-2
- Fix ejabberdctl again

* Fri Jun 03 2011 Peter Lemenkov <lemenkov@gmail.com> - 2.1.8-1
- Ver. 2.1.8 (very urgent bugfix for 2.1.7)

* Wed Jun 01 2011 Peter Lemenkov <lemenkov@gmail.com> - 2.1.7-1
- Ver. 2.1.7 (bugfixes and security)

* Wed Jun 01 2011 Paul Whalen <paul.whalen@senecac.on.ca> - 2.1.6-5
- Added arm to conditional to build without hevea.

* Thu Feb 24 2011 Peter Lemenkov <lemenkov@gmail.com> - 2.1.6-4
- Updated @online@ patch

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jan 25 2011 Martin Langhoff <martin@laptop.org> 2.1.6-2
- Apply rebased @online@ patch from OLPC - EJAB-1391

* Tue Dec 14 2010 Peter Lemenkov <lemenkov@gmail.com> 2.1.6-1
- Ver. 2.1.6 (Bugfix release)

* Thu Aug 26 2010 Peter Lemenkov <lemenkov@gmail.com> 2.1.5-6
- More patches from trunk
- Rebased patches

* Thu Aug 26 2010 Peter Lemenkov <lemenkov@gmail.com> 2.1.5-5
- Backported %%patch11 from upstream (fixes LDAP)

* Wed Aug 18 2010 Peter Lemenkov <lemenkov@gmail.com> 2.1.5-4
- Add accidentally forgotten changes to ejabberd.logrotate

* Wed Aug 18 2010 Peter Lemenkov <lemenkov@gmail.com> 2.1.5-3
- Fixed http-poll (BOSH)
- New version of GSSAPI patch (backported from upstream)
- Fixed logrotate rule

* Wed Aug  4 2010 Peter Lemenkov <lemenkov@gmail.com> 2.1.5-2
- Don't require dos2unix for building anymore

* Wed Aug  4 2010 Peter Lemenkov <lemenkov@gmail.com> 2.1.5-1
- Ver. 2.1.5
- OpenSSL >= 0.9.8
- Doc-file features.* dropped (just a part of guide.*)
- Dropped upstreamed patches
- Don't use autoreconf

* Fri Jul 16 2010 Peter Lemenkov <lemenkov@gmail.com> 2.1.4-3
- Fix for Erlang/OTP R14A
- Added BR: autoconf

* Fri Jun 18 2010 Peter Lemenkov <lemenkov@gmail.com> 2.1.4-2
- No hevea for EL-6
- No hevea for s390 and s390x

* Fri Jun  4 2010 Peter Lemenkov <lemenkov@gmail.com> 2.1.4-1
- Ver. 2.1.4
- Rebased patches

* Mon Mar 29 2010 Peter Lemenkov <lemenkov@gmail.com> 2.1.3-6
- File permissions for captcha.sh were fixed

* Thu Mar 18 2010 Peter Lemenkov <lemenkov@gmail.com> 2.1.3-5
- Init-script fixed

* Thu Mar 18 2010 Peter Lemenkov <lemenkov@gmail.com> 2.1.3-4
- Really fix issue with "File operation error: eacces".

* Thu Mar 18 2010 Peter Lemenkov <lemenkov@gmail.com> 2.1.3-3
- Relax access rights of /usr/sbin/ejabberdctl (from 0550 to 0755)
- Invoke symlinked consolehelper instead of /usr/sbin/ejabberdctl
  in init-script
- Fixed "File operation error: eacces" issue. See rhbz #564686.

* Thu Mar 18 2010 Peter Lemenkov <lemenkov@gmail.com> 2.1.3-2
- Init-script enhancements

* Fri Mar 12 2010 Peter Lemenkov <lemenkov@gmail.com> 2.1.3-1
- Ver. 2.1.3
- Patches rebased

* Fri Mar  5 2010 Peter Lemenkov <lemenkov@gmail.com> 2.1.2-4
- Fixed issue with {erorr,nxdomain}

* Tue Feb 16 2010 Peter Lemenkov <lemenkov@gmail.com> 2.1.2-3
- Do not try to backup DB on every fresh install
- Do not force copying old erlang cookie file
- Add missing release notes for ver. 2.1.2
- Require erlang-esasl for krb5 support
- No such %%configure option - --enable-debug
- Patches were rebased and renumbered
- Add new BR util-linux(-ng)

* Fri Jan 29 2010 Peter Lemenkov <lemenkov@gmail.com> 2.1.2-2
- Fixed BZ #559925 (EJAB-1173)
- Changed order of rpmbuild targets in this spec to more natural one.

* Mon Jan 18 2010 Peter Lemenkov <lemenkov@gmail.com> 2.1.2-1
- Ver. 2.1.2

* Thu Dec 24 2009 Peter Lemenkov <lemenkov@gmail.com> 2.1.1-1
- Ver. 2.1.1
- Dropped patches 9,11,12,13 (accepted upstream)

* Thu Dec 10 2009 Peter Lemenkov <lemenkov@gmail.com> 2.1.0-2
- DB backups are made on every upgrade/uninstall
- Fixed installation of captcha.sh example helper
- Added patches 9,10,11,12,13 from Debian's package

* Fri Nov 20 2009 Peter Lemenkov <lemenkov@gmail.com> 2.1.0-1
- Ver. 2.1.0
- Upstream no longer providing ChangeLog
- Dropped ejabberd-build.patch (upstreamed)
- Dropped ejabberd-captcha.patch (upstreamed)
- Dropped ejabberd-decrease_buffers_in_mod_proxy65.patch (upstreamed)
- Dropped ejabberd-dynamic_compile_loglevel.patch (upstreamed)
- Dropped ejabberd-turn_off_error_messages_in_mod_caps.patch (upstreamed)
- Docs reorganized and added ability to rebuild them if possible
- Added back ppc64 target
- SQL-scripts moved to %%{_datadir}/%%{name} from %%doc

* Thu Nov  5 2009 Peter Lemenkov <lemenkov@gmail.com> 2.0.5-10
- mod_ctlextra was updated from r873 to r1020
- Fix for BZ# 533021

* Wed Sep 16 2009 Tomas Mraz <tmraz@redhat.com> - 2.0.5-9
- Use password-auth common PAM configuration instead of system-auth

* Wed Sep  9 2009 Peter Lemenkov <lemenkov@gmail.com> 2.0.5-8
- Fixed possible issue in the config file for logrotate
- Fixed possible issue while creating dummy certificate
- Added patches #5,6,7,8 from Debian

* Thu Aug 27 2009 Tomas Mraz <tmraz@redhat.com> - 2.0.5-7
- rebuilt with new openssl

* Tue Aug 25 2009 Peter Lemenkov <lemenkov@gmail.com> 2.0.5-6
- Since now, we using only ejabberdctl in the init-script (bz# 502361)

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Apr 21 2009 Peter Lemenkov <lemenkov@gmail.com> 2.0.5-3
- CAPTCHA is back - let's test it.

* Sat Apr  4 2009 Peter Lemenkov <lemenkov@gmail.com> 2.0.5-2
- Really disable CAPTCHA

* Fri Apr  3 2009 Peter Lemenkov <lemenkov@gmail.com> 2.0.5-1
- Ver. 2.0.5
- Temporarily disabled CAPTCHA support

* Sun Mar 15 2009 Peter Lemenkov <lemenkov@gmail.com> 2.0.4-2
- Support for CAPTCHA (XEP-0158)
- Updated mod_ctlextra.erl (fixed EJAB-789, EJAB-864)

* Sun Mar 15 2009 Peter Lemenkov <lemenkov@gmail.com> 2.0.4-1
- Ver. 2.0.4

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Jan 26 2009 Peter Lemenkov <lemenkov@gmail.com> 2.0.3-1
- Ver. 2.0.3
- Merged some stuff from git://dev.laptop.org/users/martin/ejabberd-xs.git

* Fri Jan 16 2009 Tomas Mraz <tmraz@redhat.com> 2.0.2-4
- rebuild with new openssl

* Thu Oct  2 2008 Peter Lemenkov <lemenkov@gmail.com> 2.0.2-3
- Fixed broken ejabberdctl (BZ# 465196)

* Sat Aug 30 2008 Peter Lemenkov <lemenkov@gmail.com> 2.0.2-2
- Added missing Requires

* Fri Aug 29 2008 Peter Lemenkov <lemenkov@gmail.com> 2.0.2-1
- Ver. 2.0.2

* Sat Aug  9 2008 Peter Lemenkov <lemenkov@gmail.com> 2.0.2-0.3.beta1
- PAM support (BZ# 452803)

* Sat Aug  9 2008 Peter Lemenkov <lemenkov@gmail.com> 2.0.2-0.2.beta1
- Fix build with --fuzz=0

* Sat Aug  9 2008 Peter Lemenkov <lemenkov@gmail.com> 2.0.2-0.1.beta1
- Version 2.0.2-beta1
- Fixed BZ# 452326
- Fixed BZ# 227270

* Sun Jun 22 2008 Peter Lemenkov <lemenkov@gmail.com> 2.0.1-4
- Last minute fix (issue with shortnames/fqdn)

* Sun Jun 22 2008 Peter Lemenkov <lemenkov@gmail.com> 2.0.1-3
-Fixed BZ# 439583, 452326, 451554

* Thu May 29 2008 Peter Lemenkov <lemenkov@gmail.com> 2.0.1-2
- Fixed BZ# 439583

* Sat May 24 2008 Peter Lemenkov <lemenkov@gmail.com> 2.0.1-1
- Ver. 2.0.1
- Upstreamed patches dropped
- No longer uses versioned libdir (/usr/lib/ejabberd-x.x.x)
- Added sql-scripts in docs-directory

* Mon May  5 2008 Peter Lemenkov <lemenkov@gmail.com> 2.0.0-3
- Fix build against R11B-2

* Sat Feb 23 2008 Peter Lemenkov <lemenkov@gmail.com> 2.0.0-2
- Disable docs again for EPEL (we haven't hevea for EPEL)

* Sat Feb 23 2008 Peter Lemenkov <lemenkov@gmail.com> 2.0.0-1
- Version 2.0.0

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2.0.0-0.4.rc1
- Autorebuild for GCC 4.3

* Wed Jan 23 2008 Peter Lemenkov <lemenkov@gmail.com> 2.0.0-0.3.rc1
- Really enabled some previously disabled modules

* Wed Jan 23 2008 Peter Lemenkov <lemenkov@gmail.com> 2.0.0-0.2.rc1
- Enabled some previously disabled modules

* Sat Jan 19 2008 Matej Cepl <mcepl@redhat.com> 2.0.0-0.1.rc1
- Upgrade to the current upsteram version.
- Make ejabberd.init LSB compliant (missing Provides: tag)

* Thu Dec 27 2007 Matej Cepl <mcepl@redhat.com> 2.0.0-0.beta1.mc.1
- Experimental build from the upstream betaversion.

* Tue Dec 11 2007 Matej Cepl <mcepl@redhat.com> 1.1.4-2.fc9
- rebuild against new ssl library.
- rebuild against the newest erlang (see Patch
- fix %%changelog

* Wed Sep  5 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.1.4-1
- Drop LDAP patch
- Update mod_ctlextra
- Update to 1.1.4

* Tue Sep  4 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.1.3-11
- Fix ejabberdctl wrapper script - #276071

* Wed Aug 22 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.1.3-10
- Re-exclude ppc64

* Wed Aug 22 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.1.3-9
- Fix license
- Don't exclude ppc64

* Wed Aug 22 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.1.3-8
- Bump & rebuild to build against latest erlang package.

* Tue Jul 31 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.1.3-7
- Bump release and rebuild due to Koji hiccups.

* Tue Jul 31 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.1.3-6
- Don't try building on PPC64 since hevea isn't available on PPC64.

* Tue Jul 31 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.1.3-5
- Sigh...

* Tue Jul 31 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.1.3-4
- Don't forget to add patch.

* Thu Jul 26 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.1.3-3
- Add ejabberdctl (#199873)
- Add patch to fix LDAP authentication. (#248268)
- Add a sleep in init script between stop/start when restarting.
- LSB compliance cleanups for init script. (#246917)
- Don't mention "reload" in the init script usage string. (#227254)

* Tue Jul 24 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.1.3-2
- Update mod_ctlextra

* Fri Feb  2 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.1.3-1
- Update to 1.1.3

* Wed Oct 11 2006 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.1.2-2
- Fix logrotate script (BZ#210366)

* Mon Aug 28 2006 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.1.1-10
- Bump release and rebuild.

* Mon Jul 3 2006 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.1.1-9
- Updated init script - should hopefully fix some problems with status & stop commands.

* Mon Jun 26 2006 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.1.1-8
- Bump release to that tagging works on FC-5.

* Thu Jun 22 2006 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.1.1-7
- Oops drop bad patch.

* Thu Jun 22 2006 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.1.1-6
- Split documentation off to a subpackage.
- Own %%{_libdir}/ejabberd-%{version}
- Mark %%{_sysconfdir}/logrotate.d/ejabberd as %%config

* Thu Jun  8 2006 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.1.1-5
- Patch the makefile so that it adds a soname to shared libs.

* Fri May 26 2006 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.1.1-4
- Modify AD modules not to check for group membership.

* Thu May 25 2006 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.1.1-3
- Add some extra modules

* Wed May 24 2006 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.1.1-2
- Munge Makefile.in a bit more...
- Change ownership/permissions - not *everything* needs to be owned by ejabberd

* Wed May 24 2006 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.1.1-1
- First version for Fedora Extras
