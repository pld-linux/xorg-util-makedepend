Summary:	makedepend utility
Summary(pl):	Narzêdzie makedepend
Name:		xorg-util-makedepend
Version:	1.0.0
Release:	1
License:	MIT
Group:		X11/Development/Tools
# TODO: drop "-X11R7.0" from src name on upgrade
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
makedepend utility.

%description -l pl
Narzêdzie makedepend.

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
