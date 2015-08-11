Name: consul-template
Summary: Generic template rendering and notifications with Consul
License: Mozilla Public License, v2.0
Group: System/Utilities
Url: http://www.consul-template.io
Vendor: Hashicorp

Version: git20150711.a8e96a0fa0
Release: fdm
BuildArch: x86_64

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}

%description
This project provides a convenient way to populate values from Consul into the filesystem using the
consul-template daemon.

The daemon consul-template queries a Consul instance and updates any number of specified templates on the
filesystem. As an added bonus, consul-template can optionally run arbitrary commands when the update
process completes. See the Examples section for some scenarios where this functionality might prove
useful.

%prep
mkdir -p %{name}-%{version}

%build
export GOPATH=`pwd`
go get -u github.com/hashicorp/consul-template

%install
%{__install} -D bin/consul-template %{buildroot}%{_bindir}/consul-template

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/consul-template
