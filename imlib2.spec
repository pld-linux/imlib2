#
# _with_static_ltdl - build using static ltdl library

Summary:	Powerful image loading and rendering library
Name:		imlib2
Version:	1.0.6
Release:	1
License:	LGPL
Group:		X11/Libraries
Source0:	ftp://ftp.sourceforge.net/pub/sourceforge/enlightenment/%{name}-%{version}.tar.gz
Patch0:		%{name}-path.patch
Patch1:		%{name}-as.patch
Patch2:		%{name}-ltdl.patch
BuildRequires:	XFree86-devel
BuildRequires:	edb-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	freetype1-devel
BuildRequires:	libjpeg-devel >= 6b-18
%{!?_with_static_ltdl:BuildRequires:	libltdl-devel}
BuildRequires:	libpng-devel >= 1.0.8
BuildRequires:	libtiff-devel
BuildRequires:	libtool
BuildRequires:	libungif-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	libimlib2_1

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man
%define		_sysconfdir	/etc/X11

%description
Imlib2 is an advanced replacement library for libraries like libXpm
that provides many more features with much greater flexibility and
speed than standard libraries, including font rasterization, rotation,
RGBA space rendering and blending, dynamic binary filters, scripting,
and more.

%description -l pl
Imlib2 jest zaawansowan± bibliotek±, zamiennikiem takich bibliotek jak
libXpm. Imlib2 dostarcza o wiele wiêcej mo¿liwo¶ci przy du¿o wiêkszej
szybko¶ci ni¿ standardowe bilioteki (w³±czaj±c w to rasteryzacjê
fontów, obracanie, renderowanie przestrzeni RGBA, mieszanie,
dynamiczne filtry (w postaci binarnej), obs³uga jêzyka skryptowego i
wiele wiêcej.

%package devel
Summary:	Imlib header files and development documentation
Summary(fr):	Fichiers entête pour Imlib
Summary(pl):	Pliki nag³ówkowe oraz dokumentacja do imlib
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}
# Every program using imlib2 should get a list of libraries to link with by
# executing `imlib2-config --libs`. All libraries listed below are returned by
# this call, so they are required by every program compiled with imlib.
Requires:	freetype1-devel
Requires:	XFree86-devel
Obsoletes:	libimlib2_1-devel

%description devel
Header files and development documentation for Imlib.

%description devel -l fr
Fichiers entête pour Imlib.

%description devel -l pl
Pliki nag³ówkowe oraz dokumentacja do biblioteki Imlib.

%package static
Summary:	Imlib static libraries
Summary(pl):	Biblioteki statyczne imlib
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Imlib static libraries.

%description devel -l pl
Biblioteki statyczne imlib.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%{!?_with_static_ltdl:%patch2 -p1}

%build
rm -f missing
%{__libtoolize} --ltdl
# ltdl option copies libltdl sources
aclocal
%{__autoconf}
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

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/loaders
%dir %{_libdir}/%{name}/loaders/filter
%dir %{_libdir}/%{name}/loaders/image
%attr(755,root,root) %{_libdir}/%{name}/loaders/*/*.so
%attr(755,root,root) %{_libdir}/%{name}/loaders/*/*.la

%files devel
%defattr(644,root,root,755)
%doc doc/{*gif,*.html}
%attr(755,root,root) %{_bindir}/%{name}-config
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
