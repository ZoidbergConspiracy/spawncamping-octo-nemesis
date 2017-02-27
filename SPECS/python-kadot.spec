%define python_major 3

Name: python%{python_major}-kadot
Summary: Unsupervised natual language processing
License: MIT
Group: Development/Tools
URL: https://github.com/%{git_path}
Packager: Thornton Prime <thornton.prime@gmail.com>
Distribution: FDM 25

%define python_package Kadot
%define git_path the-new-sky/%{python_package}
%define git_version v%{version}
# %( git ls-remote https://github.com/%{git_path}.git | grep HEAD | cut -c 1-12 )

Version: 1.5.0
Release: 0.fdm
Epoch: %( date +"%Y%m%d" )

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch
Requires: python%{python_major}-numpy python%{python_major}-numpy python%{python_major}-scikit-learn

%description
Kadot, the unsupervised natural language processing library.

Kadot includes tokenizers, text generators, word-level and document-level
vectorizers (and I currently work on classifiers).

The philosophy of Kadot is "never hardcode the language rules": use
unsupervised solutions to support most languages. So it will never
includes Treebank based algorithms (like a POS Tagger): use TextBlob
to do that.

%changelog
* Mon Feb 27 2017 Thornton Prime <thornton.prime@gmail.com> [1.5.0]
- Build from git 1.5.0

%define __python /usr/bin/python%{python_major}
%define python_version %( %{__python} -c 'import sys; print sys.version.split()[0]' )
%define python_version_short %( %{__python} -c 'import sys; print( ".".join(sys.version.split()[0].split(".")[:2]) )' )
%define python_site_packages %( %{__python} -c 'import sys; print( [x for x in sys.path if x[-13:] == "site-packages" ][0] )' )

# Turn off the brp-python-bytecompile script
%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')

%prep
%setup -cT
git clone https://github.com/%{git_path}.git .
git checkout -b %{git_version}
git branch --set-upstream-to=origin/master %{git_version}

%build
#env CFLAGS="%{optflags}" %{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
mkdir -p %{buildroot}%{python_site_packages}
cp -r kadot %{buildroot}%{python_site_packages}/

#%{__python} setup.py install --root=%{buildroot} --record=INSTALLED_FILES
#find %{buildroot} -type f -name '*.pyo' -printf '/%P%f\n' >> INSTALLED_FILES

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
%{python_site_packages}/kadot
%doc README* LICENSE*

