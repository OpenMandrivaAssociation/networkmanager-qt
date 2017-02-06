%define major 6
%define libname %mklibname KF5NetworkManagerQt %{major}
%define devname %mklibname KF5NetworkManagerQt -d
%define debug_package %{nil}
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
%ifarch x86_64
# Workaround for clang crash at link time last verified in 4.0.0-0.281115.1
%define _disable_lto 1
%endif

Name: networkmanager-qt
Version: 5.31.0
Release: 1
Source0: http://download.kde.org/%{stable}/frameworks/%(echo %{version} |cut -d. -f1-2)/%{name}-%{version}.tar.xz
Summary: Qt style wrapper of the NetworkManager API
URL: http://kde.org/
License: LGPL v2.1
Group: System/Libraries
BuildRequires: cmake(ECM)
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5DBus)
BuildRequires: pkgconfig(Qt5Network)
BuildRequires: pkgconfig(Qt5Test)
BuildRequires: pkgconfig(libnm)
BuildRequires: pkgconfig(libnm-util)
BuildRequires: pkgconfig(libnm-glib)
BuildRequires: pkgconfig(NetworkManager)
Requires: %{libname} = %{EVRD}
%rename libnm-qt5 < 1:5.1.2-3

%description
This package provides a nice Qt style API to work with NetworkManager.

%package -n %{libname}
Summary: Qt style wrapper of the NetworkManager API
Group: System/Libraries
%rename %{_lib}KF5NetworkManagerQt5 < 1:5.1.2-3

%description -n %{libname}
This package provides a nice Qt style API to work with NetworkManager.


%package -n %{devname}
Summary: Development files for the KDE Frameworks 5 NetworkManager library
Group: Development/KDE and Qt
Requires: %{libname} = %{EVRD}
Requires: pkgconfig(NetworkManager)
Requires: pkgconfig(libnm)
Requires: pkgconfig(libnm-util)
Requires: pkgconfig(libnm-glib)
%rename %{_lib}KF5NetworkManagerQt-devel < 1:5.1.2-3

%description -n %{devname}
Development files for the KDE Frameworks 5 NetworkManager library.

This package provides a nice Qt style API to work with NetworkManager.

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%files -n %{libname}
%{_libdir}/*.so.%{major}
%{_libdir}/*.so.%{version}

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/KF5*
%{_libdir}/qt5/mkspecs/modules/qt_NetworkManagerQt.pri
