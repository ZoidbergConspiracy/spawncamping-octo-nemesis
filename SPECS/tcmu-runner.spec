Name: tcmu-runner
Summary: Userspace daemon for the LIO TCM-User backstore
Version: 1.0.4
Release: fdm
License: Apache
Group: System/Utilities
Url: https://github.com/agrover/tcmu-runner 

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: x86_64
BuildRequires: cmake kmod-devel libnl3-devel glib2-devel zlib-devel

%description
A daemon that handles the userspace side of the LIO TCM-User backstore.

LIO is the SCSI target in the Linux kernel. It is entirely kernel code, and
allows exported SCSI logical units (LUNs) to be backed by regular files or
block devices. But, if we want to get fancier with the capabilities of the
device we're emulating, the kernel is not necessarily the right place.
While there are userspace libraries for compression, encryption, and
clustered storage solutions like Ceph or Gluster, these are not accessible
from the kernel.

The TCMU userspace-passthrough backstore allows a userspace process to
handle requests to a LUN. But since the kernel-user interface that TCMU
provides must be fast and flexible, it is complex enough that we'd like to
avoid each userspace handler having to write boilerplate code.

tcmu-runner handles the messy details of the TCMU interface -- UIO,
netlink, pthreads, and DBus -- and exports a more friendly C plugin module
API. Modules using this API are called "TCMU handlers". Handler authors can
write code just to handle the SCSI commands as desired, and can also link
with whatever userspace libraries they like.

One goal of TCMU is that configuring a userspace-backed LUN should be as
easy as configuring a kernel-backed LUN. We're not quite there yet. This
will require cooperation with the LIO configuration tool, targetcli.
targetcli should list user-backed backstores along with the built-in kernel
backstores, and ensure tcmu-runner is started if a user-backed backstore is
created.

%prep

%setup -cT
git clone --branch v%{version} https://github.com/agrover/tcmu-runner.git .

%build
cmake .

%install
make install INSTALL_ROOT=%{buildroot}

mkdir -p $RPM_BUILD_ROOT/etc/dbus-1/system.d
cp tcmu-runner.conf $RPM_BUILD_ROOT/etc/dbus-1/system.d
mkdir -p $RPM_BUILD_ROOT/usr/share/dbus-1/system-services
cp org.kernel.TCMUService1.service $RPM_BUILD_ROOT/usr/share/dbus-1/system-services
mkdir -p $RPM_BUILD_ROOT/lib/systemd/system
cp tcmu-runner.service $RPM_BUILD_ROOT/lib/systemd/system


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/*

