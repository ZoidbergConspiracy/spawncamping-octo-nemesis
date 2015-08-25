Name: consul-template
Summary: Generic template rendering and notifications with Consul
License: Mozilla Public License, v2.0
Group: System/Utilities
Url: https://github.com/hashicorp/consul-template 
Vendor: Hashicorp

Version: 0.10.0
Release: fdm
BuildArch: x86_64

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
Source: https://github.com/hashicorp/consul-template/archive/v%{version}.tar.gz

%description
consul-template provides a convenient way to populate values from Consul
into the filesystem using the consul-template daemon.

The daemon consul-template queries a Consul instance and updates any number
of specified templates on the filesystem. As an added bonus,
consul-template can optionally run arbitrary commands when the update
process completes. See the Examples section for some scenarios where this
functionality might prove useful.

%prep
%setup -cT
export GOPATH=`pwd`
%{__mkdir} -p src/github.com/hashicorp
git clone https://github.com/hashicorp/consul-template.git src/github.com/hashicorp/consul-template
(
  cd src/github.com/hashicorp/consul-template
  git checkout tags/v%{version}
)

%build
export GOPATH=`pwd`
(
  cd src/github.com/hashicorp/consul-template
  %{__make}
)

%install
%{__install} -D src/github.com/hashicorp/consul-template/bin/consul-template %{buildroot}%{_bindir}/consul-template

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/consul-template
%doc src/github.com/hashicorp/consul-template/README.md
%doc src/github.com/hashicorp/consul-template/LICENSE
%doc src/github.com/hashicorp/consul-template/CHANGELOG.md

