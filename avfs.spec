# TODO
# do --enable-dav switch

Summary:	AFS - A Virtual Filesystem
Summary(pl):	AFS - wirtualny system plików
Name:		avfs
Version:	0.9.7
Release:	0.1
License:	GPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/avf/%{name}-%{version}.tar.gz
# Source0-md5:	88da3489b1c1d80d080ce780333cedef
URL:		http://sourceforge.net/projects/avf/
BuildRequires:	automake
BuildRequires:	expat-devel
BuildRequires:	neon-devel
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

%description -l pl
AVFS to system, który umo¿liwia wszystkim programom zagl±danie do
zarchiwizowanych lub skompresowanych plików lub dostêp do zdanych
plików bez rekompilacji programów lub zmiany j±dra.

Aktualnie obs³uguje dyskietki, pliki tar, gzip, zip, bzip2, ar i rar,
sesje FTP, http, webdav, rsh/rcp, ssh/scp. Jest te¿ trochê innych
procedur obs³ugi zaimplementowanych z u¿yciem extfs (zewnêtrznych
systemów plików) Midnight Commandera.

%package devel
Summary:        Header files for avfs library
Summary(pl):    Pliki nag³ówkowe bibliotek avfs
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}

%description devel
The avfs-devel package includes the header files necessary for
developing programs using the avfs libraries.

%description devel -l pl
Pakiet avfs-devel zawiera pliki nag³ówkowe niezbêdne do budowania
programów u¿ywaj±cych bibliotek avfs.

%package static
Summary:        Static avfs libraries
Summary(pl):    Statyczne biblioteki avfs
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}

%description static
This package contains the static version of avfs libraries.

%description static -l pl
Ten pakiet zawiera statyczn± wersjê bibliotek avfs.

%prep
%setup -q

%build
install /usr/share/automake/config.* .

%configure \
	--enable-library \
	--enable-xml \
	--with-neon \
	--with-ssl \
	--disable-fast-install \
	--with-kernel=%{_kernelsrcdir}
#        --enable-dav
# Comment:
# I've no idea how to build this package with dav option with expat-devel.
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
%doc README
%attr(755,root,root) %{_libdir}/*.so.*.*
%attr(755,root,root) %{_bindir}/davpass
%attr(755,root,root) %{_bindir}/ftppass
%{_libdir}/%{name}

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/avfs-config
%{_includedir}/*.h
%{_libdir}/*.la

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
