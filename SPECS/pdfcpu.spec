Name: pdfcpu
Summary: PDF Utility
License: Apache 2.0
Group: System/Utilities
URL: https://github.com/hhrutter/pdfcpu

%define git_version 0.1.14
%define git_base hhrutter
%define git_path %{git_base}/%{name}
%define git_tag %( git ls-remote https://github.com/%{git_path}.git | grep HEAD | awk '{ print $1 }' | cut -c 1-8 )

Version: %{git_version}_%{git_tag}git
Release: 1.fdm
BuildArch: x86_64
Prefix: %{_prefix}

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
PDF processing library from the ground up written in Go with strong
support for batch processing via a rich command line. Over time pdfcpu
aims to support the standard range of PDF processing features and also
any interesting use cases that may present themselves along the way.

%changelog
* Tue Nov 28 2017 Thornton Prime <thornton.prime@gmail.com> [0.8.0]
- Update to 0.8.0
- Update and build with go1.9.2
* Thu Aug 31 2017 Thornton Prime <thornton.prime@gmail.com> [0.7.1]
- Update and build with go1.9
* Sat Jun  3 2017 Thornton Prime <thornton.prime@gmail.com> [0.6.1]
- Basic build from Github

%files
%defattr(-,root,root)
%{_bindir}/pdfcpu

%prep

%setup -cT
export GOPATH=`pwd`
#mkdir -p github.com/%{git_base}
git clone https://github.com/%{git_path}.git src/github.com/%{git_path}
(cd src/github.com/%{git_path}
  git checkout -b %{git_tag}
  git branch --set-upstream-to=origin/master %{git_tag}
  #git checkout -b v%{git_version}
  #git branch --set-upstream-to=origin/master v%{git_version}
)
go get github.com/%{git_path}/cmd/...

%build
export GOPATH=`pwd`
(
go build github.com/%{git_path}/cmd/...
)

%install
%{__install} -D bin/pdfcpu ${RPM_BUILD_ROOT}%{_bindir}/pdfcpu

%clean
rm -rf $RPM_BUILD_ROOT

