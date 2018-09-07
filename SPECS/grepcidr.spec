Summary: Filter IPv4 and IPv6 addresses matching CIDR patterns
Name: grepcidr
Version: 2.0
Release: 1.fdm
Source0: http://www.pc-tools.net/files/unix/%{name}-%{version}.tar.gz
License: GPL
Group: System Environment/Utilities
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
Vendor: PC-Tools.Net
Url: http://www.pc-tools.net/unix/grepcidr/

%description
grepcidr can be used to filter a list of IP addresses against one or more
Classless Inter-Domain Routing (CIDR) specifications. As with grep, there
are options to invert matching and load patterns from a file, grepcidr is
capable of efficiently processing large numbers of IPs and networks.

grepcidr has endless uses in network software, including： mail
filtering and processing, network security, log analysis, and many custom
applications.

%prep
%setup -n %{name}-%{version}

%build
%{__make}

%install
%{__install} -D grepcidr %{buildroot}/%{_bindir}/grepcidr
%{__install} -D grepcidr.1 %{buildroot}/%{_mandir}/man1/grepcidr.1


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/grepcidr
%{_mandir}/man1/grepcidr.1*
%doc README COPYING
%doc ChangeLog
