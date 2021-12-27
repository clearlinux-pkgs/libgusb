#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libgusb
Version  : 0.3.9
Release  : 13
URL      : https://github.com/hughsie/libgusb/archive/0.3.9/libgusb-0.3.9.tar.gz
Source0  : https://github.com/hughsie/libgusb/archive/0.3.9/libgusb-0.3.9.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : LGPL-2.1
Requires: libgusb-bin = %{version}-%{release}
Requires: libgusb-data = %{version}-%{release}
Requires: libgusb-lib = %{version}-%{release}
Requires: libgusb-license = %{version}-%{release}
BuildRequires : buildreq-meson
BuildRequires : docbook-xml
BuildRequires : gobject-introspection-dev
BuildRequires : gtk-doc
BuildRequires : libusb-dev
BuildRequires : pkgconfig(libusb-1.0)
BuildRequires : vala-dev

%description
GUsb
====
GUsb is a GObject wrapper for libusb1 that makes it easy to do
asynchronous control, bulk and interrupt transfers with proper
cancellation and integration into a mainloop.
This makes it easy to integrate low level USB transfers with your
high-level application or system daemon.

%package bin
Summary: bin components for the libgusb package.
Group: Binaries
Requires: libgusb-data = %{version}-%{release}
Requires: libgusb-license = %{version}-%{release}

%description bin
bin components for the libgusb package.


%package data
Summary: data components for the libgusb package.
Group: Data

%description data
data components for the libgusb package.


%package dev
Summary: dev components for the libgusb package.
Group: Development
Requires: libgusb-lib = %{version}-%{release}
Requires: libgusb-bin = %{version}-%{release}
Requires: libgusb-data = %{version}-%{release}
Provides: libgusb-devel = %{version}-%{release}
Requires: libgusb = %{version}-%{release}

%description dev
dev components for the libgusb package.


%package doc
Summary: doc components for the libgusb package.
Group: Documentation

%description doc
doc components for the libgusb package.


%package lib
Summary: lib components for the libgusb package.
Group: Libraries
Requires: libgusb-data = %{version}-%{release}
Requires: libgusb-license = %{version}-%{release}

%description lib
lib components for the libgusb package.


%package license
Summary: license components for the libgusb package.
Group: Default

%description license
license components for the libgusb package.


%prep
%setup -q -n libgusb-0.3.9
cd %{_builddir}/libgusb-0.3.9

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1640643523
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir

%install
mkdir -p %{buildroot}/usr/share/package-licenses/libgusb
cp %{_builddir}/libgusb-0.3.9/COPYING %{buildroot}/usr/share/package-licenses/libgusb/9a1929f4700d2407c70b507b3b2aaf6226a9543c
DESTDIR=%{buildroot} ninja -C builddir install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/gusbcmd

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/GUsb-1.0.typelib
/usr/share/gir-1.0/*.gir
/usr/share/vala/vapi/gusb.deps
/usr/share/vala/vapi/gusb.vapi

%files dev
%defattr(-,root,root,-)
/usr/include/gusb-1/gusb.h
/usr/include/gusb-1/gusb/gusb-autocleanups.h
/usr/include/gusb-1/gusb/gusb-context-private.h
/usr/include/gusb-1/gusb/gusb-context.h
/usr/include/gusb-1/gusb/gusb-device-list.h
/usr/include/gusb-1/gusb/gusb-device-private.h
/usr/include/gusb-1/gusb/gusb-device.h
/usr/include/gusb-1/gusb/gusb-endpoint-private.h
/usr/include/gusb-1/gusb/gusb-endpoint.h
/usr/include/gusb-1/gusb/gusb-interface-private.h
/usr/include/gusb-1/gusb/gusb-interface.h
/usr/include/gusb-1/gusb/gusb-source.h
/usr/include/gusb-1/gusb/gusb-util.h
/usr/include/gusb-1/gusb/gusb-version.h
/usr/lib64/libgusb.so
/usr/lib64/pkgconfig/gusb.pc

%files doc
%defattr(0644,root,root,0755)
/usr/share/gtk-doc/html/gusb/faq.html
/usr/share/gtk-doc/html/gusb/gusb-GUsbContext.html
/usr/share/gtk-doc/html/gusb/gusb-GUsbDevice.html
/usr/share/gtk-doc/html/gusb/gusb-GUsbDeviceList.html
/usr/share/gtk-doc/html/gusb/gusb-gusb-endpoint.html
/usr/share/gtk-doc/html/gusb/gusb-gusb-interface.html
/usr/share/gtk-doc/html/gusb/gusb-gusb-source.html
/usr/share/gtk-doc/html/gusb/gusb-gusb-version.html
/usr/share/gtk-doc/html/gusb/gusb.devhelp2
/usr/share/gtk-doc/html/gusb/home.png
/usr/share/gtk-doc/html/gusb/index.html
/usr/share/gtk-doc/html/gusb/introduction.html
/usr/share/gtk-doc/html/gusb/left-insensitive.png
/usr/share/gtk-doc/html/gusb/left.png
/usr/share/gtk-doc/html/gusb/libgusb-helpers.html
/usr/share/gtk-doc/html/gusb/libgusb.html
/usr/share/gtk-doc/html/gusb/right-insensitive.png
/usr/share/gtk-doc/html/gusb/right.png
/usr/share/gtk-doc/html/gusb/specification.html
/usr/share/gtk-doc/html/gusb/style.css
/usr/share/gtk-doc/html/gusb/up-insensitive.png
/usr/share/gtk-doc/html/gusb/up.png

%files lib
%defattr(-,root,root,-)
/usr/lib64/libgusb.so.2
/usr/lib64/libgusb.so.2.0.10

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libgusb/9a1929f4700d2407c70b507b3b2aaf6226a9543c
