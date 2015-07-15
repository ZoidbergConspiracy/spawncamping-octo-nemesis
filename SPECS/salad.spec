Summary: A Content Anomaly Detector based on n-Grams
Name: salad
Version: 0.5.0
Release: 1.fdm
Source0: http://www.mlsec.org/salad/files/%{name}-%{version}.tar.gz 
License: GPL3
Group: Applications/Text
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Vendor: MLSec (http://www.mlsec.org)
URL: http://www.mlsec.org/salad/

BuildRequires: zlib-devel >= 1.2.1
BuildRequires: libconfig-devel >= 1.4
BuildRequires: libarchive-devel >= 2.70
Prefix: %{_prefix}

%description
Letter Salad or Salad for short, is an efficient and flexible implementation
of the well-known anomaly detection method Anagram by Wang et al. (RAID
2006)
Salad enables detecting anomalies in large-scale string data. The tool is
based on the concepts of n-grams, that is, strings are compared using all
substrings of length n. During training, these n-grams are extracted from a
collection of strings and stored in a Bloom filter. This enables the
detector to represent a large number of n-grams in very little memory.
During anomaly detection, the n-grams of unknown strings are matched
against the Bloom filter and strings containing several n-grams not seen
during training are flagged as anomalous.
Salad extends the original method Anagram in different ways: First, the
tool does not only operate on n-grams of bytes, but is also capable of
comparing n-grams over words and tokens. Second, Salad implements a 2-class
version of the detector that enables discriminating strings of two types.
Finally, the tool features a build-in inspection and statistic mode that
can help to analyze the learned Bloom filter and its predictions.
The tool can be utilized in different fields of application. For example,
the concept underlying Salad has been prominently used for intrusion
detection, but is not limited to this scenario. To illustrate the
versatility of Salad we provide some concrete examples of its usage. All
examples come with data sets and instructions.

%prep
%setup -n %{name}-%{version}-1

%build
cmake -D CMAKE_INSTALL_PREFIX:PATH=%{buildroot} .
%{__make}

%install
%{makeinstall}
rm -rf %{buildroot}/usr
mkdir -p %{buildroot}/usr
mv %{buildroot}/bin %{buildroot}/usr
mv %{buildroot}/share %{buildroot}/usr

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/salad*
%{_mandir}/man?/*
%doc README.md LICENSE CHANGELOG
