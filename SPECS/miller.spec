Name: miller
Summary: A command line tool for parsing CSV and other structured data
Version: 1.0.0
Release: fdm
License: MIT
Group: System/Utilities
Url: http://johnkerl.org/miller/doc/ 

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}
Prefix: %{_prefix}
BuildArch: x86_64

Source: https://github.com/johnkerl/miller/archive/v%{version}.tar.gz 

%description
Miller is like sed, awk, cut, join, and sort for name-indexed data such as
CSV. With Miller you get to use named fields without needing to count positional
indices.

This is something the Unix toolkit always could have done, and arguably
always should have done. It operates on key-value-pair data while the
familiar Unix tools operate on integer-indexed fields: if the natural data
structure for the latter is the array, then Miller’s natural data structure
is the insertion-ordered hash map. This encompasses a variety of data
formats, including but not limited to the familiar CSV. (Miller can handle
positionally-indexed data as a special case.)

%prep
%setup

%build
%{__make}

%install
%{__mkdir} -p %{buildroot}%{_usr}/bin
%{makeinstall} HOME=%{buildroot}%{_usr}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/mlr
%doc README.md LICENSE.txt doc/*
