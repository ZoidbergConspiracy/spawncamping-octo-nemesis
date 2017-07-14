Name: rmlint
Summary: rmlint finds space waste and other broken things on your filesystem and offers to remove it.
Group: Applications/System
License: GPLv3
URL: http://rmlint.rtfd.org

Version: 2.6.1
Release: 1.fdm
Source0: https://github.com/sahib/rmlint/archive/rmlint-%{version}.tar.gz
Requires: glib2 libblkid elfutils-libelf json-glib
BuildRequires: scons python3-sphinx gettext libblkid-devel elfutils-libelf-devel glib2-devel json-glib-devel

%description
rmlint finds space waste and other broken things and offers to remove it. It is
especially an extremely fast tool to remove duplicates from your filesystem.

%changelog
* Fri Jul 14 2017 Thornton Prime <thornton.prime@gmail.com> [2.6.1]
- Update to FDM26 and 2.6.1
* Mon May 29 2017 Thornton Prime <thornton.prime@gmail.com> [2.4.5]
- Update to FDM and 2.4.5
* Sun May 10 2015 Christopher Pahl <sahib@online.de> - 2.2.0
- Update version to 2.2.0
* Sat Dec 20 2014 Christopher Pahl <sahib@online.de> - 2.0.0
- Use autosetup instead of setup -q
* Fri Dec 19 2014 Christopher Pahl <sahib@online.de> - 2.0.0
- Updated wrong dependency list
* Mon Dec 01 2014 Christopher Pahl <sahib@online.de> - 2.0.0
- Initial release of RPM package 

%prep 
# %autosetup -c rmlint-%{version}

%setup -q -n %{name}-%{version}
scons config

%build
scons -j4 --prefix=%{buildroot}/usr --actual-prefix=/usr --libdir=lib64

%install
# Build rmlint, install it into BUILDROOT/<name>-<version>/,
# but take care rmlint thinks it's installed to /usr (--actual_prefix)
scons install -j4 --prefix=%{buildroot}/usr --actual-prefix=/usr --libdir=lib64

# Find all rmlint.mo files and put them in rmlint.lang
%find_lang %{name}

rm -rf %{buildroot}/usr/lib \
       %{buildroot}/usr/share/applications \
       %{buildroot}/usr/share/icons \
       %{buildroot}/usr/share/glib-2.0

%clean
rm -rf %{buildroot}

# List all files that will be in the packaget
%files -f %{name}.lang
%doc README.rst COPYING
%{_bindir}/*
%{_mandir}/man1/*

# Not used yet:
# %{_libdir}/*
# %{_includedir}/*

