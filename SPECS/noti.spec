Name: noti
Summary: Trigger Notifications
License: MIT
Group: Applications/Internet
Url: https://github.com/variadico/noti

%define git_version 0.2.1
%define git_package variadico/noti\

Version: %{git_version}
Release: fdm
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: x86_64

%changelog
* Mon Aug 29 2016 Thornton Prime <thornton.prime@gmail.com> [0.2.1]
- Update to 0.2.1
- Build with go1.7

%description
Trigger notifications when a process completes.

Never sit and wait for some long-running process to finish!
noti will alert you when it's done—on your computer or smartphone—so
you can stop worrying about constantly checking the terminal.

%files
%defattr(-,root,root)
%{_bindir}/noti
%doc src/github.com/%{git_package}/{README.md,LICENSE,CHANGELOG.md,CONTRIBUTING.md}

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
%{__install} -D bin/noti ${RPM_BUILD_ROOT}%{_bindir}/noti

%clean
rm -rf $RPM_BUILD_ROOT

