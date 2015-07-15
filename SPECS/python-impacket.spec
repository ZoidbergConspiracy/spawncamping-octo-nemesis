%global srcname impacket

Name:           python-%{srcname}
Version:        0.9.13
Release:        2%{?dist}
Summary:        Collection of Python classes providing access to network packets

License:        ASL 1.1 and zlib
URL:            http://code.google.com/p/impacket/
Source0:        https://pypi.python.org/packages/source/i/%{srcname}/%{srcname}-%{version}.tar.gz
#Patch0:         impacket-0.9.11-setup.patch
BuildArch:      noarch

BuildRequires:  python2-devel
BuildRequires:  python-setuptools

%description
Impacket is a collection of Python classes focused on providing access to
network packets. Impacket allows Python developers to craft and decode network
packets in simple and consistent manner. it is highly effective when used in
conjunction with a packet capture utility or package such as Pcapy. Packets
can be constructed from scratch, as well as parsed from raw data. Furthermore,
the object oriented API makes it simple to work with deep protocol hierarchies.

%prep
%setup -q -n %{srcname}-%{version}
for file in uncrc32.py nmapAnswerMachine.py os_ident.py loopchain.py; do
    sed -i -e '1i#!/usr/bin/env python' examples/$file
done

%build
%{__python2} setup.py build

%install
%{__python2} setup.py install --skip-build --root %{buildroot}
for file in tds.py ese.py; do
    chmod a+x %{buildroot}%{python2_sitelib}/%{srcname}/$file
done
rm -rf %{buildroot}/usr/bin %{buildroot}/usr/share/doc/impacket

%files
%doc ChangeLog LICENSE README examples
%{python2_sitelib}/%{srcname}/
%{python2_sitelib}/impacket*.egg-info
%exclude %{_defaultdocdir}/%{name}/testcases/*

%changelog
* Sat Jun 28 2014 Fabian Affolter <mail@fabian-affolter.ch> - 0.9.11-2
- Move files out of /usr/bin
- Update licence (according to mailing list)

* Wed Feb 26 2014 Fabian Affolter <mail@fabian-affolter.ch> - 0.9.11-1
- Updated to new upstream release 0.9.11

* Sat Aug 10 2013 Fabian Affolter <mail@fabian-affolter.ch> - 0.9.10-1
- Updated to new upstream release 0.9.10

* Sat Nov 17 2012 Fabian Affolter <mail@fabian-affolter.ch> - 0.9.9.9-1
- Initial package
