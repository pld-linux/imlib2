Summary:	Powerful image loading and rendering library
Summary(pl):	Potê¿na biblioteka wczytuj±ca i renderuj±ca obrazki
Name:		imlib2
Version:	1.3.0
Release:	1
License:	LGPL
Group:		X11/Libraries
Source0:	http://dl.sourceforge.net/enlightenment/%{name}-%{version}.tar.gz
# Source0-md5:	00b724fc6d2dcfa3045bb6a554bb2c8a
Patch0:		%{name}-ac.patch
URL:		http://enlightenment.org/Libraries/Imlib2/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	bzip2-devel
BuildRequires:	freetype-devel >= 2.1
BuildRequires:	giflib-devel
BuildRequires:	libid3tag-devel
BuildRequires:	libjpeg-devel >= 6b-18
BuildRequires:	libltdl-devel
BuildRequires:	libpng-devel >= 1.0.8
BuildRequires:	libtiff-devel
BuildRequires:	libtool
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	zlib-devel
Obsoletes:	libimlib2_1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Imlib2 is an advanced replacement library for libraries like libXpm
that provides many more features with much greater flexibility and
speed than standard libraries, including font rasterization, rotation,
RGBA space rendering and blending, dynamic binary filters, scripting,
and more.

%description -l pl
Imlib2 jest zaawansowan± bibliotek±, zamiennikiem takich bibliotek jak
libXpm. Imlib2 dostarcza o wiele wiêcej mo¿liwo¶ci przy du¿o wiêkszej
szybko¶ci ni¿ standardowe biblioteki (w³±czaj±c w to rasteryzacjê
fontów, obracanie, renderowanie przestrzeni RGBA, mieszanie, dynamiczne 
filtry (w postaci binarnej), obs³uga jêzyka skryptowego i wiele wiêcej.

%package devel
Summary:	Imlib2 header files and development documentation
Summary(fr):	Fichiers entête pour Imlib2
Summary(pl):	Pliki nag³ówkowe oraz dokumentacja do imlib2
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	freetype-devel
Requires:	libltdl-devel
Requires:	xorg-lib-libXext-devel
Obsoletes:	libimlib2_1-devel

%description devel
Header files and development documentation for Imlib2.

%description devel -l fr
Fichiers entête pour Imlib2.

%description devel -l pl
Pliki nag³ówkowe oraz dokumentacja do biblioteki Imlib2.

%package static
Summary:	Imlib2 static libraries
Summary(pl):	Biblioteki statyczne imlib2
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Imlib2 static libraries.

%description static -l pl
Biblioteki statyczne imlib2.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
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
rm -f $RPM_BUILD_ROOT%{_libdir}/imlib2/*/*.a

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/imlib2_*
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%dir %{_libdir}/imlib2
%dir %{_libdir}/imlib2/filters
%dir %{_libdir}/imlib2/loaders
%attr(755,root,root) %{_libdir}/imlib2/*/*.so
%{_libdir}/imlib2/*/*.la
%{_datadir}/imlib2

%files devel
%defattr(644,root,root,755)
%doc doc/{*.gif,*.html}
%attr(755,root,root) %{_bindir}/imlib2-config
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/Imlib2.h
%{_pkgconfigdir}/imlib2.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
