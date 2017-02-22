%define python_version 2
%define __python /usr/bin/python2

Name: python%{python_version}-pycrypto
Summary: Python Cryptography Toolkit
License: Apache
URL: https://www.dlitz.net/software/pycrypto/
Group: Development/Tools

Packager: Thornton Prime <thornton.prime@gmail.com>
Distribution: FDM 6

Version: 2.6
Release: 1.fdm
Epoch: %( date +"%Y%m%d" )

%description
This is a collection of both secure hash functions (such as SHA256 and
RIPEMD160), and various encryption algorithms (AES, DES, RSA, ElGamal,
etc.).  The package is structured to make adding new modules easy.

%changelog
* Fri Oct 28 2016 Thornton Prime <thornton.prime@gmail.com> [0.4.1]
- Update to 0.4.1
* Thu Apr  7 2016 Thornton Prime <thornton.prime@gmail.com> [0.3.0]
- Updated to pull directly from git
* Sat Oct 27 2012 Thornton Prime <thornton@yoyoweb.com> []
- 

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%define python_package pycrypto
%define git_package dlitz/pycrypto
%define git_version v%{version}

%define python_version %( %{__python} -c 'import sys; print sys.version.split()[0]' )
%define python_version_short %( %{__python} -c 'import sys; print ".".join(sys.version.split()[0].split(".")[:2])' )
%define python_site_packages %( %{__python} -c 'import sys; print [x for x in sys.path if x[-13:] == "site-packages" ][0]' )

# Turn off the brp-python-bytecompile script
%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')

%prep
%setup -cT
git clone https://github.com/%{git_package}.git .
git checkout -b %{git_version}
git branch --set-upstream-to=origin/master %{git_version}

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
%doc README* COPYRIGHT* ACKS*

