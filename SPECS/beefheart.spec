Name: beefheart
Version: 0.2
Release: 1.fdm
Summary: A simple captive portal system for IPTables

Group: System Environment
License: GPLv2

URL: http://www.yoyoweb.com
Source1: beefheart
Source2: beefheart.init
Source3: beefheart.firewall

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch: noarch

%description
Beefheart is a simple captive portal system for IPTables.

Users are redirected to a portal when trying to access the internet, and
they are prompted for a token. A valid token grants them access for a fixed
period of time, during which outgoing packets are marked for MASQUERADE.

The daemon monitors the table and expires tokens as well as handling the
captive web portal. The same program, used from the CLI, enables token
management.

%prep
%setup -q  -c -T
cp %{SOURCE1} %{SOURCE2} %{SOURCE3} .

%build

%install
rm -rf $RPM_BUILD_ROOT

# yum
mkdir -p ${RPM_BUILD_ROOT}%{_sbindir}
install -pm 755 %{SOURCE1} $RPM_BUILD_ROOT/%{_sbindir}
mkdir -p ${RPM_BUILD_ROOT}%{_sysconfdir}/init.d
install -pm 755 %{SOURCE2} ${RPM_BUILD_ROOT}%{_sysconfdir}/init.d/beefheart
mkdir -p ${RPM_BUILD_ROOT}%{_sharedstatedir}/beefheart
%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_sbindir}/beefheart
%{_sysconfdir}/init.d/beefheart
%dir %{_sharedstatedir}/beefheart
%doc beefheart.firewall

%changelog
* Wed Sep 12 2012 Thornton Prime <theoszi@yahoo.com> - 1-1
- Initial FDM build.

