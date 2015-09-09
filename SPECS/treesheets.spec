Name: treesheets
Summary: Free Form Data Organizer
License: ZLIB
Group: Applications/Editors
Url: http://treesheets.com

Version: 0.6dcbba2f08
Release: 0.fdm
BuildArch: x86_64

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}

%changelog
* Wed Sep 09 2015 Thornton Prime <thornton.prime@gmail.com> - 0.6dcbba2f08
- Initial packaging with broken dir structure

%description
The ultimate replacement for spreadsheets, mind mappers, outliners, PIMs,
text editors and small databases.

Suitable for any kind of data organization, such as Todo lists, calendars,
project management, brainstorming, organizing ideas, planning, requirements
gathering, presentation of information, etc.

%prep
%setup -cT
git clone https://github.com/aardappel/treesheets.git .
git clone https://github.com/wxWidgets/wxWidgets.git

%build
(cd wxWidgets; ./configure; make)
export PATH=`pwd`/wxWidgets:${PATH}
cd src
make

%install
%{__install} -D TS/treesheets %{buildroot}%{_bindir}/treesheets
mkdir -p  %{buildroot}%{_datarootdir}/treesheets/
cp -r TS/docs TS/examples TS/images TS/readme.html %{buildroot}%{_datarootdir}/treesheets/
ln -s %{_bindir}/treesheets %{buildroot}%{_datarootdir}/treesheets/treesheets

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/treesheets
%{_datarootdir}/treesheets

