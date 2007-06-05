%define	name	epsilon
%define	version 0.3.0.008
%define release %mkrel 4

%define major 	0
%define libname %mklibname %{name} %major
%define libnamedev %mklibname %{name} %major -d

Summary: 	Enlightenment thumbnailing library
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
License: 	BSD
Group: 		Graphical desktop/Enlightenment
URL: 		http://get-e.org/
Source: 	%{name}-%{version}.tar.bz2
#Patch0:		epsilon-0.3.0.007-ipc_server_send.patch
BuildRoot: 	%{_tmppath}/%{name}-buildroot
BuildRequires:	imlib2-devel
BuildRequires:	epeg-devel png-devel
BuildRequires:	multiarch-utils
BuildRequires:  evas-devel >= 0.9.9.038
BuildRequires:  ecore-devel
BuildRequires:  edje-devel
Buildrequires:  %{mklibname xine1}-devel
BuildRequires:	autoconf2.5

%description
This is a small, display independent, and quick thumbnailing library.
The lib itself conforms to the standard put forth by freedesktop.org.

This package is part of the Enlightenment DR17 desktop shell.

%package -n %libname
Summary: Libraries for the %{name} package
Group: System/Libraries

%description -n %libname
Libraries for %{name}

%package -n %libnamedev
Summary: Headers and development libraries from %{name}
Group: Development/Other
Requires: %libname = %{version}
Provides: lib%{name}-devel = %{version}-%{release}
Provides: %name-devel = %{version}-%{release}

%description -n %libnamedev
%{name} development headers and libraries

%prep
%setup -q 
#%patch0 -p0

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall
%multiarch_binaries %buildroot/%_bindir/%name-config

%post -n %libname -p /sbin/ldconfig
%postun -n %libname -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS COPYING README
%{_bindir}/%name
%{_bindir}/%{name}_*

%files -n %libname
%defattr(-,root,root)
%{_libdir}/*.so.*
%{_libdir}/%name/plugins/xine_thumbnailer.so


%files -n %libnamedev
%defattr(-,root,root)
%{_libdir}/pkgconfig/*
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/%name/plugins/xine_thumbnailer.*a
%{_includedir}/*.h
%{_bindir}/%name-config
%multiarch %multiarch_bindir/%name-config


