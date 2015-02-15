%define major 6
%define libname %mklibname KF5NetworkManagerQt %{major}
%define devname %mklibname KF5NetworkManagerQt -d
%define debug_package %{nil}
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Name: networkmanager-qt
Version: 5.7.0
Release: 1
Source0: http://ftp5.gwdg.de/pub/linux/kde/%{stable}/frameworks/%(echo %{version} |cut -d. -f1-2)/%{name}-%{version}.tar.xz
Summary: Qt style wrapper of the NetworkManager API
URL: http://kde.org/
License: LGPL v2.1
Group: System/Libraries
BuildRequires: cmake
BuildRequires: qmake5
BuildRequires: extra-cmake-modules5
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5DBus)
BuildRequires: pkgconfig(Qt5Network)
BuildRequires: pkgconfig(libnm)
BuildRequires: pkgconfig(libnm-util)
BuildRequires: pkgconfig(libnm-glib)
BuildRequires: pkgconfig(NetworkManager)
BuildRequires: cmake(ECM)
BuildRequires: ninja
Requires: %{libname} = %{EVRD}

%description
This package provides a nice Qt style API to work with NetworkManager.

%package -n %{libname}
Summary: Qt style wrapper of the NetworkManager API
Group: System/Libraries

%description -n %{libname}
This package provides a nice Qt style API to work with NetworkManager.


%package -n %{devname}
Summary: Development files for the KDE Frameworks 5 NetworkManager library
Group: Development/KDE and Qt
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files for the KDE Frameworks 5 NetworkManager library.

This package provides a nice Qt style API to work with NetworkManager.

%prep
%setup -q
%cmake -G Ninja \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON

%build
ninja -C build

%install
DESTDIR="%{buildroot}" ninja -C build install %{?_smp_mflags}

%files -n %{libname}
%{_libdir}/*.so.%{major}
%{_libdir}/*.so.%{version}

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/KF5*
%{_libdir}/qt5/mkspecs/modules/qt_NetworkManagerQt.pri
