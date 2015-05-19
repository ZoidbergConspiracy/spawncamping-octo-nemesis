Summary: HandBrake video converter
Name: HandBrake
Version: 0.9.9
Release: 0.fdm
Source0: http://downloads.sourceforge.net/project/handbrake/%{version}/%{name}-%{version}.tar.bz2
License: UNKNOWN
Group: Media/Utils
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
Url: http://handbrake.fr/

BuildRequires: libass-devel libtheora-devel libvorbis-devel libsamplerate-devel intltool

%description
HandBrake is a tool for converting video from nearly any format to a
selection of modern, widely supported codecs.

%package gtk
Summary: GTK Interface for HandBrake

%description gtk
HandBrake is a tool for converting video from nearly any format to a
selection of modern, widely supported codecs.

%prep
%setup -n %{name}-%{version}

%build
%{_configure} --build=%{_build} \
    --prefix=%{_prefix} \
    --fetch=curl

( cd %{_build}; make )

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
cp x86_64-redhat-linux-gnu/HandBrakeCLI $RPM_BUILD_ROOT/%{_bindir}
cp x86_64-redhat-linux-gnu/gtk/src/ghb $RPM_BUILD_ROOT/%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/HandBrakeCLI
%doc AUTHORS COPYING CREDITS NEWS THANKS

%files gtk
%{_bindir}/ghb

