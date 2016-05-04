Name: cfssl
Summary: PKI/TLS Toolkit from Cloudflare
Version: 1.2.0
Release: fdm
License: MIT-Like
Group: System/Utilities
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: x86_64
Url: https://cfssl.org/ 

%description
FSSL is CloudFlare's PKI/TLS swiss army knife. It is both a command line tool
and an HTTP API server for signing, verifying, and bundling TLS certificates.

CFSSL consists of:

* a set of packages useful for building custom TLS PKI tools
* the cfssl program, which is the canonical command line utility using the
  CFSSL packages.
* the multirootca program, which is a certificate authority server that can
  use multiple signing keys.
* the mkbundle program is used to build certificate pool bundles.
* the cfssljson program, which takes the JSON output from the cfssl and
  multirootca programs and writes certificates, keys, CSRs, and bundles to
  disk.

%prep

%setup -cT
export GOPATH=`pwd`

mkdir -p src/github.com/cloudflare/cfssl
git clone --branch %{version} https://github.com/cloudflare/cfssl.git src/github.com/cloudflare/cfssl
go get -f -u ./... || true

%build
export GOPATH=`pwd`

for BIN in cfssl cfssl-bundle cfssl-certinfo cfssljson cfssl-newkey cfssl-scan mkbundle multirootca; do
  go build github.com/cloudflare/cfssl/cmd/${BIN}
done

%install

for BIN in cfssl cfssl-bundle cfssl-certinfo cfssljson cfssl-newkey cfssl-scan mkbundle multirootca; do
  %{__install} -D ${BIN} ${RPM_BUILD_ROOT}%{_bindir}/${BIN}
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/*

