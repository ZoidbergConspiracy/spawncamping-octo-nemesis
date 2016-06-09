Name: hugo
Summary: Static Site Generator
Release: fdm
License: Apache 2.0
Group: Applications/Publishing
Url: http://gohugo.io

Version: 0.16
BuildArch: x86_64
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}

#Source0:  https://github.com/spf13/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

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

%define repo_url https://github.com/spf13/%{name}.git
%define repo_src_path %( echo %{repo_url} | sed -e 's@^https://@src/@' -e 's@\.git$@@' )
%define pkg_path %( echo %{repo_url} | sed -e 's@^https://@@' -e 's@\.git$@@' )

%prep

%setup -cT
export GOPATH=`pwd`

echo %{repo_url}
mkdir -p %{repo_src_path}
git clone --branch v%{version} %{repo_url} %{repo_src_path}
go get -f -u ./... || true

%build
export GOPATH=`pwd`
go build %{pkg_path}

%install

%{__install} -D hugo ${RPM_BUILD_ROOT}%{_bindir}/hugo


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/hugo
%doc %{repo_src_path}/{LICENSE.md,README.md}

