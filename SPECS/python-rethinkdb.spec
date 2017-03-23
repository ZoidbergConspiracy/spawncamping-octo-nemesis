Name: python-rethinkdb
Summary: Python RethinkDB Driver
License: Apache
URL: https://github.com/uiri/rethinkdb
Group: Development/Tools

Packager: Thornton Prime <thornton.prime@gmail.com>
Distribution: FDM 25

%define python_package rethinkdb

Version: 2.3.5
Release: 1.fdm
Epoch: %( date +"%Y%m%d" )
BuildArch: noarch

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%changelog
* Wed Mar 16 2017 Thornton Prime <thornton.prime@gmail.com> [2.3.5]
- Build for FDM25
* Thu Sep 01 2016 Thornton Prime <thornton.prime@gmail.com> [2.3.0.post6]
- Build for FDM24
* Thu Jun 19 2014 Thornton Prime <thornton.prime@gmail.com> [0.0.9.20140619]
- Initial build based off git snapshot.

%description
Python client driver for RethinkDB.

%define python_package rethinkdb
%define git_package rethinkdb/%{python_package}
%define git_version v%{version}

%define python_version %( %{__python} -c 'import sys; print sys.version.split()[0]' )
%define python_version_short %( %{__python} -c 'import sys; print ".".join(sys.version.split()[0].split(".")[:2])' )
%define python_site_packages %( %{__python} -c 'import sys; print [x for x in sys.path if x[-13:] == "site-packages" ][0]' )

# Turn off the brp-python-bytecompile script
%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')

%prep
%setup -cT
git clone https://github.com/%{git_package}.git .
git checkout -b %{git_version}
# git branch --set-upstream-to=origin/master %{git_version}

%build
./configure --allow-fetch
make -C ./drivers/python

%install
%{__rm} -rf %{buildroot}
( cd drivers/python
%{__python} setup.py install --root=%{buildroot} --record=INSTALLED_FILES
# find %{buildroot} -type f -name '*.pyo' -printf '/%P%f\n' >> INSTALLED_FILES
)
mv drivers/python/INSTALLED_FILES .

%clean
%{__rm} -rf %{buildroot}

%files -f INSTALLED_FILES
%defattr(-,root,root)
%doc README*

