%define debug_package %{nil}

Name:       prosody
Version:    0.8.2
Release:    3
Summary:    Light Lua Jabber/XMPP server
URL:        https://prosody.im/
Group:      System/Servers
License:    MIT
Requires(pre):  rpm-helper
Requires(post):	rpm-helper
Requires(preun):    rpm-helper
Requires(postun):   rpm-helper
Requires:   lua-sec
Requires:   lua-socket
Requires:   lua-expat
Requires:   lua-filesystem
BuildRequires: lua-devel openssl-devel idn-devel
Source0:    http://prosody.im/downloads/source/%{name}-%{version}.tar.gz
Source1:    %{name}.init
Source2:    %{name}.sysconfig
Source3:    %{name}.config

%description
Prosody is an exciting new server for Jabber/XMPP written in Lua. It aims to 
be easy to use, and light on resources. For developers it aims to give a 
flexible system on which to rapidly develop added functionality, or 
prototype new protocols

%prep
%setup -q 
 
%build
./configure --with-lua='' --with-lua-include=/usr/include --prefix=/usr
%make

%install
%makeinstall_std


mkdir -p %{buildroot}%{_initrddir}
cat %{SOURCE1} > %{buildroot}%{_initrddir}/%{name}

mkdir -p %{buildroot}%{_sysconfdir}/sysconfig/
cat %{SOURCE2} > %{buildroot}%{_sysconfdir}/sysconfig/%{name}

cat %{SOURCE3} > %{buildroot}%{_sysconfdir}/%{name}/%{name}.cfg.lua 

mkdir -p %{buildroot}/%{_localstatedir}/lib/%{name}
mkdir -p %{buildroot}/%{_var}/run/%{name}/

%pre
%_pre_useradd %{name} /var/empty /bin/bash

%post
%_post_service %{name}

%preun
%_preun_service %{name}

%postun 
%_postun_userdel %{name}

%files
%doc doc/*
%config(noreplace) %{_sysconfdir}/%{name}/
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}
%attr(755,root,root) %config(noreplace) %{_initrddir}/%{name}
%attr(700,%name,%name) %{_localstatedir}/lib/%{name}
%{_bindir}/%{name}ctl
%{_bindir}/%name
%{_prefix}/lib/%{name}
%attr(-,%name,%name) %{_var}/run/%{name}/
%{_mandir}/man1/%{name}ctl.*
