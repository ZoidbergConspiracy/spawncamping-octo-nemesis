Name: goed
Summary: Terminal based code/text editor
Release: fdm
License: MIT
Group: Applications/Editors

%define git_version_prefix 0
%define git_version_date 20160514
%define git_version_tag a7b18b9
%define git_package tcolar/goed

Version: %{git_version_prefix}.%{git_version_date}.%{git_version_tag}
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: x86_64
Url: https://github.com/tcolar/goed

%description
Goed is a Terminal based code/text editor, somewhat inspired by Acme.

%changelog
* Fri Jun 24 2016 Thornton Prime <thornton.prime@gmail.com> [0.20160514.a7b18b9]
- Current version.
* Thu Apr  7 2016 Thornton Prime <thornton.prime@gmail.com> [0.9.0]
- Updated to pull directly from git

%prep

%setup -cT
export GOPATH=`pwd`

git clone https://github.com/%{git_package}.git src/github.com/%{git_package}
(cd src/github.com/%{git_package}; git reset --hard %{git_version_tag} )

%build
export GOPATH=`pwd`
go get -u github.com/%{git_package}

%install
%{__install} -D bin/goed ${RPM_BUILD_ROOT}%{_bindir}/goed

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/goed


