Name: leptonica
Version: 1.69
Release: 1%{?dist}
Summary: Image processing and analysis library

Group: System Environment/Base
License: BSD
URL: http://www.leptonica.com/ 
Source0: http://www.leptonica.com/source/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
Leptonica is a pedagogically-oriented open source site containing software
that is broadly useful for image processing and image analysis applications.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags} CFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_bindir}/*
%{_libdir}/*
%{_includedir}/leptonica
%doc README.html version-notes.html leptonica-license.txt

%changelog
* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 14-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

