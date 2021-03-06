%define name pypuzzle
%define version 1.1
%define unmangled_version 1.1
%define release 1

Summary: PyPuzzle -- A Python binding for libpuzzle
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{unmangled_version}.tar.gz
License: UNKNOWN
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
Vendor: Archangel_SDY <Archangel.SDY@gmail.com>
Url: https://github.com/ArchangelSDY/PyPuzzle

%description
This module provides Python bindings for libpuzzle.

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
