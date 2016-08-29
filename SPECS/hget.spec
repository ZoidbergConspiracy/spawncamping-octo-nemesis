Name: hget
Summary: Rocket fast resumable dowmoad accelerator
License: PP
Group: Applications/Internet
Url: https://github.com/huydx/hget

%define git_version 0.%{expand:%%(date +%Y%m%d)}
%define git_package huydx/hget

Version: %{git_version}
Release: fdm
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: x86_64

%changelog
* Fri Jul 29 2016 Thornton Prime <thornton.prime@gmail.com> [0.0.1]
- Current version.

%description
Rocket fast download accelerator written in golang.

%files
%defattr(-,root,root)
%{_bindir}/hget
%doc src/github.com/%{git_package}/README.md

%prep
%setup -cT
export GOPATH=`pwd`
git clone https://github.com/%{git_package}.git src/github.com/%{git_package}
#(cd src/github.com/%{git_package}; git checkout -b v%{git_version} )
go get -f -u github.com/%{git_package}/... || true

%build
export GOPATH=`pwd`
go build github.com/%{git_package}

%install
%{__install} -D hget ${RPM_BUILD_ROOT}%{_bindir}/hget

%clean
rm -rf $RPM_BUILD_ROOT

