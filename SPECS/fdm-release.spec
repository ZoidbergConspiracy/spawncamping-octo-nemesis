Name: fdm-release       
Version: 3
Release: 1.fdm
Summary: Packages for Farnsworth's Deadly Machines
URL: http://www.yoyoweb.com

Group: System Environment/Base 
License: GPLv2

BuildArch:     noarch
Source1: fdm.repo	

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
This package includes the yum repository file for the FDM distribution.

The Farnsworth's Deadly Machines (FDM) distribution is a set of packages that add
onto RedHat, Fedora, CentOS or other similar distributions.

%changelog
* Wed Oct 08 2014 Thornton Prime <thornton.prime@gmail.com> [3]
- Updated URL

* Mon Apr 28 2014 Thornton Prime <theoszi@yahoo.com> [1.4]
- Build for FDM 2

* Thu Aug 16 2012 Thornton Prime <theoszi@yahoo.com> - 1-1
- Initial FDM build.

* Wed May  9 2012 Jens Petersen <petersen@redhat.com> - 6-7
- add ppc64 to ghc_arches

%prep
%setup -q  -c -T
install -pm 644 %{SOURCE1} .

%build

%install
rm -rf $RPM_BUILD_ROOT

# yum
install -dm 755 $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d
install -pm 644 %{SOURCE1} \
    $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d

%clean
rm -rf $RPM_BUILD_ROOT

%postun 
#sed -i '/^yum\ fdm/d' %{_sysconfdir}/sysconfig/rhn/sources
#sed -i '/^\#\ fdm\ repo\ /d' %{_sysconfdir}/sysconfig/rhn/sources


%files
%defattr(-,root,root,-)
%config(noreplace) /etc/yum.repos.d/*



