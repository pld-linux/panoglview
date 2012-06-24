Summary:	OpenGL-based panorama viewer
Summary(pl):	Oparta na OpenGL-u przegl�darka panoram
Name:		panoglview
Version:	0.2.1
Release:	1
License:	GPL v2+
Group:		Applications/Graphics
Source0:	http://dl.sourceforge.net/hugin/%{name}-%{version}.tar.gz
# Source0-md5:	0acb180b81997aa8c08d03ff9dfd2437
Patch0:		%{name}-link.patch
URL:		http://hugin.sourceforge.net/
BuildRequires:	OpenGL-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool >= 2:1.5
#BuildRequires:	tuvista-devel (for plugin) - ??? found only tuvionlib and vistalab
BuildRequires:	wxGTK2-gl-devel >= 2.6.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OpenGL-based panorama viewer.

%description -l pl
Oparta na OpenGL-u przegl�darka panoram.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	WX_CONFIG_NAME=wx-gtk2-ansi-config
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog
%attr(755,root,root) %{_bindir}/panoglview
