Name: pget
Summary: Parallel Download Client
License: GPL
Group: Applications/Internet
Url: https://github.com/Code-Hex/pget

%define git_version 0.0.1
%define git_package Code-Hex/pget

Version: %{git_version}
Release: fdm
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: x86_64

%changelog
* Tue Jul  5 2016 Thornton Prime <thornton.prime@gmail.com> [0.0.1]
- Current version.

%description

Parallel file download.

%files
%defattr(-,root,root)
%{_bindir}/pget
%doc src/github.com/%{git_package}/{README.md,MANUAL*,RELEASE*,CONTRIBUTING*,COPYING*}

%prep
%setup -cT
export GOPATH=`pwd`
git clone https://github.com/%{git_package}.git src/github.com/%{git_package}
(cd src/github.com/%{git_package}; git checkout -b v%{git_version} )
go get -f -u %{git_package}/cmd/pget || true

%build
export GOPATH=`pwd`
go build github.com/%{git_package}/cmd/pget

%install

%{__install} -D pget ${RPM_BUILD_ROOT}%{_bindir}/pget

%clean
rm -rf $RPM_BUILD_ROOT

