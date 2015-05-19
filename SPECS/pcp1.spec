Summary: Growl Notification Transport Protocol for Python
Name: pcp1
Version: 0.1.5
Release: 0.fdm
Source0: http://www.daemon.de/idisk/Apps/PrettyCurvedPrivacy/pretty-curved-privacy-%{version}.tag.gz
License: UNKNOWN
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Paul Traylor <UNKNOWN>
Url: http://www.daemon.de/PrettyCurvedPrivacy

%description
Pretty Curved Privacy (pcp1) is a commandline utility which can be used to
encrypt files. pcp1 uses eliptc curve cryptography for encryption
(CURVE25519 by Dan J. Bernstein). While CURVE25519 is no worldwide accepted
standard it hasn't been compromised by the NSA - which might be better,
depending on your point of view.

%prep
%setup -n pretty-curved-privacy-%{version}

%build
( git clone git://github.com/jedisct1/libsodium.git
 cd libsodium
 ./autogen.sh
 ./configure && make check
)

%install

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)
