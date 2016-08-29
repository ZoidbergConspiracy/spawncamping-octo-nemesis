Name: mylg
Summary: Network Diagnostic Tool
License: MIT
Group: Applications/Internet
Url: http://mylg.io/

%define git_version 0.2.2
%define git_package mehrdadrad/mylg

Version: %{git_version}
Release: fdm
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: x86_64
BuildRequires: libpcap-devel

%changelog
* Wed Aug 24 2016 Thornton Prime <thornton.prime@gmail.com> [0.2.2]
- Update to 0.2.2
- Build with go1.7

%description
Looking glass is open source software utility which combines the functions
of the different network probes in one network diagnostic tool.

Features
 * Popular looking glasses (ping/trace/bgp) like Telia, Level3
 * More than 200 countries DNS Lookup information
 * Local fast ping and trace
 * Packet analyzer - TCP/IP and other packets
 * Local HTTP/HTTPS ping (GET, POST, HEAD)
 * RIPE information (ASN, IP/CIDR)
 * PeeringDB information
 * Port scanning fast
 * Network LAN Discovery
 * Web dashboard
 * Support vi and emacs mode, almost all basic features
 * CLI auto complete and history features

%files
%defattr(-,root,root)
%{_bindir}/mylg
%doc src/github.com/%{git_package}/{README.md,LICENSE}

%prep

%setup -cT
export GOPATH=`pwd`
git clone https://github.com/%{git_package}.git src/github.com/%{git_package}
(
  cd src/github.com/%{git_package}
  git checkout -b v%{git_version}
  git branch --set-upstream-to=origin/master v%{git_version}
)
go get -f -u github.com/%{git_package}/... || true


%build
export GOPATH=`pwd`
go build github.com/%{git_package}

%install
%{__install} -D mylg ${RPM_BUILD_ROOT}%{_bindir}/mylg

%clean
rm -rf $RPM_BUILD_ROOT

