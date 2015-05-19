Name: python-lmdb
Summary: Python Binding for LMDB 'Lightning' Database
License: Apache
URL: https://github.com/dw/py-lmdb/
Group: Development/Tools

Packager: Thornton Prime <thornton.prime@gmail.com>
Distribution: FDM 6

Version: 0.84
Release: 1.fdm
Epoch: %( date +"%Y%m%d" )
#BuildArch: noarch

BuildRequires: python-cffi lmdb-devel

%define python_package lmdb
%define python_version %( python -c 'import sys; print sys.version.split()[0]' )
%define python_version_short %( python -c 'import sys; print ".".join(sys.version.split()[0].split(".")[:2])' )
%define python_site_packages %( python -c 'import sys; print [x for x in sys.path if x[-13:] == "site-packages" ][0]' )

# Turn off the brp-python-bytecompile script
%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')

Source: https://pypi.python.org/packages/source/l/%{python_package}/%{python_package}-%{version}.tar.gz

%description
This is a universal Python binding for the LMDB ‘Lightning’ Database. LMDB
is a tiny database with some excellent properties:

* Ordered map interface (keys are always sorted)
* Reader/writer transactions: readers don’t block writers, writers don’t
block readers. Each environment supports one concurrent write transaction.
* Read transactions are extremely cheap.
* Environments may be opened by multiple processes on the same host,
making it ideal for working around Python’s GIL.
* Multiple named databases may be created with transactions covering all
named databases.
* Memory mapped, allowing for zero copy lookup and iteration. This is
optionally exposed to Python using the buffer() interface.
* Maintenance requires no external process or background threads.
* No application-level caching is required: LMDB fully exploits the
operating system’s buffer cache.


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

