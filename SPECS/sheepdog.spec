%define repoversion sheepdog-7971160
%define kver %( uname -r )
%define kver_clean %( uname -r | tr '-' '_' )

Name: sheepdog
Summary: The Sheepdog Distributed Storage System for QEMU
#Version: %{repoversion}
Version: 0.9.0_rc2
Release: 0%{?dist}
License: GPLv2 and GPLv2+
Group: System Environment/Base
URL: http://www.osrg.net/sheepdog
#Source0: http://downloads.sourceforge.net/project/sheepdog/%{name}/%{version}/%{name}-%{repoversion}.tar.gz
Source0: http://downloads.sourceforge.net/project/sheepdog/%{name}/%{version}/%{name}-%{version}.tar.gz
Source1: sheepdog.service
Source2: sheepdog.sysconfig

# Runtime bits
Requires: corosync userspace-rcu fcgi
Requires(post): chkconfig
Requires(preun): chkconfig
Requires(preun): initscripts

# Build bits
BuildRequires: autoconf automake yasm
BuildRequires: corosynclib-devel userspace-rcu-devel fcgi-devel

BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

%description
This package contains the Sheepdog server, and command line tool which offer
a distributed object storage system for QEMU.

%package sbd
Summary: Sheepdog kernel block driver client
Version: %{version}_%{kver_clean}
Requires: kernel-%{kver}

%description sbd
Installs the kernel block driver client for Sheepdog. For more information:
https://github.com/sheepdog/sheepdog/wiki/Sheepdog-Block-Device-(SBD)

%changelog
* Fri Aug 22 2014 Autotools generated version <nobody@nowhere.org> - 0.8.2-1.@alphatag@
- Autotools generated version

%prep
%setup -q -n sheepdog-0.9.0_rc2

%build
./autogen.sh
%{configure} --with-initddir=%{_initrddir} %{_configopts} \
  --enable-sheepfs --enable-http --enable-shepherd --enable-zookeeper

make %{_smp_mflags}

cd sbd
make

%install
rm -rf %{buildroot}

make install DESTDIR=%{buildroot}

ln -s dog %{buildroot}/%{_sbindir}/collie

rm %{buildroot}/%{_initddir}/sheepdog
%{__install} -d -m0755 %{buildroot}%{_unitdir}/
%{__install} -m 0644 %{SOURCE1} %{buildroot}%{_unitdir}/sheepdog.service

%{__install} -d -m0755 %{buildroot}%{_sysconfdir}/sysconfig
%{__install} -m 0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/sysconfig/sheepdog

%{__install} -d -m0755 %{buildroot}/lib/modules/%{kver}/extra/drivers/block
%{__install} sbd/sbd.ko %{buildroot}/lib/modules/%{kver}/extra/drivers/block

## tree fixup
# drop static libs
rm -f %{buildroot}%{_libdir}/*.a

%clean
rm -rf %{buildroot}

%post
systemctl enable sheepdog

%post sbd
depmod -a

%preun
if [ $1 -eq 0 ] ; then
  systemctl stop sheepdog
  systemctl disable sheepdog
fi

%postun sbd
depmod -a

%files
%defattr(-,root,root,-)
%doc COPYING README INSTALL
%{_sbindir}/sheep
%{_sbindir}/sheepfs
%{_sbindir}/dog
%{_sbindir}/shepherd
%{_sbindir}/collie
#%attr(755,-,-)%config %{_initddir}/sheepdog
%{_unitdir}/sheepdog.service
%config %{_sysconfdir}/sysconfig/sheepdog
%dir %{_localstatedir}/lib/sheepdog
%config %{_sysconfdir}/bash_completion.d/dog
%{_mandir}/man8/sheep.8*
%{_mandir}/man8/sheepfs.8*
%{_mandir}/man8/dog.8*

%files sbd
/lib/modules/%{kver}/extra/drivers/block/sbd.ko

