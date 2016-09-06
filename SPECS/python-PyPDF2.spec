Name: python-PyPDF2
Summary: Pure Python PDF Library
License: Apache
URL: http://mstamy2.github.com/PyPDF2
Group: Development/Tools

Packager: Thornton Prime <thornton.prime@gmail.com>
Distribution: FDM

%define python_package PyPDF2

Version: 1.26.0
Release: 1.fdm
Epoch: %( date +"%Y%m%d" )
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Source: %{python_package}-%{version}.tar.gz

%changelog
* Thu Sep 01 2016 Thornton Prime <thornton.prime@gmail.com> [1.26.0]
- Build for FDM24

%description
A Pure-Python library built as a PDF toolkit. It is capable of:

 * extracting document information (title, author, …)
 * splitting documents page by page
 * merging documents page by page
 * cropping pages
 * merging multiple pages into a single page
 * encrypting and decrypting PDF files
 * and more!

By being Pure-Python, it should run on any Python platform without any
dependencies on external libraries. It can also work entirely on StringIO
objects rather than file streams, allowing for PDF manipulation in memory.
It is therefore a useful tool for websites that manage or manipulate PDFs.

%define python_version %( python -c 'import sys; print sys.version.split()[0]' )
%define python_version_short %( python -c 'import sys; print ".".join(sys.version.split()[0].split(".")[:2])' )
%define python_site_packages %( python -c 'import sys; print [x for x in sys.path if x[-13:] == "site-packages" ][0]' )

# Turn off the brp-python-bytecompile script
%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')

%prep
%setup -q -n %{python_package}-%{version}

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

