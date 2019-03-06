Name: ipfs
Summary: IPFS - The Permanent Web
License: MIT
Group: System/Utilities
URL: https://ipfs.io

%define git_version 0.4.18
%define git_path ipfs/go-ipfs

Version: %{git_version}
Release: 1.fdm
BuildArch: x86_64
Prefix: %{_prefix}

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
IPFS (the InterPlanetary File System) is a new hypermedia distribution
protocol, addressed by content and identities. IPFS enables the creation of
completely distributed applications. It aims to make the web faster, safer,
and more open.

IPFS is a distributed file system that seeks to connect all computing devices
with the same system of files. In some ways, this is similar to the original
aims of the Web, but IPFS is actually more similar to a single bittorrent
swarm exchanging git objects. You can read more about its origins in the
paper IPFS - Content Addressed, Versioned, P2P File System.

%changelog
* Mon Oct 02 2017 Thornton Prime <thornton.prime@gmail.com> [0.4.11]
- Update and build with go1.9

%files
%defattr(-,root,root)
%{_bindir}/ipfs

%prep

%setup -cT
export GOPATH=`pwd`
# git clone https://github.com/%{git_path}.git src/github.com/%{git_path}
git clone https://github.com/%{git_path}.git .
git checkout -b v%{git_version}
git branch --set-upstream-to=origin/master v%{git_version}

%build
export GOPATH=`pwd`
go get -u -d github.com/ipfs/go-ipfs

( cd src/github.com/ipfs/go-ipfs
make build
)

%install
%{__install} -D src/github.com/ipfs/go-ipfs/cmd/ipfs/ipfs \
  ${RPM_BUILD_ROOT}%{_bindir}/ipfs

%clean
rm -rf $RPM_BUILD_ROOT

