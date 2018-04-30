Name: conspire
Summary: Share Secrets with Friends
License: MIT
Group: System/Utilities
Url: https://github.com/ZoidbergConspiracy/conspire

%define git_version 0.9.5
%define git_path zoidbergconspiracy/%{name}

Version: 0.9.5
Release: 4.fdm
BuildArch: x86_64
Prefix: %{_prefix}
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Conspire is a tool for setting up and managing Conspiracies.

It uses PGP/GPG keyrings to encrypts sets of secrets in a special directory,
called a vault. Each keyring is a group of users who are set up as shared
recepients for a secret file, which is stored in the vault.

Sharing secrets among groups of people with GPG is a little awkward,
because there is no facility to manage groups. This tool aims to make it
simpler to manage secrets among groups.

%changelog
* Thu Aug 31 2017 Thornton Prime <thornton.prime@gmail.com> [0.9.5-4.fdm]
- Compile with Go1.9
* Thu Jul 13 2017 Thornton Prime <thornton.prime@gmail.com> [0.9.5]
* Wed Feb 22 2017 Thornton Prime <thornton.prime@gmail.com> [0.9.5]
- New build from github template
- Compile with go1.8
* Tue Nov 29 2016 Thornton Prime <thornton.prime@gmail.com> [0.9.5]
- Build for Fedora 25

* Thu Apr  7 2016 Thornton Prime <thornton.prime@gmail.com> [0.9.5]
- Fixed paths.
- Update to v0.9.5
* Thu Apr  7 2016 Thornton Prime <thornton.prime@gmail.com> [0.9.0]
- Updated to pull directly from git

%files
%defattr(-,root,root)
%{_bindir}/conspire

%prep

%setup -cT
export GOPATH=`pwd`
git clone https://github.com/%{git_path}.git src/github.com/%{git_path}
(
  cd src/github.com/%{git_path}
  git checkout -b v%{git_version}
  git branch --set-upstream-to=origin/master v%{git_version}
)

%build
export GOPATH=`pwd`
go get -f -u github.com/%{git_path}

%install
%{__install} -D bin/conspire ${RPM_BUILD_ROOT}%{_bindir}/conspire

%clean
rm -rf $RPM_BUILD_ROOT

