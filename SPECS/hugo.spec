Name: hugo
Summary: Static Site Generator
License: Apache 2.0
Group: Applications/Publishing
Url: http://gohugo.io

%define git_version 0.40.2
%define git_tag v%{git_version}
%define git_path gohugoio/%{name}

Version: %{git_version}
Release: 0.fdm
BuildArch: x86_64
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}

%changelog
* Thu Jun  9 2016 Thornton Prime <thornton.prime@gmail.com> [0.16]
- Updated to pull directly from git

%description

Hugo is a static HTML and CSS website generator written in Go. It is
optimized for speed, easy use and configurability. Hugo takes a directory
with content and templates and renders them into a full HTML website.

Hugo relies on Markdown files with front matter for meta data. And you can
run Hugo from any directory. This works well for shared hosts and other
systems where you don’t have a privileged account.

Hugo renders a typical website of moderate size in a fraction of a second.
A good rule of thumb is that each piece of content renders in around 1
millisecond.

Hugo is designed to work well for any kind of website including blogs,
tumbles and docs.

%prep

%setup -cT
export GOPATH=`pwd`
git clone https://github.com/%{git_path}.git src/github.com/%{git_path}
(
  cd src/github.com/%{git_path}
  git checkout -b %{git_tag}
  git branch --set-upstream-to=origin/master %{git_tag}
)

%build
export GOPATH=`pwd`
go get -f -u github.com/%{git_path}

%install
%{__install} -D bin/hugo ${RPM_BUILD_ROOT}%{_bindir}/hugo


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/hugo
%doc src/github.com/%{git_path}/{LICENSE,README.md}

