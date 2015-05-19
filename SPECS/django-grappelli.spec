%define name django-grappelli
%define version 2.4.8
%define unmangled_version 2.4.8
%define unmangled_version 2.4.8
%define release 1

Summary: A jazzy skin for the Django Admin-Interface.
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{unmangled_version}.tar.gz
License: UNKNOWN
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Patrick Kranzlmueller, Axel Swoboda (vonautomatisch) <office@vonautomatisch.at>
Url: http://django-grappelli.readthedocs.org

%description
Django Grappelli
================

**A jazzy skin for the Django admin interface**.

Grappelli is a grid-based alternative/extension to the `Django <http://www.djangoproject.com>`_ administration interface.

Code
----

https://github.com/sehmaschine/django-grappelli

Documentation
-------------

http://readthedocs.org/docs/django-grappelli/

Releases
--------

**Grappelli is always developed against the latest stable Django release and is NOT tested with Djangos trunk.**

* |grappelli| 2.5.0 (November 13th, 2013): Compatible with Django 1.6
* |grappelli| 2.4.8 (November 12th, 2013): Compatible with Django 1.4/1.5

Current development branches:

* |grappelli| 2.5.1 (Development version for Django 1.6, not yet released, see branch Stable/2.5.x)
* |grappelli| 2.4.9 (Development version for Django 1.4/1.5, not yet released, see branch Stable/2.4.x)

Older versions are availabe at GitHub, but are not supported anymore.


%prep
%setup -n %{name}-%{unmangled_version} -n %{name}-%{unmangled_version}

%build
python setup.py build

%install
python setup.py install --single-version-externally-managed -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)
