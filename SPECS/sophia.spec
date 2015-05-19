%global __os_install_post %{nil}

Summary: Simple and Fast Key-Value Database
Name: sophia
Version: 20131212
Release: 1.fdm
Source0: %{name}-%{version}.tar.gz
License: BSD
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
Vendor: Dmitry Simonenko <pmwkaa@gmail.com>
Url: http://sphia.org/

%description
Sophia is a modern embeddable key-value database designed for a high load
environment.

It has unique architecture that was created as a result of research and
rethinking of primary algorithmic constraints, associated with a getting
popular Log-file based data structures, such as LSM-tree.

%package devel
Summary: Development files for Sophia Database
Group: Development/Libraries

%description devel
Development headers and libraries for Sophia database.

%prep
%setup -n %{name}-%{version}

%build
make %{?_smp_mflags}

%install
mkdir -p ${RPM_BUILD_ROOT}%{_libdir}
cp -d db/*.so* ${RPM_BUILD_ROOT}%{_libdir}
cp db/*.a ${RPM_BUILD_ROOT}%{_libdir}
mkdir -p ${RPM_BUILD_ROOT}%{_includedir}/sophia
cp db/sophia.h db/sp.h ${RPM_BUILD_ROOT}%{_includedir}/sophia

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%defattr(-,root,root)
%{_libdir}/*.so*
%doc README COPYRIGHT

%files devel
%defattr(-,root,root)
%{_libdir}/*.a
%{_includedir}/sophia
