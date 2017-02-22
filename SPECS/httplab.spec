Name: httplab
Summary: An Interactive Web Server
License: MIT
Group: System/Utilities
Url: https://github.com/gchaincl/httplab

%define git_url gchaincl/%{name}
# %define git_version 0.9.5
%define git_version %( git ls-remote https://github.com/%{git_url}.git | grep HEAD | cut -c 1-12 )

# Version: 0.9.5
Version: 0.%(date  +"%Y%m%d" ).%{git_version}.git
Release: 1.fdm
BuildArch: x86_64
Prefix: %{_prefix}
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
An interactive web server.

HTTPLabs let you inspect HTTP requests and forge responses.

%changelog
* Wed Feb 22 2017 Thornton Prime <thornton.prime@gmail.com> [0.git]
- New build from github template
- Compile with go1.8

%files
%defattr(-,root,root)
%{_bindir}/httplab

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
go get -f -u github.com/%{git_url}

%install
%{__install} -D bin/httplab ${RPM_BUILD_ROOT}%{_bindir}/httplab

%clean
rm -rf $RPM_BUILD_ROOT

