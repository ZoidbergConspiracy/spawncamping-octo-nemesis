Name: python-bitstring
Summary: Python Bitsting Module
License: GPL
Vendor: Bollore Telecom
URL: https://code.google.com/p/python-bitstring/
Group: Development/Tools

Packager: Thornton Prime <thornton@yoyoweb.com>
Distribution: FDM 6

Version: 3.1.1
Release: 1.fdm
Epoch: %( date +"%Y%m%d" )
BuildArch: noarch

%define python_package bitstring
%define python_version %( python -c 'import sys; print sys.version.split()[0]' )
%define python_version_short %( python -c 'import sys; print ".".join(sys.version.split()[0].split(".")[:2])' )
%define python_site_packages %( python -c 'import sys; print [x for x in sys.path if x[-13:] == "site-packages" ][0]' )

Source: https://python-bitstring.googlecode.com/files/%{python_package}-%{version}.zip

%description
A Python module that makes the creation, manipulation and analysis of
binary data as simple and natural as possible.

Bitstrings can be constructed from integers, floats, hex, octal, binary,
bytes or files. They can also be created and interpreted using flexible
format strings.

Bitstrings can be sliced, joined, reversed, inserted into, overwritten,
etc. with simple methods or using slice notation. They can also be read
from, searched and replaced, and navigated in, similar to a file or stream.

Internally the bit data is efficiently stored in byte arrays, the module
has been optimized for speed, and excellent code coverage is given by over
400 unit tests.

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
%doc README.txt release_notes.txt
%doc doc/*

