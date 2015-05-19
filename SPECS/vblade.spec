Name:           vblade
Version:        20
Release:        1%{?dist}
Summary:        Virtual EtherDrive (R) blade daemon

Group:          System Environment/Base
License:        GPLv2
URL:            http://sourceforge.net/projects/aoetools/
Source0:        http://dl.sf.net/aoetools/%{name}-%{version}.tgz
Source1:        %{name}.init
Source2:        %{name}.conf
Patch0:         %{name}-makefile.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires(post):  /sbin/chkconfig
Requires(post):  /sbin/service
Requires(preun): /sbin/chkconfig
Requires(preun): /sbin/service


%description
The vblade is the virtual EtherDrive (R) blade, a program that makes a
seekable file available over an ethernet local area network (LAN) via
the ATA over Ethernet (AoE) protocol.

The seekable file is typically a block device like /dev/md0 but even
regular files will work.  When vblade exports the block storage over
AoE it becomes a storage target.  Another host on the same LAN can
access the storage if it has a compatible aoe kernel driver.


%prep
%setup -q
%patch0 -p1


%build
make %{?_smp_mflags} CFLAGS="$RPM_OPT_FLAGS"


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/var/run/%{name}
install -D -m 755 %{SOURCE1} $RPM_BUILD_ROOT%{_initrddir}/%{name}
install -D -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.conf


%clean
rm -rf $RPM_BUILD_ROOT


%post
if [ "$1" = "2" ]; then # if we're being upgraded
    /sbin/service %{name} condrestart >/dev/null 2>&1 || :
else # if we're being installed
    /sbin/chkconfig --add %{name}
fi

%preun
if [ "$1" = "0" ]; then     # execute this only if we are NOT doing an upgrade
    /sbin/service %{name} stop >/dev/null 2>&1 || :
    /sbin/chkconfig --del %{name}
fi


%files
%defattr(-,root,root,-)
%doc COPYING HACKING NEWS README
%config(noreplace) %{_sysconfdir}/%{name}.conf
%dir /var/run/%{name}
%{_initrddir}/%{name}
%{_sbindir}/vblade
%{_sbindir}/vbladed
%{_mandir}/man8/vblade.8*


%changelog
* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 14-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 14-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 14-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 13 2008 Patrick "Jima" Laughton <jima@beer.tclug.org> 14-4
- Bump-n-build for GCC 4.3

* Wed Aug 22 2007 Patrick "Jima" Laughton <jima@beer.tclug.org> 14-3
- Add missing /var/run/vblade/
- Rebuild for BuildID
- License clarification

* Sat Apr 07 2007 Patrick "Jima" Laughton <jima@beer.tclug.org> 14-2
- Forced CFLAGS on build

* Wed Apr 04 2007 Patrick "Jima" Laughton <jima@beer.tclug.org> 14-1
- Initial Fedora RPM
