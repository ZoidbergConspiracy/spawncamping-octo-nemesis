%define name django-filebrowser
%define version 3.5.2
%define unmangled_version 3.5.2
%define unmangled_version 3.5.2
%define release 1

Summary: Media-Management with Grappelli
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{unmangled_version}.tar.gz
License: UNKNOWN
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Patrick Kranzlmueller, Axel Swoboda, Vaclav Mikolasek (vonautomatisch) <office@vonautomatisch.at>
Url: http://django-filebrowser.readthedocs.org

%description
Django FileBrowser
==================

**Media-Management with Grappelli**.

The FileBrowser is an extension to the `Django <http://www.djangoproject.com>`_ administration interface in order to:

* browse directories on your server and upload/delete/edit/rename files.
* include images/documents to your models/database using the ``FileBrowseField``.
* select images/documents with TinyMCE.

Requirements
------------

FileBrowser 3.5 requires

* Django 1.4 (http://www.djangoproject.com)
* Grappelli 2.4 (https://github.com/sehmaschine/django-grappelli)
* PIL (http://www.pythonware.com/products/pil/)

Documentation
-------------

http://readthedocs.org/docs/django-filebrowser/

Translation
-----------

https://www.transifex.net/projects/p/django-filebrowser/

Releases
--------

* FileBrowser 3.5.3 (Development Version, not yet released, see Branch Stable/3.5.x)
* FileBrowser 3.5.2 (February 22 2013): Compatible with Django 1.4/1.5
* FileBrowser 3.4.3 (April 2012): Compatible with Django 1.3

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
