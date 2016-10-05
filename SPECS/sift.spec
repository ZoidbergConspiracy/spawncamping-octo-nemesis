Name: sift
Summary: A fast and powerful open source alternative to grep.
License: GPL
Group: Applications/Text
Url: https://sift-tool.org/

%define git_version 0.8.0
%define git_package svent/sift

Version: %{git_version}
Release: fdm
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: x86_64

%changelog
* Fri Sep 16  2016 Thornton Prime <thornton.prime@gmail.com> [0.8.0]
- Update to 0.8.0
- Build with go1.7

%description
Most of the existing tools for searching through large amounts of text are
either fast but inflexible (the original grep) or slightly more flexible
but slow or complicated to install.

sift is an alternative that aims for both speed and flexibility - i.e.
adding features while trying to reach (or even surpass) the performance
of the original grep. The additional features include gitignore support,
conditions (e.g. match A only when preceded by B within X lines) , full
multi-core support and multiline matching. 

%files
%defattr(-,root,root)
%{_bindir}/sift
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
%{__install} -D bin/sift ${RPM_BUILD_ROOT}%{_bindir}/sift

%clean
rm -rf $RPM_BUILD_ROOT

