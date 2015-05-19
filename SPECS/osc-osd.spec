Name:    osc-osd
Version: 20131025git
Release: 1.1%{dist}
License: GPL
Summary: Object Storage Devices are a new type of SCSI storage devices
URL:     http://www.open-osd.org
Group:   System Environment/Daemons

Source0: osc-osd-20131025git.tar.gz
Patch0:  osc-osd.patch
BuildRequires:  sqlite-devel
BuildRoot: %{_tmppath}/%{name}-%{version}-build

%description
Object Storage Devices are a new type of SCSI storage devices providing a
richer command set improving storage manageability and security.

The OSD Standard was initially developed by the Storage Networking Industry
Association (SNIA) and was ratified in July 2004 by incits Technical
Committee T10. A new version of the OSD standard, OSD-2, has been developed
based on experience gathered from commercial implementations and
prototypes. 

%prep
%setup -q -n osc-osd
%patch0 -p1

%build
make %{?_smp_mflags}

%install
make install INSTALL_ROOT=%{buildroot}

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
* Fri Oct 25 2012 thornton.prime@gmail.com
- Initial build.

