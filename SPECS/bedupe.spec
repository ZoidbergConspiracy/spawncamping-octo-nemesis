Name: bedupe
Summary: Btrfs File Dedupe
License: GPL2
URL: https://github.com/g2p/bedup
Group: System/Administration

Packager: Thornton Prime <thornton@yoyoweb.com>
Distribution: FDM 6

Version: 0svn.20140418
Release: 2.fdm
Epoch: %( date +"%Y%m%d" )

Source: bedupe-20140418.tar.gz

BuildRequires: python-cffi
Requires: python-cffi
Requires: python-sqlalchemy python-sqlalchemy python-contextlib2 python-alembic
Requires: pyxdg python-setuptools

%description
Deduplication for Btrfs.

bedup looks for new and changed files, making sure that multiple copies of
identical files share space on disk. It integrates deeply with btrfs so
that scans are incremental and low-impact.

%changelog
* Fri Apr 18 2014 Thornton Prime <thornton@yoyoweb.com> [0svn.20140418]
- Initial build

%prep
%setup -q -n %{name}-20140418

%build
env CFLAGS="%{optflags}" %{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install --root=%{buildroot} --record=INSTALLED_FILES
#find %{buildroot} -type f -name '*.pyo' -printf '/%P%f\n' >> INSTALLED_FILES

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README.rst COPYING
/usr/bin/bedup
/usr/lib64/python2.7/site-packages/bedup
/usr/lib64/python2.7/site-packages/bedup-0.9.0-py2.7.egg-info/
