Name: hamsterdb
Version: 2.1.3
Release: 1%{?dist}
Summary: Lightweight embedded NoSQL Database

Group: System Environment/Base
License: GPL
URL: http://hamsterdb.com/ 
Source0: http://hamsterdb.com/dl/%{name}-%{version}-unstable.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: boost-devel
%description
hamsterdb is a lightweight embedded "NoSQL" key-value store. It
concentrates on ease of use, high performance, stability and scalability.

%prep
%setup -q -n %{name}-%{version}-unstable

%build
export CFLAGS="$RPM_OPT_FLAGS -ggdb2 -O2 -fno-strict-aliasing"
%{configure}
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
cd build
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_bindir}/*
%{_libdir}/*
%{_includedir}/hamsterdb
%doc README.html version-notes.html hamsterdb-license.txt

%changelog
* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 14-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

