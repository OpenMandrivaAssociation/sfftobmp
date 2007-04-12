Summary:	Tool to transform SFF files to BMP
Name:		sfftobmp
Version:	3.1
Release:	%mkrel 1
License:	MIT
Group:		Communications
URL:		http://sfftools.sourceforge.net/
Source0:	sfftobmp_3_1_src.tar.bz2
Patch0:		sfftobmp-3.0-errno.diff
BuildRequires:	libtool
BuildRequires:	autoconf2.5
BuildRequires:	automake1.7
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

%setup -q -n %{name}%{version}
%patch0 -p0

for i in `find . -type d -name CVS` `find . -type f -name .cvs\*` `find . -type f -name .#\*`; do
    if [ -e "$i" ]; then rm -rf $i; fi >&/dev/null
done

%build
export WANT_AUTOCONF_2_5=1
rm -f configure
libtoolize --copy --force && aclocal-1.7 && autoconf --force && autoheader

%configure2_5x

%make 

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc doc/*
%{_bindir}/%{name}


