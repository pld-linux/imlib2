Summary:	Powerful image loading and rendering library
Summary(pl.UTF-8):	Potężna biblioteka wczytująca i renderująca obrazki
Name:		imlib2
Version:	1.7.1
Release:	1
License:	BSD-like
Group:		X11/Libraries
Source0:	http://downloads.sourceforge.net/enlightenment/%{name}-%{version}.tar.bz2
# Source0-md5:	98569de9b10bcb6fd5d13e4d331ddd81
URL:		https://docs.enlightenment.org/api/imlib2/html/
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake >= 1.6
BuildRequires:	bzip2-devel
BuildRequires:	freetype-devel >= 2.1
BuildRequires:	giflib-devel
BuildRequires:	libid3tag-devel
BuildRequires:	libjpeg-devel >= 6b-18
BuildRequires:	libpng-devel >= 1.0.8
BuildRequires:	libtiff-devel
BuildRequires:	libtool
BuildRequires:	libwebp-devel
BuildRequires:	libxcb-devel >= 1.9
BuildRequires:	pkgconfig
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	zlib-devel
Requires:	freetype >= 2.1
Requires:	libjpeg >= 6b-18
Requires:	libpng >= 1.0.8
Requires:	libxcb >= 1.9
Obsoletes:	libimlib2_1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Imlib2 is an advanced replacement library for libraries like libXpm
that provides many more features with much greater flexibility and
speed than standard libraries, including font rasterization, rotation,
RGBA space rendering and blending, dynamic binary filters, scripting,
and more.

%description -l pl.UTF-8
Imlib2 jest zaawansowaną biblioteką, zamiennikiem takich bibliotek jak
libXpm. Imlib2 dostarcza o wiele więcej możliwości przy dużo większej
szybkości niż standardowe biblioteki (włączając w to rasteryzację
fontów, obracanie, renderowanie przestrzeni RGBA, mieszanie,
dynamiczne filtry (w postaci binarnej), obsługa języka skryptowego i
wiele więcej.

%package devel
Summary:	Imlib2 header files and development documentation
Summary(fr.UTF-8):	Fichiers entête pour Imlib2
Summary(pl.UTF-8):	Pliki nagłówkowe oraz dokumentacja do imlib2
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	freetype-devel
Requires:	libltdl-devel
Requires:	xorg-lib-libXext-devel
Obsoletes:	libimlib2_1-devel

%description devel
Header files and development documentation for Imlib2.

%description devel -l fr.UTF-8
Fichiers entête pour Imlib2.

%description devel -l pl.UTF-8
Pliki nagłówkowe oraz dokumentacja do biblioteki Imlib2.

%package static
Summary:	Imlib2 static library
Summary(pl.UTF-8):	Biblioteka statyczna imlib2
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Imlib2 static library.

%description static -l pl.UTF-8
Biblioteka statyczna imlib2.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
%ifarch i586 i686 pentium3 pentium4 athlon
	--enable-mmx
%else
	--disable-mmx
%endif

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# not needed
%{__rm} $RPM_BUILD_ROOT%{_libdir}/imlib2/*/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING COPYING-PLAIN ChangeLog README
%attr(755,root,root) %{_bindir}/imlib2_*
%attr(755,root,root) %{_libdir}/libImlib2.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libImlib2.so.1
%dir %{_libdir}/imlib2
%dir %{_libdir}/imlib2/filters
%attr(755,root,root) %{_libdir}/imlib2/filters/*.so
%dir %{_libdir}/imlib2/loaders
%attr(755,root,root) %{_libdir}/imlib2/loaders/*.so
%{_datadir}/imlib2

%files devel
%defattr(644,root,root,755)
%doc doc/{*.gif,*.html}
%attr(755,root,root) %{_bindir}/imlib2-config
%attr(755,root,root) %{_libdir}/libImlib2.so
%{_libdir}/libImlib2.la
%{_includedir}/Imlib2.h
%{_pkgconfigdir}/imlib2.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libImlib2.a
