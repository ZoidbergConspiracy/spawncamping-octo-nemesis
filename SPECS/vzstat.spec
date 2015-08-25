%define debug_package %{nil}

Summary:	shows you neat usage report of your KVM guests
Name:		kvmstat
Version:	0.1
Release:	1.vortex%{?dist}
Vendor:		Vortex RPM
BuildArch:	noarch
License:	MIT
Group:		Applications/System
URL:		https://github.com/thesharp/kvmstat
Source0:	https://github.com/downloads/thesharp/%{name}/%{name}-%{version}.tar.gz
Requires:	qemu-kvm, libvirt
Requires:	libvirt-python
Requires:	python >= 2.6
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
kvmstat shows you neat usage report of your KVM guests.

%prep
%setup -q -n %{name}-%{version}

%build

%install
rm -rf %{buildroot}
%{__install} -D -p -m 0755 kvmstat %{buildroot}/%{_bindir}/kvmstat

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_bindir}/kvmstat
%doc LICENSE README.md

%changelog
* Sun May 11 2014 Ilya Otyutskiy <ilya.otyutskiy@icloud.com> - 1.0-1.vortex
- Initial packaging for Enterprise Linux.
