Name: gron
Summary: Command line YAML processor
License: MIT
Group: System/Utilities

%define git_tag 0.5.2
%define git_version  %{git_tag}
%define git_path tomnomnom/%{name}

Version: %{git_version}
Release: 0.fdm
BuildArch: x86_64
URL: https://github.com/%{git_path}
Prefix: %{_prefix}

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
gron transforms JSON into discrete assignments to make it easier to grep for
what you want and see the absolute 'path' to it. It eases the exploration of
APIs that return large blobs of JSON but have terrible documentation.

%changelog
* Wed Apr  4 2018 Thornton Prime <thornton.prime@gmail.com> [0.5.2]
- Update and build with go1.9
- Basic build from Github

%files
%defattr(-,root,root)
%{_bindir}/gron

%prep

%setup -cT
export GOPATH=`pwd`
git clone https://github.com/%{git_path}.git src/github.com/%{git_path}
(
  cd src/github.com/%{git_path}
  git checkout -b %{git_version}
  git branch --set-upstream-to=origin/master %{git_version}
)

%build
export GOPATH=`pwd`
go get -f -u github.com/%{git_path}

%install
%{__install} -D bin/gron ${RPM_BUILD_ROOT}%{_bindir}/gron

%clean
rm -rf $RPM_BUILD_ROOT

