Name: python-authomatic
Summary: Python Authomatic
License: Apache
URL: http://peterhudec.github.io/authomatic/
Group: Development/Tools

Packager: Thornton Prime <thornton.prime@gmail.com>
Distribution: FDM 6

Version: 0.0.9.20140619
Release: 1.fdm
Epoch: %( date +"%Y%m%d" )
BuildArch: noarch

%define python_package authomatic
%define python_version %( python -c 'import sys; print sys.version.split()[0]' )
%define python_version_short %( python -c 'import sys; print ".".join(sys.version.split()[0].split(".")[:2])' )
%define python_site_packages %( python -c 'import sys; print [x for x in sys.path if x[-13:] == "site-packages" ][0]' )

# Turn off the brp-python-bytecompile script
%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')

Source: %{python_package}-%{version}.tar.gz

Requires: python-openid

%description
iAuthomatic is an authorization / authentication client library for Python
web applications inspired by Alex Vagin’s Simpleauth.

%changelog
* Thu Jun 19 2014 Thornton Prime <thornton.prime@gmail.com> [0.0.9.20140619]
- Initial build based off git snapshot.

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
%doc README* LICENSE.txt
%doc doc/* examples

