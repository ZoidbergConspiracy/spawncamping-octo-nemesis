Name: certigo
Summary: A utility to examine and validate certificates in a variety of formats
Release: fdm
License: Apache 2.0
Group: System Environment/Utilities

%define git_version 1.1.0
%define git_package square/certigo

Version: %{git_version}
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: x86_64
Url: https://github.com/square/certigo

%description
Certigo is a utility to examine and validate certificates in a variety of formats.

%changelog
* Fri Jun 24 2016 Thornton Prime <thornton.prime@gmail.com> [1.1.0]
- Current version.
* Thu Apr  7 2016 Thornton Prime <thornton.prime@gmail.com> [0.9.0]
- Updated to pull directly from git

%prep

%setup -cT
export GOPATH=`pwd`
git clone https://github.com/%{git_package}.git src/github.com/%{git_package}
(cd src/github.com/%{git_package}; git checkout -b v%{git_version} )
go get -f -u ./... || true

%build
export GOPATH=`pwd`
go build github.com/%{git_package}

%install
%{__install} -D certigo ${RPM_BUILD_ROOT}%{_bindir}/certigo

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/certigo


