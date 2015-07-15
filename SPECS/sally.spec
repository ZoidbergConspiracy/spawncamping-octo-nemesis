Summary: Tool for Emebeding Strings in Vector Spaces
Name: sally
Version: 1.0.0
Release: 1.fdm
Source0: http://www.mlsec.org/sally/files/%{name}-%{version}.tar.gz 
License: GPL3
Group: Applications/Text
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Vendor: MLSec (http://www.mlsec.org)
URL: http://www.mlsec.org/sally/

BuildRequires: zlib-devel >= 1.2.1
BuildRequires: libconfig-devel >= 1.4
BuildRequires: libarchive-devel >= 2.70
Prefix: %{_prefix}

%description
Sally is a small tool for mapping a set of strings to a set of vectors.
This mapping is referred to as embedding and allows for applying techniques
of machine learning and data mining for analysis of string data. Sally can
be applied to several types of string data, such as text documents, DNA
sequences or log files, where it can handle string data in directories,
archives and text files.

%prep
%setup -n %{name}-%{version}

%build
%{configure} --enable-libarchive --enable-openmp --enable-md5hash
%{__make}

%install
%{makeinstall}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/sally
%{_mandir}/man?/*
%doc README.md COPYING CHANGES doc/sally.txt doc/example.cfg
