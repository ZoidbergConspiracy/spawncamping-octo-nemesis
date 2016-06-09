Name: rclone
Summary: Sync files to and from multiple cloud services
Version: 1.29
Release: fdm
License: MIT
Group: Applications/Internet
Url: http://rclone.org/

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: x86_64

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

%prep

%setup -cT
export GOPATH=`pwd`

mkdir -p src/github.com/ncw/rclone
git clone --branch v%{version} https://github.com/ncw/rclone.git src/github.com/ncw/rclone
go get -f -u ./... || true

%build
export GOPATH=`pwd`
go build github.com/ncw/rclone

%install

%{__install} -D rclone ${RPM_BUILD_ROOT}%{_bindir}/rclone
%{__install} -D src/github.com/ncw/rclone/rclone.1 ${RPM_BUILD_ROOT}%{_mandir}/man1/rclone.1


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/rclone
%{_mandir}/man1/rclone*
%doc src/github.com/ncw/rclone/{README.md,MANUAL*,RELEASE*,CONTRIBUTING*,COPYING*}

