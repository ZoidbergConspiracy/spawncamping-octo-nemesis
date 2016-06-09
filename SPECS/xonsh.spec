Name: xonsh
Summary: Python-ish, BASHwards-looking Shell
License: Apache
URL: https://github.com/burnash/gspread
Group: System/Shells

Packager: Thornton Prime <thornton.prime@gmail.com>
Distribution: FDM 6

Version: 0.3.2
Release: 1.fdm
Epoch: %( date +"%Y%m%d" )
BuildArch: noarch
BuildRequires: python3-ply python3-prompt_toolkit python3-jupyter_core python3-setproctitle python3-distro-info

# Turn off the brp-python-bytecompile script
%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')

%description
Xonsh is a Python-ish, BASHwards-looking shell language and command prompt.
The language is a superset of Python 3.4+ with additional shell primitives
that you are used to from Bash and IPython.

%changelog
* Thu Apr  7 2016 Thornton Prime <thornton.prime@gmail.com> [0.3.0]
- Updated to pull directly from git
* Sat Oct 27 2012 Thornton Prime <thornton@yoyoweb.com> []
- 

%prep
%setup -cT

git clone --branch %{version} https://github.com/scopatz/xonsh.git .

%build
env CFLAGS="%{optflags}" python3 setup.py build

%install
%{__rm} -rf %{buildroot}
python3 setup.py install --root=%{buildroot} --record=INSTALLED_FILES
#find %{buildroot} -type f -name '*.pyo' -printf '/%P%f\n' >> INSTALLED_FILES

%clean
%{__rm} -rf %{buildroot}

%files -f INSTALLED_FILES
%defattr(-,root,root)
%doc README* license*

