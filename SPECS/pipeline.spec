Name: pipeline
Summary: Tool for quick iteration through pipeline activities
License: Apache
Group: Applications/Utilities
Url: https://github.com/skelterjohn/pipeline

%define git_version git%( date +'%Y%m%d' )
%define git_package skelterjohn/pipeline

Version: %{git_version}
Release: fdm
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: x86_64

%changelog
* Sun Nov 06 2016 Thornton Prime <thornton.prime@gmail.com> [%{git_version}]
- Build with go1.7

%description
pipeline is a tool to help with quick iteration on complex shell pipelines.

Pipe some data into pipeline, and edit your pipeline while watching the output
in real time. When you're satisfied, hit return to have its output piped to
the next stage. Or, hit ctrl-c or escape to cancel and exit 1 with no output.

%files
%defattr(-,root,root)
%{_bindir}/pipeline

%prep

%setup -cT
export GOPATH=`pwd`
git clone https://github.com/%{git_package}.git src/github.com/%{git_package}

%build
export GOPATH=`pwd`
go get -f -u github.com/%{git_package}/...

%install
%{__install} -D bin/pipeline ${RPM_BUILD_ROOT}%{_bindir}/pipeline

%clean
rm -rf $RPM_BUILD_ROOT

