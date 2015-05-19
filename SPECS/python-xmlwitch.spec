Name: python-xmlwitch
Summary: Python XML Generation through context generators
License: GPL
URL: https://pypi.python.org/pypi/xmlwitch
Group: Development/Tools

Packager: Thornton Prime <thornton@yoyoweb.com>
Distribution: FDM 6

Version: 0.2.1
Release: 1.fdm
Epoch: %( date +"%Y%m%d" )
BuildArch: noarch

%define version_expanded 0.2.1
%define python_package xmlwitch
%define python_version %( python -c 'import sys; print sys.version.split()[0]' )
%define python_version_short %( python -c 'import sys; print ".".join(sys.version.split()[0].split(".")[:2])' )
%define python_site_packages %( python -c 'import sys; print [x for x in sys.path if x[-13:] == "site-packages" ][0]' )

# Turn off the brp-python-bytecompile script
%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')

Source: https://pypi.python.org/packages/source/r/xmlwitch/%{python_package}-%{version_expanded}.tar.gz

%description
xmlwitch offers Pythonic XML generation through context generators in a
minimalist implementation with less than 100 lines of code.

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
%doc README.*

