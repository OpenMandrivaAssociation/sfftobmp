%define version 3.1.2
%define realver %(echo %version|sed -e 's#\\.#_#g')

Summary:	Tool to transform SFF files to BMP
Name:		sfftobmp
Version:	%version
Release:	%mkrel 6
License:	MIT
Group:		Communications
URL:		http://sfftools.sourceforge.net/
Source0:	http://downloads.sourceforge.net/project/sfftools/%{name}/%{name}_%{realver}/%{name}%{realver}_src.zip
Patch0:		sfftobmp-3.1.1-gcc44-and-boost-1_37.patch
BuildRequires:	boost-devel
BuildRequires:	libtiff-devel
BuildRequires:	jpeg-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
SffToBmp is a converter tool, written in C++, to transform SFF files to BMP,
JPEG or multipage TIFF format.
In addition generation of PBM files (Portable Bitmap) is also possible which
can be transformed into nearby any other graphics format using the PBMPLUS
tools that are included in almost every Linux distribution nowadays.

%prep
%setup -q -n %{name}%{realver}
%patch0 -p1

%build
%configure2_5x
%make 

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}
%makeinstall_std

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc doc/*
%{_bindir}/%{name}


