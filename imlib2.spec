Summary:	Powerful image loading and rendering library
Summary(pl):	Biblioteka do ≥adowania i renderowania obrazkÛw
Name:		imlib2
Version:	1.0.3
Release:	2
License:	LGPL
Group:		X11/Libraries
Group(de):	X11/Libraries
Group(es):	X11/Bibliotecas
Group(fr):	X11/Librairies
Group(pl):	X11/Biblioteki
Group(pt_BR):	X11/Bibliotecas
Group(ru):	X11/‚…¬Ã…œ‘≈À…
Group(uk):	X11/‚¶¬Ã¶œ‘≈À…
Source0:	http://prdownloads.sourceforge.net/enlightenment/%{name}-%{version}.tar.gz
Patch0:		%{name}-path.patch
Patch1:		%{name}-ltdl.patch
BuildRequires:	libtool
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtiff-devel
BuildRequires:	libungif-devel
BuildRequires:	libpng-devel >= 1.0.8
BuildRequires:	libjpeg-devel >= 6b-18
BuildRequires:	edb-devel
BuildRequires:	zlib-devel
BuildRequires:	freetype1-devel
BuildRequires:	XFree86-devel
BuildRequires:	libltdl-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
libXpm. Imlib2 dostarcza o wiele wiÍcej moøliwo∂ci przy duøo wiÍkszej
szybko∂ci niø standardowe bilioteki (w≥±czaj±c w to rasteryzacjÍ
fontÛw, obracanie, renderowanie przestrzeni RGBA, mieszanie,
dynamiczne filtry (w postaci binarnej), obs≥uga jÍzyka skryptowego i
wiele wiÍcej.

%package devel
Summary:	Imlib header files and development documentation
Summary(fr):	Fichiers entÍte pour Imlib
Summary(pl):	Pliki nag≥Ûwkowe oraz dokumentacja do imlib
Group:		X11/Development/Libraries
Group(de):	X11/Entwicklung/Libraries
Group(es):	X11/Desarrollo/Bibliotecas
Group(fr):	X11/Development/Librairies
Group(pl):	X11/Programowanie/Biblioteki
Group(pt_BR):	X11/Desenvolvimento/Bibliotecas
Group(ru):	X11/Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):	X11/Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…
Requires:	%{name} = %{version}
# Every program using imlib2 should get a list of libraries to link with by
# executing `imlib2-config --libs`. All libraries listed below are returned by
# this call, so they are required by every program compiled with imlib.
Requires:	freetype1-devel
Requires:	XFree86-devel

%description devel
Header files and development documentation for Imlib.

%description devel -l fr
Fichiers entÍte pour Imlib.

%description devel -l pl
Pliki nag≥Ûwkowe oraz dokumentacja do biblioteki Imlib.

%package static
Summary:	Imlib static libraries
Summary(pl):	Biblioteki statyczne imlib
Group:		X11/Development/Libraries
Group(de):	X11/Entwicklung/Libraries
Group(es):	X11/Desarrollo/Bibliotecas
Group(fr):	X11/Development/Librairies
Group(pl):	X11/Programowanie/Biblioteki
Group(pt_BR):	X11/Desenvolvimento/Bibliotecas
Group(ru):	X11/Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):	X11/Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…
Requires:	%{name}-devel = %{version}

%description static
Imlib static libraries.

%description devel -l pl
Biblioteki statyczne imlib.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
rm missing
libtoolize --copy --force
aclocal
autoconf
automake -a -c
%configure \
%ifarch i586 i686
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
