Name: mod_auth_openidc
Summary: Apache OpenID Connect Module
Version: 1.8.0
Release: 0%{?dist}
License: Apache
Group: System Environment/Daemons
URL: https://github.com/pingidentity/mod_auth_openidc/
Source: https://github.com/pingidentity/mod_auth_openidc/archive/%{name}-%{version}.tar.gz 

BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXXXX)
BuildRequires: jansson-devel pcre-devel curl-devel openssl-devel

%description
mod_auth_openidc is an authentication/authorization module for the
Apache 2.x HTTP server that authenticates users against an OpenID
Connect Provider. It can also function as an OAuth 2.0 Resource Server,
validating access tokens presented by OAuth 2.0 clients against an OAuth
2.0 Authorization Server.

%changelog
* Mon Oct 27 2014 Thornton Prime <thornton.prime@gmail.com>
- Basic build

%prep

%setup -q

%build
./autogen.sh
%{configure} --with-apxs2=/usr/bin/apxs
make

%install
rm -rf %{buildroot}

%{__install} -d -m0755 %{buildroot}%{_libdir}/httpd/modules
%{__install} src/.libs/mod_auth_openidc.so \
   %{buildroot}%{_libdir}/httpd/modules/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc LICENSE.txt README.md ChangeLog DISCLAIMER
%doc auth_openidc.conf
%{_libdir}/httpd/modules/mod_auth_openidc.so

