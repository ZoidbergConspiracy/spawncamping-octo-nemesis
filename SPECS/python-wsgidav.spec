%define python_major 3

Name: python%{python_major}-wsgidav
Summary: Python implemntation of WebDAV Server
License: MIT
URL: https://github.com/mar10/wsgidav
Group: Development/Tools

Packager: Thornton Prime <thornton.prime@gmail.com>
Distribution: FDM

%define python_package wsgidav
%define git_path mar10/wsgidav
%define git_version 2.2.1
%define git_tag v%{git_version}
#%define git_tag %( git ls-remote https://github.com/%{git_path}.git | grep HEAD | awk '{ print $1 }' )

Version: 2.2.1
#Version: Version: %{git_version}_%( echo %{git_tag} | cut -c 1-8 )git
Release: 1.fdm
Epoch: %( date +"%Y%m%d" )
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires: python%{python_major}-defusedxml python%{python_major}-lxml

%changelog
* Sat May 13 2017 Thornton Prime <thornton.prime@gmail.com> [2.2.1]
- Build for Python3
* Fri Jan 20 2017 Thornton Prime <thornton.prime@gmail.com> [git]
- Build for FDM25

%description
WsgiDAV is a generic WebDAV server written in Python and based on WSGI.

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
%{__python} setup.py install -O1 --root=%{buildroot} --record=INSTALLED_FILES
#find %{buildroot} -type f -name '*.pyo' -printf '/%P%f\n' >> INSTALLED_FILES

%clean
%{__rm} -rf %{buildroot}

%files -f INSTALLED_FILES
%defattr(-,root,root)
%doc LICENSE* README* THANKS* TODO* CHANGELOG* CONTRIBUTING*
