%define python_major 3

Name: python%{python_major}-thinc
Summary: Machine learning for NLP in Python
License: MIT
URL: https://github.com/explosion/thinc
Group: Development/Tools

Packager: Thornton Prime <thornton.prime@gmail.com>
Distribution: FDM

%define python_package thinc
%define git_path explosion/thinc
%define git_version 6.7.3
%define git_tag v%{git_version}
%define git_tagx %( git ls-remote https://github.com/%{git_path}.git | grep HEAD | awk '{ print $1 }' )

Version: %{git_version}
#Version: Version: %{git_version}_%( echo %{git_tag} | cut -c 1-8 )git
Release: 1.fdm
Epoch: %( date +"%Y%m%d" )
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

Requires: python%{python_major}-Cython

%changelog
* Tue Jun 13 2017 Thornton Prime <thornton.prime@gmail.com> [6.7.3]
- Update for Python3

%description
Thinc is the machine learning library powering spaCy. It features a
battle-tested linear model designed for large sparse learning problems, and a
flexible neural network model under development for spaCy v2.0.

Thinc is a practical toolkit for implementing models that follow the "Embed,
encode, attend, predict" architecture. It's designed to be easy to install,
efficient for CPU usage and optimised for NLP and deep learning with text – in
particular, hierarchically structured input and variable-length sequences.

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

