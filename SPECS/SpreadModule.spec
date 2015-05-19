%define name SpreadModule
%define version 1.5v4
%define unmangled_version 1.5v4
%define release 1

Summary:  SpreadModule:  Python wrapper for Spread client libraries
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{unmangled_version}.tar.gz
License: Python
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
Vendor: Zope Corporation <zodb-dev@zope.org>
Url: http://zope.org/Members/tim_one/spread

%description
This package contains a simple Python wrapper module for the Spread
toolkit.  The wrapper is known to be compatible with Python 2.3 and 2.4.
It may work with earlier Pythons, but this has not been tested.

Spread (www.spread.org) is a group communications package.  You'll
need to download and install it separately.  The Python API has been
built and tested against Spreads 3.16.1 through 3.17.3, although at
least Spread 3.17 is required to use this version of the wrapper.
3.17.3 is recommended.

Copyright (c) 2001-2005 Python Software Foundation.  All rights reserved.

This code is released under the standard PSF license.
See the file LICENSE.


%prep
%setup -n %{name}-%{unmangled_version}

%build
env CFLAGS="$RPM_OPT_FLAGS" python setup.py build

%install
python setup.py install -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)
