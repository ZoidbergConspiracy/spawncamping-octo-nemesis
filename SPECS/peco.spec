Name: peco
Summary: Interactive filtering tool
License: MIT
Group: System/Utilities

%define git_version 0.4.7
%define git_url peco/%{name}

Version: %{git_version}
Release: 0.fdm
BuildArch: x86_64
URL: https://github.com/%{git_url}
Prefix: %{_prefix}

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: glide

%description
peco (pronounced peh-koh) is based on a python tool, percol. percol was
darn useful, but I wanted a tool that was a single binary, and forget
about python. peco is written in Go, and therefore you can just grab
the binary releases and drop it in your $PATH.

peco can be a great tool to filter stuff like logs, process stats, find
files, because unlike grep, you can type as you think and look through
the current results.

%changelog
* Wed Feb  9 2017 Thornton Prime <thornton.prime@gmail.com> [1.5]
- Basic build from Github

%files
%defattr(-,root,root)
%{_bindir}/peco

%prep

%setup -cT
export GOPATH=`pwd`
git clone https://github.com/%{git_url}.git src/github.com/%{git_url}
(
  cd src/github.com/%{git_url}
  git checkout -b %{git_version}
  git branch --set-upstream-to=origin/master %{git_version}
  glide install
)

%build
export GOPATH=`pwd`
mkdir ${GOPATH}/bin
(
  cd src/github.com/%{git_url}
  go build cmd/peco/peco.go
  mv peco ${GOPATH}/bin/
)

%install
%{__install} -D bin/peco ${RPM_BUILD_ROOT}%{_bindir}/peco

%clean
rm -rf $RPM_BUILD_ROOT

