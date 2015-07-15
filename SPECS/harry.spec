Summary: Tool for Measuring String Similarity
Name: harry
Version: 0.4.0
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

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')

%prep
%setup -n %{name}-%{version}

%build
%{configure} --enable-libarchive --enable-openmp --enable-md5hash
%{__make}

%install
%{makeinstall}
rm -rf %{buildroot}/usr/lib/python2.7/site-packages/harry.py?

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/harry
/usr/lib/python2.7/site-packages/harry.py
%{_mandir}/man?/*
%doc README.md COPYING CHANGES doc/harry.txt doc/example.cfg
