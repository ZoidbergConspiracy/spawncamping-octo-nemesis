Name: rclone
Summary: Sync files to and from multiple cloud services
License: MIT
Group: Applications/Internet
Url: http://rclone.org/

%define git_version 1.34
%define git_package ncw/rclone

Version: %{git_version}
Release: fdm
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: x86_64

%changelog
* Wed Aug 31 2016 Thornton Prime <thornton.prime@gmail.com> [1.33]
* Thu Aug 18 2016 Thornton Prime <thornton.prime@gmail.com> [1.32]
- Update to 1.32
- Build with go1.7
* Tue Jun 28 2016 Thornton Prime <thornton.prime@gmail.com> [1.30]
- Current version.

%description

Rclone is a command line program to sync files and directories to and from
  * Google Drive
  * Amazon S3
  * Openstack Swift / Rackspace cloud files / Memset Memstore
  * Dropbox
  * Google Cloud Storage
  * Amazon Cloud Drive
  * Microsoft One Drive
  * Hubic
  * Backblaze B2
  * Yandex Disk
  * The local filesystem

Features
  * MD5/SHA1 hashes checked at all times for file integrity
  * Timestamps preserved on files
  * Partial syncs supported on a whole file basis
  * Copy mode to just copy new/changed files
  * Sync (one way) mode to make a directory identical
  * Check mode to check for file hash equality
  * Can sync to and from network, eg two different cloud accounts

%files
%defattr(-,root,root)
%{_bindir}/rclone
%{_mandir}/man1/rclone*
%doc src/github.com/ncw/rclone/{README.md,MANUAL*,RELEASE*,CONTRIBUTING*,COPYING*}

%prep

%setup -cT
export GOPATH=`pwd`
git clone https://github.com/%{git_package}.git src/github.com/%{git_package}
(
  cd src/github.com/%{git_package}
  git checkout -b v%{git_version}
  git branch --set-upstream-to=origin/master v%{git_version}
)


%build
export GOPATH=`pwd`
go get -f -u github.com/%{git_package}/...

%install
%{__install} -D bin/rclone ${RPM_BUILD_ROOT}%{_bindir}/rclone
%{__install} -D src/github.com/ncw/rclone/rclone.1 ${RPM_BUILD_ROOT}%{_mandir}/man1/rclone.1

%clean
rm -rf $RPM_BUILD_ROOT

