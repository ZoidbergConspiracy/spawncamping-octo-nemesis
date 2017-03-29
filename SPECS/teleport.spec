Name: teleport
Summary: Modern SSH server for clusters and teams
License: Apache
Group: System/Utilities

%define git_path gravitational/%{name}
#%define git_tag %( git ls-remote https://github.com/%{git_path}.git | grep HEAD | awk '{ print $1 }' )
%define git_tag v2.0.0-rc.2

#Version: 0.%( echo %{git_tag} | cut -c 1-8 )git
Version: 2.0.0.rc2
Release: 4.fdm
URL: http://gravitational.com/teleport/
#URL: https://github.com/%{git_package}

BuildArch: x86_64
Prefix: %{_prefix}
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Gravitational Teleport is a modern SSH server for remotely accessing clusters
of Linux servers via SSH or HTTPS. It is intended to be used instead of sshd.
Teleport enables teams to easily adopt the best SSH practices like:

* No need to distribute keys: Teleport uses certificate-based access with
  automatic expiration time.
* Enforcement of 2nd factor authentication.
* Cluster introspection: every Teleport node becomes a part of a cluster
  and is visible on the Web UI.
* Record and replay SSH sessions for knowledge sharing and auditing purposes.
* Collaboratively troubleshoot issues through session sharing.
* Connect to clusters located behind firewalls without direct Internet access
  via SSH bastions.
* Ability to integrate SSH credentials with your organization identities via
  OAuth (Google Apps, Github).
* Keep the full audit log of all SSH sessions within a cluster.

%changelog
* Mon Mar 27 2017 Thornton Prime <thornton.prime@gmail.com> [2.0.0.rc2]
- Basic build from Github

# Disable stripping because it breaks the teleport web assets
%global __os_install_post %{nil}

%files
%defattr(-,root,root)
%{_bindir}/*
%{_sbindir}/*
%{_unitdir}/teleport.service
%dir %{_sharedstatedir}/teleport
%config(noreplace) %{_sysconfdir}/sysconfig/teleport

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
#go get -f -u github.com/%{git_path}
(
  cd src/github.com/%{git_path}
  make release
)
cat >> teleport.service <<_SYSTEMD_UNIT_
[Unit]
Description=Teleport SSH Service
After=network.target 

[Service]
Type=simple
Restart=always
EnvironmentFile=/etc/sysconfig/teleport
ExecStart=/usr/sbin/teleport start \$OPTIONS

[Install]
WantedBy=multi-user.target
_SYSTEMD_UNIT_

cat >> teleport.sysconfig <<_SYSCONFIG_
# Options for teleport
#
# Should work by default with no flags
OPTIONS=""

# Alternative would be to specify a config file
#OPTIONS="--config=/etc/teleport.yaml"

# Or some simple tags
#OPTIONS='--labels kernel=[1h:"uname -r"],platform=[24h:"uname -o"]'

_SYSCONFIG_

tar xvfz src/github.com/%{git_path}/teleport-*-bin.tar.gz

%install
%{__install} -D teleport/teleport ${RPM_BUILD_ROOT}%{_sbindir}/teleport
%{__install} -D teleport/tsh ${RPM_BUILD_ROOT}%{_bindir}/tsh
%{__install} -D teleport/tctl ${RPM_BUILD_ROOT}%{_bindir}/tctl
%{__install} -d ${RPM_BUILD_ROOT}%{_sharedstatedir}/teleport
%{__install} -D teleport.service ${RPM_BUILD_ROOT}%{_unitdir}/teleport.service
%{__install} -D teleport.sysconfig ${RPM_BUILD_ROOT}%{_sysconfdir}/sysconfig/teleport

%clean
rm -rf $RPM_BUILD_ROOT

