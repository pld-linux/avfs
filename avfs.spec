# TODO
# do --enable-dav switch

Summary:	AFS - A Virtual Filesystem
Summary(pl):	AFS - wirtualny system plików
Name:		avfs
Version:	0.9.6
Release:	0.1
License:	GPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/avf/%{name}-%{version}.tar.gz
# Source0-md5:	59829701fb2d7593ed7c1de9e0a5ac63
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

%prep
%setup -q

%build
install /usr/share/automake/config.* .

%configure \
	--enable-preload \
	--enable-xml \
	--with-neon \
	--with-ssl \
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
%{_libdir}/avfs_preload.a
%{_libdir}/avfs_preload.la
