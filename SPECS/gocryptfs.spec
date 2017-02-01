Name: gocryptfs
Summary: Encrypted Overlay FUSE
License: MIT
Group: System/Utilities

%define git_version 1.2
%define git_package rfjakob/%{name}

Version: %{git_version}
Release: 0.fdm
BuildArch: x86_64
# Url: https://github.com/%{git_package}
URL: https://nuetzlich.net/gocryptfs/
Prefix: %{_prefix}
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
An encrypted overlay filesystem written in Go.

gocryptfs is built on top the excellent go-fuse
FUSE library and its LoopbackFileSystem API.

%changelog
* Tue Jan 31 2017 Thornton Prime <thornton.prime@gmail.com> [1.2]
- Basic build from Github

%files
%defattr(-,root,root)
%{_bindir}/gocryptfs

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
%{__install} -D bin/gocryptfs ${RPM_BUILD_ROOT}%{_bindir}/gocryptfs

%clean
rm -rf $RPM_BUILD_ROOT

