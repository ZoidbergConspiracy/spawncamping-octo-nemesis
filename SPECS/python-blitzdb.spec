%define python_major 3
  
Name: python%{python_major}-blitzdb
Summary: Document-oriented database for Python that is backend-agnostic
License: MIT
Group: Development/Tools

Packager: Thornton Prime <thornton.prime@gmail.com>
Distribution: FDM

%define python_package blitzdb
%define git_path adewes/%{python_package}
%define git_version 0.4.4
%define xgit_tag v%{git_version}
%define git_tag %( git ls-remote https://github.com/%{git_path}.git | grep HEAD | awk '{ print $1 }' )

#Version: {git_version}
Version: %{git_version}_git%( echo %{git_tag} | cut -c 1-8 )
Release: 3.fdm
Epoch: %( date +"%Y%m%d" )
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch

Requires: python%{python_major}-six

%changelog
* Thu Jan  11 2018 Thornton Prime <thornton.prime@gmail.com> [0.4.4_gitX]
- Fix version number
* Thu Jan  11 2018 Thornton Prime <thornton.prime@gmail.com> [0.2.12_gitX]
- Updated to latest git version
* Mon Jan  8 2018 Thornton Prime <thornton.prime@gmail.com> [0.2.12]
- Updated to 0.2.12

%description
Blitz is a document-oriented database for Python that is backend-agnostic.
It comes with a flat-file database for JSON documents and provides MongoDB-
like querying capabilities.

%define __python /usr/bin/python%{python_major}
%define python_version %( %{__python} -c 'import sys; print sys.version.split()[0]' )
%define python_version_short %( %{__python} -c 'import sys; print ".".join(sys.version.split()[0].split(".")[:2])' )
%define python_site_packages %( %{__python} -c 'import sys; print [x for x in sys.path if x[-13:] == "site-packages" ][0]' )

# Turn off the brp-python-bytecompile script
%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')

%prep
%setup -cT
git clone https://github.com/%{git_path}.git .
git checkout -b %{git_tag}
git branch --set-upstream-to=origin/master %{git_tag}

%build
env CFLAGS="%{optflags}" %{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install --root=%{buildroot} --record=INSTALLED_FILES
#find %{buildroot} -type f -name '*.pyo' -printf '/%P%f\n' >> INSTALLED_FILES

%clean
%{__rm} -rf %{buildroot}

%files -f INSTALLED_FILES
%defattr(-,root,root)
%doc README.md LICENSE
