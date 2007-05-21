%define	name	epsilon
%define	version 0.3.0.008
%define release %mkrel 1

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
Patch0:		epsilon-0.3.0.007-ipc_server_send.patch
BuildRoot: 	%{_tmppath}/%{name}-buildroot
BuildRequires:	imlib2-devel
BuildRequires:	epeg-devel png-devel
BuildRequires:	multiarch-utils
BuildRequires:  evas-devel
BuildRequires:  ecore-devel
BuildRequires:  edje-devel
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



%changelog
* Wed May 16 2007 Antoine Ginies <aginies@mandriva.com> 0.3.0.008-1mdv2008.0
- snapshot 20070516

* Thu May 03 2007 Pascal Terjan <pterjan@mandriva.org> 0.3.0.007-1mdv2008.0
+ Revision: 22053
- Fix build
- 0.3.0.007
- Use mkrel
- BuildREquires autoconf2.5


* Fri Mar 24 2006 Austin Acton <austin@mandriva.org> 0.3.0.006-0.20060323.1mdk
- new cvs checkout

* Fri Feb 17 2006 Austin Acton <austin@mandriva.org> 0.3.0.005-0.20060216.1mdk
- new cvs checkout

* Wed Jan 18 2006 Austin Acton <austin@mandriva.org> 0.3.0.005-0.20060117.1mdk
- new cvs checkout

* Thu Jan 12 2006 Austin Acton <austin@mandriva.org> 0.3.0.004-0.20060111.1mdk
- new cvs checkout

* Fri Nov 25 2005 Austin Acton <austin@mandriva.org> 0.3.0.004-0.20051124.1mdk
- new cvs checkout

* Wed Nov 09 2005 Austin Acton <austin@mandriva.org> 0.3.0.004-0.20051109.1mdk
- new cvs checkout

* Sat Nov 05 2005 Austin Acton <austin@mandriva.org> 0.3.0.004-0.20051104.1mdk
- new cvs checkout

* Thu Oct 06 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.3.0.004-0.20050904.2mdk
- Fix BuildRequires

* Mon Sep 05 2005 Austin Acton <austin@mandriva.org> 0.3.0.004-0.20050904.1mdk
- new cvs checkout

* Sun Aug 14 2005 Austin Acton <austin@mandriva.org> 0.3.0.004-0.20050813.1mdk
- new cvs checkout

* Mon Jun 27 2005 Austin Acton <austin@mandriva.org> 0.3.0.003-0.20050627.1mdk
- new cvs checkout

* Wed Jun 08 2005 Austin Acton <austin@mandriva.org> 0.3.0.003-0.20050608.1mdk
- new cvs checkout

* Wed May 25 2005 Austin Acton <austin@mandriva.org> 0.3.0.003-0.20050524.3mdk
- buildrequires

* Wed May 25 2005 Austin Acton <austin@mandriva.org> 0.3.0.003-0.20050524.2mdk
- multiarch binaries

* Wed May 25 2005 Austin Acton <austin@mandriva.org> 0.3.0.003-0.20050524.1mdk
- new cvs checkout

* Sun May 15 2005 Austin Acton <austin@mandriva.org> 0.3.0.003-0.20050511.2mdk
- clean spec

* Thu May 12 2005 Austin Acton <austin@mandriva.org> 0.3.0.003-0.20050511.1mdk
- initial package

