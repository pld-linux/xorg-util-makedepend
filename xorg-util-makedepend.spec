Summary:	makedepend utility - create dependencies in makefiles
Summary(pl.UTF-8):	Narzędzie makedepend - tworzenie zależności w makefile'ach
Name:		xorg-util-makedepend
Version:	1.0.0
Release:	1
License:	MIT
Group:		X11/Development/Tools
Source0:	http://xorg.freedesktop.org/releases/individual/util/makedepend-%{version}.tar.bz2
# Source0-md5:	fa194caa4f059f5621ed2c5a51efb4d0
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-proto-xproto-devel
BuildRequires:	xorg-util-util-macros >= 0.99.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The makedepend program reads each sourcefile in sequence and parses it
like a C-preprocessor, processing all "#include", "#define", "#undef",
"#ifdef", "#ifndef", "#endif", "#if", "#elif" and "#else" directives
so that it can correctly tell which #include directives would be used
in a compilation. Any "#include", directives can reference files
having other "#include" directives, and parsing will occur in these
files as well.

Every file that a sourcefile includes, directly or indirectly, is what
makedepend calls a dependency. These dependencies are then written to
a makefile in such a way that make will know which object files
must be recompiled when a dependency has changed.

%description -l pl.UTF-8
Program makedepend czyta po kolei wszystkie pliki źródłowe i analizuje
je tak, jak robi to preprocesor C, przetwarzając wszystkie dyrektywy
"#include", "#define", "#undef", "#ifdef", "#ifndef", "#endif", "#if",
"#elif" aby móc stwierdzić, które dyrektywy "#include" będą użyte
podczas kompilacji. Każda dyrektywa "#include" może odnosić się do
plików mających kolejne dyrektywy "#include", a wtedy te pliki będą
także przeanalizowane.

Każdy plik dołączany przez plik źródłowy, bezpośrednio lub pośrednio,
jest nazywany przez makedepend zależnością. Zależności te są
dopisywane do pliku makefile w taki sposób, aby program make wiedział,
które pliki wynikowe muszą być przekompilowane w przypadku zmiany
którejś zależności.

%prep
%setup -q -n makedepend-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog
%attr(755,root,root) %{_bindir}/makedepend
%{_mandir}/man1/makedepend.1x*
