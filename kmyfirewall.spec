#
# Please submit bugfixes or comments via http://www.trinitydesktop.org/
#

# TDE variables
%define tde_epoch 2
%if "%{?tde_version}" == ""
%define tde_version 14.1.5
%endif
%define tde_pkg kmyfirewall
%define tde_prefix /opt/trinity
%define tde_bindir %{tde_prefix}/bin
%define tde_confdir %{_sysconfdir}/trinity
%define tde_datadir %{tde_prefix}/share
%define tde_docdir %{tde_datadir}/doc
%define tde_includedir %{tde_prefix}/include
%define tde_libdir %{tde_prefix}/%{_lib}
%define tde_mandir %{tde_datadir}/man
%define tde_tdeappdir %{tde_datadir}/applications/tde
%define tde_tdedocdir %{tde_docdir}/tde
%define tde_tdeincludedir %{tde_includedir}/tde
%define tde_tdelibdir %{tde_libdir}/trinity

%if 0%{?mdkversion}
%undefine __brp_remove_la_files
%define dont_remove_libtool_files 1
%define _disable_rebuild_configure 1
%endif

# fixes error: Empty %files file …/debugsourcefiles.list
%define _debugsource_template %{nil}

%define tarball_name %{tde_pkg}-trinity
%global toolchain %(readlink /usr/bin/cc)


Name:		trinity-%{tde_pkg}
Epoch:		%{tde_epoch}
Version:	1.1.1
Release:	%{?tde_version}_%{?!preversion:1}%{?preversion:0_%{preversion}}%{?dist}
Summary:	Iptables based firewall configuration tool for TDE
Group:		Applications/Utilities
URL:		http://www.trinitydesktop.org/

%if 0%{?suse_version}
License:	GPL-2.0+
%else
License:	GPLv2+
%endif

#Vendor:		Trinity Desktop
#Packager:	Francois Andriot <francois.andriot@free.fr>

Prefix:		%{tde_prefix}

Source0:		https://mirror.ppa.trinitydesktop.org/trinity/releases/R%{tde_version}/main/applications/settings/%{tarball_name}-%{tde_version}%{?preversion:~%{preversion}}.tar.xz
Source1:		%{name}-rpmlintrc

BuildRequires:  cmake make
BuildRequires:	trinity-tdelibs-devel >= %{tde_version}
BuildRequires:	trinity-tdebase-devel >= %{tde_version}
BuildRequires:	desktop-file-utils

BuildRequires:	autoconf automake libtool m4
%if "%{?toolchaing}" != "clang"
BuildRequires:	gcc-c++
%endif
BuildRequires:	pkgconfig
BuildRequires:	libtool

# SUSE desktop files utility
%if 0%{?suse_version}
BuildRequires:	update-desktop-files
%endif

%if 0%{?opensuse_bs} && 0%{?suse_version}
# for xdg-menu script
BuildRequires:	brp-check-trinity
%endif

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
%{tde_bindir}/kmyfirewall
%{tde_libdir}/libkmfcore.so.*
%{tde_libdir}/libkmfwidgets.so.*
%{tde_tdelibdir}/libkmfcompiler_ipt.la
%{tde_tdelibdir}/libkmfcompiler_ipt.so
%{tde_tdelibdir}/libkmfgenericinterfacepart.la
%{tde_tdelibdir}/libkmfgenericinterfacepart.so
%{tde_tdelibdir}/libkmfinstaller_linux.la
%{tde_tdelibdir}/libkmfinstaller_linux.so
%{tde_tdelibdir}/libkmfinstallerplugin.la
%{tde_tdelibdir}/libkmfinstallerplugin.so
%{tde_tdelibdir}/libkmfipteditorpart.la
%{tde_tdelibdir}/libkmfipteditorpart.so
%{tde_tdelibdir}/libkmfruleoptionedit_custom.la
%{tde_tdelibdir}/libkmfruleoptionedit_custom.so
%{tde_tdelibdir}/libkmfruleoptionedit_interface.la
%{tde_tdelibdir}/libkmfruleoptionedit_interface.so
%{tde_tdelibdir}/libkmfruleoptionedit_ip.la
%{tde_tdelibdir}/libkmfruleoptionedit_ip.so
%{tde_tdelibdir}/libkmfruleoptionedit_limit.la
%{tde_tdelibdir}/libkmfruleoptionedit_limit.so
%{tde_tdelibdir}/libkmfruleoptionedit_mac.la
%{tde_tdelibdir}/libkmfruleoptionedit_mac.so
%{tde_tdelibdir}/libkmfruleoptionedit_protocol.la
%{tde_tdelibdir}/libkmfruleoptionedit_protocol.so
%{tde_tdelibdir}/libkmfruleoptionedit_state.la
%{tde_tdelibdir}/libkmfruleoptionedit_state.so
%{tde_tdelibdir}/libkmfruleoptionedit_tos.la
%{tde_tdelibdir}/libkmfruleoptionedit_tos.so
%{tde_tdelibdir}/libkmfruletargetoptionedit_log.la
%{tde_tdelibdir}/libkmfruletargetoptionedit_log.so
%{tde_tdelibdir}/libkmfruletargetoptionedit_mark.la
%{tde_tdelibdir}/libkmfruletargetoptionedit_mark.so
%{tde_tdelibdir}/libkmfruletargetoptionedit_nat.la
%{tde_tdelibdir}/libkmfruletargetoptionedit_nat.so
%{tde_tdelibdir}/libkmfruletargetoptionedit_tos.la
%{tde_tdelibdir}/libkmfruletargetoptionedit_tos.so
%{tde_tdeappdir}/kmyfirewall.desktop
%{tde_datadir}/apps/kmfgenericinterfacepart/
%{tde_datadir}/apps/kmfipteditorpart/
%{tde_datadir}/apps/kmfsystray/
%{tde_datadir}/apps/kmyfirewall/
%{tde_datadir}/config.kcfg/kmfconfig.kcfg
%config(noreplace) %{_sysconfdir}/kmyfirewallrc
%{tde_tdedocdir}/HTML/en/kmyfirewall/
%{tde_datadir}/icons/hicolor/*/apps/kmyfirewall.png
%{tde_datadir}/icons/locolor/*/apps/kmyfirewall.png
%{tde_datadir}/mimelnk/application/kmfgrs.desktop
%{tde_datadir}/mimelnk/application/kmfnet.desktop
%{tde_datadir}/mimelnk/application/kmfpkg.desktop
%{tde_datadir}/mimelnk/application/kmfrs.desktop
%{tde_datadir}/services/kmf*.desktop
%{tde_datadir}/servicetypes/kmf*.desktop
%{tde_mandir}/man1/kmyfirewall.1*
%lang(it) %{tde_datadir}/locale/it/LC_MESSAGES/kmfsystray.mo
%lang(ka) %{tde_datadir}/locale/ka/LC_MESSAGES/kmfsystray.mo
%lang(nl) %{tde_datadir}/locale/nl/LC_MESSAGES/kmfsystray.mo
%lang(nl) %{tde_datadir}/locale/nl/LC_MESSAGES/kmyfirewall.mo

##########

%package devel
Summary:		Development files for %{name}
Group:			Development/Libraries
Requires:		%{name} = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
%{summary}

%files devel
%{tde_tdeincludedir}/kmyfirewall
%{tde_libdir}/libkmfcore.la
%{tde_libdir}/libkmfcore.so
%{tde_libdir}/libkmfwidgets.la
%{tde_libdir}/libkmfwidgets.so

##########

%if 0%{?suse_version} && 0%{?opensuse_bs} == 0
%debug_package
%endif

##########


%prep
%autosetup -n %{tarball_name}-%{tde_version}%{?preversion:~%{preversion}}


%build
unset QTDIR QTINC QTLIB
export PATH="%{tde_bindir}:${PATH}"
export PKG_CONFIG_PATH="%{tde_libdir}/pkgconfig"

if ! rpm -E %%cmake|grep -e 'cd build\|cd ${CMAKE_BUILD_DIR:-build}'; then
  %__mkdir_p build
  cd build
fi

%cmake \
  -DCMAKE_BUILD_TYPE="RelWithDebInfo" \
  -DCMAKE_C_FLAGS="${RPM_OPT_FLAGS}" \
  -DCMAKE_CXX_FLAGS="${RPM_OPT_FLAGS}" \
  -DCMAKE_SKIP_RPATH=OFF \
  -DCMAKE_SKIP_INSTALL_RPATH=OFF \
  -DCMAKE_INSTALL_RPATH="%{tde_libdir}" \
  -DCMAKE_VERBOSE_MAKEFILE=ON \
  -DWITH_GCC_VISIBILITY=OFF \
  \
  -DCMAKE_INSTALL_PREFIX=%{tde_prefix} \
  -DINCLUDE_INSTALL_DIR=%{tde_tdeincludedir} \
  -DDATA_INSTALL_DIR=%{tde_datadir}/apps \
  -DMIME_INSTALL_DIR=%{tde_datadir}/mimelnk \
  -DXDG_APPS_INSTALL_DIR=%{tde_tdeappdir} \
  -DSHARE_INSTALL_PREFIX="%{tde_datadir}"\
  -DDOC_INSTALL_DIR=%{tde_tdedocdir} \
  -DLIB_INSTALL_DIR=%{tde_libdir} \
  \
  -DBUILD_DOC=ON \
  -DBUILD_ALL=ON \
  ..

# Not SMP safe !
%__make


%install
export PATH="%{tde_bindir}:${PATH}"
%__make install DESTDIR=%{buildroot} -C build

# Updates applications categories for openSUSE
%if 0%{?suse_version}
%suse_update_desktop_file -r "%{tde_pkg}" System Network
%endif

# Remove unwanted pixmaps
%__rm -rf "%{buildroot}%{tde_datadir}/pixmaps/"

