# TODO
# do --enable-dav switch

Summary:	AVFS - A Virtual Filesystem
Summary(pl.UTF-8):	AVFS - wirtualny system plików
Name:		avfs
Version:	1.1.4
Release:	2
License:	GPL v2+
Group:		Libraries
Source0:	https://downloads.sourceforge.net/avf/%{name}-%{version}.tar.bz2
# Source0-md5:	c333462d744aeab2e6bee7a1af02350e
URL:		http://sourceforge.net/projects/avf/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	bzip2-devel
BuildRequires:	libfuse-devel >= 2.6.0
BuildRequires:	libtool
BuildRequires:	lzlib-devel
BuildRequires:	openssl-devel
BuildRequires:	pkgconfig
BuildRequires:	xz-devel
BuildRequires:	zlib-devel
BuildRequires:	zstd-devel
Requires:	libfuse >= 2.6.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
AVFS is a system, which enables all programs to look inside archived
or compressed files, or access remote files without recompiling the
programs or changing the kernel.

At the moment it supports floppies, tar and gzip files, zip, bzip2, ar
and rar files, FTP sessions, http, webdav, rsh/rcp, ssh/scp. Quite a
few other handlers are implemented with the Midnight Commander's
external FS.

%description -l pl.UTF-8
AVFS to system, który umożliwia wszystkim programom zaglądanie do
zarchiwizowanych lub skompresowanych plików lub dostęp do zdanych
plików bez rekompilacji programów lub zmiany jądra.

Aktualnie obsługuje dyskietki, pliki tar, gzip, zip, bzip2, ar i rar,
sesje FTP, http, webdav, rsh/rcp, ssh/scp. Jest też trochę innych
procedur obsługi zaimplementowanych z użyciem extfs (zewnętrznych
systemów plików) Midnight Commandera.

%package devel
Summary:	Header files for avfs library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki avfs
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
The avfs-devel package includes the header files necessary for
developing programs using the avfs library.

%description devel -l pl.UTF-8
Pakiet avfs-devel zawiera pliki nagłówkowe niezbędne do budowania
programów używających biblioteki avfs.

%package static
Summary:	Static avfs library
Summary(pl.UTF-8):	Statyczna biblioteka avfs
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description static
This package contains the static version of avfs library.

%description static -l pl.UTF-8
Ten pakiet zawiera statyczną wersję biblioteki avfs.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	EMACS=%{_bindir}/emacs \
	PERL=%{_bindir}/perl \
	ZIP=%{_bindir}/zip \
	UNZIP=%{_bindir}/unzip \
	--disable-avfscoda \
	--disable-dav \
	--enable-fuse \
	--enable-library \
	--with-system-bzlib \
	--with-system-zlib \
	--with-xz \
	--with-zstd
# Comment:
# I've no idea how to build this package with dav option with expat-devel  --blekot
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
%doc README doc/README.avfs-fuse
%attr(755,root,root) %{_libdir}/libavfs.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libavfs.so.0
%attr(755,root,root) %{_bindir}/avfsd
%attr(755,root,root) %{_bindir}/davpass
%attr(755,root,root) %{_bindir}/ftppass
%attr(755,root,root) %{_bindir}/mountavfs
%attr(755,root,root) %{_bindir}/umountavfs
%{_libdir}/%{name}

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/avfs-config
%attr(755,root,root) %{_libdir}/libavfs.so
%{_libdir}/libavfs.la
%{_includedir}/*.h
%{_pkgconfigdir}/avfs.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libavfs.a
