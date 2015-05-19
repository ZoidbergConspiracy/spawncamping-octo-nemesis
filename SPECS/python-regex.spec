Name: python-regex
Summary: Python Regex
License: GPL
URL: https://pypi.python.org/pypi/regex
Group: Development/Tools

Packager: Thornton Prime <thornton@yoyoweb.com>
Distribution: FDM 6

Version: 20130804
Release: 1.fdm
Epoch: %( date +"%Y%m%d" )
#BuildArch: noarch

%define version_expanded 2013-08-04
%define python_package regex
%define python_version %( python -c 'import sys; print sys.version.split()[0]' )
%define python_version_short %( python -c 'import sys; print ".".join(sys.version.split()[0].split(".")[:2])' )
%define python_site_packages %( python -c 'import sys; print [x for x in sys.path if x[-13:] == "site-packages" ][0]' )

# Turn off the brp-python-bytecompile script
%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')

Source: https://pypi.python.org/packages/source/r/regex/%{python_package}-%{version_expanded}.tar.gz

%description
python-regex is a set of modules for the  Python programming language
which allows you to manipulate  regex rules.

It is released under the terms of the GNU General Public License version 3 or
later.

%changelog
* Sat Oct 27 2012 Thornton Prime <thornton@yoyoweb.com> []
- 

%prep
%setup -q -n %{python_package}-%{version_expanded}

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
%doc README docs/Features.html docs/UnicodeProperties.txt

