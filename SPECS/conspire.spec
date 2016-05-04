Name: conspire
Summary: Share Secrets with Friends
Version: 0.9.0
Release: fdm
License: MIT
Group: System/Utilities
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: x86_64
Url: https://github.com/ZoidbergConspiracy/conspire

%description
Conspire is a tool for setting up and managing Conspiracies.

It uses PGP/GPG keyrings to encrypts sets of secrets in a special directory,
called a vault. Each keyring is a group of users who are set up as shared
recepients for a secret file, which is stored in the vault.

Sharing secrets among groups of people with GPG is a little awkward,
because there is no facility to manage groups. This tool aims to make it
simpler to manage secrets among groups.

%prep

%setup -cT
export GOPATH=`pwd`

mkdir -p src/github.com/odeke-em/conspire
git clone --branch v%{version} https://github.com/ZoidbergConspiracy/conspire.git src/github.com/ZoidbergConspiracy/conspire
go get -f -u ./... || true

%build
export GOPATH=`pwd`
go build github.com/ZoidbergConspiracy/conspire

%install
%{__install} -D conspire ${RPM_BUILD_ROOT}%{_bindir}/conspire

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/conspire

