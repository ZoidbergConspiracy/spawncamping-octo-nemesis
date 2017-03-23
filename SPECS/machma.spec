Name: machma
Summary: Easy parallel execution of commands
License: BSD-2
Group: System/Utilities

%define git_path fd0/%{name}
%define git_tag %( git ls-remote https://github.com/%{git_path}.git | grep HEAD | awk '{ print $1 }' )

Version: 0.%( echo %{git_tag} | cut -c 1-8 )git
Release: 0.fdm
BuildArch: x86_64
URL: https://github.com/%{git_package}
Prefix: %{_prefix}

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
In order to fully utilize modern machines, jobs need to be run in parallel. For
example, resizing images sequentially takes a lot of time, whereas working on
multiple images in parallel makes much better use of a multi-core CPU and
therefore is much faster. This tool makes it very easy to execute tasks in
parallel and provides live feedback. In case of errors or lines printed by the
program, the messages are tagged with the job name.

machma by default reads newline-separated values and replaces all command-line
arguments set to {} with the file name. The number of jobs is set to the number
of cores for the CPU of the host machma is running on.

%changelog
* Thu Mar 23 2017 Thornton Prime <thornton.prime@gmail.com> [0.git]
- Basic build from Github

%files
%defattr(-,root,root)
%{_bindir}/machma

%prep

%setup -cT
export GOPATH=`pwd`
git clone https://github.com/%{git_path}.git src/github.com/%{git_path}
(
  cd src/github.com/%{git_path}
  git checkout -b %{git_tag}
  git branch --set-upstream-to=origin/master %{git_tag}
)

%build
export GOPATH=`pwd`
go get -f -u github.com/%{git_path}

%install
%{__install} -D bin/machma ${RPM_BUILD_ROOT}%{_bindir}/machma

%clean
rm -rf $RPM_BUILD_ROOT

