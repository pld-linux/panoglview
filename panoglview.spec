Summary:	OpenGL-based panorama viewer
Summary(pl):	Oparta na OpenGL-u przegl±darka panoram
Name:		panoglview
Version:	0.2
Release:	1
License:	GPL v2+
Group:		Applications/Graphics
Source0:	http://dl.sourceforge.net/hugin/%{name}-%{version}.tar.gz
# Source0-md5:	8e8f391ed85d8def1d06f87a84f65167
URL:		http://hugin.sourceforge.net/
BuildRequires:	OpenGL-devel
BuildRequires:	sed >= 4.0
#BuildRequires:	tuvista-devel (for plugin) - ??? found only tuvionlib and vistalab
BuildRequires:	wxGTK2-devel >= 2.6.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OpenGL-based panorama viewer.

%description -l pl
Oparta na OpenGL-u przegl±darka panoram.

%prep
%setup -q

sed -i -e 's/wx-config/wx-gtk2-ansi-config/g' configure

%build
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
%doc AUTHORS ChangeLog
%attr(755,root,root) %{_bindir}/panoglview
