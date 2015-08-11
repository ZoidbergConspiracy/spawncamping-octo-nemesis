Name: drive
Summary: Pull or Push Google Drive Files
Version: git20150711.9050e2b2da
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
mkdir -p %{name}-%{version}

%build
export GOPATH=`pwd`
go get -u github.com/odeke-em/drive/cmd/drive

%install
%{__install} -D bin/drive ${RPM_BUILD_ROOT}%{_bindir}/drive

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/drive

