%define python_major 3

Name: python%{python_major}-pygsheets
Summary: Python Google Sheets API
License: MIT
Group: Development/Tools
URL: http://pygsheets.readthedocs.io/

Packager: Thornton Prime <thornton.prime@gmail.com>
Distribution: FDM 25

Version: 1.0.0
Release: 1.fdm
Epoch: %( date +"%Y%m%d" )

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch
Requires: python-enum python%{python_major}-google-api-client

%description
Simple, intutive library for google sheets which gets most of your work done.

Features:
* Google spreadsheet api v4 support
* Open, create, delete and share spreadsheets using title or key
* Control permissions of spreadsheets.
* Extract range, entire row or column values.
* Do all the updates and push the changes in a batch

%changelog
* Mon Feb 20 2017 Thornton Prime <thornton.prime@gmail.com> [1.0.0]
- Build from git 1.0.0
* Fri Oct 28 2016 Thornton Prime <thornton.prime@gmail.com> [0.4.1]
- Update to 0.4.1
* Thu Apr  7 2016 Thornton Prime <thornton.prime@gmail.com> [0.3.0]
- Updated to pull directly from git
* Sat Oct 27 2012 Thornton Prime <thornton@yoyoweb.com> []
- 
%define python_package pygsheets
%define git_package nithinmurali/%{python_package}
%define git_version v%{version}

%define __python /usr/bin/python%{python_major}
%define python_version %( %{__python} -c 'import sys; print sys.version.split()[0]' )
%define python_version_short %( %{__python} -c 'import sys; print ".".join(sys.version.split()[0].split(".")[:2])' )
%define python_site_packages %( %{__python} -c 'import sys; print [x for x in sys.path if x[-13:] == "site-packages" ][0]' )

# Turn off the brp-python-bytecompile script
%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')

%prep
%setup -cT
git clone https://github.com/%{git_package}.git .
git checkout -b %{git_version}
git branch --set-upstream-to=origin/master %{git_version}

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
%doc README* LICENSE*

