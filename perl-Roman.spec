%include	/usr/lib/rpm/macros.perl
%define	pnam	Roman
Summary:	Perl module for conversion between Roman and Arabic numerals
Summary(pl):	Modu³ Perla do konwersji miêdzy liczbami rzymskimi a arabskimi
Name:		perl-%{pnam}
Version:	1.1
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pnam}/%{pnam}-%{version}.tar.gz
URL:		http://search.cpan.org/~ozawa/Roman-1.1/Roman.pm
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides some functions which help conversion of numeric
notation between Roman and Arabic.

%description -l pl
Pakiet udostêpnia kilka funkcji które pomagaj± w konwersji
numerycznych notacji pomiêdzy liczbami rzymskimi a arabskimi.

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
