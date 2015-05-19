Name: python-mmh3
Summary: Python MurmurHash Implementation
License: Public Domain
Vendor: Bollore Telecom
URL: https://pypi.python.org/pypi/mmh3/2.2
Group: Development/Tools

Packager: Thornton Prime <thornton@yoyoweb.com>
Distribution: FDM 6

Version: 2.3
Release: 1.fdm
Epoch: %( date +"%Y%m%d" )

%define python_package mmh3
%define python_version %( python -c 'import sys; print sys.version.split()[0]' )
%define python_version_short %( python -c 'import sys; print ".".join(sys.version.split()[0].split(".")[:2])' )
%define python_site_packages %( python -c 'import sys; print [x for x in sys.path if x[-13:] == "site-packages" ][0]' )

Source: https://pypi.python.org/packages/source/m/mmh3/%{python_package}-%{version}.tar.gz

%description
Python wrapper for MurmurHash (MurmurHash3), a set of fast and robust hash
functions.

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
%doc README.rst

