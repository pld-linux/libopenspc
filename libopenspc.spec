Summary:	OpenSPC - SPC file player
Summary(pl.UTF-8):	OpenSPC - odtwarzacz plików SPC
Name:		libopenspc
Version:	0.3.99
%define	snap	20050926
Release:	0.%{snap}.2
# SNEeSe in on other, GPL-compatible license, but interface part implies LGPL
License:	LGPL v2+
Group:		Libraries
Source0:	http://home.comcast.net/~brad.martin1/OpenSPC_snap-%{snap}.tar.bz2
# Source0-md5:	a7b4e60e3780bb06608c1bd73f1bf1b4
URL:		http://home.comcast.net/~brad.martin1/
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OpenSPC - SPC file player.

%description -l pl.UTF-8
OpenSPC - odtwarzacz plików SPC.

%package devel
Summary:	Header files for OpenSPC library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki OpenSPC
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	zlib-devel

%description devel
Header files for OpenSPC library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki OpenSPC.

%package static
Summary:	Static OpenSPC library
Summary(pl.UTF-8):	Statyczna biblioteka OpenSPC
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static OpenSPC library.

%description static -l pl.UTF-8
Statyczna biblioteka OpenSPC.

%prep
%setup -q

mv -f libopenspc/SNEeSe/LICENSE LICENSE.SNEeSe
mv -f libopenspc/SNEeSe/README README.SNEeSe

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog README LICENSE.SNEeSe README.SNEeSe
%attr(755,root,root) %{_bindir}/ospcplay
%attr(755,root,root) %{_libdir}/libopenspc.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libopenspc.so
%{_libdir}/libopenspc.la
%{_includedir}/openspc.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libopenspc.a
