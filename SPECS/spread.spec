Name: spread
Summary: High performance messaging toolkit
License: BSD-ish
URL: http://www.spread.org/
Group: Development/Libraries

Packager: Thornton Prime <tprime@amgen.com>
Distribution: Amgen 8.0

Version: 4.3.0
Release: 1.fdm
Epoch: %( date +"%Y%m%d" )

Source: http://www.cnds.jhu.edu/download/spread-src-%{version}.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
Spread is a toolkit that provides a high performance messaging service
that is resilient to faults across external or internal networks.
Spread functions as a unified message bus for distributed applications,
and provides highly tuned application-level multicast and group
communication support. Spread services range from reliable message
passing to fully ordered messages with delivery guarantees, even in
case of computer failures and network partitions. Spread is designed to
encapsulate the challenging aspects of asynchronous networks and enable
the construction of scalable distributed applications, allowing
application builders to focus on the differentiating components of
their application.

%changelog

%prep
%setup -q -n %{name}-src-%{version}

%build
%{configure} \
	--with-mantype=man \
	--with-pid-dir=/var/run/spread \
	--with-unix-socket-dir=/var/run/spread

for MAN in docs/*.?; do
	cp ${MAN} ${MAN}.out
done

make

%install
%{__rm} -rf $RPM_BUILD_ROOT
%{makeinstall}
rm -rf $RPM_BUILD_ROOT/usr/share/doc/spread

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/*
%{_sbindir}/*
%{_includedir}/*
%{_mandir}/man?/*
%{_libdir}/*
%config %{_sysconfdir}/spread.conf
%doc license.txt Readme.txt docs/*.txt docs/sample*

