Name: qri
Summary: P2P Dataset Version Control System
License: GPL-3.0
Group: System/Utilities

%define git_version 0.5.6
%define git_tag v%{git_version}
%define git_path qri-io/%{name}

Version: %{git_version}
Release: 0.fdm
BuildArch: x86_64
URL: https://github.com/%{git_path}
Prefix: %{_prefix}

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Qri is a distributed dataset version control system built with peer-2-peer
data exchange. Peers create datasets, which are stored in versions. Qri
peers form a distributed network to exchange information about their
datasets, which they transmit between each other over the distributed web.

%changelog
* Mon Nov 05 2018 Thornton Prime <thornton.prime@gmail.com> [0.5.6]
- Update and build with go1.9

%files
%defattr(-,root,root)
%{_bindir}/qri

%prep

%setup -cT
export GOPATH=`pwd`
git clone https://github.com/%{git_path}.git src/github.com/%{git_path}
(
  cd src/github.com/%{git_path}
  git checkout -b %{git_tag}
  git branch --set-upstream-to=origin/master %{git_tag}
)

%build
export GOPATH=`pwd`
#go get -f -u github.com/%{git_path}
( 
  cd src/github.com/%{git_path}
  make build
)

%install
%{__install} -D bin/qri ${RPM_BUILD_ROOT}%{_bindir}/qri

%clean
rm -rf $RPM_BUILD_ROOT

