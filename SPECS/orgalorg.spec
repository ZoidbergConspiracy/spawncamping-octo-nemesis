Name: orgalorg
Summary: Next generation parallel SSH and file synchronization tool
License: MIT
Group: Applications/Internet
Url: https://github.com/reconquest/orgalorg

%define git_version 1.0.0
%define git_package reconquest/orgalorg

Version: %{git_version}
Release: fdm
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: x86_64

%changelog
* Mon Jul 11 2016 Thornton Prime <thornton.prime@gmail.com> [1.0.0]
- Current version.

%description
Ultimate parallel cluster file synchronization tool and SSH commands
executioner.

%files
%defattr(-,root,root)
%{_bindir}/orgalorg
%doc src/github.com/%{git_package}/{README.md,LICENSE}

%prep
%setup -cT
export GOPATH=`pwd`
git clone https://github.com/%{git_package}.git src/github.com/%{git_package}
#(cd src/github.com/%{git_package}; git checkout -b v%{git_version} )
go get -f -u github.com/%{git_package} || true

%build
export GOPATH=`pwd`
go build github.com/%{git_package}

%install

%{__install} -D orgalorg ${RPM_BUILD_ROOT}%{_bindir}/orgalorg

%clean
rm -rf $RPM_BUILD_ROOT

