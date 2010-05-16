#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pnam	Roman
Summary:	Perl module for conversion between Roman and Arabic numerals
Summary(pl.UTF-8):	Moduł Perla do konwersji między liczbami rzymskimi a arabskimi
Name:		perl-Roman
Version:	1.23
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/C/CH/CHORNY/%{pnam}-%{version}.zip
# Source0-md5:	5a80a72a8ff4b1956b7f3258b24ab403
URL:		http://search.cpan.org/dist/Roman/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	unzip
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides some functions which help conversion of numeric
notation between Roman and Arabic.

%description -l pl.UTF-8
Pakiet udostępnia kilka funkcji które pomagają w konwersji
numerycznych notacji pomiędzy liczbami rzymskimi a arabskimi.

%prep
%setup -q -n %{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Roman.pm
%{_mandir}/man3/*
