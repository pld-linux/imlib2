#
# _with_static_ltdl - build using static ltdl library (just asking for trouble)
#
Summary:	Powerful image loading and rendering library
Summary(pl):	Pot�na biblioteka wczytuj�ca i renderuj�ca obrazki
Name:		imlib2
Version:	1.0.6
Release:	4
License:	LGPL
Group:		X11/Libraries
Source0:	http://dl.sourceforge.net/enlightenment/%{name}-%{version}.tar.gz
# Source0-md5:	e3475376bf27347c47c7a9ffb49bdb96
Patch0:		%{name}-path.patch
Patch1:		%{name}-as.patch
Patch2:		%{name}-ltdl.patch
Patch3:		%{name}-AC_LIBOBJ.patch
BuildRequires:	XFree86-devel
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
Imlib2 jest zaawansowan� bibliotek�, zamiennikiem takich bibliotek jak
libXpm. Imlib2 dostarcza o wiele wi�cej mo�liwo�ci przy du�o wi�kszej
szybko�ci ni� standardowe bilioteki (w��czaj�c w to rasteryzacj�
font�w, obracanie, renderowanie przestrzeni RGBA, mieszanie,
dynamiczne filtry (w postaci binarnej), obs�uga j�zyka skryptowego i
wiele wi�cej.

%package devel
Summary:	Imlib header files and development documentation
Summary(fr):	Fichiers ent�te pour Imlib
Summary(pl):	Pliki nag��wkowe oraz dokumentacja do imlib
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}
# Every program using imlib2 should get a list of libraries to link with by
# executing `imlib2-config --libs`. All libraries listed below are returned by
# this call, so they are required by every program compiled with imlib.
Requires:	XFree86-devel
Requires:	freetype1-devel
%{!?_with_static_ltdl:Requires:	libltdl-devel}
Obsoletes:	libimlib2_1-devel

%description devel
Header files and development documentation for Imlib.

%description devel -l fr
Fichiers ent�te pour Imlib.

%description devel -l pl
Pliki nag��wkowe oraz dokumentacja do biblioteki Imlib.

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
%patch3 -p1

%build
rm -f missing
# ltdl option copies libltdl sources
%{__libtoolize} %{?_with_static_ltdl:--ltdl}
%{__aclocal}
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

# shutup check-files
rm -f  $RPM_BUILD_ROOT/%{_libdir}/%{name}/loaders/*/*.a

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
%{_libdir}/%{name}/loaders/*/*.la

%files devel
%defattr(644,root,root,755)
%doc doc/{*gif,*.html}
%attr(755,root,root) %{_bindir}/%{name}-config
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
