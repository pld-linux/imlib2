Summary:	Powerful image loading and rendering library
Summary(pl):	Pot�na biblioteka wczytuj�ca i renderuj�ca obrazki
Name:		imlib2
Version:	1.1.0
Release:	2
License:	LGPL
Group:		X11/Libraries
Source0:	http://dl.sourceforge.net/enlightenment/%{name}-%{version}.tar.gz
# Source0-md5:	1589ebb054da76734fe08ae570460034
Patch0:		%{name}-path.patch
Patch1:		%{name}-ltdl.patch
Patch2:		%{name}-link.patch
BuildRequires:	XFree86-devel
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	freetype-devel >= 2.0
BuildRequires:	libjpeg-devel >= 6b-18
BuildRequires:	libltdl-devel
BuildRequires:	libpng-devel >= 1.0.8
BuildRequires:	libtiff-devel
BuildRequires:	libtool
BuildRequires:	libungif-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	libimlib2_1

%define		_sysconfdir	/etc/X11

%description
Imlib2 is an advanced replacement library for libraries like libXpm
that provides many more features with much greater flexibility and
speed than standard libraries, including font rasterization, rotation,
RGBA space rendering and blending, dynamic binary filters, scripting,
and more.

%description -l pl
Imlib2 jest zaawansowan� bibliotek�, zamiennikiem takich bibliotek jak
libXpm. Imlib2 dostarcza o wiele wi�cej mo�liwo�ci przy du�o wi�kszej
szybko�ci ni� standardowe bilioteki (w��czaj�c w to rasteryzacj�
font�w, obracanie, renderowanie przestrzeni RGBA, mieszanie,
dynamiczne filtry (w postaci binarnej), obs�uga j�zyka skryptowego i
wiele wi�cej.

%package devel
Summary:	Imlib2 header files and development documentation
Summary(fr):	Fichiers ent�te pour Imlib2
Summary(pl):	Pliki nag��wkowe oraz dokumentacja do imlib2
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}
Requires:	XFree86-devel
Requires:	freetype-devel
Requires:	libltdl-devel
Obsoletes:	libimlib2_1-devel

%description devel
Header files and development documentation for Imlib2.

%description devel -l fr
Fichiers ent�te pour Imlib2.

%description devel -l pl
Pliki nag��wkowe oraz dokumentacja do biblioteki Imlib2.

%package static
Summary:	Imlib2 static libraries
Summary(pl):	Biblioteki statyczne imlib2
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Imlib2 static libraries.

%description static -l pl
Biblioteki statyczne imlib2.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
rm -rf libltdl configure.in
%{__libtoolize} --ltdl
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
%ifarch i586 i686 athlon
	--enable-mmx
%else
	--disable-mmx
%endif

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# no static plugins - shut up check-files
# plugins are lt_dlopened w/o extension, so *.la should be left
rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}/loaders/*/*.a

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/loaders
%dir %{_libdir}/%{name}/loaders/filter
%dir %{_libdir}/%{name}/loaders/image
%attr(755,root,root) %{_libdir}/%{name}/loaders/*/*.so
%{_libdir}/%{name}/loaders/*/*.la

%files devel
%defattr(644,root,root,755)
%doc doc/{*gif,*.html}
%attr(755,root,root) %{_bindir}/imlib2-config
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*
%{_pkgconfigdir}/imlib2.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
