%include	/usr/lib/rpm/macros.perl
%define		pnam	Roman
Summary:	Perl module for conversion between Roman and Arabic numerals
Summary(pl.UTF-8):   Moduł Perla do konwersji między liczbami rzymskimi a arabskimi
Name:		perl-%{pnam}
Version:	1.1
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pnam}/%{pnam}-%{version}.tar.gz
# Source0-md5:	67b0e6affdc50fdf28cfc438c045fd9b
URL:		http://search.cpan.org/~ozawa/Roman-1.1/Roman.pm
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
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

%install
rm -rf $RPM_BUILD_ROOT
install -D %{pnam}.pm $RPM_BUILD_ROOT%{perl_vendorlib}/%{pnam}.pm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorlib}/%{pnam}.pm
