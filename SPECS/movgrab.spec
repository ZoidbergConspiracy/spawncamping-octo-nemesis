Summary: Movie Downloader
Name: movgrab
Version: 1.2.1
Release: 0.fdm
Source0: https://sites.google.com/site/columscode/files/%{name}-%{version}.tar.gz
License: UNKNOWN
Group: Media/Utils
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
Vendor: Colum's Code
Url: https://sites.google.com/site/columscode/home/movgrab

%description
Movgrab is a downloader for all those pesky sites that insist you use a
big fat browser that runs flash in order to see their content. It's a
command-line app written in straight C, and so doesn't require you to
install perl. Nor ruby. Nor python. Nor guile, scheme, glib, gtk, qt,
gnome, kde, X-windows, m4, firefox or windows. No! Not any of that!


%prep
%setup -n %{name}-%{version}

%build
%{configure} --enable-largefiles --enable-ssl
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
%{makeinstall}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/movgrab
%doc README LICENCE INSTALL
%doc Docs/*
