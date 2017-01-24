%define __python /usr/bin/python3
Name: python3-cx_Freeze
Summary: Python Scripts to freeze and unfreeze executables
License: PSF
URL: http://cx-freeze.readthedocs.io/en/latest/
Group: Development/Tools

Packager: Thornton Prime <thornton.prime@gmail.com>
Distribution: FDM

%define python_package cx_Freeze
%define hg_source https://bitbucket.org/anthony_tuininga/cx_freeze
%define hg_version 5.0.1

# Version: %{hg_version}
Version: 0.hg%( date +"%Y%m%d" )
Release: 1.fdm
Epoch: %( date +"%Y%m%d" )
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%changelog
* Fri Jan 20 2017 Thornton Prime <thornton.prime@gmail.com> [hg]
- Build for FDM25

%description
cx_Freeze is a set of scripts and modules for freezing Python scripts into
executables in much the same way that py2exe and py2app do. Unlike these
two tools, cx_Freeze is cross platform and should work on any platform that
Python itself works on. It requires Python 2.7 or higher and does work with
Python 3.

%define python_version %( %{__python} -c 'import sys; print ( sys.version.split()[0] )' )
%define python_version_short %( %{__python} -c 'import sys; print ( ".".join(sys.version.split()[0].split(".")[:2]) )' )
%define python_site_packages %( %{__python} -c 'import sys; print ( [x for x in sys.path if x[-13:] == "site-packages" ][0] )' )

# Turn off the brp-python-bytecompile script
%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')

%prep
%setup -cT
hg clone -u %{hg_version} %{hg_source} .

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

