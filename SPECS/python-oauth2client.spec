Name: python-oauth2client
Summary: Python Google Spreadsheets API
License: Apache
URL: https://github.com/google/oauth2client
Group: Development/Tools

Packager: Thornton Prime <thornton.prime@gmail.com>
Distribution: FDM 6

Version: 2.0.1
Release: 1.fdm
Epoch: %( date +"%Y%m%d" )
BuildArch: noarch

%define python_package python-oauth2client
%define python_version %( python -c 'import sys; print sys.version.split()[0]' )
%define python_version_short %( python -c 'import sys; print ".".join(sys.version.split()[0].split(".")[:2])' )
%define python_site_packages %( python -c 'import sys; print [x for x in sys.path if x[-13:] == "site-packages" ][0]' )

# Turn off the brp-python-bytecompile script
%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')

%description
This is a client library for accessing resources protected by OAuth 2.0.

%changelog
* Thu Apr  7 2016 Thornton Prime <thornton.prime@gmail.com> [0.3.0]
- Updated to pull directly from git
- 

%prep
%setup -cT

git clone --branch v%{version} https://github.com/google/oauth2client.git .

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
%doc README* LICENSE*

