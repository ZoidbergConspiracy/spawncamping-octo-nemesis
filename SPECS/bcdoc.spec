%define name bcdoc
%define version 0.12.2
%define unmangled_version 0.12.2
%define unmangled_version 0.12.2
%define release 1

Summary: ReST document generation tools for botocore.
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{unmangled_version}.tar.gz
License: Apache
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Mitch Garnaat <mitch@garnaat.com>
Url: https://github.com/botocore/bcdoc

%description
bcdoc
=====

|Build Status|


Tools to help document botocore-based projects

.. |Build Status| image:: https://travis-ci.org/boto/bcdoc.png?branch=develop
   :target: https://travis-ci.org/boto/bcdoc


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
