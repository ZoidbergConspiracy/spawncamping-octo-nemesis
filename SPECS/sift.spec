Name: sift
Summary: A fast and powerful open source alternative to grep
License: GPL
Group: System/Utilities
Url: http://sift-tool.org

Version: 0.3.2
Release: 0.fdm
BuildArch: x86_64

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}

%description
A fast and powerful open source alternative to grep

%prep
%setup -cT
export GOPATH=`pwd`
go get github.com/svent/sift
#mkdir -p src/github.com/svent/sift
#git clone https://github.com/svent/sift.git src/github.com/svent/sift
#(
#  cd src/github.com/sevent/sift
#  git checkout tags/v%{version}
#)

%build
export GOPATH=`pwd`
go install github.com/svent/sift

%install
%{__install} -D bin/sift %{buildroot}%{_bindir}/sift

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/sift
