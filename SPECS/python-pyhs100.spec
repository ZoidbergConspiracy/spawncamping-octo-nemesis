%define python_major 3
  
Name: python%{python_major}-pyhs100
Summary: API for Managing TP-Link Power Switches and Bulbs
License: GPLv3
Group: Development/Tools

Packager: Thornton Prime <thornton.prime@gmail.com>
Distribution: FDM

%define python_package pyHS100
%define git_path GadgetReactor/%{python_package}
%define git_version 0.3.0
%define git_tag %{git_version}
%define xgit_tag %( git ls-remote https://github.com/%{git_path}.git | grep HEAD | awk '{ print $1 }' )

Version: %{git_version}
#Version: Version: %{git_version}_%( echo %{git_tag} | cut -c 1-8 )git
Release: 1.fdm
Epoch: %( date +"%Y%m%d" )
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch

Requires: python%{python_major}-click

%changelog
* Wed Oct 11 2017 Thornton Prime <thornton.prime@gmail.com> [0.3.0]
- Updated to 0.3.0
* Mon Jan 30 2017 Thornton Prime <thornton.prime@gmail.com> [%{git_tag}]
- Build for FDM25

%description
Python Library to control TPLink Switch (HS100 / HS110)

%define __python /usr/bin/python%{python_major}
%define python_version %( %{__python} -c 'import sys; print sys.version.split()[0]' )
%define python_version_short %( %{__python} -c 'import sys; print ".".join(sys.version.split()[0].split(".")[:2])' )
%define python_site_packages %( %{__python} -c 'import sys; print [x for x in sys.path if x[-13:] == "site-packages" ][0]' )

# Turn off the brp-python-bytecompile script
%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')

%prep
%setup -cT
git clone https://github.com/%{git_path}.git .
git checkout -b %{git_tag}
git branch --set-upstream-to=origin/master %{git_tag}

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
%doc README.md LICENSE
