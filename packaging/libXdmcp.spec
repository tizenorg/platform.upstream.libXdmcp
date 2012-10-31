Name:           libXdmcp
Version:        1.1.1
Release:        1
License:        MIT
Summary:        X Display Manager Control Protocol library
Url:            http://www.x.org
Group:          System Environment/Libraries

Source:         %{name}-%{version}.tar.bz2

BuildRequires:  pkgconfig(xorg-macros)
BuildRequires:  pkgconfig(xproto)

%description
X Display Manager Control Protocol library.

%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}
Provides:       libxdmcp-devel

%description devel
libXdmcp development package.

%prep
%setup -q

%build
%reconfigure --disable-static \
           LDFLAGS="${LDFLAGS} -Wl,--hash-style=both -Wl,--as-needed"
make %{?_smp_mflags}

%install
%make_install

%remove_docs

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc COPYING 
%{_libdir}/libXdmcp.so.6
%{_libdir}/libXdmcp.so.6.0.0

%files devel
%defattr(-,root,root,-)
%{_includedir}/X11/Xdmcp.h
%{_libdir}/libXdmcp.so
%{_libdir}/pkgconfig/xdmcp.p
