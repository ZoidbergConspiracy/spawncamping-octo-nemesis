Name: keepassx
Version: 2.0a4
Release: 1%{?dist}
Summary: Password keeper

Group: System Environment/Base
License: GPL
URL: http://www.keepassx.org/ 
Source0: http://www.keepassx.org/dev/attachments/download/36/keepassx-2.0-alpha4.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
KeePassX saves many different information e.g. user names, passwords, urls,
attachments and comments in one single database. For a better management
user-defined titles and icons can be specified for each single entry.
Furthermore the entries are sorted in groups, which are customizable as
well. The integrated search function allows to search in a single group or
the complete database.
KeePassX offers a little utility for secure password generation. The
password generator is very customizable, fast and easy to use. Especially
someone who generates passwords frequently will appreciate this feature.

The complete database is always encrypted either with AES (alias Rijndael)
or Twofish encryption algorithm using a 256 bit key. Therefore the saved
information can be considered as quite safe. KeePassX uses a database
format that is compatible with KeePass Password Safe. This makes the use of
that application even more favourable.

%prep
%setup -q -n %{name}-2.0-alpha4

%build
mkdir build
cd build
cmake .. -DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_BUILD_TYPE=Release
make %{?_smp_mflags} CFLAGS="$RPM_OPT_FLAGS"

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
%{_includedir}/keepassx
%doc README.html version-notes.html keepassx-license.txt

%changelog
* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 14-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

