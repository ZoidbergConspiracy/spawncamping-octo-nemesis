Name: bees
Summary: Best-Effort Extent-Same, a btrfs dedup agent
Group: Applications/System
License: GPLv3
URL: https://github.com/Zygo/bees

%define git_path Zygo/bees
%define git_version 0.4
%define xgit_tag %{git_version}
%define git_tag %( git ls-remote https://github.com/%{git_path}.git | grep HEAD | awk '{ print $1 }' )

#Version: %{git_version}
Version: %{git_version}.git%( echo %{git_tag} | cut -c 1-6 )
Release: 1.fdm
#Source0: https://github.com/Zygo/%{name}/archive/v%{version}.tar.gz
#Source0: %{name}-%{version}.tar.gz
Epoch: %( date +"%Y%m%d" )

BuildRequires: btrfs-progs-devel libuuid-devel
Requires: btrfs-progs libuuid

%description
Bees is a block-oriented userspace dedup agent designed to avoid scalability
problems on large filesystems.

%changelog
* Thu Nov 02 2017 Thornton Prime <thornton.prime@gmail.com> [0.4.0]
- Update to FDM26 and 0.4.0

%prep
%setup -cT
git clone https://github.com/%{git_path}.git .
git checkout -b %{git_tag}
git branch --set-upstream-to=origin/master %{git_tag}

%build
make src

%install
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

