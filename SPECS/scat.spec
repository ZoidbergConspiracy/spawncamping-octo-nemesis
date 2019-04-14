Name: scat
Summary: Decentralized, trustless backup
License: MIT
Group: System/Utilities
URL: https://github.com/Roman2K/scat

%define git_version 3
%define git_path Roman2K/scat
%define xgit_tag %{git_version}
%define git_tag %( git ls-remote https://github.com/%{git_path}.git | grep HEAD | awk '{ print $1 }' )

Version: %{git_version}_git%( echo %{git_tag} | cut -c 1-8 )
Release: 1.fdm
BuildArch: x86_64
Prefix: %{_prefix}

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description

%changelog
* Sun Apr 14 2019 Thornton Prime <thornton.prime@gmail.com> [3]
- New Build

%files
%defattr(-,root,root)
%{_bindir}/scat

%prep

%setup -cT
export GOPATH=`pwd`
git clone https://github.com/%{git_path}.git src/github.com/%{git_path}
( cd src/github.com/%{git_path}
  git checkout -b %{git_tag}
  git branch --set-upstream-to=origin/master %{git_tag}
)

%build
export GOPATH=`pwd`
go get -u -d github.com/%{git_path}/...
go build -o scat github.com/%{git_path}/cmd

%install
%{__install} -D scat \
  ${RPM_BUILD_ROOT}%{_bindir}/scat

%clean
rm -rf $RPM_BUILD_ROOT

