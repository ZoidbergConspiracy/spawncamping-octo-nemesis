Name: python-contextlib2
Summary: Python Contextlib Backport
License: GPL
URL: https://pypi.python.org/pypi/contextlib2
Group: Development/Tools

Packager: Thornton Prime <thornton@yoyoweb.com>
Distribution: FDM 6

Version: 0.4.0
Release: 1.fdm
Epoch: %( date +"%Y%m%d" )
BuildArch: noarch

%define version_expanded 0.4.0
%define python_package contextlib2
%define python_version %( python -c 'import sys; print sys.version.split()[0]' )
%define python_version_short %( python -c 'import sys; print ".".join(sys.version.split()[0].split(".")[:2])' )
%define python_site_packages %( python -c 'import sys; print [x for x in sys.path if x[-13:] == "site-packages" ][0]' )

# Turn off the brp-python-bytecompile script
%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')

Source: https://pypi.python.org/packages/source/r/contextlib2/%{python_package}-%{version_expanded}.tar.gz

%description
contextlib2 is a backport of the standard library's contextlib module to earlier Python versions.

It also serves as a real world proving ground for possible future enhancements to the standard library version.

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
%doc README.txt NEWS.rst VERSION.txt LICENSE.txt
%doc docs/*

