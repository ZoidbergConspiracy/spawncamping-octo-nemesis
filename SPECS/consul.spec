Name: consul
Summary: Tool for service discovery, monitoring and configuration
License: Mozilla Public License, v2.0
Group: System/Utilities
Url: http://www.consul.io
Vendor: Hashicorp

Version: 0.5.2
Release: fdm
BuildArch: x86_64

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
Source: https://github.com/hashicorp/consul/archive/v%{version}.tar.gz
Source1: consul.service
Source2: consul.sysconfig
Source3: consul.base

%description
Consul is a tool for service discovery and configuration.
Consul is distributed, highly available, and extremely scalable.

%prep
%setup -cT
export GOPATH=`pwd`
%{__mkdir} -p src/github.com/hashicorp
git clone https://github.com/hashicorp/consul.git src/github.com/hashicorp/consul
(
  cd src/github.com/hashicorp/consul
  git checkout tags/v%{version}
)

%build
export GOPATH=`pwd`
(
  cd src/github.com/hashicorp/consul
  %{__make}
)

%install
%{__install} -D src/github.com/hashicorp/consul/bin/consul %{buildroot}%{_bindir}/consul
%{__install} -D %{SOURCE1} %{buildroot}%{_unitdir}/consul.service
%{__install} -D %{SOURCE2} %{buildroot}%{_sysconfdir}/sysconfig/consul
%{__install} -D %{SOURCE3} %{buildroot}%{_sysconfdir}/consul.d/base.json
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
