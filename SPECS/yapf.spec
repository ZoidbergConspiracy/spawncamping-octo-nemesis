Name: yapf
Summary: API for Managing TP-Link Power Switches and Bulbs
License: MIT
Group: Development/Tools

Packager: Thornton Prime <thornton.prime@gmail.com>
Distribution: FDM

%define python_package yapf
%define git_url google/%{python_package}
# %define git_version %( git ls-remote https://github.com/%{git_url}.git | grep HEAD | cut -c 1-12 )
%define git_version 0.15.2
%define __python /usr/bin/python2

# Version: %(date  +"%Y%m%d" ).%{git_version}.git
Version: %{git_version}
Release: 1.fdm
Epoch: %( date +"%Y%m%d" )
URL: https://github.com/%{git_url}
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch

Requires: python2-futures

%changelog
*Wed Feb 01 2017 Thornton Prime <thornton.prime@gmail.com> [%{git_version}]
- Build for FDM25

%description
Most of the current formatters for Python --- e.g., autopep8, and pep8ify ---
are made to remove lint errors from code. This has some obvious limitations.
For instance, code that conforms to the PEP 8 guidelines may not be
reformatted. But it doesn't mean that the code looks good.

YAPF takes a different approach. It's based off of 'clang-format', developed by
Daniel Jasper. In essence, the algorithm takes the code and reformats it to the
best formatting that conforms to the style guide, even if the original code
didn't violate the style guide. The idea is also similar to the 'gofmt' tool
for the Go programming language: end all holy wars about formatting - if the
whole codebase of a project is simply piped through YAPF whenever modifications
are made, the style remains consistent throughout the project and there's no
point arguing about style in every code review.

The ultimate goal is that the code YAPF produces is as good as the code that a
programmer would write if they were following the style guide. It takes away
some of the drudgery of maintaining your code.

%define python_version %( %{__python} -c 'import sys; print sys.version.split()[0]' )
%define python_version_short %( %{__python} -c 'import sys; print ".".join(sys.version.split()[0].split(".")[:2])' )
%define python_site_packages %( %{__python} -c 'import sys; print [x for x in sys.path if x[-13:] == "site-packages" ][0]' )

# Turn off the brp-python-bytecompile script
%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')

%prep
%setup -cT
git clone https://github.com/%{git_url}.git .
# git checkout %{git_version}
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

