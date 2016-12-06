Name: jid
Summary: JSON Incremenal Digger
License: MIT
Group: System/Utilities
Url: https://github.com/simeji/jid

%define git_version 0.6.1
%define git_package simeji/%{name}

Version: %{git_version}
Release: 1.fdm
BuildArch: x86_64
Prefix: %{_prefix}
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
You can drill down JSON interactively by using filtering queries like jq.

Suggestion and Auto completion of this tool will provide you a very
comfortable JSON drill down.

%changelog
* Tue Dec  6 2016 Thornton Prime <thornton.prime@gmail.com> [0.6.1]
- Build for Fedora 25

%files
%defattr(-,root,root)
%{_bindir}/jid

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
go get -f -u github.com/%{git_package}/cmd/jid

%install
%{__install} -D bin/jid ${RPM_BUILD_ROOT}%{_bindir}/jid

%clean
rm -rf $RPM_BUILD_ROOT

