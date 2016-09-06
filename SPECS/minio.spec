Name: minio
Summary: Object storage server compatible with Amazon S3
License: Apache 2.0
Group: System Environment/Daemons
Url:  https://minio.io

%define git_version 1434511043
%define git_package minio/minio

Version: %{git_version}
Release: fdm
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: x86_64

%description
Minio is an object storage server released under Apache License v2.0. It is
compatible with Amazon S3 cloud storage service. It is best suited for storing
unstructured data such as photos, videos, log files, backups and container / VM
images. Size of an object can range from a few KBs to a maximum of 5TB.

%changelog
* Wed Aug 31 2016 Thornton Prime <thornton.prime@gmail.com> [1.0.1]
- Update to 1.0.1
- Build with go1.7

%files
%defattr(-,root,root)
%{_bindir}/minio
%doc src/github.com/%{git_package}/{README.md,LICENSE}

%prep

%setup -cT
export GOPATH=`pwd`
git clone https://github.com/%{git_package}.git src/github.com/%{git_package}
(
  cd src/github.com/%{git_package}
  git checkout -b release-%{git_version}
  git branch --set-upstream-to=origin/master release-%{git_version}
)

%build
export GOPATH=`pwd`
go get -f -u github.com/%{git_package}/... || true

%install
%{__install} -D bin/minio ${RPM_BUILD_ROOT}%{_bindir}/minio

%clean
rm -rf $RPM_BUILD_ROOT

