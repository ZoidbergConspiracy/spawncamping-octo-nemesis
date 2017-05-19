%define python_major 3

Name: python%{python_major}-cymem
Summary: A Cython Memory Helper
License: MIT
URL: https://github.com/explosion/cymem
Group: Development/Tools

Packager: Thornton Prime <thornton.prime@gmail.com>
Distribution: FDM

%define python_package cymem
%define git_path explosion/cymem
%define git_version 1.31.2
%define git_tag v%{git_version}
%define git_tagx %( git ls-remote https://github.com/%{git_path}.git | grep HEAD | awk '{ print $1 }' )

Version: %{git_version}
#Version: Version: %{git_version}_%( echo %{git_tag} | cut -c 1-8 )git
Release: 1.fdm
Epoch: %( date +"%Y%m%d" )
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

Requires: python%{python_major}-Cython

%changelog
* Thu May 18 2017 Thornton Prime <thornton.prime@gmail.com> [1.8.2]
- Update for Python3
* Mon Jan 23 2017 Thornton Prime <thornton.prime@gmail.com> [1.31.2]
- Build for FDM25

%description
cymem provides two small memory-management helpers for Cython. They make
it easy to tie memory to a Python object's life-cycle, so that the memory
is freed when the object is garbage collected.

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
CFLAGS="%{optflags}" LANG=en_US.UTF-8 %{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
LANG=en_US.UTF-8 %{__python} setup.py install --root=%{buildroot} --record=INSTALLED_FILES
#find %{buildroot} -type f -name '*.pyo' -printf '/%P%f\n' >> INSTALLED_FILES

%clean
%{__rm} -rf %{buildroot}

%files -f INSTALLED_FILES
%defattr(-,root,root)

