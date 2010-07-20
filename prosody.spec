Name:       prosody
Version:    0.7.0
Release:    %mkrel 1
Summary:    Light Lua Jabber/XMPP server
URL:        http://prosody.im/
Group:      System/Servers
License:    MIT
Requires(pre):  rpm-helper
Requires(post):	rpm-helper
Requires(preun):    rpm-helper
Requires(postun):   rpm-helper
Requires:   lua-sec
Requires:   lua-socket
Requires:   lua-expat
BuildRequires: lua-devel openssl-devel idn-devel
Source0:    http://prosody.im/downloads/source/%name-%version.tar.gz
Source1:    %{name}.init
Source2:    %{name}.sysconfig
Source3:    %{name}.config
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot

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
rm -rf ${RPM_BUILD_ROOT}

%makeinstall_std


mkdir -p ${RPM_BUILD_ROOT}%{_initrddir}
cat %{SOURCE1} > ${RPM_BUILD_ROOT}%{_initrddir}/%{name}

mkdir -p ${RPM_BUILD_ROOT}%{_sysconfdir}/sysconfig/
cat %{SOURCE2} > ${RPM_BUILD_ROOT}%{_sysconfdir}/sysconfig/%{name}

cat %{SOURCE3} > ${RPM_BUILD_ROOT}%{_sysconfdir}/%{name}/%{name}.cfg.lua 

mkdir -p $RPM_BUILD_ROOT/%_localstatedir/lib/%{name}
mkdir -p $RPM_BUILD_ROOT/%_var/run/%name/

%clean
rm -rf ${RPM_BUILD_ROOT}

%pre
%_pre_useradd %{name} /var/empty /bin/bash

%post
%_post_service %{name}

%preun
%_preun_service %{name}

%postun 
%_postun_userdel %{name}

%files
%defattr(-,root,root)
%doc doc/*
%config(noreplace) %_sysconfdir/%name/
%config(noreplace) %_sysconfdir/sysconfig/%name
%attr(755,root,root) %config(noreplace) %_initrddir/%name
%attr(700,%name,%name) %_localstatedir/lib/%{name}
%_bindir/%{name}ctl
%_bindir/%name
%_prefix/lib/%name
%attr(-,%name,%name) %_var/run/%name/
%_mandir/man1/%{name}ctl.*

