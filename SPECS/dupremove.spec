Name: duperemove
Summary: Tools for Deduping Files
License: GPL2
Group: System/servers
Url: https://github.com/markfasheh/duperemove 

Version: 0.10
Release: 0.fdm
BuildArch: x86_64

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}

%description
Duperemove is a simple tool for finding duplicated extents and submitting
them for deduplication. When given a list of files it will hash their
contents on a block by block basis and compare those hashes to each other,
finding and categorizing extents that match each other. When given the -d
option, duperemove will submit those extents for deduplication using the
btrfs-extent-same ioctl.

%prep
%setup -cT
git clone --branch v%{version} https://github.com/markfasheh/duperemove.git .

%build
%{__make}

%install
%{__make} install PREFIX=%{buildroot}/usr

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_sbindir}/*
%{_mandir}/man?/*
%doc README.md LICENSE.* FAQ.md

