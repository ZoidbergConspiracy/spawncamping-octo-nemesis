Name: sup
Summary: Super Simple Deployment Tool
License: MIT
Group: Utilities/Management
Url: https://pressly.github.io/sup

%define git_version 0.4.1
%define git_package pressly/sup

Version: %{git_version}
Release: fdm
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: x86_64

%changelog
* Fri Jul 29 2016 Thornton Prime <thornton.prime@gmail.com> [0.0.1]
- Current version.

%description
Super simple deployment tool - just Unix - think of it like 'make' for a network
of servers. 

%files
%defattr(-,root,root)
%{_bindir}/sup
%doc src/github.com/%{git_package}/{README.md,LICENSE}

%prep
%setup -cT
export GOPATH=`pwd`
git clone https://github.com/%{git_package}.git src/github.com/%{git_package}
(cd src/github.com/%{git_package}; git checkout -b v%{git_version} )
go get -f -u github.com/%{git_package}/... || true

%build
export GOPATH=`pwd`
go build github.com/%{git_package}/cmd/sup

%install
%{__install} -D sup ${RPM_BUILD_ROOT}%{_bindir}/sup

%clean
rm -rf $RPM_BUILD_ROOT

