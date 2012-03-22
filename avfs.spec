# TODO
# do --enable-dav switch

Summary:	AVFS - A Virtual Filesystem
Summary(pl.UTF-8):	AVFS - wirtualny system plików
Name:		avfs
Version:	1.0.0
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/avf/%{name}-%{version}.tar.gz
# Source0-md5:	be6dd4417c3e96a294f1539ad22fddc9
Patch0:		%{name}-unrar.c.patch
URL:		http://sourceforge.net/projects/avf/
BuildRequires:	automake
BuildRequires:	libfuse-devel >= 0:2.4
#BuildRequires:	neon-devel >= 0.12
#BuildRequires:	neon-devel < 0.13
BuildRequires:	openssl-devel >= 0.9.7d
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
%patch0 -p1

%build
cp -f /usr/share/automake/config.* .
%configure \
	--disable-avfscoda \
	--enable-fuse \
	--enable-library \
	--with-ssl
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
%attr(755,root,root) %ghost %{_libdir}libavfs.so.0
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

%files static
%defattr(644,root,root,755)
%{_libdir}/libavfs.a
