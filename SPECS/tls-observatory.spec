Name: tls-observatory
Summary: An observatory for RLS configurations, X509 certificates, and more.
License: Mozilla
Group: Applications/Internet
Url: https://github.com/mozilla/tls-observatory

%define git_version 1.0.0
%define git_package mozilla/tls-observatory

Version: %{git_version}
Release: fdm
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: x86_64

%changelog
* Mon Jul 11 2016 Thornton Prime <thornton.prime@gmail.com> [1.0.0]
- Current version.

%description
An observatory for RLS configurations, X509 certificates, and more.
You can use the TLS Observatory to compare your site against the mozilla
guidelines.

%files
%defattr(-,root,root)
%{_bindir}/tlsobs
%doc src/github.com/%{git_package}/{README.md,LICENSE}

%prep
%setup -cT
export GOPATH=`pwd`
git clone https://github.com/%{git_package}.git src/github.com/%{git_package}
(cd src/github.com/%{git_package}; git checkout -b v%{git_version} )
go get -f -u %{git_package}/cmd/pget || true

%build
export GOPATH=`pwd`
go build github.com/%{git_package}/tlsobs

%install

%{__install} -D tlsobs ${RPM_BUILD_ROOT}%{_bindir}/tlsobs

%clean
rm -rf $RPM_BUILD_ROOT

