Name: micro
Summary: A modern and intuitive terminal-based text editor
License: MIT
Group: Applications/Editors
Url: https://github.com/zyedidia/micro

%define git_version 1.0.2
%define git_package zyedidia/micro

Version: %{git_version}
Release: fdm
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: x86_64

%changelog
* Tue Sep  6 2016 Thornton Prime <thornton.prime@gmail.com> [1.0.2]
- Update to 1.0.2
- Build with go1.7
* Wed Aug 31 2016 Thornton Prime <thornton.prime@gmail.com> [1.0.1]
- Update to 1.0.1
- Build with go1.7

%description
Micro is a terminal-based text editor that aims to be easy to use and intuitive,
while also taking advantage of the full capabilities of modern terminals. It comes
as one single, batteries-included, static binary with no dependencies, and you can
download and use it right now.

As the name indicates, micro aims to be somewhat of a successor to the nano editor
by being easy to install and use in a pinch, but micro also aims to be enjoyable
to use full time, whether you work in the terminal because you prefer it (like
me), or because you need to (over ssh).

%files
%defattr(-,root,root)
%{_bindir}/micro
%doc src/github.com/%{git_package}/{README.md,LICENSE}

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

%install
%{__install} -D bin/micro ${RPM_BUILD_ROOT}%{_bindir}/micro

%clean
rm -rf $RPM_BUILD_ROOT

