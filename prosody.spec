Name:       prosody
Version:    0.8.2
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
Requires:   lua-filesystem
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



%changelog
* Fri Aug 12 2011 Michael Scherer <misc@mandriva.org> 0.8.2-1mdv2012.0
+ Revision: 694065
- new version 0.8.2

* Tue Jul 20 2010 Michael Scherer <misc@mandriva.org> 0.7.0-1mdv2011.0
+ Revision: 555132
- update to new version 0.7.0

* Mon Apr 19 2010 Sandro Cazzaniga <kharec@mandriva.org> 0.6.2-1mdv2010.1
+ Revision: 536825
- update to 0.6.2

* Tue Apr 13 2010 Funda Wang <fwang@mandriva.org> 0.6.1-2mdv2010.1
+ Revision: 534502
- rebuild

* Thu Nov 26 2009 Michael Scherer <misc@mandriva.org> 0.6.1-1mdv2010.1
+ Revision: 470310
- update to new version 0.6.1

* Wed Nov 25 2009 Michael Scherer <misc@mandriva.org> 0.6.0-1mdv2010.1
+ Revision: 470011
- update to new version 0.6.0

* Tue Sep 29 2009 Michael Scherer <misc@mandriva.org> 0.5.2-1mdv2010.0
+ Revision: 450816
- update to new version 0.5.2

* Thu Jul 30 2009 Frederik Himpe <fhimpe@mandriva.org> 0.5.1-1mdv2010.0
+ Revision: 404692
- update to new version 0.5.1

* Sat Jul 25 2009 Michael Scherer <misc@mandriva.org> 0.5.0-1mdv2010.0
+ Revision: 399845
- update to 0.5.0

* Sat Jul 18 2009 Michael Scherer <misc@mandriva.org> 0.4.2-2mdv2010.0
+ Revision: 397126
- fix directory ownership

* Sat Jul 18 2009 Michael Scherer <misc@mandriva.org> 0.4.2-1mdv2010.0
+ Revision: 396967
- give a proper shell to prosody user
- new version 0.4.2
- no longer run as root

* Sat May 02 2009 Michael Scherer <misc@mandriva.org> 0.4.0-1mdv2010.0
+ Revision: 370410
- fix again BuildRequires
- add BuildRequires
- remove logrotate, and use syslog, prosody do not have support for reloading the file
- adapt initscript
- fix the specfile
- add a default configfile
- import prosody


