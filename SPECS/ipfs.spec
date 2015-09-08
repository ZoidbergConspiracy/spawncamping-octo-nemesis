Name: ipfs
Summary: Interplanetary Filesystem distributed media
License: MIT
Group: System/servers
Url: https://ipfs.io

Version: 0.3.7
Release: 0.fdm
BuildArch: x86_64

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}

%description
Ipfs is a global, versioned, peer-to-peer filesystem. It combines good ideas
from Git, BitTorrent, Kademlia, SFS, and the Web. It is like a single
bittorrent swarm, exchanging git objects. IPFS provides an interface as
simple as the HTTP web, but with permanence built in. You can also mount the
world at /ipfs.

%prep
%setup -cT
export GOPATH=`pwd`
mkdir -p src/github.com/ipfs/go-ipfs
git clone https://github.com/ipfs/go-ipfs.git src/github.com/ipfs/go-ipfs
(
  cd src/github.com/ipfs/go-ipfs
  git checkout tags/v%{version}
)

%build
export GOPATH=`pwd`
go install github.com/ipfs/go-ipfs/cmd/ipfs

%install
%{__install} -D bin/ipfs %{buildroot}%{_bindir}/ipfs

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/ipfs
