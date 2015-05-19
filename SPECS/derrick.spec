Name: derrick
Version: 20140630
Release: 1%{?dist}
Summary: A Simple Network Stream Recorder

Group: System Environment/Network
License: GPL
URL: https://github.com/rieck/derrick

Source0: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: libnet-devel libpcap-devel libnids-devel
Requires: libnet libpcap libnids

%description
Derrick is a simple tool for recording data streams of TCP and UDP traffic.
It shares similarities with other network recorders, such as tcpflow and
wireshark, where it is more advanced than the first and clearly inferior to
the latter.

Derrick has been specifically designed to monitor application-layer
communication. In contrast to other tools the application data is logged in
a line-based ASCII format. Common UNIX tools, such as grep, sed & awk, can
be directly applied. Even replay of recorded communication is straight
forward using netcat.

Derrick supports on-the-fly compression and rotation of log files. The
payloads of TCP sessions are re-assembled using Libnids and can be merged
or truncated. UDP payloads are logged as-is. Details of lower network
layers are omitted.

%prep
%setup -q -n %{name}

%build
export CFLAGS="$RPM_OPT_FLAGS -ggdb2 -O2 -fno-strict-aliasing"
./bootstrap
%{configure}
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_bindir}/*
%{_mandir}/man?/*
%doc README* COPYING

%changelog
* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 14-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

