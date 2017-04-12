Name: tiedot
Summary: NoSQL Database with REST API
License: BSD-2
Group: System/Utilities

%define git_path houzuoguo/%{name}
%define git_tag %( git ls-remote https://github.com/%{git_path}.git | grep HEAD | awk '{ print $1 }' )
# define git_tag 3.3

Version: 3.3_%( echo %{git_tag} | cut -c 1-8 )git
Release: 0.fdm
BuildArch: x86_64
URL: https://github.com/%{git_path}
Prefix: %{_prefix}

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
tiedot is a document database engine that uses JSON as document notation;
it has a powerful query processor that supports advanced set operations;
it can be embedded into your program, or run a stand-alone server using
HTTP for an API. It runs on *nix and Windows operating systems.

%changelog
* Tue Apr 11 2017 Thornton Prime <thornton.prime@gmail.com> [3.3_git]
- Basic build from Github

%files
%defattr(-,root,root)
%{_bindir}/tiedot
%doc LICENSE doc/*
%config /etc/%{name}
%{_bindir}/%{name}
%{_unitdir}/%{name}.service

#%pre
#%systemd_add_pre %{name}.service

#%post
#%systemd_add_post %{name}.service

#%preun
#%systemd_del_preun %{name}.service

#%postun
#%systemd_del_postun %{name}.service

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
go get -f -u github.com/%{git_path}
mv src/github.com/%{git_path}/LICENSE .
mv src/github.com/%{git_path}/doc .

%install
%{__install} -D bin/tiedot %{buildroot}%{_bindir}/tiedot
install -D -p -m 0644 src/github.com/%{git_path}/distributable/etc/%{name} %{buildroot}%{_sysconfdir}/%{name}
install -D -p -m 0644 src/github.com/%{git_path}/distributable/%{name}.service %{buildroot}%_unitdir/%{name}.service

%clean
rm -rf $RPM_BUILD_ROOT
