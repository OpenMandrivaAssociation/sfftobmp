%define realver %(echo %version|sed -e 's#\\.#_#g')

Summary:	Tool to transform SFF files to BMP
Name:		sfftobmp
Version:	3.1.2
Release:	7
License:	MIT
Group:		Communications
URL:		https://sfftools.sourceforge.net/
Source0:	http://downloads.sourceforge.net/project/sfftools/%{name}/%{name}_%{realver}/%{name}%{realver}_src.zip
Patch0:		sfftobmp-3.1.1-gcc44-and-boost-1_37.patch
BuildRequires:	boost-devel
BuildRequires:	tiff-devel
BuildRequires:	jpeg-devel

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
export CXXFLAGS="%optflags  -DBOOST_FILESYSTEM_VERSION=2"
%configure2_5x
%make LIBS='-lboost_system'

%install
%makeinstall_std

%files
%doc doc/*
%{_bindir}/%{name}

