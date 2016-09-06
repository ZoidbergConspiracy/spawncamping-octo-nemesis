Name: cayley
Summary: Open Source Graph Database
License: Apache 2.0
Group: Applications/Database
Url: https://cayley.io/

%define git_version 0.5.0
%define git_package cayleygraph/cayley

Version: %{git_version}
Release: fdm
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: x86_64

%changelog
* Mon Aug 29 2016 Thornton Prime <thornton.prime@gmail.com> [0.5.0]
- Update to 0.5.0
- Build with go1.7

%description
Cayley is an open-source graph inspired by the graph database behind
Freebase and Google's Knowledge Graph.

Its goal is to be a part of the developer's toolbox where Linked Data
and graph-shaped data (semantic webs, social networks, etc) in general
are concerned.

%files
%defattr(-,root,root)
%{_bindir}/cayley
%doc src/github.com/%{git_package}/{README.md,LICENSE,AUTHORS,CONTRIBUTORS}
%doc src/github.com/%{git_package}/{docs,examples,data}
%doc src/github.com/%{git_package}/cayley.cfg.example

%prep

%setup -cT
export GOPATH=`pwd`
git clone https://github.com/%{git_package}.git src/github.com/%{git_package}
(
  cd src/github.com/%{git_package}
  git checkout -b v%{git_version}
  git branch --set-upstream-to=origin/master v%{git_version}
)
go get -f -u github.com/%{git_package}/... || true


%build
export GOPATH=`pwd`
go build github.com/%{git_package}/cmd/cayley

%install
%{__install} -D bin/cayley ${RPM_BUILD_ROOT}%{_bindir}/cayley

%clean
rm -rf $RPM_BUILD_ROOT

