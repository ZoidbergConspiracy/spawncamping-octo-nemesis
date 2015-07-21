Name:		lsgvt
Version:	0.3
Release:	0.1%{?dist}
Summary:	List Gluster Volume Toplogy

Group:		Applications/System
License:	GPLv3
URL:		https://forge.gluster.org/lsgvt
#Source0:	https://forge.gluster.org/lsgvt/lsgvt/archive-tarball/v%{version}
Source0:	%{name}-%{version}.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires:	python-devel

%description
This program shows a pretty graphical representation of a Gluster volume's
topology. It uses the fuse-<volname>.vol file for it's source. If you do not
give any parameters, it shows the topology for all the volumes. Otherwise it
will show the topology for the given space-separated list of volume names.


%prep
%setup -q -n %{name}-%{name}


%build


%install
rm -rf %{buildroot}
install -D -m 755 lsgvt %{buildroot}/%{_bindir}/lsgvt


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc COPYING README.md
%{_bindir}/lsgvt


%changelog
* Mon Mar 24 2014 Niels de Vos <ndevos@redhat.com> - 0.3-0.1
- Update to version 0.3
- Fix the install command

* Thu Mar 20 2014 Niels de Vos <ndevos@redhat.com> - 0.2-0.1
- Initial packaging.
