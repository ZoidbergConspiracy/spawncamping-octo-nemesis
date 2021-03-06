Name: python-simple-pbkdf2
Summary: PBKDF2 for Python
License: BSD
Vendor:  Armin Ronacher
URL: https://pypi.python.org/pypi/simple-pbkdf2/
Group: Development/Tools

Packager: Thornton Prime <thornton@yoyoweb.com>
Distribution: FDM 6

Version: 1.0
Release: 1.fdm
Epoch: %( date +"%Y%m%d" )
BuildArch: noarch

%define python_package simple-pbkdf2
%define python_version %( python -c 'import sys; print sys.version.split()[0]' )
%define python_version_short %( python -c 'import sys; print ".".join(sys.version.split()[0].split(".")[:2])' )
%define python_site_packages %( python -c 'import sys; print [x for x in sys.path if x[-13:] == "site-packages" ][0]' )

# Turn off the brp-python-bytecompile script
%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')

Source: https://pypi.python.org/packages/source/s/simple-pbkdf2/%{python_package}-%{version}.tar.gz 

%description
Unlike bcrypt this is easy to understand, secure enough given a sufficently
random salt and implemented on top of the stdlib in about 20 lines of code.
Also easy to understand and analyze.

%changelog
* Thu Apr 10 2014 Thornton Prime <thornton@yoyoweb.com> []
- Initial build

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
%doc README

