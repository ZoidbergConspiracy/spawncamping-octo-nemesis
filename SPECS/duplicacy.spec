Name: duplicacy
Summary: New generation cloud backup tool
License: BSD-2-Clause
Group: System/Utilities
URL: https://duplicacy.com/

%define git_version 2.0.0
%define git_path gilbertchen/%{name}

Version: %{git_version}
Release: 0.fdm
BuildArch: x86_64
Prefix: %{_prefix}

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Duplicacy is a new generation cross-platform cloud backup tool based on the
idea of Lock-Free Deduplication. It is the only cloud backup tool that allows
multiple computers to back up to the same storage simultaneously without using
any locks (thus readily amenable to various cloud storage services).

%changelog
* Fri Jun  9 2017 Thornton Prime <thornton.prime@gmail.com> [2.0.0]
- Basic build from Github

%files
%defattr(-,root,root)
%{_bindir}/duplicacy

%prep

%setup -cT
export GOPATH=`pwd`
# git clone https://github.com/%{git_path}.git src/github.com/%{git_path}
git clone https://github.com/%{git_path}.git .
git checkout -b v%{git_version}
git branch --set-upstream-to=origin/master v%{git_version}

%build
export GOPATH=`pwd`
go get ./... || true
go build main/duplicacy_main.go

%install
%{__install} -D duplicacy_main ${RPM_BUILD_ROOT}%{_bindir}/duplicacy

%clean
rm -rf $RPM_BUILD_ROOT

