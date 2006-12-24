Summary:	makedepend utility - create dependencies in makefiles
Summary(pl):	Narzêdzie makedepend - tworzenie zale¿no¶ci w makefile'ach
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

%description -l pl
Program makedepend czyta po kolei wszystkie pliki ¼ród³owe i analizuje
je tak, jak robi to preprocesor C, przetwarzaj±c wszystkie dyrektywy
"#include", "#define", "#undef", "#ifdef", "#ifndef", "#endif", "#if",
"#elif" aby móc stwierdziæ, które dyrektywy "#include" bêd± u¿yte
podczas kompilacji. Ka¿da dyrektywa "#include" mo¿e odnosiæ siê do
plików maj±cych kolejne dyrektywy "#include", a wtedy te pliki bêd±
tak¿e przeanalizowane.

Ka¿dy plik do³±czany przez plik ¼ród³owy, bezpo¶rednio lub po¶rednio,
jest nazywany przez makedepend zale¿no¶ci±. Zale¿no¶ci te s±
dopisywane do pliku makefile w taki sposób, aby program make wiedzia³,
które pliki wynikowe musz± byæ przekompilowane w przypadku zmiany
której¶ zale¿no¶ci.

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
