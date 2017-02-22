Name: upspin
Summary: An Interactive Web Server
License: BSD
Group: System/Utilities
Url: https://upspin.io

%define git_url upspin/%{name}
# %define git_version 0.9.5
%define git_version %( git ls-remote https://github.com/%{git_url}.git | grep HEAD | cut -c 1-12 )

# Version: 0.9.5
Version: 0.%(date  +"%Y%m%d" ).%{git_version}.git
Release: 1.fdm
BuildArch: x86_64
Prefix: %{_prefix}
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
A framework for naming and sharing files and other data securely,
uniformly, and globally: a global name system of sorts.

It is not a file system, but a set of protocols and reference
implementations that can be used to join things like file systems
and other storage services to the name space.

%changelog
* Wed Feb 22 2017 Thornton Prime <thornton.prime@gmail.com> [0.git]
- New build from github template
- Compile with go1.8

%files
%defattr(-,root,root)
%{_bindir}/*

%prep

%setup -cT
export GOPATH=`pwd`
git clone https://github.com/%{git_url}.git src/github.com/%{git_url}
(
  cd src/github.com/%{git_url}
  git checkout -b %{git_version}
  git branch --set-upstream-to=origin/master %{git_version}
)

%build
export GOPATH=`pwd`
# go get -f -u github.com/%{git_url}
go get -u upspin.io/cmd/...

%install
mkdir -p ${RPM_BUILD_ROOT}%{_bindir}/
%{__install} bin/* ${RPM_BUILD_ROOT}%{_bindir}/

%clean
rm -rf $RPM_BUILD_ROOT

