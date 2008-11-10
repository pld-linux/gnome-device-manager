Summary:	GNOME application to manage devices and device drivers
Summary(pl.UTF-8):	Aplikacja GNOME do zarządzania urządzeniami i sterownikami urządzeń
Name:		gnome-device-manager
Version:	0.2
Release:	2
License:	GPL
Group:		X11/Applications
Source0:	http://hal.freedesktop.org/releases/%{name}-%{version}.tar.bz2
# Source0-md5:	b833a90c940dd6cc992c42ad05ca6831
BuildRequires:	autoconf
BuildRequires:	automake >= 1:1.9
BuildRequires:	gnome-common
BuildRequires:	gnome-doc-utils
BuildRequires:	gtk+2-devel >= 2:2.6.0
BuildRequires:	hal-devel >= 0.5.10
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libgnomeui-devel >= 2.14.0
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	scrollkeeper >= 0.3.14
Requires(post,postun):	gtk+2
Requires(post,postun):	hicolor-icon-theme
Requires(post,postun):	scrollkeeper
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a GNOME program to manage devices and device drivers. It's
inspired by hal-device-manager, from the HAL project, but rewritten in
C for efficiency and an outlook to actually make it manage devices
rather than just show information.

%description -l pl.UTF-8
Ten pakiet zawiera aplikację GNOME do zarządzania urządzeniami i
sterownikami urządzeń. Jest zainspirowana programem hal-device-manager
z projektu HAL, ale napisana w C pod kątem wydajności i ze zwróceniem
uwagi, aby zarządzała urządzeniami, a nie tylko pokazywała informacje.

%package devel
Summary:	gnome-device-manager header files
Summary(pl.UTF-8):	Pliki nagłówkowe gnome-device-manager
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
gnome-device-manager header files

%description devel -l pl.UTF-8
Pliki nagłówkowe gnome-device-manager.

%package static
Summary:	Static libgnome-device-manager library
Summary(pl.UTF-8):	Statyczna biblioteka libgnome-device-manager
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libgnome-device-manager library.

%description static -l pl.UTF-8
Statyczna biblioteka libgnome-device-manager.

%prep
%setup -q

%build
%{__glib_gettextize}
%{__intltoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-scrollkeeper
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-gnome --with-omf

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
%scrollkeeper_update_post
%update_icon_cache hicolor

%postun
/sbin/ldconfig
%scrollkeeper_update_postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README TODO
%attr(755,root,root) %{_bindir}/gnome-device-manager
%attr(755,root,root) %{_libdir}/libgnome-device-manager.so.*.*.*
%{_desktopdir}/gnome-device-manager.desktop
%{_iconsdir}/hicolor/*/apps/*.png

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgnome-device-manager.so
%{_libdir}/libgnome-device-manager.la
%{_includedir}/gnome-device-manager
%{_pkgconfigdir}/gnome-device-manager.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libgnome-device-manager.a
