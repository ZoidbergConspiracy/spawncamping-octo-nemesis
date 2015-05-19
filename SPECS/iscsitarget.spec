# Generate version information for kernel module
# use rpmbuild -ba --define "kernel xxxxx" SPEC
%{!?kernel:	%define kernel %(uname -r | sed -e 's@\.%{_arch}@@')}

Summary: iSCSI Enterprise Target 
Name: iscsitarget
Version: 1.4.20.2
Release: 3.fdm
License: GPL
Group: System Environment/Daemons
URL: http://sourceforge.net/projects/iscsitarget/
Source0: http://downloads.sourceforge.net/project/iscsitarget/iscsitarget/1.4.20.2/%{name}-%{version}.tar.gz
BuildRequires: gcc, /usr/bin/install, openssl-devel
Requires: %{name}-kernel-module = %{version}

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
iSCSI Enterprise Target

%package kernel-module-%{kernel}
Summary: iSCSI Enterprise Target kernel module
Group: System Environment/Kernel
Requires: kernel = %{kernel}
Provides: %{name}-kernel-module
BuildRequires: kernel-devel = %{kernel}

%description kernel-module-%{kernel}
iSCSI Enterprise Target kernel module

%prep
%setup

%build
make KSRC=/lib/modules/%{kernel}.%{_arch}/build

%install
%{__rm} -rf %{buildroot}

make install KSRC=/lib/modules/%{kernel}.%{_arch}/build DISTDIR=%{buildroot} DESTDIR=%{buildroot} 
mkdir -p %{buildroot}/etc/init.d/
mv %{buildroot}/etc/rc.d/init.d/iscsi-target %{buildroot}/etc/init.d/iscsitarget
install -m 644 -D doc/manpages/ietd.8 %{buildroot}%{_mandir}/man8/ietd.8
install -m 644 -D doc/manpages/ietd.conf.5 %{buildroot}%{_mandir}/man5/ietd.conf.5

rm -f %{buildroot}/lib/modules/%{kernel}.%{_arch}/modules.*
rm -rf %{buildroot}/usr/share/doc/iscsitarget

%clean
%{__rm} -rf %{buildroot}

%post
/sbin/depmod %{kernel} -A

%preun 
modprobe -r -q --set-version %{kernel} iscsi_trgt
/sbin/depmod %{kernel} -A

%files
%defattr(-, root, root, 0755)
/usr/sbin/*
/etc/init.d/iscsitarget
%defattr(-, root, root, 0644)
%dir /etc/iet
%config(noreplace) /etc/iet/ietd.conf
%config(noreplace) /etc/iet/initiators.allow
%config(noreplace) /etc/iet/targets.allow
%doc COPYING README ChangeLog README.vmware README.initiators
%{_mandir}/man?/*

%files kernel-module-%{kernel}
%defattr(-, root, root, 0744)
/lib/modules/%{kernel}.%{_arch}/extra/iscsi/iscsi_trgt.ko

%changelog
* Thu Nov 03 2005 Bastiaan Bakker <bastiaan.bakker@lifeline.nl> - 0.4.12-6
- added openssl-devel build requirement
- removed '.ko' extension in modprobe command

* Wed Nov 02 2005 Bastiaan Bakker <bastiaan.bakker@lifeline.nl> - 0.4.12-5
- fixed kernel-devel BuildRequires

* Fri Sep 23 2005 Bastiaan Bakker <bastiaan.bakker@lifeline.nl> - 0.4.12-4
- fixed modprobe -r 'FATAL' message
- run depmod with correct kernel version

* Fri Sep 23 2005 Bastiaan Bakker <bastiaan.bakker@lifeline.nl> - 0.4.12-3
- added config files
- set kernel module file permissions to 744
- fixed provides/requires of kernel module
- removed BuildArch restriction

* Thu Sep 22 2005 Bastiaan Bakker <bastiaan.bakker@lifeline.nl> - 0.4.12-2
- create separate subpackage for kernel module
- include man pages
- added kernel compatibility patch for kernels < 2.6.11

* Wed Aug 03 2005 Bastiaan Bakker <bastiaan.bakker@lifeline.nl>
- First version.


