%bcond clang 1

# TDE variables
%define tde_epoch 2
%if "%{?tde_version}" == ""
%define tde_version 14.1.5
%endif
%define pkg_rel 2

%define tde_pkg kmyfirewall
%define tde_prefix /opt/trinity


%undefine __brp_remove_la_files
%define dont_remove_libtool_files 1
%define _disable_rebuild_configure 1

# fixes error: Empty %files file …/debugsourcefiles.list
%define _debugsource_template %{nil}

%define tarball_name %{tde_pkg}-trinity


Name:		trinity-%{tde_pkg}
Epoch:		%{tde_epoch}
Version:	1.1.1
Release:	%{?tde_version}_%{?!preversion:%{pkg_rel}}%{?preversion:0_%{preversion}}%{?dist}
Summary:	Iptables based firewall configuration tool for TDE
Group:		Applications/Utilities
URL:		http://www.trinitydesktop.org/

License:	GPLv2+


Source0:		https://mirror.ppa.trinitydesktop.org/trinity/releases/R%{tde_version}/main/applications/settings/%{tarball_name}-%{tde_version}%{?preversion:~%{preversion}}.tar.xz
Source1:		%{name}-rpmlintrc

BuildSystem:    cmake

BuildOption:    -DCMAKE_BUILD_TYPE="RelWithDebInfo"
BuildOption:    -DCMAKE_INSTALL_PREFIX=%{tde_prefix}
BuildOption:    -DINCLUDE_INSTALL_DIR=%{tde_prefix}/include/tde
BuildOption:    -DDATA_INSTALL_DIR=%{tde_prefix}/share/apps
BuildOption:    -DMIME_INSTALL_DIR=%{tde_prefix}/share/mimelnk
BuildOption:    -DXDG_APPS_INSTALL_DIR=%{tde_prefix}/share/applications/tde
BuildOption:    -DSHARE_INSTALL_PREFIX=%{tde_prefix}/share
BuildOption:    -DDOC_INSTALL_DIR=%{tde_prefix}/share/doc/tde
BuildOption:    -DBUILD_DOC=ON
BuildOption:    -DBUILD_ALL=ON
BuildOption:    -DWITH_GCC_VISIBILITY=%{!?with_clang:ON}%{?with_clang:OFF}

BuildRequires:	trinity-tdelibs-devel >= %{tde_version}
BuildRequires:	trinity-tdebase-devel >= %{tde_version}
BuildRequires:	desktop-file-utils

BuildRequires:	autoconf automake libtool m4

%{!?with_clang:BuildRequires:	gcc-c++}

BuildRequires:	pkgconfig
BuildRequires:	libtool

BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(sm)


%description
KMyFirewall attempts to make it easier to setup iptables based firewalls on
Linux systems. It will be the right tool if you like to have a so called
"Personal Firewall" running on your Linux box, but don't have the time and/or
the interest to spend hours in front of the iptables manual just to setup a 
Firewall that keeps the "bad" people out.

There is also the possibility to save entire rule sets, so you only have to
configure your rule set one time and then you can use it on several computers
giving each of them a similar configuration (p.e. school networks, office,
university etc.)

%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING COPYING-DOCS README TODO
%{tde_prefix}/bin/kmyfirewall
%{tde_prefix}/%{_lib}/libkmfcore.so.*
%{tde_prefix}/%{_lib}/libkmfwidgets.so.*
%{tde_prefix}/%{_lib}/trinity/libkmfcompiler_ipt.la
%{tde_prefix}/%{_lib}/trinity/libkmfcompiler_ipt.so
%{tde_prefix}/%{_lib}/trinity/libkmfgenericinterfacepart.la
%{tde_prefix}/%{_lib}/trinity/libkmfgenericinterfacepart.so
%{tde_prefix}/%{_lib}/trinity/libkmfinstaller_linux.la
%{tde_prefix}/%{_lib}/trinity/libkmfinstaller_linux.so
%{tde_prefix}/%{_lib}/trinity/libkmfinstallerplugin.la
%{tde_prefix}/%{_lib}/trinity/libkmfinstallerplugin.so
%{tde_prefix}/%{_lib}/trinity/libkmfipteditorpart.la
%{tde_prefix}/%{_lib}/trinity/libkmfipteditorpart.so
%{tde_prefix}/%{_lib}/trinity/libkmfruleoptionedit_custom.la
%{tde_prefix}/%{_lib}/trinity/libkmfruleoptionedit_custom.so
%{tde_prefix}/%{_lib}/trinity/libkmfruleoptionedit_interface.la
%{tde_prefix}/%{_lib}/trinity/libkmfruleoptionedit_interface.so
%{tde_prefix}/%{_lib}/trinity/libkmfruleoptionedit_ip.la
%{tde_prefix}/%{_lib}/trinity/libkmfruleoptionedit_ip.so
%{tde_prefix}/%{_lib}/trinity/libkmfruleoptionedit_limit.la
%{tde_prefix}/%{_lib}/trinity/libkmfruleoptionedit_limit.so
%{tde_prefix}/%{_lib}/trinity/libkmfruleoptionedit_mac.la
%{tde_prefix}/%{_lib}/trinity/libkmfruleoptionedit_mac.so
%{tde_prefix}/%{_lib}/trinity/libkmfruleoptionedit_protocol.la
%{tde_prefix}/%{_lib}/trinity/libkmfruleoptionedit_protocol.so
%{tde_prefix}/%{_lib}/trinity/libkmfruleoptionedit_state.la
%{tde_prefix}/%{_lib}/trinity/libkmfruleoptionedit_state.so
%{tde_prefix}/%{_lib}/trinity/libkmfruleoptionedit_tos.la
%{tde_prefix}/%{_lib}/trinity/libkmfruleoptionedit_tos.so
%{tde_prefix}/%{_lib}/trinity/libkmfruletargetoptionedit_log.la
%{tde_prefix}/%{_lib}/trinity/libkmfruletargetoptionedit_log.so
%{tde_prefix}/%{_lib}/trinity/libkmfruletargetoptionedit_mark.la
%{tde_prefix}/%{_lib}/trinity/libkmfruletargetoptionedit_mark.so
%{tde_prefix}/%{_lib}/trinity/libkmfruletargetoptionedit_nat.la
%{tde_prefix}/%{_lib}/trinity/libkmfruletargetoptionedit_nat.so
%{tde_prefix}/%{_lib}/trinity/libkmfruletargetoptionedit_tos.la
%{tde_prefix}/%{_lib}/trinity/libkmfruletargetoptionedit_tos.so
%{tde_prefix}/share/applications/tde/kmyfirewall.desktop
%{tde_prefix}/share/apps/kmfgenericinterfacepart/
%{tde_prefix}/share/apps/kmfipteditorpart/
%{tde_prefix}/share/apps/kmfsystray/
%{tde_prefix}/share/apps/kmyfirewall/
%{tde_prefix}/share/config.kcfg/kmfconfig.kcfg
%config(noreplace) %{_sysconfdir}/kmyfirewallrc
%{tde_prefix}/share/doc/tde/HTML/en/kmyfirewall/
%{tde_prefix}/share/icons/hicolor/*/apps/kmyfirewall.png
%{tde_prefix}/share/icons/locolor/*/apps/kmyfirewall.png
%{tde_prefix}/share/mimelnk/application/kmfgrs.desktop
%{tde_prefix}/share/mimelnk/application/kmfnet.desktop
%{tde_prefix}/share/mimelnk/application/kmfpkg.desktop
%{tde_prefix}/share/mimelnk/application/kmfrs.desktop
%{tde_prefix}/share/services/kmf*.desktop
%{tde_prefix}/share/servicetypes/kmf*.desktop
%{tde_prefix}/share/man/man1/kmyfirewall.1*
%lang(it) %{tde_prefix}/share/locale/it/LC_MESSAGES/kmfsystray.mo
%lang(ka) %{tde_prefix}/share/locale/ka/LC_MESSAGES/kmfsystray.mo
%lang(nl) %{tde_prefix}/share/locale/nl/LC_MESSAGES/kmfsystray.mo
%lang(nl) %{tde_prefix}/share/locale/nl/LC_MESSAGES/kmyfirewall.mo

##########

%package devel
Summary:		Development files for %{name}
Group:			Development/Libraries
Requires:		%{name} = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
%{summary}

%files devel
%{tde_prefix}/include/tde/kmyfirewall
%{tde_prefix}/%{_lib}/libkmfcore.la
%{tde_prefix}/%{_lib}/libkmfcore.so
%{tde_prefix}/%{_lib}/libkmfwidgets.la
%{tde_prefix}/%{_lib}/libkmfwidgets.so


%conf -p
unset QTDIR QTINC QTLIB
export PATH="%{tde_prefix}/bin:${PATH}"
export PKG_CONFIG_PATH="%{tde_prefix}/%{_lib}/pkgconfig"


%install -a
# Remove unwanted pixmaps
%__rm -rf "%{buildroot}%{tde_prefix}/share/pixmaps/"

