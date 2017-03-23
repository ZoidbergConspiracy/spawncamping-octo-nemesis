Name: python-spacy
Summary: Industrial-strength Natural Language Processing (NLP) with Python and Cython
License: MIT
URL: https://spaCy.io
Group: Development/Tools

Packager: Thornton Prime <thornton.prime@gmail.com>
Distribution: FDM

%define python_package spacy
%define git_package explosion/spacy
%define git_version 1.7.2
%define __python /usr/bin/python2

Version: %{git_version}
Release: 2.fdm
Epoch: %( date +"%Y%m%d" )
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

Requires: python2-numpy python2-ujson python2-tqdm python2-toolz python2-Cython python2-cytoolz
Requires: python-six python-pathlib python-flexmock 

Requires: python-cymem python-thinc
Requires: python-sputnik
Requires: python-semver python-cloudpickle python-plac 

%changelog
* Fri Oct 21 2016 Thornton Prime <thornton.prime@gmail.com> [1.0.0]
- Build for FDM24

%description
spaCy is a library for advanced natural language processing in Python
and Cython. See here for documentation and details. spaCy is built on
the very latest research, but it isn't researchware. It was designed
from day 1 to be used in real products. 

%define python_version %( %{__python} -c 'import sys; print sys.version.split()[0]' )
%define python_version_short %( %{__python} -c 'import sys; print ".".join(sys.version.split()[0].split(".")[:2])' )
%define python_site_packages %( %{__python} -c 'import sys; print [x for x in sys.path if x[-13:] == "site-packages" ][0]' )

# Turn off the brp-python-bytecompile script
%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')

# BuildRequires: python3-Cython

%prep
%setup -cT
git clone https://github.com/%{git_package}.git .
git checkout -b v%{git_version}
git branch --set-upstream-to=origin/master v%{git_version}

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

