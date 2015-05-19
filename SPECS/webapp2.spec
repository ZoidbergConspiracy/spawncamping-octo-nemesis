%define name webapp2
%define version 2.5.1
%define unmangled_version 2.5.1
%define unmangled_version 2.5.1
%define release 1

Summary: Taking Google App Engine's webapp to the next level!
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{unmangled_version}.tar.gz
License: Apache Software License
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Rodrigo Moraes <rodrigo.moraes@gmail.com>
Url: http://webapp-improved.appspot.com

%description

webapp2
=======
`webapp2`_ is a lightweight Python web framework compatible with Google App
Engine's `webapp`_.

webapp2 is `simple`_. it follows the simplicity of webapp, but
improves it in some ways: it adds better URI routing and exception handling,
a full featured response object and a more flexible dispatching mechanism.

webapp2 also offers the package `webapp2_extras`_ with several optional
utilities: sessions, localization, internationalization, domain and subdomain
routing, secure cookies and others.

webapp2 can also be used outside of Google App Engine, independently of the
App Engine SDK.

For a complete description of how webapp2 improves webapp, see
`webapp2 features`_.

Quick links
-----------

- `User Guide <http://webapp-improved.appspot.com/>`_
- `Repository <http://code.google.com/p/webapp-improved/>`_
- `Discussion Group <https://groups.google.com/forum/#!forum/webapp2>`_
- `@webapp2 <https://twitter.com/#!/webapp2>`_

.. _webapp: http://code.google.com/appengine/docs/python/tools/webapp/
.. _webapp2: http://code.google.com/p/webapp-improved/
.. _simple: http://code.google.com/p/webapp-improved/source/browse/webapp2.py
.. _webapp2_extras: http://webapp-improved.appspot.com/#api-reference-webapp2-extras
.. _webapp2 features: http://webapp-improved.appspot.com/features.html


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
