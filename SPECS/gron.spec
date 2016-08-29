Name: gron
Summary: Make JSON Greppable
License: MIT
Group: Utilities/Management
Url: https://github.com/tomnomnom/gron

%define git_version 0.3.1
%define git_package tomnomnom/gron

Version: %{git_version}
Release: fdm
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: x86_64

%changelog
* Fri Jul 29 2016 Thornton Prime <thornton.prime@gmail.com> [0.0.1]
- Current version.

%description
gron transforms JSON into discrete assignments to make it easier to grep for what
you want and see the absolute 'path' to it. It eases the exploration of APIs that
return large blobs of JSON but have terrible documentation.

%files
%defattr(-,root,root)
%{_bindir}/gron
%doc src/github.com/%{git_package}/{*.mkd,LICENSE}

%prep
%setup -cT
export GOPATH=`pwd`
git clone https://github.com/%{git_package}.git src/github.com/%{git_package}
(
  cd src/github.com/%{git_package}
  git checkout -b v%{git_version}
  git branch --set-upstream-to=origin/master v%{git_version}
)
go get -f -u github.com/%{git_package}/... || true

%build
export GOPATH=`pwd`
go build github.com/%{git_package}

%install
%{__install} -D gron ${RPM_BUILD_ROOT}%{_bindir}/gron

%clean
rm -rf $RPM_BUILD_ROOT

