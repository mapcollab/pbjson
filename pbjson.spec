Name: pbjson
Version: 1.0.0
Release: 1%{?dist}
Summary: pbjson library
Group: Development/Libraries
URL: http://www.thalesgroup.com/
Vendor: Thales Avionics, Inc.
License: BSD 3-clause
Packager: Builder <builder@thales-ktw.site>
Source: %{name}-%{version}.tar.gz

Requires:	systemd

%description
Shared pbjson library for converting GPB-JSON in C++

%define debug_package %{nil}

%package -n pbjson-devel
Summary:	Development headers for %{name}
Group:		Development/C
Requires:	%{name} = %{version}
%description -n pbjson-devel
Develpoments headers for pbjson.

%prep
%setup -q -n %{name}-%{version}

%build
make

%install
mkdir -p %{buildroot}/%{_libdir}/
mkdir -p %{buildroot}/%{_includedir}/
mkdir -p %{buildroot}/%{_includedir}/rapidjson
install -m755 *.so     %{buildroot}/%{_libdir}/
cp -afr src/pbjson.hpp         %{buildroot}/%{_includedir}/
cp -afr src/rapidjson/*        %{buildroot}/%{_includedir}/rapidjson

%files
%attr(0755,root,root) %{_libdir}/*.so

%files -n pbjson-devel
%defattr(0644,root,root,0755)
%{_includedir}/

%changelog
