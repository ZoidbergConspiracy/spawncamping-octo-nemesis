Name: drive
Summary: Pull or Push Google Drive Files
Version: 0.3.5
Release: fdm
License: Apache 2.0
Group: System/Utilities
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: x86_64
Url: https://github.com/odeke-em/drive

%description
drive is a tiny program to pull or push Google Drive files.

%prep

%setup -cT
export GOPATH=`pwd`

mkdir -p src/github.com/odeke-em/drive
git clone --branch v%{version} https://github.com/odeke-em/drive.git src/github.com/odeke-em/drive
go get -f -u ./... || true

%build
export GOPATH=`pwd`
go build github.com/odeke-em/drive/cmd/drive

%install
%{__install} -D drive ${RPM_BUILD_ROOT}%{_bindir}/drive

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/drive

