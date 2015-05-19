# OpenSUSE spec file format
Summary: 	Library to create and manage 64-bit disk based hash tables	
Name: 		libdbh2
Version: 	5.0.11
Release: 	1
License:	LGPL-3.0
URL: 		http://dbh.sourceforge.net/
Source0: 	%{name}-%{version}.tar.gz
#Source0: 	http://sf.net/projects/dbh/files/%%{version}/dbh-%%{version}.tar.gz
Group: 		Development/Libraries/C and C++
BuildRoot: 	%{_tmppath}/%{name}-root

BuildRequires:	libtool >= 2.2.6
BuildRequires:	fdupes
BuildRequires:	gtk-doc
BuildRequires:	pkgconfig


%description
Library to create and manage hash tables residing 
on disk. Associations are made between keys and 
values so that for a given a key the value can be 
found and loaded into memory quickly. Being disk based 
allows for large and persistent hashes. 64 bit support
allows for hashtables with sizes over 4 Gigabytes on 32
bit systems. Cuantified key generation allows for 
minimum access time on balanced multidimensional trees.

%prep
%setup -q

%build
%configure --with-examples=no
make
strip -s src/.libs/libdbh.so.2.0.1

%install
make install DESTDIR=%buildroot mandir=%{_mandir}
# create symlinks for man pages
%fdupes -s %buildroot/%_mandir

%changelog
* Fri Nov 22 2013  <edscott@xfce.org> 5.0.11-1
- RPM release

%clean
rm -rf %buildroot

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc README TODO ChangeLog NEWS AUTHORS examples/simple_hash.c examples/filesystem.c
%{_libdir}/libdbh.so.2.0.1
%{_libdir}/libdbh.la

%package devel
Summary: 	Library to create and manage 64-bit disk based hash tables	
Group: 		Development/Libraries/C and C++
Requires:	libdbh2 >= 5.0.11

%description devel
Library to create and manage hash tables residing 
on disk. Associations are made between keys and 
values so that for a given a key the value can be 
found and loaded into memory quickly. Being disk based 
allows for large and persistent hashes. 64 bit support
allows for hashtables with sizes over 4 Gigabytes on 32
bit systems. Cuantified key generation allows for 
minimum access time on balanced multidimensional trees.

%files devel
%defattr(-,root,root)
%dir %{_includedir}/dbh 
%dir %{_datadir}/dbh 
%dir %{_datadir}/gtk-doc/html/dbh 
%{_includedir}/dbh/dbh.h
%{_mandir}/man1/dbh.1.gz
%{_mandir}/man1/dbh.h.1.gz
%{_mandir}/man3/dbh_close.3.gz
%{_mandir}/man3/dbh_create.3.gz
%{_mandir}/man3/dbh_destroy.3.gz
%{_mandir}/man3/dbh_erase.3.gz
%{_mandir}/man3/dbh_exit_fanout.3.gz
%{_mandir}/man3/dbh_exit_sweep.3.gz
%{_mandir}/man3/dbh_fanout.3.gz
%{_mandir}/man3/dbh_find.3.gz
%{_mandir}/man3/dbh_foreach_fanout.3.gz
%{_mandir}/man3/dbh_foreach_sweep.3.gz
%{_mandir}/man3/dbh_genkey.3.gz
%{_mandir}/man3/dbh_genkey2.3.gz
%{_mandir}/man3/dbh_load.3.gz
%{_mandir}/man3/dbh_load_address.3.gz
%{_mandir}/man3/dbh_load_child.3.gz
%{_mandir}/man3/dbh_load_parent.3.gz
%{_mandir}/man3/dbh_macros.3.gz
%{_mandir}/man3/dbh_open.3.gz
%{_mandir}/man3/dbh_open_ro.3.gz
%{_mandir}/man3/dbh_orderkey.3.gz
%{_mandir}/man3/dbh_prune.3.gz
%{_mandir}/man3/dbh_regen_fanout.3.gz
%{_mandir}/man3/dbh_regen_sweep.3.gz
%{_mandir}/man3/dbh_set_data.3.gz
%{_mandir}/man3/dbh_set_key.3.gz
%{_mandir}/man3/dbh_set_recordsize.3.gz
%{_mandir}/man3/dbh_set_size.3.gz
%{_mandir}/man3/dbh_settempdir.3.gz
%{_mandir}/man3/dbh_sweep.3.gz
%{_mandir}/man3/dbh_unerase.3.gz
%{_mandir}/man3/dbh_unprune.3.gz
%{_mandir}/man3/dbh_update.3.gz
%{_mandir}/man3/dbh_writeheader.3.gz
%{_datadir}/gtk-doc/html/dbh/DBH.html
%{_datadir}/gtk-doc/html/dbh/calc.png
%{_datadir}/gtk-doc/html/dbh/ch01.html
%{_datadir}/gtk-doc/html/dbh/home.png
%{_datadir}/gtk-doc/html/dbh/index.html
%{_datadir}/gtk-doc/html/dbh/index.sgml
%{_datadir}/gtk-doc/html/dbh/left.png
%{_datadir}/gtk-doc/html/dbh/right.png
%{_datadir}/gtk-doc/html/dbh/style.css
%{_datadir}/gtk-doc/html/dbh/up.png
%{_datadir}/dbh/Makefile.am
%{_datadir}/dbh/dbh.vim
%{_datadir}/dbh/filesystem.c
%{_datadir}/dbh/simple_hash.c
%{_libdir}/libdbh.a
%{_libdir}/libdbh.so
%{_libdir}/pkgconfig/dbh2.pc
%{_libdir}/libdbh.so.2

