Summary:	GNOME application to manage devices and device drivers
Name:		gnome-device-manager
Version:	0.1
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://people.freedesktop.org/~david/dist/%{name}-%{version}.tar.bz2
# Source0-md5:	82949f0b58d85743bc062ecfb4c8406c
Patch0:		%{name}-desktop.patch
BuildRequires:	autoconf
BuildRequires:	automake >= 1:1.9
BuildRequires:	gnome-common
BuildRequires:	gnome-doc-utils
BuildRequires:	gtk+2-devel >= 2:2.6.0
BuildRequires:	hal-devel >= 0.5.9
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libgnomeui-devel >= 2.14.0
BuildRequires:	pkgconfig
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

%prep
%setup -q
%patch0 -p1

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

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%scrollkeeper_update_post
%update_icon_cache hicolor

%postun
%scrollkeeper_update_postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README TODO
%attr(755,root,root) %{_bindir}/gnome-device-manager
%{_desktopdir}/gnome-device-manager.desktop
%{_iconsdir}/hicolor/*/apps/*.png
%dir %{_omf_dest_dir}/gnome-device-manager
%{_omf_dest_dir}/gnome-device-manager/gnome-device-manager-C.omf
