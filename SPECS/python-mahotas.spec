Name: python-mahotas
Summary: Python Mahotas Imaging Library
License: As-Is
Vendor: LuisPedro.org
URL: http://luispedro.org/software/mahotas
Group: Development/Tools

Packager: Thornton Prime <thornton@yoyoweb.com>
Distribution: FDM 6

Version: 20140212
Release: 1.fdm
Epoch: %( date +"%Y%m%d" )

%define python_package mahotas
%define python_version %( python -c 'import sys; print sys.version.split()[0]' )
%define python_version_short %( python -c 'import sys; print ".".join(sys.version.split()[0].split(".")[:2])' )
%define python_site_packages %( python -c 'import sys; print [x for x in sys.path if x[-13:] == "site-packages" ][0]' )

Source: %{python_package}-%{version}.tar.gz

%description
Mahotas is a computer vision and image processing library for Python.

%changelog
* Wed Feb 12 2014 Thornton Prime <thornton@yoyoweb.com> []
- 

%prep
%setup -q -n %{python_package}-%{version}

%build
env CFLAGS="%{optflags}" %{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install --root=%{buildroot} --record=INSTALLED_FILES
find %{buildroot} -name '*.pyo' -exec rm {} \;
#find %{buildroot} -type f -name '*.pyo' -printf '/%P%f\n' >> INSTALLED_FILES


%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
/usr/lib64/python2.7/site-packages/mahotas
/usr/lib64/python2.7/site-packages/mahotas-1.1.0-py2.7.egg-info
%doc README.*
%doc AUTHORS CITATION COPYING
%doc docs/*

