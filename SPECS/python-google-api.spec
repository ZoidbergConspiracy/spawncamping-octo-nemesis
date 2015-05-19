Name: python-google-api
Summary: Python Google API
License: Apache
URL: http://code.google.com/p/google-api-python-client/
Group: Development/Tools

Packager: Thornton Prime <thornton@yoyoweb.com>
Distribution: FDM 6

Version: 1.2
Release: 1.fdm
Epoch: %( date +"%Y%m%d" )
BuildArch: noarch

%define python_package google-api-python-client
%define python_version %( python -c 'import sys; print sys.version.split()[0]' )
%define python_version_short %( python -c 'import sys; print ".".join(sys.version.split()[0].split(".")[:2])' )
%define python_site_packages %( python -c 'import sys; print [x for x in sys.path if x[-13:] == "site-packages" ][0]' )

Requires: python-uri-templates
Requires: python-httplib2

# Turn off the brp-python-bytecompile script
%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')

Source: https://pypi.python.org/packages/source/g/%{python_package}/%{python_package}-%{version}.tar.gz

%description
The Google API Client for Python is a client library for accessing the
Plus, Moderator, and many other Google APIs.

%changelog
* Sat Oct 27 2012 Thornton Prime <thornton@yoyoweb.com> []
- 

%prep
%setup -q -n %{python_package}-%{version}

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
%doc README* LICENSE FAQ README

