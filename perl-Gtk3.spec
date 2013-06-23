#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Gtk3
Summary:	Perl interface to the 3.x series of the Gimp Toolkit library
Summary(pl.UTF-8):	Interfejs perlowy do wersji 3.x biblioteki Gimp Toolkit
Name:		perl-Gtk3
Version:	0.009
Release:	1
License:	LGPL v2.1+
Group:		Development/Languages/Perl
Source0:	http://downloads.sourceforge.net/gtk2-perl/%{pdir}-%{version}.tar.gz
# Source0-md5:	813ec7972a4f98019ca463f57b2d3c39
URL:		http://gtk2-perl.sourceforge.net/
BuildRequires:	perl-ExtUtils-MakeMaker >= 6.30
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.192
%if %{with tests}
BuildRequires:	perl-Cairo-GObject >= 1.000
BuildRequires:	perl-Glib >= 1.260
BuildRequires:	perl-Glib-Object-Introspection >= 0.014
%endif
# gdk-pixbuf2, gtk+3, pango with gobject-introspection bindings
Requires:	gdk-pixbuf2 >= 2.22
Requires:	gtk+3 >= 3.0.0
Requires:	pango >= 1:1.26
Requires:	perl-Cairo-GObject >= 1.000
Requires:	perl-Glib >= 1.260
Requires:	perl-Glib-Object-Introspection >= 0.014
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Gtk3 module allows a perl developer to use the GTK+ graphical user
interface library.

%description -l pl.UTF-8
Moduł Gtk3 pozwala programistom perlowym na używanie biblioteki
interfejsu graficznego GTK+.

%prep
%setup -q -n %{pdir}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS README
%{perl_vendorlib}/Gtk3.pm
%{_mandir}/man3/Gtk3.3pm*
