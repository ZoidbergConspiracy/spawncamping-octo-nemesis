%define python_major 3

Name: python%{python_major}-wptools
Summary: Wikipedia Tools for Humans
License: MIT
URL: https://github.com/siznax/wptools
Group: Development/Tools

Packager: Thornton Prime <thornton.prime@gmail.com>
Distribution: FDM

%define python_package wptools
%define git_path siznax/wptools
%define git_version 0
%define xgit_tag v%{git_version}
%define git_tag %( git ls-remote https://github.com/%{git_path}.git | grep HEAD | awk '{ print $1 }' )

#Version: %{git_version}
Version: %{git_version}_%( echo %{git_tag} | cut -c 1-8 )git
Release: 2.fdm
Epoch: %( date +"%Y%m%d" )
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

Requires: python%{python_major}-certifi
Requires: python%{python_major}-html2text
Requires: python%{python_major}-lxml
Requires: python%{python_major}-pycurl

%changelog
* Mon Jul 10 2017 Thornton Prime <thornton.prime@gmail.com> [0_git]
- Update for Python3
- Build for FDM25

%description
Python and command-line MediaWiki access for Humans.

get an HTML or plain text "extract" (lead or summary)
get a representative image (pageimage, thumb, etc.)
get an Infobox as a python dictionary
get any/all Wikidata by title
get info in any language
get random info

This package is intended to make it as easy as possible to get data from
MediaWiki instances, expose more Wikidata, and extend Wikimedia APIs just
for kicks.

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
env > foo.txt
LANG=en_US.UTF-8 %{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
LANG=en_US.UTF-8 %{__python} setup.py install --root=%{buildroot} --record=INSTALLED_FILES
#find %{buildroot} -type f -name '*.pyo' -printf '/%P%f\n' >> INSTALLED_FILES

%clean
%{__rm} -rf %{buildroot}

%files -f INSTALLED_FILES
%defattr(-,root,root)

