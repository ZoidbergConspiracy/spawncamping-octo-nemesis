Name: perkeep
Summary: Personal storage system for life
License: Apache-2.0
Group: System/Utilities
URL: https://perkeep.github.io/

%define git_path perkeep/%{name}
%define git_version 0.10
%define git_tag %( git ls-remote https://github.com/%{git_path}.git | grep HEAD | awk '{ print $1 }' | cut -c 1-8 )

# Version: %{git_version}
Version: %{git_version}_%{git_tag}git
Release: 1.fdm
BuildArch: x86_64
Prefix: %{_prefix}

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Perkeep is your personal storage system for life： a way of storing,
syncing, sharing, modelling and backing up content.

%changelog
* Tue Nov 28 2017 Thornton Prime <thornton.prime@gmail.com> [0.8.0]
- Update to 0.8.0
- Update and build with go1.9.2
* Thu Aug 31 2017 Thornton Prime <thornton.prime@gmail.com> [0.7.1]
- Update and build with go1.9
* Sat Jun  3 2017 Thornton Prime <thornton.prime@gmail.com> [0.6.1]
- Basic build from Github

%files
%defattr(-,root,root)
%{_bindir}/perkeepd
%{_bindir}/pk
%{_bindir}/pk-get
%{_bindir}/pk-put
%{_bindir}/pk-mount

%prep

%setup -cT
export GOPATH=`pwd`
mkdir -p src
# git clone https://github.com/%{git_path}.git src/github.com/%{git_path}
git clone https://github.com/%{git_path}.git src/perkeep.org
(cd src/perkeep.org
git checkout -b v%{git_version}
#git branch --set-upstream-to=origin/master v%{git_version}
git checkout %{git_tag}
)

%build
export GOPATH=`pwd`
( cd src/perkeep.org
go run make.go
)

%install
%{__install} -D bin/perkeepd ${RPM_BUILD_ROOT}%{_bindir}/perkeepd
%{__install} -D bin/pk ${RPM_BUILD_ROOT}%{_bindir}/
%{__install} -D bin/pk-get ${RPM_BUILD_ROOT}%{_bindir}/
%{__install} -D bin/pk-put ${RPM_BUILD_ROOT}%{_bindir}/
%{__install} -D bin/pk-mount ${RPM_BUILD_ROOT}%{_bindir}/

%clean
rm -rf $RPM_BUILD_ROOT

