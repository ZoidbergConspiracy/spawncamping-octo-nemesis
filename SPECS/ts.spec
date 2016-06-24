Summary: Task Spooler Unix Batch System
Name: ts
Version: 0.7.6
Release: 0.fdm
Source0: http://vicerveza.homeunix.net/~viric/soft/ts/%{name}-%{version}.tar.gz
License: GPL2
Group: System Environment/Utilities
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
Vendor: Lluís Batlle i Rossell
Url: http://vicerveza.homeunix.net/~viric/soft/ts/

%description
task spooler is a Unix batch system where the tasks spooled run one after
the other. The amount of jobs to run at once can be set at any time. Each
user in each system has his own job queue. The tasks are run in the correct
context (that of enqueue) from any shell/process, and its output/results
can be easily watched. It is very useful when you know that your commands
depend on a lot of RAM, a lot of disk use, give a lot of output, or for
whatever reason it's better not to run them all at the same time, while you
want to keep your resources busy for maximum benfit. Its interface allows
using it easily in scripts.

%prep
%setup -n %{name}-%{version}

%build
%{__make}

%install
%{__install} -D ts %{buildroot}/%{_bindir}/ts
%{__install} -D ts.1 %{buildroot}/%{_mandir}/man1/ts.1


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/ts
%{_mandir}/man1/ts.1*
%doc README COPYING
%doc Changelog
%doc OBJECTIVES PORTABILITY PROTOCOL TRICKS
