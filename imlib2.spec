#
# Conditional build:
%bcond_without	jxl		# JPEG XL loader
%bcond_without	heif		# HEIF loader
%bcond_without	avif		# AVIF loader
%bcond_with	ps		# PostScript support
%bcond_without	static_libs	# static library

Summary:	Powerful image loading and rendering library
Summary(pl.UTF-8):	Potężna biblioteka wczytująca i renderująca obrazki
Name:		imlib2
Version:	1.12.5
Release:	3
License:	BSD-like
Group:		X11/Libraries
Source0:	https://downloads.sourceforge.net/enlightenment/%{name}-%{version}.tar.xz
# Source0-md5:	c81c9f91d92ecbd87cf652f867ec5d74
URL:		https://docs.enlightenment.org/api/imlib2/html/
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake >= 1.6
BuildRequires:	bzip2-devel
BuildRequires:	doxygen
BuildRequires:	freetype-devel >= 2.1
BuildRequires:	giflib-devel
%{?with_avif:BuildRequires:	libavif-devel}
%{?with_heif:BuildRequires:	libheif-devel}
BuildRequires:	libid3tag-devel
BuildRequires:	libjpeg-devel >= 6b-18
%{?with_jxl:BuildRequires:	libjxl-devel}
BuildRequires:	libpng-devel >= 1.0.8
BuildRequires:	libraw-devel
BuildRequires:	librsvg-devel >= 2.46
%{?with_ps:BuildRequires:    libspectre-devel}
BuildRequires:	libtiff-devel >= 4
BuildRequires:	libtool >= 2:2
BuildRequires:	libwebp-devel
BuildRequires:	libxcb-devel >= 1.9
BuildRequires:	libyuv-devel
BuildRequires:	openjpeg2-devel >= 2
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.527
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xz
BuildRequires:	xz-devel
BuildRequires:	zlib-devel
Requires:	freetype >= 2.1
Requires:	libjpeg >= 6b-18
Requires:	libpng >= 1.0.8
Requires:	libxcb >= 1.9
Conflicts:	imlib2_loaders < 1.10.0
Obsoletes:	libimlib2_1 < 2
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
Obsoletes:	libimlib2_1-devel < 2

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

# missing in dist tarball, make a stub
install -d test
touch test/Makefile.am

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
	%{__enable_disable static_libs static} \
	--enable-doc-build \
	%{!?with_ps:--without-ps} \
%ifarch i586 i686 pentium3 pentium4 athlon
	--enable-mmx \
%else
	--disable-mmx \
%endif
%ifarch %{x8664}
	--enable-amd64 \
%endif
	%{!?with_avif:--without-avif} \
	%{!?with_heif:--without-heif} \
	%{!?with_jxl:--without-jxl}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# not needed
%{__rm} $RPM_BUILD_ROOT%{_libdir}/imlib2/*/*.la
# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libImlib2.la

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
%doc doc/html
%attr(755,root,root) %{_libdir}/libImlib2.so
%{_includedir}/Imlib2.h
%{_includedir}/Imlib2_Loader.h
%{_pkgconfigdir}/imlib2.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libImlib2.a
%endif
