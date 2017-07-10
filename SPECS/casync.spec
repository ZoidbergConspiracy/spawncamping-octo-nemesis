%global gitcommit cc63fcd2b23def5ca6b824cdaf7ba6deda3d23de
%{?gitcommit:%global gitcommitshort %(c=%{gitcommit}; echo ${c:0:7})}

Name:           casync
Version:        1
Release:        4%{?gitcommit:.git%{gitcommitshort}}%{?dist}
Summary:        Content Addressable Data Synchronizer

License:        LGPLv2+
URL:            https://github.com/systemd/casync
%if %{defined gitcommit}
Source0:        https://github.com/keszybz/casync/archive/%{?gitcommit}.tar.gz#/%{name}-%{gitcommitshort}.tar.gz
%else
Source0:        https://github.com/systemd/casync/archive/v%{version}/%{name}-%{version}.tar.gz
%endif

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  pkgconfig(liblzma) >= 5.1.0
BuildRequires:  pkgconfig(libcurl) >= 7.32.0
BuildRequires:  pkgconfig(fuse) >= 2.6
BuildRequires:  libgcrypt-devel
BuildRequires:  libacl-devel
# for tests
BuildRequires:  rsync

%description
casync provides a way to efficiently transfer files which change over
time over the internet. It will split a given set into a git-inspired
content-addressable set of smaller compressed chunks, which can then
be conveniently transferred using HTTP. On the receiving side those
chunks will be uncompressed and merged together to recreate the
original data. When the original data is modified, only the new chunks
have to be transferred during an update.

%prep
%if %{defined gitcommit}
%autosetup -n %{name}-%{gitcommit} -p1
%else
%autosetup -p1
%endif

%build
%meson
%meson_build

%check
export LC_CTYPE=C.utf8
%meson_test

%install
%meson_install

%files
%license LICENSE.LGPL2.1
%doc README.md TODO
%_bindir/casync
%dir %_prefix/lib/casync
%dir %_prefix/lib/casync/protocols
%_prefix/lib/casync/protocols/casync-ftp
%_prefix/lib/casync/protocols/casync-http
%_prefix/lib/casync/protocols/casync-https

%changelog
* Fri Jun 23 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1-4.git
- Pull in fixes for failures on non-amd64 arches

* Tue Jun 20 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1-1
- Initial packaging
