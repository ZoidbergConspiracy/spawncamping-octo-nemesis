Name: python3-pureconfig
Summary: Python implemntation of the Pure configuration specification
License: MIT
URL: https://github.com/sefakilic/pureconfig
Group: Development/Tools

Packager: Thornton Prime <thornton.prime@gmail.com>
Distribution: FDM

%define python_package pureconfig
%define git_package pureconfig/pureconfig
# %define git_version 1.0.0
%define __python /usr/bin/python3

# Version: %{git_version}
Version: 0.git%( date +"%Y%m%d" )
Release: 1.fdm
Epoch: %( date +"%Y%m%d" )
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%changelog
* Thu Dec 22 2016 Thornton Prime <thornton.prime@gmail.com> [git]
- Build for FDM25

%description
Pure is a specification for a configuration file format. Its goal is
to suck less than other configuration file formats.

Most people will find Pure entirely natural to read and edit. 

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
# env CFLAGS="%{optflags}" %{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
#%{__python} setup.py install --root=%{buildroot} --record=INSTALLED_FILES
#find %{buildroot} -type f -name '*.pyo' -printf '/%P%f\n' >> INSTALLED_FILES
mkdir -p %{buildroot}%{python_site_packages}
cp -r python3/pure %{buildroot}%{python_site_packages}
%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
%{python_site_packages}/pure

