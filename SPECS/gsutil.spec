%define name gsutil
%define version 3.37
%define unmangled_version 3.37
%define unmangled_version 3.37
%define release 1

Summary: A command line tool for interacting with cloud storage services.
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{unmangled_version}.tar.gz
License: Apache 2.0
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Google Inc. <gs-team@google.com>
Url: https://developers.google.com/storage/docs/gsutil

%description

gsutil is a Python application that lets you access Google Cloud Storage from
the command line. You can use gsutil to do a wide range of bucket and object
management tasks, including:
 * Creating and deleting buckets.
 * Uploading, downloading, and deleting objects.
 * Listing buckets and objects.
 * Moving, copying, and renaming objects.
 * Editing object and bucket ACLs.


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
