Name: fzf
Summary: A command-line fuzzy finder 
Version: git20150818.55d566b72f
Release: fdm
License: Apache 2.0
Group: System/Utilities
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: x86_64
Url: https://github.com/junegunn/fzf/

%description
fzf is a general-purpose command-line fuzzy finder.

%prep
mkdir -p %{name}-%{version}

%build
export GOPATH=`pwd`
go get -u github.com/junegunn/fzf/src

%install
%{__install} -D bin/fzf ${RPM_BUILD_ROOT}%{_bindir}/fzf

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/fzf

