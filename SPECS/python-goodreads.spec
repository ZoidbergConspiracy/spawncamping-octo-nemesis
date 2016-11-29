Name: python-goodreads
Summary: Python Wrapper for the Goodreads API
License: MIT
URL: https://github.com/sefakilic/goodreads
Group: Development/Tools

Packager: Thornton Prime <thornton.prime@gmail.com>
Distribution: FDM

%define python_package goodreads
%define git_package sefakilic/goodreads
# %define git_version 1.0.0
# %define __python /usr/bin/python2

# Version: %{git_version}
Version: 0.git%( date +"%Y%m%d" )
Release: 1.fdm
Epoch: %( date +"%Y%m%d" )
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires: python-requests python2-xmltodict python-rauth

%changelog
* Mon Nov 28 2016 Thornton Prime <thornton.prime@gmail.com> [1.0.0]
- Build for FDM24

%description
This package provides a Python interface for the Goodreads API. Using it,
you can do pretty much anything that Goodreads allows to do with their
own data.

%define python_version %( %{__python} -c 'import sys; print sys.version.split()[0]' )
%define python_version_short %( %{__python} -c 'import sys; print ".".join(sys.version.split()[0].split(".")[:2])' )
%define python_site_packages %( %{__python} -c 'import sys; print [x for x in sys.path if x[-13:] == "site-packages" ][0]' )

# Turn off the brp-python-bytecompile script
%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')

%prep
%setup -cT
git clone https://github.com/%{git_package}.git .
#git checkout -b v%{git_version}
#git branch --set-upstream-to=origin/master v%{git_version}

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

