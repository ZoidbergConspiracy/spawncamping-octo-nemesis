Summary:	Lessfs is an inline data deduplicating filesystem
Name:		lessfs
Version:	1.7.0
Release:	fdm%{?dist}
License:	GPLv3+
Group:		Applications/System
URL:            http://www.lessfs.com
Source:         http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}
BuildRequires:  tokyocabinet-devel 
BuildRequires:  db4-devel 
BuildRequires:  openssl-devel 
BuildRequires:  mhash-devel
BuildRequires:  fuse-devel
BuildRequires:  autoconf

Requires: fuse
Requires: mhash
Requires: tokyocabinet
Requires: db4

%description
Lessfs is an inline data deduplicating filesystem.

%prep
%setup -q

%build
autoconf
export CFLAGS="-O2"
%configure --with-crypto --with-berkeleydb
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install
install -D -m 755 etc/lessfs-init_example %{buildroot}/etc/init.d/lessfs-init_example
install -D -m 755 etc/lessfs.cfg-bdb %{buildroot}/etc/lessfs.cfg-bdb

rm -rf %{buildroot}%{_datadir}/%{name}
rm -rf %{buildroot}%{_libdir}/lib%{name}.a

%clean
rm -rf %{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-, root, root, -)
%doc FAQ ChangeLog COPYING README
%{_bindir}/lessfs
%{_sbindir}/mklessfs
%{_sbindir}/replogtool
%{_sbindir}/lessfsck
%{_sbindir}/listdb
%{_mandir}/man1/lessfs.1.gz
%{_mandir}/man1/replogtool.1.gz
/etc/init.d/lessfs-init_example
/etc/lessfs.cfg-bdb

%changelog
* Sat Apr 21 2011 Mark Ruijter <mruijter@lessfs.com> - 1.5.11
- A bug in configure.in caused DEBUG to support
- to be compiled in when --disable-debug was specified.
- This was a major cause of slow performance reports.
