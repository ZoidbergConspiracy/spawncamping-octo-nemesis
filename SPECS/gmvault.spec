Name: gmvault
Summary: Backup and restore your Gmail
License: AGPL-2
URL: http://gmvault.org/index.html
Group: Internet/Applications

Packager: Thornton Prime <thornton.prime@gmail.com>
Distribution: FDM

%define python_package gmvault
%define git_package gaubert/%{python_package}
%define git_version 1.9.1
%define git_minor 2016031
%define __python /usr/bin/python2

Version: %{git_version}
BuildArch: noarch
Release: 1.fdm
Epoch: %( date +"%Y%m%d" )
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires: python-logbook
%changelog
* Fri Nov 18 2016 Thornton Prime <thornton.prime@gmail.com> [1.9.1]
- Build for FDM24

%description
Gmvault is a tool for backing up your gmail account and never lose email
correspondence.

%define python_version %( %{__python} -c 'import sys; print sys.version.split()[0]' )
%define python_version_short %( %{__python} -c 'import sys; print ".".join(sys.version.split()[0].split(".")[:2])' )
%define python_site_packages %( %{__python} -c 'import sys; print [x for x in sys.path if x[-13:] == "site-packages" ][0]' )

# Turn off the brp-python-bytecompile script
%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')

%prep
%setup -cT
git clone https://github.com/%{git_package}.git .
git checkout -b v%{git_version}-%{git_minor}
git branch --set-upstream-to=origin/master v%{git_version}-%{git_minor}

%build
env CFLAGS="%{optflags}" %{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install --root=%{buildroot} --record=INSTALLED_FILES
#find %{buildroot} -type f -name '*.pyo' -printf '/%P%f\n' >> INSTALLED_FILES

%clean
%{__rm} -rf %{buildroot}

%files -f INSTALLED_FILES
%defattr(-,root,root)

