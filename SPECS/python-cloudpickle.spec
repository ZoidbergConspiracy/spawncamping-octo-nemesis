Name: python-cloudpickle
Summary: Python extended pickling support
License: MIT
URL: https://github.com/cloudpipe/cloudpickle
Group: Development/Tools

Packager: Thornton Prime <thornton.prime@gmail.com>
Distribution: FDM

%define python_package cloudpickle
%define git_package cloudpipe/cloudpickle
%define git_version 0.2.1
%define __python /usr/bin/python2

Version: %{git_version}
Release: 1.fdm
Epoch: %( date +"%Y%m%d" )
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: python-preshed python-murmurhash

%changelog
* Mon Jan 23 2017 Thornton Prime <thornton.prime@gmail.com> [2.7.4]
- Build for FDM25

%description
cloudpickle makes it possible to serialize Python constructs not
supported by the default pickle module from the Python standard library.

cloudpickle is especially useful for cluster computing where Python
expressions are shipped over the network to execute on remote hosts,
possibly close to the data.

Among other things, cloudpickle supports pickling for lambda expressions,
functions and classes defined interactively in the __main__ module.

%define python_version %( %{__python} -c 'import sys; print sys.version.split()[0]' )
%define python_version_short %( %{__python} -c 'import sys; print ".".join(sys.version.split()[0].split(".")[:2])' )
%define python_site_packages %( %{__python} -c 'import sys; print [x for x in sys.path if x[-13:] == "site-packages" ][0]' )

# Turn off the brp-python-bytecompile script
%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')

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

