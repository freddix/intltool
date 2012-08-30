%include	/usr/lib/rpm/macros.perl

Summary:	Utility scripts for internationalizing various kinds of data files
Name:		intltool
Version:	0.50.2
Release:	2
License:	GPL v2
Group:		Development/Tools
Source0:	http://edge.launchpad.net/intltool/trunk/0.50.2/+download/%{name}-%{version}.tar.gz
# Source0-md5:	23fbd879118253cb99aeac067da5f591
URL:		http://www.gnome.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	perl-XML-Parser
BuildRequires:	rpm-perlprov
Requires:	patch
# not detected automaticaly
Requires:	perl-XML-Parser
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Automatically extracts translatable strings from oaf, glade, bonobo
ui, nautilus theme and other files into the po files.

Automatically merges translations from po files back into .oaf files
(encoding to be 7-bit clean). I can also extend this merging mechanism
to support other types of files.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	aclocaldir=%{_aclocaldir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README TODO doc/I18N-HOWTO
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/intltool
%attr(755,root,root) %{_datadir}/intltool/*
%{_aclocaldir}/*.m4
%{_mandir}/man8/*.8*

