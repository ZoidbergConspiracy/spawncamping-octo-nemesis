%define _enable_debug_packages %{nil}
%define debug_package          %{nil}

%define up_name Linux_MegaCLI

Summary:	Manage SAS RAID controllers
Name:		megacli
Version:	8.02.21
Release:	1
License:	Commercial
Group:		System/Configuration/Hardware
URL:		http://www.lsi.com
Source0:	http://www.lsi.com/support/downloads/megaraid/miscellaneous/%{version}_MegaCLI.zip

%description
MegaCli is used to manage SAS RAID controllers.

%prep
%setup -q -c
cd %{version}_%{up_name}/
unzip MegaCliLin.zip
rpm2cpio MegaCli-%{version}-1.noarch.rpm | cpio -id

%build

%install
export DONT_STRIP=1

install -d -m 755 %{buildroot}/sbin
%ifarch x86_64
install -m 755 %{version}_%{up_name}/opt/MegaRAID/MegaCli/MegaCli64 %{buildroot}/sbin/megacli
%else
install -m 755 %{version}_%{up_name}/opt/MegaRAID/MegaCli/MegaCli %{buildroot}/sbin/megacli
%endif

%files 
%doc %{version}_MegaCLI.txt
/sbin/megacli


%changelog
* Sat May 19 2012 Alexander Khrukin <akhrukin@mandriva.org> 8.02.21-1
+ Revision: 799622
- version update 8.02.21

* Mon Jan 04 2010 Thierry Vignaud <tv@mandriva.org> 5.00.20-2mdv2010.1
+ Revision: 486161
- fix description

* Fri Jan 01 2010 Guillaume Rousse <guillomovitch@mandriva.org> 5.00.20-1mdv2010.1
+ Revision: 484692
- new version

* Mon Jul 06 2009 Guillaume Rousse <guillomovitch@mandriva.org> 4.00.11-1mdv2010.0
+ Revision: 392803
- new version
- fix description

* Mon Sep 15 2008 Oden Eriksson <oeriksson@mandriva.com> 2.00.11-2mdv2009.0
+ Revision: 284889
- merge changes from private package

* Thu Sep 11 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.00.11-1mdv2009.0
+ Revision: 283751
- new version

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 1.01.39-2mdv2009.0
+ Revision: 241708
- rebuild

* Mon Feb 04 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.01.39-1mdv2008.1
+ Revision: 162042
- import megacli

