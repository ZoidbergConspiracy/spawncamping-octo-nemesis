%define python_major 3

Name: python%{python_major}-spacy
Summary: Industrial-strength Natural Language Processing (NLP) with Python and Cython
License: MIT
URL: https://spaCy.io
Group: Development/Tools

Packager: Thornton Prime <thornton.prime@gmail.com>
Distribution: FDM

%define python_package spacy
%define git_path explosion/spacy
%define git_version 1.8.2
%define git_tag v%{git_version}
%define git_tagx %( git ls-remote https://github.com/%{git_path}.git | grep HEAD | awk '{ print $1 }' )

Version: %{git_version}
#Version: Version: %{git_version}_%( echo %{git_tag} | cut -c 1-8 )git
Release: 2.fdm
Epoch: %( date +"%Y%m%d" )
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

# Core Fedora packages
Requires: python%{python_major}-Cython
Requires: python%{python_major}-numpy
Requires: python%{python_major}-pathlib2
Requires: python%{python_major}-six
Requires: python%{python_major}-ujson
Requires: python%{python_major}-dill
Requires: python%{python_major}-requests
Requires: python%{python_major}-regex

# FDM Explosion Packages
Requires: python%{python_major}-cymem
Requires: python%{python_major}-thinc

# FDM Other Packages
#preshed
#murmurhash
#plac
#ftfy

%changelog
* Thu May 18 2017 Thornton Prime <thornton.prime@gmail.com> [1.8.2]
- Update for Python3
- Build for FDM25
* Fri Oct 21 2016 Thornton Prime <thornton.prime@gmail.com> [1.0.0]
- Build for FDM24

%description
spaCy is a library for advanced natural language processing in Python
and Cython. See here for documentation and details. spaCy is built on
the very latest research, but it isn't researchware. It was designed
from day 1 to be used in real products. 

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

