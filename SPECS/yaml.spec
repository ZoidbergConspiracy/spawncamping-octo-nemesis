Name: yaml
Summary: Command line YAML processor
License: MIT
Group: System/Utilities

%define git_tag 1.14.0
%define git_version  %{git_tag}
%define git_path mikefarah/%{name}

Version: %{git_version}
Release: 0.fdm
BuildArch: x86_64
URL: https://github.com/%{git_path}
Prefix: %{_prefix}

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
yaml is a lightweight and flexible command-line YAML processor

The aim of the project is to be the jq or sed of yaml files.

%changelog
* Thu Aug 31 2017 Thornton Prime <thornton.prime@gmail.com> [1.12]
- Update and build with go1.9
* Thu Jul 13 2017 Thornton Prime <thornton.prime@gmail.com> [1.11]
- Build for FDM26
* Wed Apr 26 2017 Thornton Prime <thornton.prime@gmail.com> [1.10]
* Wed Apr 12 2017 Thornton Prime <thornton.prime@gmail.com> [1.8]
* Wed Feb  9 2017 Thornton Prime <thornton.prime@gmail.com> [1.5]
- Basic build from Github

%files
%defattr(-,root,root)
%{_bindir}/yaml

%prep

%setup -cT
export GOPATH=`pwd`
git clone https://github.com/%{git_path}.git src/github.com/%{git_path}
(
  cd src/github.com/%{git_path}
  git checkout -b %{git_version}
  git branch --set-upstream-to=origin/master %{git_version}
)

%build
export GOPATH=`pwd`
go get -f -u github.com/%{git_path}

%install
%{__install} -D bin/yaml ${RPM_BUILD_ROOT}%{_bindir}/yaml

%clean
rm -rf $RPM_BUILD_ROOT

