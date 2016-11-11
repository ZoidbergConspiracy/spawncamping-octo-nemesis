Name: seaweedfs
Summary: Simple and highly scalable distributed file system
License: Apache 2.0
Group: Applications/Internet
Url: https://github.com/chrislusf/seaweedfs

%define git_version 0.70
%define git_package chrislusf/seaweedfs

Version: %{git_version}
Release: fdm
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: x86_64

%changelog
* Fri Nov 11 2016 Thornton Prime <thornton.prime@gmail.com> [0.70]
- First FDM build

%description
SeaweedFS is a simple and highly scalable distributed file system. There are two
objectives: to store billions of files! to serve the files fast! Instead of supporting
full POSIX file system semantics, SeaweedFS choose to implement only a key~file mapping.
Similar to the word "NoSQL", you can call it as "NoFS".

%files
%defattr(-,root,root)
%{_bindir}/weed
%doc src/github.com/%{git_package}/{README.md,LICENSE}

%prep

%setup -cT
export GOPATH=`pwd`
git clone https://github.com/%{git_package}.git src/github.com/%{git_package}
(
  cd src/github.com/%{git_package}
  git checkout -b v%{git_version}
  git branch --set-upstream-to=origin/master v%{git_version}
)


%build
export GOPATH=`pwd`
go get -f -u github.com/%{git_package}/...

%install
%{__install} -D bin/weed ${RPM_BUILD_ROOT}%{_bindir}/weed

%clean
rm -rf $RPM_BUILD_ROOT

