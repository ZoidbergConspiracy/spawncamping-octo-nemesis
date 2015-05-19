Name: python-gspread
Summary: Python Google Spreadsheets API
License: Apache
URL: https://github.com/burnash/gspread
Group: Development/Tools

Packager: Thornton Prime <thornton.prime@gmail.com>
Distribution: FDM 6

Version: svn.20140718
Release: 1.fdm
Epoch: %( date +"%Y%m%d" )
BuildArch: noarch

%define python_package python-gspread
%define python_version %( python -c 'import sys; print sys.version.split()[0]' )
%define python_version_short %( python -c 'import sys; print ".".join(sys.version.split()[0].split(".")[:2])' )
%define python_site_packages %( python -c 'import sys; print [x for x in sys.path if x[-13:] == "site-packages" ][0]' )

# Turn off the brp-python-bytecompile script
%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')

Source: https://pypi.python.org/packages/source/g/%{python_package}/%{python_package}.tar.gz

%description
Manage your spreadsheets with gspread in Python.

Features:

    Open a spreadsheet by its title or url.
    Extract range, entire row or column values.
    Independent of Google Data Python client library.
    Python 3 support.


%changelog
* Sat Oct 27 2012 Thornton Prime <thornton@yoyoweb.com> []
- 

%prep
%setup -q -n %{python_package}

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

