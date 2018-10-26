Name: duperemove
Summary: Tools for Deduping Files
License: GPL2
Group: System/servers
Url: https://github.com/markfasheh/duperemove 

%define git_version 0.11
%define git_base markfasheh
%define git_path %{git_base}/%{name}
%define git_tag %( git ls-remote https://github.com/%{git_path}.git | grep HEAD | awk '{ print $1 }' | cut -c 1-8 )

Version: %{git_version}_%{git_tag}git
Release: 1.fdm
BuildArch: x86_64
Prefix: %{_prefix}

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}

BuildRequires: sqlite-devel

%description
Duperemove is a simple tool for finding duplicated extents and submitting
them for deduplication. When given a list of files it will hash their
contents on a block by block basis and compare those hashes to each other,
finding and categorizing extents that match each other. When given the -d
option, duperemove will submit those extents for deduplication using the
btrfs-extent-same ioctl.

%changelog
* Tue Nov 28 2017 Thornton Prime <thornton.prime@gmail.com> [0.8.0]
- Update to 0.8.0


%prep
%setup -cT
git clone https://github.com/%{git_path}.git .

git checkout -b %{git_tag}
git branch --set-upstream-to=origin/master %{git_tag}
#git checkout -b v%{git_version}
#git branch --set-upstream-to=origin/master v%{git_version}

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
%doc README.md LICENSE.*

