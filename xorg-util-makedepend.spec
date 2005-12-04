Summary:	makedepend utility
Summary(pl):	Narz�dzie makedepend
Name:		xorg-util-makedepend
Version:	0.99.3
Release:	0.1
License:	MIT
Group:		X11/Development/Tools
Source0:	http://xorg.freedesktop.org/releases/X11R7.0-RC3/util/makedepend-%{version}.tar.bz2
# Source0-md5:	2f94794b7d9ab2b829153223a79aeb18
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
Narz�dzie makedepend.

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
