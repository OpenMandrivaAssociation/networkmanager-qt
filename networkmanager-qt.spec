%define major 6
%define libname %mklibname KF5NetworkManagerQt %{major}
%define devname %mklibname KF5NetworkManagerQt -d
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Name: networkmanager-qt
Version: 5.104.0
Release: 2
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
# For building QCH docs
BuildRequires:  doxygen
BuildRequires:  qt5-assistant
Requires: %{libname} = %{EVRD}
%rename libnm-qt5

%description
This package provides a nice Qt style API to work with NetworkManager.

%package -n %{libname}
Summary: Qt style wrapper of the NetworkManager API
Group: System/Libraries
Obsoletes:KF5NetworkManagerQt5 < %{EVRD}
Requires: %{name} = %{EVRD}

%description -n %{libname}
This package provides a nice Qt style API to work with NetworkManager.

%package -n %{devname}
Summary: Development files for the KDE Frameworks 5 NetworkManager library
Group: Development/KDE and Qt
Requires: %{libname} = %{EVRD}
Requires: pkgconfig(libnm)
%rename %{_lib}KF5NetworkManagerQt-devel

%description -n %{devname}
Development files for the KDE Frameworks 5 NetworkManager library.

This package provides a nice Qt style API to work with NetworkManager.

%package -n %{name}-devel-docs
Summary: Developer documentation for %{name} for use with Qt Assistant
Group: Documentation
Suggests: %{devname} = %{EVRD}

%description -n %{name}-devel-docs
Developer documentation for %{name} for use with Qt Assistant

%prep
%autosetup -p1
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%files
%{_datadir}/qlogging-categories5/*.categories
%{_datadir}/qlogging-categories5/networkmanagerqt.renamecategories

%files -n %{libname}
%{_libdir}/*.so.%{major}
%{_libdir}/*.so.%{version}

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/KF5*

%files -n %{name}-devel-docs
%{_docdir}/qt5/*.{tags,qch}
