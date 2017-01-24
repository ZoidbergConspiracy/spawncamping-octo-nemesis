%define __python /usr/bin/python2
Name: python2-wsgidav
Summary: Python implemntation of WebDAV Server
License: MIT
URL: https://github.com/mar10/wsgidav
Group: Development/Tools

Packager: Thornton Prime <thornton.prime@gmail.com>
Distribution: FDM

%define python_package wsgidav
%define git_package mar10/wsgidav
# %define git_version 1.0.0

# Version: %{git_version}
Version: 0.git%( date +"%Y%m%d" )
Release: 1.fdm
Epoch: %( date +"%Y%m%d" )
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires: python2-defusedxml python2-lxml

%changelog
* Fri Jan 20 2017 Thornton Prime <thornton.prime@gmail.com> [git]
- Build for FDM25

%description
WsgiDAV is a generic WebDAV server written in Python and based on WSGI.

%define python_version %( %{__python} -c 'import sys; print ( sys.version.split()[0] )' )
%define python_version_short %( %{__python} -c 'import sys; print ( ".".join(sys.version.split()[0].split(".")[:2]) )' )
%define python_site_packages %( %{__python} -c 'import sys; print ( [x for x in sys.path if x[-13:] == "site-packages" ][0] )' )

# Turn off the brp-python-bytecompile script
%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')

%prep
%setup -cT
git clone https://github.com/%{git_package}.git .
#git checkout -b v%{git_version}
#git branch --set-upstream-to=origin/master v%{git_version}

%build
env CFLAGS="%{optflags}" %{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install --single-version-externally-managed -O1 --root=%{buildroot} --record=INSTALLED_FILES
#find %{buildroot} -type f -name '*.pyo' -printf '/%P%f\n' >> INSTALLED_FILES

%clean
%{__rm} -rf %{buildroot}

%files -f INSTALLED_FILES
%defattr(-,root,root)

