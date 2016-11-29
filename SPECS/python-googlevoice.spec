Name: python-googlevoice
Summary: API to Google Voice
License: MIT
URL: http://sphinxdoc.github.com/pygooglevoice/
Group: Development/Tools

Packager: Thornton Prime <thornton.prime@gmail.com>
Distribution: FDM

%define python_package pygooglevoice
%define git_package pettazz/%{python_package}
#%define git_version 1.0.0
%define __python /usr/bin/python2

#Version: %{git_version}
Version: 0.git%( date +"%Y%m%d" )
Release: 1.fdm
Epoch: %( date +"%Y%m%d" )
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%changelog
* Wed Nov 16 2016 Thornton Prime <thornton.prime@gmail.com> [0.git]
- Build for FDM24

%description
Google Voice for Python Allows you to place calls, send sms, download
voicemail, and check the various folders of your Google Voice Accounts.
You can use the Python API or command line script to schedule calls,
check for new recieved calls/sms, or even sync your recorded
voicemails/calls.

%define python_version %( %{__python} -c 'import sys; print sys.version.split()[0]' )
%define python_version_short %( %{__python} -c 'import sys; print ".".join(sys.version.split()[0].split(".")[:2])' )
%define python_site_packages %( %{__python} -c 'import sys; print [x for x in sys.path if x[-13:] == "site-packages" ][0]' )

# Turn off the brp-python-bytecompile script
%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')

%prep
%setup -cT
git clone https://github.com/%{git_package}.git .
# git checkout -b v%{git_version}
# git branch --set-upstream-to=origin/master v%{git_version}

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

