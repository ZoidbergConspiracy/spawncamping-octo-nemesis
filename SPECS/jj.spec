Name: jj
Summary: JSON Stream Editor
License: MIT
Group: System/Utilities

%define git_tag 1.2.1
%define git_version  %{git_tag}
%define git_path tidwall/%{name}

Version: %{git_version}
Release: 0.fdm
BuildArch: x86_64
URL: https://github.com/%{git_path}
Prefix: %{_prefix}

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
JJ is a command line utility that provides a fast and simple way to retrieve
or update values from JSON documents. It's powered by GJSON and SJSON under
the hood.

It's fast because it avoids parsing irrelevant sections of json, skipping
over values that do not apply, and aborts as soon as the target value has
been found or updated.

%changelog
* Mon Dec 18 2017 Thornton Prime <thornton.prime@gmail.com> [1.0.1]
- Update and build with go1.9
- Basic build from Github

%files
%defattr(-,root,root)
%{_bindir}/jj

%prep

%setup -cT
export GOPATH=`pwd`
git clone https://github.com/%{git_path}.git src/github.com/%{git_path}
(
  cd src/github.com/%{git_path}
  git checkout -b %{git_version}
  git branch --set-upstream-to=origin/master %{git_version}
)

%build
export GOPATH=`pwd`
(
  cd src/github.com/%{git_path}
  make
)

%install
%{__install} -D src/github.com/%{git_path}/jj ${RPM_BUILD_ROOT}%{_bindir}/jj

%clean
rm -rf $RPM_BUILD_ROOT

