#
# spec file for package ostinato
#

%define _qmake qmake
%if 0%{?fedora_version}
%define _qmake qmake-qt4
%endif
%if 0%{?rhel_version} || 0%{?centos_version} || 0%{?scientificlinux_version}
%ifarch x86_64
%define _qmake /usr/lib64/qt4/bin/qmake
%else
%define _qmake /usr/lib/qt4/bin/qmake
%endif
%endif

Name:           ostinato
Version:        0.5.1
Release:        1.1
License:        GPL-3.0+
Summary:        Packet/Traffic Generator and Analyzer
Url:            http://code.google.com/p/ostinato/
Group:          Productivity/Networking/Diagnostic
Source0:        http://ostinato.googlecode.com/files/%{name}-src-%{version}.tar.gz
Source1:        %{name}.desktop
%if 0%{?suse_version}
# Only needed for the icon installation
BuildRequires:  ImageMagick
%endif
%if 0%{?centos_version} || 0%{?fedora_version} || 0%{?rhel_version} || 0%{?scientificlinux_version}
BuildRequires:  gcc-c++
%endif
BuildRequires:  libpcap-devel
BuildRequires:  qt4-devel
BuildRequires:  protobuf-devel >= 2.3
%if 0%{?suse_version}
BuildRequires:  update-desktop-files
%endif
%if 0%{?centos_version} || 0%{?fedora_version} || 0%{?rhel_version} || 0%{?scientificlinux_version}
Requires:       wireshark
%endif
%if 0%{?suse_version} || 0%{?mandriva_version}
Recommends:     wireshark
%endif
BuildRoot: %{_tmppath}/%{name}-%{version}-build

%description
Ostinato is a network packet/traffic generator and analyzer
with a friendly GUI. It aims to be "Wireshark in Reverse"
and thus become complementary to Wireshark. It features custom
packet crafting with editing of any field for several protocols:
Ethernet, 802.3, LLC SNAP, VLAN (with Q-in-Q), ARP, IPv4, IPv6,
IP-in-IP a.k.a IP Tunneling, TCP, UDP, ICMPv4, ICMPv6, IGMP, MLD,
HTTP, SIP, RTSP, NNTP, etc. It is useful for both functional and
performance testing.

%prep
%setup -q

# Fix permissions (fix for rpmlint warning "spurious-executable-perm")
chmod 644 COPYING

%build
%if 0%{?suse_version}
%{_qmake} QMAKE_CXXFLAGS+="%{optflags}" PREFIX=%{_prefix}
%else
%{_qmake} PREFIX=%{_prefix}
%endif
make %{?_smp_mflags}

%install
make install INSTALL_ROOT=%{buildroot}

# Install a desktop file for openSUSE using xdg-su for executing ostinato (same as wireshark)
%if 0%{?suse_version}
# Install an icon
mkdir -p %{buildroot}%{_datadir}/pixmaps
install -pm 0644 client/icons/logo.png %{buildroot}%{_datadir}/pixmaps/%{name}.png
mogrify -extent "200x200" -background transparent -gravity "south" %{buildroot}%{_datadir}/pixmaps/%{name}.png
mogrify -scale 64x64 -background transparent %{buildroot}%{_datadir}/pixmaps/%{name}.png

# Install desktop file
%suse_update_desktop_file -i %{name}
%endif

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc COPYING
%{_bindir}/drone
%{_bindir}/ostinato
%if 0%{?suse_version}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%endif

%changelog
* Fri Jun 29 2012 asterios.dramis@gmail.com
- Recommend instead of Require wireshark (not mandatory) for openSUSE and
  Mandriva.
* Fri Jun 15 2012 asterios.dramis@gmail.com
- Changes on spec file based on spec-cleaner run.
- Updated License: to GPL-3.0+.
- Removed gcc-c++ indirect build dependency for openSUSE and Mandriva (not
  needed).
- Install and fix permissions of COPYING file (fix for rpmlint warning
  "spurious-executable-perm") (done for all distributions).
- Fixed openSUSE rpm post build check warning "File is compiled without
  RPM_OPT_FLAGS".
- Added a desktop file for openSUSE using xdg-su for executing ostinato.
  Install also a temporary icon (using ImageMagick to fix its size).
