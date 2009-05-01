Name:		prosody
Version:	0.4.0
Release:	%mkrel 1
Summary:    TODO
URL:		http://prosody.im/
Group:		TODO
License:	mit
Requires(pre):	rpm-helper
Requires(post):	rpm-helper
Requires(preun):	rpm-helper
Requires(postun):	rpm-helper
Requires:	lua-sec
Requires:	lua-socket
Requires:	lua-expat
Source0:	http://prosody.im/downloads/source/%name-%version.tar.gz
#
Source1:	%{name}.logrotate
#
Source2:	%{name}.init
#
Source3: 	%{name}.sysconfig
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
#TODO

%prep
%setup -q 
 
%build
./configure --with-lua='' --with-lua-include=/usr/include --prefix=/usr
%make

%install
rm -rf ${RPM_BUILD_ROOT}

%makeinstall_std


mkdir -p ${RPM_BUILD_ROOT}%{_initrddir}
cat %{SOURCE2} > ${RPM_BUILD_ROOT}%{_initrddir}/%{name}

mkdir -p ${RPM_BUILD_ROOT}%{_sysconfdir}/logrotate.d
cat %{SOURCE1} > ${RPM_BUILD_ROOT}%{_sysconfdir}/logrotate.d/%{name}

mkdir -p ${RPM_BUILD_ROOT}%{_sysconfdir}/sysconfig/
cat %{SOURCE3} > ${RPM_BUILD_ROOT}%{_sysconfdir}/sysconfig/%{name}

mkdir -p $RPM_BUILD_ROOT/%_localstatedir/lib/%{name}
 
%clean
[ "${RPM_BUILD_ROOT}" != "/" ] && rm -rf ${RPM_BUILD_ROOT}

%post
%_post_service %{name}

%preun
%_preun_service %{name}

%files
%defattr(-,root,root)
%_sysconfdir/%name/
%_sysconfdir/sysconfig/%name
%_sysconfdir/logrotate.d/%name
%_initrddir/%name
%_localstatedir/lib/%{name}
%_bindir/%name
%_prefix/lib/%name
