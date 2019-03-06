Name: brig
Summary: File synchronization on top of ipfs with git-like interface
License: MIT
Group: System/Utilities
URL: https://brig.io

%define git_version 0.2.0
%define git_path sahib/brig
%define Xgit_tag v%{git_version}
%define git_tag %( git ls-remote https://github.com/%{git_path}.git | grep HEAD | awk '{ print $1 }' | cut -c 1-8 )

Version: %{git_version}_%{git_tag}git
Release: 1.fdm
BuildArch: x86_64
Prefix: %{_prefix}

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
brig is a distributed & secure file synchronization tool with version
control. It is based on IPFS, written in Go and will feel familiar to
git users.

%changelog
* Mon Oct 02 2017 Thornton Prime <thornton.prime@gmail.com> [0.4.11]
- Update and build with go1.9

%files
%defattr(-,root,root)
%{_bindir}/brig

%prep

%setup -cT
export GOPATH=`pwd`
git clone https://github.com/%{git_path}.git src/github.com/%{git_path}
# git clone https://github.com/%{git_path}.git .
(
  cd src/github.com/%{git_path}
  git checkout -b %{git_tag}
  git branch --set-upstream-to=origin/master %{git_tag}
)

%build
export GOPATH=`pwd`
go get -u -v -d github.com/%{git_path}
(
  cd src/github.com/%{git_path}
  make build GOBIN=${GOPATH}/bin
)

%install
%{__install} -D bin/brig \
  ${RPM_BUILD_ROOT}%{_bindir}/brig

%clean
rm -rf $RPM_BUILD_ROOT

