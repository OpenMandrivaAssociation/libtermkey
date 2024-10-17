#we only need major.minor in the SONAME in the stable (even numbered) series
#this should be changed to %%{version} in unstable (odd numbered) releases
%global sover 0.10

%define major 1
%define Basename_ termkey
%define oldlibname %mklibname %{Basename_} 1
%define libname %mklibname %{Basename_}
%define develname %mklibname %{Basename_} -d
%define staticdevelname %mklibname %{Basename_} -d -s

Name:		libtermkey
Version:	0.22
Release:	5
Summary:	Library for easy processing of keyboard entry
# the licensing breakdown is described in detail in the LICENSE file
License:	MIT and BSD and ISC
Group:		Development/C
URL:		https://www.leonerd.org.uk/code/libtermkey/
Source0:	http://www.leonerd.org.uk/code/libtermkey/%{name}-%{version}.tar.gz
# ****ing libtool is good for nothing and messes with crosscompiling.
# Let's just get rid of it!
Patch0:		libtermkey-0.22-libtool-die-die-die.patch
BuildRequires:	pkgconfig(ncurses)

%description
This library allows easy processing of keyboard entry from terminal-based
programs. It handles all the necessary logic to recognize special keys, UTF-8
combining, and so on, with a simple interface.

%package -n %{libname}
Summary: Library for easy processing of keyboard entry
%rename %{oldlibname}

%description -n %{libname}
This library allows easy processing of keyboard entry from terminal-based
programs. It handles all the necessary logic to recognize special keys, UTF-8
combining, and so on, with a simple interface.

%package -n %{develname}
Summary: Development libraries for libtermkey
Group: Development/C
Requires: %{libname} = %{version}-%{release}
Requires: pkgconfig

%description -n %{develname}
Development libraries for libtermkey

%prep
%autosetup -p1

sed -e '/^all:/s:$(DEMOS)::' -i Makefile

%build
%set_build_flags
%make_build PREFIX="%{_prefix}" LIBDIR="%{_libdir}"

%install
%make_install PREFIX="%{_prefix}" LIBDIR="%{_libdir}"

%files -n %{libname}
%{_libdir}/libtermkey.so.*

%files -n %{develname}
%{_libdir}/libtermkey.so
%{_libdir}/pkgconfig/termkey.pc
%{_includedir}/termkey*.h
%{_mandir}/man*/*
