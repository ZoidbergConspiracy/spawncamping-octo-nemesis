Name: delve
Summary: A debugger for the Go programming language
License: GPL
Group: System/Utilities
Url: https://github.com/derekparker/delve/wiki/Usage

Version: 0.8.1a
Release: 0.fdm
BuildArch: x86_64

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}

%description
Delve is a debugger for the Go programming language. The goal of the project
is to provide a simple, full featured debugging tool for Go. Delve should be
easy to invoke and easy to use. Chances are if you're using a debugger, most
likely things aren't going your way. With that in mind, Delve should stay out
of your way as much as possible.

%prep
%setup -cT
export GOPATH=`pwd`
#go get github.com/derekparker/delve
mkdir -p src/github.com/derekparker/delve
git clone https://github.com/derekparker/delve.git src/github.com/derekparker/delve
(
  cd src/github.com/derekparker/delve
  #git checkout tags/v%{version}
  git checkout tags/v0.8.1-alpha
)

%build
export GOPATH=`pwd`
go get -u github.com/derekparker/delve/cmd/dlv
go install github.com/derekparker/delve/cmd/dlv

%install
%{__install} -D bin/dlv %{buildroot}%{_bindir}/dlv

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/dlv

