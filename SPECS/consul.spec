Name: consul
Summary: Tool for service discovery, monitoring and configuration
License: Mozilla Public License, v2.0
Group: System/Utilities
Url: http://www.consul.io
Vendor: Hashicorp

Version: git20150711.00e35cdc41
Release: fdm
BuildArch: x86_64

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
Source0: consul.service
Source1: consul.sysconfig
Source2: consul.base

%description
Consul is a tool for service discovery and configuration.
Consul is distributed, highly available, and extremely scalable.

%prep
mkdir -p %{name}-%{version}

%build
export GOPATH=`pwd`
go get -u github.com/hashicorp/consul

%install
%{__install} -D bin/consul %{buildroot}%{_bindir}/consul
%{__install} -D %{SOURCE0} %{buildroot}%{_unitdir}/consul.service
%{__install} -D %{SOURCE1} %{buildroot}%{_sysconfdir}/sysconfig/consul
%{__install} -D %{SOURCE2} %{buildroot}%{_sysconfdir}/consul.d/base.json
%{__install} -d %{buildroot}%{_sharedstatedir}/consul

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/consul
%{_unitdir}/consul.service
%dir %{_sysconfdir}/consul.d
%dir /var/lib/consul
%config %{_sysconfdir}/sysconfig/consul
%config %{_sysconfdir}/consul.d/base.json
