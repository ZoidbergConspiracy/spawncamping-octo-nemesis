Summary: Tool for Measuring String Similarity
Name: harry
Version: 0.2
Release: 1.fdm
Source0: http://www.mlsec.org/harry/files/%{name}-%{version}.tar.gz 
License: GPL3
Group: Applications/Text
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Vendor: MLSec (http://www.mlsec.org)
URL: http://www.mlsec.org/harry

BuildRequires: zlib-devel >= 1.2.1
BuildRequires: libconfig-devel >= 1.4
BuildRequires: libarchive-devel >= 2.70
Prefix: %{_prefix}

%description
Harry is a small tool for comparing strings and measuring their similarity.
The tool supports several common distance and kernel functions for strings
as well as some excotic similarity measures. The focus of Harry lies on
implicit similarity measures, that is, comparison functions that do not
give rise to an explicit vector space. Examples of such similarity measures
are the Levenshtein distance and the Jaro-Winkler distance.

%prep
%setup -n %{name}-%{version}

%build
%{configure} --enable-libarchive --enable-openmp --enable-md5hash
%{__make} check

%install
%{makeinstall}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/harry
%{_mandir}/man?/*
%doc README.md COPYING CHANGES TODO.md doc/harry.txt doc/example.cfg
