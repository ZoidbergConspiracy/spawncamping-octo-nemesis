%define name Python_WebDAV_Library
%define version 0.4.2
%define unmangled_version 0.4.2
%define release 1

Summary: This library provides a WebDAV client.
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{unmangled_version}.tar.gz
License: UNKNOWN
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Deutsches Zentrum fuer Luft- und Raumfahrt e.V. (DLR) <Tobias.Schlauch@dlr.de>
Url: https://launchpad.net/python-webdav-lib

%description
This library provides a WebDAV client including ACP and searching support.

%prep
%setup -n %{name}-%{unmangled_version}

%build
python setup.py build

%install
python setup.py install -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)
