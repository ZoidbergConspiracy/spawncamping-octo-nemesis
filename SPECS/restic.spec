Name: restic
Summary: Restic Backup Program
License: BSD-2-Clause
Group: System/Utilities
URL: https://restic.github.io/

%define git_version 0.9.3
%define git_path restic/%{name}

Version: %{git_version}
Release: 1.fdm
BuildArch: x86_64
Prefix: %{_prefix}

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
restic is a program that does backups right. The design goals are to
be easy, fast, verifiable, secure, efficient, and free.

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
%{_bindir}/restic

%prep

%setup -cT
export GOPATH=`pwd`
# git clone https://github.com/%{git_path}.git src/github.com/%{git_path}
git clone https://github.com/%{git_path}.git restic
(cd restic
git checkout -b v%{git_version}
git branch --set-upstream-to=origin/master v%{git_version}
)

%build
export GOPATH=`pwd`
( cd restic
go run -mod vendor build.go --goos linux --goarch amd64
)

%install
%{__install} -D restic/restic ${RPM_BUILD_ROOT}%{_bindir}/restic

%clean
rm -rf $RPM_BUILD_ROOT

