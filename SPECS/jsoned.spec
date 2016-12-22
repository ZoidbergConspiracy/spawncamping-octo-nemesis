Name: jd
Summary: Interactive JSON Editor
License: MIT
Group: System/Utilities
Url: https://github.com/tidwall/jd

%define git_version 0.3.1
%define git_package tidwall/%{name}

Version: %{git_version}
Release: 1.fdm
BuildArch: x86_64
Prefix: %{_prefix}
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
It's an experimental tool for querying and editing JSON documents.

%changelog
* Sun Dec 11 2016 Thornton Prime <thornton.prime@gmail.com> [0.3.1]
- Build for Fedora 25

%files
%defattr(-,root,root)
%{_bindir}/jd

%prep

%setup -cT
export GOPATH=`pwd`
git clone https://github.com/%{git_package}.git src/github.com/%{git_package}
(
  cd src/github.com/%{git_package}
  git checkout -b %{git_version}
  git branch --set-upstream-to=origin/master %{git_version}
)

%build
export GOPATH=`pwd`
go get -f -u github.com/%{git_package}/cmd/jd

%install
%{__install} -D bin/jd ${RPM_BUILD_ROOT}%{_bindir}/jd

%clean
rm -rf $RPM_BUILD_ROOT

