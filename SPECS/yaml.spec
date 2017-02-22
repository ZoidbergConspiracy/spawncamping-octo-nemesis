Name: yaml
Summary: Command line YAML processor
License: MIT
Group: System/Utilities

%define git_version 1.5
%define git_package mikefarah/%{name}

Version: %{git_version}
Release: 0.fdm
BuildArch: x86_64
URL: https://github.com/%{git_package}
Prefix: %{_prefix}

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
yaml is a lightweight and flexible command-line YAML processor

The aim of the project is to be the jq or sed of yaml files.

%changelog
* Wed Feb  9 2017 Thornton Prime <thornton.prime@gmail.com> [1.5]
- Basic build from Github

%files
%defattr(-,root,root)
%{_bindir}/yaml

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
go get -f -u github.com/%{git_package}

%install
%{__install} -D bin/yaml ${RPM_BUILD_ROOT}%{_bindir}/yaml

%clean
rm -rf $RPM_BUILD_ROOT

