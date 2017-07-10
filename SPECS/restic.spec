Name: restic
Summary: Restic Backup Program
License: BSD-2-Clause
Group: System/Utilities
URL: https://restic.github.io/

%define git_version 0.6.1
%define git_path restic/%{name}

Version: %{git_version}
Release: 0.fdm
BuildArch: x86_64
Prefix: %{_prefix}

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
restic is a program that does backups right. The design goals are to
be easy, fast, verifiable, secure, efficient, and free.

%changelog
* Sat Jun  3 2017 Thornton Prime <thornton.prime@gmail.com> [0.6.1]
- Basic build from Github

%files
%defattr(-,root,root)
%{_bindir}/restic

%prep

%setup -cT
export GOPATH=`pwd`
# git clone https://github.com/%{git_path}.git src/github.com/%{git_path}
git clone https://github.com/%{git_path}.git .
git checkout -b v%{git_version}
git branch --set-upstream-to=origin/master v%{git_version}

%build
export GOPATH=`pwd`
go run build.go --goos linux --goarch amd64

%install
%{__install} -D restic ${RPM_BUILD_ROOT}%{_bindir}/restic

%clean
rm -rf $RPM_BUILD_ROOT

