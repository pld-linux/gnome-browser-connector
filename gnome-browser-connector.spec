Summary:	GNOME Shell browser connector
Summary(pl.UTF-8):	Pakiet łączący GNOME Shell z przeglądarką
Name:		gnome-browser-connector
Version:	42.1
Release:	1
License:	GPL v3+
Group:		Libraries
Source0:	https://download.gnome.org/sources/gnome-browser-connector/42/%{name}-%{version}.tar.xz
# Source0-md5:	d5b00a3ff63dad073c86d855b2017661
URL:		https://gitlab.gnome.org/GNOME/gnome-browser-connector
BuildRequires:	meson
BuildRequires:	python3 >= 1:3
BuildRequires:	python3-pygobject3 >= 3
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	python3-pygobject3 >= 3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OS-native connector counterpart for GNOME Shell browser extension.

%description -l pl.UTF-8
Natywna dla systemu część łącznika GNOME Shell z przeglądarką.

%prep
%setup -q

%build
%meson build

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS README.md
%attr(755,root,root) %{_bindir}/gnome-browser-connector
%attr(755,root,root) %{_bindir}/gnome-browser-connector-host
%{py3_sitescriptdir}/gnome_browser_connector
%{_datadir}/dbus-1/services/org.gnome.BrowserConnector.service
%{_desktopdir}/org.gnome.BrowserConnector.desktop
%{_iconsdir}/hicolor/*x*/apps/org.gnome.BrowserConnector.png
# XXX: which package(s) should own native-messaging-hosts dirs
%dir %{_sysconfdir}/chromium
%dir %{_sysconfdir}/chromium/native-messaging-hosts
%{_sysconfdir}/chromium/native-messaging-hosts/org.gnome.browser_connector.json
%{_sysconfdir}/chromium/native-messaging-hosts/org.gnome.chrome_gnome_shell.json
%dir %{_sysconfdir}/opt
%dir %{_sysconfdir}/opt/chrome
%dir %{_sysconfdir}/opt/chrome/native-messaging-hosts
%{_sysconfdir}/opt/chrome/native-messaging-hosts/org.gnome.browser_connector.json
%{_sysconfdir}/opt/chrome/native-messaging-hosts/org.gnome.chrome_gnome_shell.json
%dir %{_libdir}/mozilla/native-messaging-hosts
%{_libdir}/mozilla/native-messaging-hosts/org.gnome.browser_connector.json
%{_libdir}/mozilla/native-messaging-hosts/org.gnome.chrome_gnome_shell.json
