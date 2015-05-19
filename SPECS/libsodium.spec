Summary: 	Library doer NaCl operations
Name: 		libsodium
Version: 	0.4.5
Release: 	1.fdm
License:	LGPL-3.0
URL: 		https://github.com/jedisct1/libsodium
Source0: 	%{name}-%{version}.tar.gz
Group: 		Development/Libraries
BuildRoot: 	%{_tmppath}/%{name}-root

%description
NaCl (pronounced "salt") is a new easy-to-use high-speed
software library for network communication, encryption,
decryption, signatures, etc.

NaCl's goal is to provide all of the core operations
needed to build higher-level cryptographic tools.

Sodium is a portable, cross-compilable, installable,
packageable fork of NaCl (based on the latest released
upstream version nacl-20110221), with a compatible API.

%package devel
Summary: 	Development libraries and headers for libsodium
Group: 		Development/Libraries
Requires:	libsodium = %{version}

%description devel
Development libraries and headers for libsodium.

%prep
%setup -q

%build
%configure --with-example
make

%install
%{makeinstall}
rm -rf $RPM_BUILD_ROOT/usr/share/doc

%changelog
* Fri Nov 22 2013  <edscott@xfce.org> 5.0.11-1
- RPM release

%clean
rm -rf %buildroot

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc README LICENSE ChangeLog AUTHORS THANKS
%{_libdir}/libsodium.so.4.5.0

%files devel
%defattr(-,root,root)
%{_includedir}/sodium.h
%{_includedir}/sodium
%{_libdir}/libsodium.a
%{_libdir}/libsodium.la
%{_libdir}/libsodium.so
%{_libdir}/libsodium.so.4
%{_libdir}/pkgconfig/libsodium.pc
