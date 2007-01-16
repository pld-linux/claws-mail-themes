Summary:	Themes for Claws-Mail (metapackage)
Summary(pl):	Motywy dla programu Claws-Mail (metapakiet)
Name:		claws-mail-themes
Version:	20070116
Release:	1
License:	GPL
Group:		Themes
Source0:	http://dl.sourceforge.net/sylpheed-claws/%{name}-%{version}.tar.bz2
# Source0-md5:	f75f14fac8927671aa0a17d896347035
URL:		http://www.claws-mail.net/themes.php
Requires:	claws-mail-theme-Achileus-noname = %{version}-%{release}
Requires:	claws-mail-theme-Black = %{version}-%{release}
Requires:	claws-mail-theme-Blue_Anarchy = %{version}-%{release}
Requires:	claws-mail-theme-Clawsola = %{version}-%{release}
Requires:	claws-mail-theme-Crystal = %{version}-%{release}
Requires:	claws-mail-theme-Everaldo_Kids = %{version}-%{release}
Requires:	claws-mail-theme-Gnomaws = %{version}-%{release}
Requires:	claws-mail-theme-Gnomeria = %{version}-%{release}
Requires:	claws-mail-theme-Gorillaws = %{version}-%{release}
Requires:	claws-mail-theme-Graphitte = %{version}-%{release}
Requires:	claws-mail-theme-GurUnix = %{version}-%{release}
Requires:	claws-mail-theme-Korillaws = %{version}-%{release}
Requires:	claws-mail-theme-Kovico = %{version}-%{release}
Requires:	claws-mail-theme-Logos = %{version}-%{release}
Requires:	claws-mail-theme-Mongrel = %{version}-%{release}
Requires:	claws-mail-theme-Mongrel2 = %{version}-%{release}
Requires:	claws-mail-theme-Mozilla = %{version}-%{release}
Requires:	claws-mail-theme-New_Session = %{version}-%{release}
Requires:	claws-mail-theme-OldDark = %{version}-%{release}
Requires:	claws-mail-theme-Orbit-Claws = %{version}-%{release}
Requires:	claws-mail-theme-Phoenity = %{version}-%{release}
Requires:	claws-mail-theme-Plain_and_Bluish = %{version}-%{release}
Requires:	claws-mail-theme-STW = %{version}-%{release}
Requires:	claws-mail-theme-Skypilot-Clawssic = %{version}-%{release}
Requires:	claws-mail-theme-SylZilla = %{version}-%{release}
Requires:	claws-mail-theme-Sylpholution = %{version}-%{release}
Requires:	claws-mail-theme-TangoClaws = %{version}-%{release}
Requires:	claws-mail-theme-XeNtish = %{version}-%{release}
Requires:	claws-mail-theme-tml02c = %{version}-%{release}
Requires:	claws-mail-theme-tom2 = %{version}-%{release}
Provides:	sylpheed-claws-themes = %{version}
Obsoletes:	sylpheed-claws-themes
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_themesdir	%{_datadir}/claws-mail/themes

%description
Themes for Claws-Mail (metapackage).

%description -l pl
Motywy dla programu Claws-Mail (metapakiet).

%package -n claws-mail-theme-Achileus-noname
Summary:	Achileus-noname theme for Claws-Mail
Summary(pl):	Motyw Achileus-noname dla Claws-Mail
Group:		Themes
Requires:	claws-mail
Provides:	sylpheed-claws-theme-Achileus-noname
Obsoletes:	sylpheed-claws-theme-Achileus-noname
Conflicts:	sylpheed-claws-themes <= 2.3.0-1

%description -n claws-mail-theme-Achileus-noname
Achileus-noname theme for Claws-Mail.

%description -n claws-mail-theme-Achileus-noname -l pl
Motyw Achileus-noname dla Claws-Mail.

%package -n claws-mail-theme-Black
Summary:	Black theme for Claws-Mail
Summary(pl):	Motyw Black dla Claws-Mail
Group:		Themes
Requires:	claws-mail
Provides:	sylpheed-claws-theme-Black
Obsoletes:	sylpheed-claws-theme-Black
Conflicts:	sylpheed-claws-themes <= 2.3.0-1

%description -n claws-mail-theme-Black
Black theme for Claws-Mail.

%description -n claws-mail-theme-Black -l pl
Motyw Black dla Claws-Mail.

%package -n claws-mail-theme-Blue_Anarchy
Summary:	Blue Anarchy theme for Claws-Mail
Summary(pl):	Motyw Blue Anarchy dla Claws-Mail
Group:		Themes
Requires:	claws-mail
Provides:	sylpheed-claws-theme-Blue_Anarchy
Obsoletes:	sylpheed-claws-theme-Blue_Anarchy
Conflicts:	sylpheed-claws-themes <= 2.3.0-1

%description -n claws-mail-theme-Blue_Anarchy
Blue Anarchy theme for Claws-Mail.

%description -n claws-mail-theme-Blue_Anarchy -l pl
Motyw Blue Anarchy dla Claws-Mail.

%package -n claws-mail-theme-Clawsola
Summary:	Clawsola theme for Claws-Mail
Summary(pl):	Motyw Clawsola dla Claws-Mail
Group:		Themes
Requires:	claws-mail
Provides:	sylpheed-claws-theme-Clawsola
Obsoletes:	sylpheed-claws-theme-Clawsola
Conflicts:	sylpheed-claws-themes <= 2.3.0-1

%description -n claws-mail-theme-Clawsola
Clawsola theme for Claws-Mail.

%description -n claws-mail-theme-Clawsola -l pl
Motyw Clawsola dla Claws-Mail.

%package -n claws-mail-theme-Crystal
Summary:	Crystal theme for Claws-Mail
Summary(pl):	Motyw Crystal dla Claws-Mail
Group:		Themes
Requires:	claws-mail
Provides:	sylpheed-claws-theme-Crystal
Obsoletes:	sylpheed-claws-theme-Crystal
Conflicts:	sylpheed-claws-themes <= 2.3.0-1

%description -n claws-mail-theme-Crystal
Crystal theme for Claws-Mail.

%description -n claws-mail-theme-Crystal -l pl
Motyw Crystal dla Claws-Mail.

%package -n claws-mail-theme-Everaldo_Kids
Summary:	Everaldo Kids theme for Claws-Mail
Summary(pl):	Motyw Everaldo Kids dla Claws-Mail
Group:		Themes
Requires:	claws-mail
Provides:	sylpheed-claws-theme-Everaldo_Kids
Obsoletes:	sylpheed-claws-theme-Everaldo_Kids
Conflicts:	sylpheed-claws-themes <= 2.3.0-1

%description -n	claws-mail-theme-Everaldo_Kids
Everaldo Kids theme for Claws-Mail.

%description -n claws-mail-theme-Everaldo_Kids -l pl
Motyw Everaldo Kids dla Claws-Mail.

%package -n claws-mail-theme-Gnomaws
Summary:	Gnomaws theme for Claws-Mail
Summary(pl):	Motyw Gnomaws dla Claws-Mail
Group:		Themes
Requires:	claws-mail
Provides:	sylpheed-claws-theme-Gnomaws
Obsoletes:	sylpheed-claws-theme-Gnomaws
Conflicts:	sylpheed-claws-themes <= 2.3.0-1

%description -n claws-mail-theme-Gnomaws
Gnomaws theme for Claws-Mail.

%description -n claws-mail-theme-Gnomaws -l pl
Motyw Gnomaws dla Claws-Mail.

%package -n claws-mail-theme-Gnomeria
Summary:	Gnomeria theme for Claws-Mail
Summary(pl):	Motyw Gnomeria dla Claws-Mail
Group:		Themes
Requires:	claws-mail
Provides:	sylpheed-claws-theme-Gnomeria
Obsoletes:	sylpheed-claws-theme-Gnomeria
Conflicts:	sylpheed-claws-themes <= 2.3.0-1

%description -n claws-mail-theme-Gnomeria
Gnomeria theme for Claws-Mail.

%description -n claws-mail-theme-Gnomeria -l pl
Motyw Gnomeria dla Claws-Mail.

%package -n claws-mail-theme-Gorillaws
Summary:	Gorillaws theme for Claws-Mail
Summary(pl):	Motyw Gorillaws dla Claws-Mail
Group:		Themes
Requires:	claws-mail
Provides:	sylpheed-claws-theme-Gorillaws
Obsoletes:	sylpheed-claws-theme-Gorillaws
Conflicts:	sylpheed-claws-themes <= 2.3.0-1

%description -n claws-mail-theme-Gorillaws
Gorillaws theme for Claws-Mail.

%description -n claws-mail-theme-Gorillaws -l pl
Motyw Gorillaws dla Claws-Mail.

%package -n claws-mail-theme-Graphitte
Summary:	Graphitte theme for Claws-Mail
Summary(pl):	Motyw Graphitte dla Claws-Mail
Group:		Themes
Requires:	claws-mail
Provides:	sylpheed-claws-theme-Graphitte
Obsoletes:	sylpheed-claws-theme-Graphitte
Conflicts:	sylpheed-claws-themes <= 2.3.0-1

%description -n claws-mail-theme-Graphitte
Graphitte theme for Claws-Mail.

%description -n claws-mail-theme-Graphitte -l pl
Motyw Graphitte dla Claws-Mail.

%package -n claws-mail-theme-GurUnix
Summary:	GurUnix theme for Claws-Mail
Summary(pl):	Motyw GurUnix dla Claws-Mail
Group:		Themes
Requires:	claws-mail
Provides:	sylpheed-claws-theme-GurUnix
Obsoletes:	sylpheed-claws-theme-GurUnix
Conflicts:	sylpheed-claws-themes <= 2.3.0-1

%description -n claws-mail-theme-GurUnix
GurUnix theme for Claws-Mail.

%description -n claws-mail-theme-GurUnix -l pl
Motyw GurUnix dla Claws-Mail.

%package -n claws-mail-theme-Korillaws
Summary:	Korillaws theme for Claws-Mail
Summary(pl):	Motyw Korillaws dla Claws-Mail
Group:		Themes
Requires:	claws-mail
Provides:	sylpheed-claws-theme-Korillaws
Obsoletes:	sylpheed-claws-theme-Korillaws
Conflicts:	sylpheed-claws-themes <= 2.3.0-1

%description -n claws-mail-theme-Korillaws
Korillaws theme for Claws-Mail.

%description -n claws-mail-theme-Korillaws -l pl
Motyw Korillaws dla Claws-Mail.

%package -n claws-mail-theme-Kovico
Summary:	Kovico theme for Claws-Mail
Summary(pl):	Motyw Kovico dla Claws-Mail
Group:		Themes
Requires:	claws-mail
Provides:	sylpheed-claws-theme-Kovico
Obsoletes:	sylpheed-claws-theme-Kovico
Conflicts:	sylpheed-claws-themes <= 2.3.0-1

%description -n claws-mail-theme-Kovico
Kovico theme for Claws-Mail.

%description -n claws-mail-theme-Kovico -l pl
Motyw Kovico dla Claws-Mail.

%package -n claws-mail-theme-Logos
Summary:	Logos theme for Claws-Mail
Summary(pl):	Motyw Logos dla Claws-Mail
Group:		Themes
Requires:	claws-mail
Provides:	sylpheed-claws-theme-Logos
Obsoletes:	sylpheed-claws-theme-Logos
Conflicts:	sylpheed-claws-themes <= 2.3.0-1

%description -n claws-mail-theme-Logos
Logos theme for Claws-Mail.

%description -n claws-mail-theme-Logos -l pl
Motyw Logos dla Claws-Mail.

%package -n claws-mail-theme-Mongrel
Summary:	Mongrel theme for Claws-Mail
Summary(pl):	Motyw Mongrel dla Claws-Mail
Group:		Themes
Requires:	claws-mail
Provides:	sylpheed-claws-theme-Mongrel
Obsoletes:	sylpheed-claws-theme-Mongrel
Conflicts:	sylpheed-claws-themes <= 2.3.0-1

%description -n claws-mail-theme-Mongrel
Mongrel theme for Claws-Mail.

%description -n claws-mail-theme-Mongrel -l pl
Motyw Mongrel dla Claws-Mail.

%package -n claws-mail-theme-Mongrel2
Summary:	Mongrel2 theme for Claws-Mail
Summary(pl):	Motyw Mongrel2 dla Claws-Mail
Group:		Themes
Requires:	claws-mail
Provides:	sylpheed-claws-theme-Mongrel2
Obsoletes:	sylpheed-claws-theme-Mongrel2
Conflicts:	sylpheed-claws-themes <= 2.3.0-1

%description -n claws-mail-theme-Mongrel2
Mongrel2 theme for Claws-Mail.

%description -n claws-mail-theme-Mongrel2 -l pl
Motyw Mongrel2 dla Claws-Mail.

%package -n claws-mail-theme-Mozilla
Summary:	Mozilla theme for Claws-Mail
Summary(pl):	Motyw Mozilla dla Claws-Mail
Group:		Themes
Requires:	claws-mail
Provides:	sylpheed-claws-theme-Mozilla
Obsoletes:	sylpheed-claws-theme-Mozilla
Conflicts:	sylpheed-claws-themes <= 2.3.0-1

%description -n claws-mail-theme-Mozilla
Mozilla theme for Claws-Mail.

%description -n claws-mail-theme-Mozilla -l pl
Motyw Mozilla dla Claws-Mail.

%package -n claws-mail-theme-New_Session
Summary:	New Session theme for Claws-Mail
Summary(pl):	Motyw New Session dla Claws-Mail
Group:		Themes
Requires:	claws-mail
Provides:	sylpheed-claws-theme-New_Session
Obsoletes:	sylpheed-claws-theme-New_Session
Conflicts:	sylpheed-claws-themes <= 2.3.0-1

%description -n	claws-mail-theme-New_Session
New Session theme for Claws-Mail.

%description -n claws-mail-theme-New_Session -l pl
Motyw New Session dla Claws-Mail.

%package -n claws-mail-theme-OldDark
Summary:	OldDark theme for Claws-Mail
Summary(pl):	Motyw OldDark dla Claws-Mail
Group:		Themes
Requires:	claws-mail
Provides:	sylpheed-claws-theme-OldDark
Obsoletes:	sylpheed-claws-theme-OldDark
Conflicts:	sylpheed-claws-themes <= 2.3.0-1

%description -n claws-mail-theme-OldDark
OldDark theme for Claws-Mail.

%description -n claws-mail-theme-OldDark -l pl
Motyw OldDark dla Claws-Mail.

%package -n claws-mail-theme-Orbit-Claws
Summary:	Orbit-Claws theme for Claws-Mail
Summary(pl):	Motyw Orbit-Claws dla Claws-Mail
Group:		Themes
Requires:	claws-mail
Provides:	sylpheed-claws-theme-Orbit-Claws
Obsoletes:	sylpheed-claws-theme-Orbit-Claws
Conflicts:	sylpheed-claws-themes <= 2.3.0-1

%description -n claws-mail-theme-Orbit-Claws
Orbit-Claws theme for Claws-Mail.

%description -n claws-mail-theme-Orbit-Claws -l pl
Motyw Orbit-Claws dla Claws-Mail.

%package -n claws-mail-theme-Phoenity
Summary:	Phoenity theme for Claws-Mail
Summary(pl):	Motyw Phoenity dla Claws-Mail
Group:		Themes
Requires:	claws-mail
Provides:	sylpheed-claws-theme-Phoenity
Obsoletes:	sylpheed-claws-theme-Phoenity
Conflicts:	sylpheed-claws-themes <= 2.3.0-1

%description -n claws-mail-theme-Phoenity
Phoenity theme for Claws-Mail.

%description -n claws-mail-theme-Phoenity -l pl
Motyw Phoenity dla Claws-Mail.

%package -n claws-mail-theme-Plain_and_Bluish
Summary:	Plain and Bluish theme for Claws-Mail
Summary(pl):	Motyw Plain and Bluish dla Claws-Mail
Group:		Themes
Requires:	claws-mail
Provides:	sylpheed-claws-theme-Plain_and_Bluish
Obsoletes:	sylpheed-claws-theme-Plain_and_Bluish
Conflicts:	sylpheed-claws-themes <= 2.3.0-1

%description -n claws-mail-theme-Plain_and_Bluish
Plain and Bluish theme for Claws-Mail.

%description -n claws-mail-theme-Plain_and_Bluish -l pl
Motyw Plain and Bluish dla Claws-Mail.

%package -n claws-mail-theme-STW
Summary:	STW theme for Claws-Mail
Summary(pl):	Motyw STW dla Claws-Mail
Group:		Themes
Requires:	claws-mail
Provides:	sylpheed-claws-theme-STW
Obsoletes:	sylpheed-claws-theme-STW
Conflicts:	sylpheed-claws-themes <= 2.3.0-1

%description -n claws-mail-theme-STW
STW theme for Claws-Mail.

%description -n claws-mail-theme-STW -l pl
Motyw STW dla Claws-Mail.

%package -n claws-mail-theme-Skypilot-Clawssic
Summary:	Skypilot-Clawssic theme for Claws-Mail
Summary(pl):	Motyw Skypilot-Clawssic dla Claws-Mail
Group:		Themes
Requires:	claws-mail
Provides:	sylpheed-claws-theme-Skypilot-Clawssic
Obsoletes:	sylpheed-claws-theme-Skypilot-Clawssic
Conflicts:	sylpheed-claws-themes <= 2.3.0-1

%description -n claws-mail-theme-Skypilot-Clawssic
Skypilot-Clawssic theme for Claws-Mail.

%description -n claws-mail-theme-Skypilot-Clawssic -l pl
Motyw Skypilot-Clawssic dla Claws-Mail.

%package -n claws-mail-theme-Sylpholution
Summary:	Sylpholution theme for Claws-Mail
Summary(pl):	Motyw Sylpholution dla Claws-Mail
Group:		Themes
Requires:	claws-mail
Provides:	sylpheed-claws-theme-Sylpholution
Obsoletes:	sylpheed-claws-theme-Sylpholution
Conflicts:	sylpheed-claws-themes <= 2.3.0-1

%description -n claws-mail-theme-Sylpholution
Sylpholution theme for Claws-Mail.

%description -n claws-mail-theme-Sylpholution -l pl
Motyw Sylpholution dla Claws-Mail.

%package -n claws-mail-theme-SylZilla
Summary:	SylZilla theme for Claws-Mail
Summary(pl):	Motyw SylZilla dla Claws-Mail
Group:		Themes
Requires:	claws-mail
Provides:	sylpheed-claws-theme-SylZilla
Obsoletes:	sylpheed-claws-theme-SylZilla
Conflicts:	sylpheed-claws-themes <= 2.3.0-1

%description -n claws-mail-theme-SylZilla
SylZilla theme for Claws-Mail.

%description -n claws-mail-theme-SylZilla -l pl
Motyw SylZilla dla Claws-Mail.

%package -n claws-mail-theme-TangoClaws
Summary:	TangoClaws theme for Claws-Mail
Summary(pl):	Motyw TangoClaws dla Claws-Mail
Group:		Themes
Requires:	claws-mail
Provides:	sylpheed-claws-theme-TangoClaws
Obsoletes:	sylpheed-claws-theme-TangoClaws
Conflicts:	sylpheed-claws-themes <= 2.3.0-1

%description -n claws-mail-theme-TangoClaws
TangoClaws theme for Claws-Mail.

%description -n claws-mail-theme-TangoClaws -l pl
Motyw TangoClaws dla Claws-Mail.

%package -n claws-mail-theme-XeNtish
Summary:	XeNtish theme for Claws-Mail
Summary(pl):	Motyw XeNtish dla Claws-Mail
Group:		Themes
Requires:	claws-mail
Provides:	sylpheed-claws-theme-XeNtish
Obsoletes:	sylpheed-claws-theme-XeNtish
Conflicts:	sylpheed-claws-themes <= 2.3.0-1

%description -n claws-mail-theme-XeNtish
XeNtish theme for Claws-Mail.

%description -n claws-mail-theme-XeNtish -l pl
Motyw XeNtish dla Claws-Mail.

%package -n claws-mail-theme-tml02c
Summary:	tml02c theme for Claws-Mail
Summary(pl):	Motyw tml02c dla Claws-Mail
Group:		Themes
Requires:	claws-mail
Provides:	sylpheed-claws-theme-tml02c
Obsoletes:	sylpheed-claws-theme-tml02c
Conflicts:	sylpheed-claws-themes <= 2.3.0-1

%description -n claws-mail-theme-tml02c
tml02c theme for Claws-Mail.

%description -n claws-mail-theme-tml02c -l pl
Motyw tml02c dla Claws-Mail.

%package -n claws-mail-theme-tom2
Summary:	tom2 theme for Claws-Mail
Summary(pl):	Motyw tom2 dla Claws-Mail
Group:		Themes
Requires:	claws-mail
Provides:	sylpheed-claws-theme-tom2
Obsoletes:	sylpheed-claws-theme-tom2
Conflicts:	sylpheed-claws-themes <= 2.3.0-1

%description -n	claws-mail-theme-tom2
tom2 theme for Claws-Mail.

%description -n claws-mail-theme-tom2 -l pl
Motyw tom2 dla Claws-Mail.

%prep
%setup -q

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

%files -n claws-mail-theme-Achileus-noname
%defattr(644,root,root,755)
%{_themesdir}/achileus-noname

%files -n claws-mail-theme-Black
%defattr(644,root,root,755)
%doc black/README
%{_themesdir}/black

%files -n claws-mail-theme-Blue_Anarchy
%defattr(644,root,root,755)
%doc blue_anarchy/README
%{_themesdir}/blue_anarchy

%files -n claws-mail-theme-Clawsola
%defattr(644,root,root,755)
%doc clawsola/{ChangeLog,README}
%{_themesdir}/clawsola

%files -n claws-mail-theme-Crystal
%defattr(644,root,root,755)
%{_themesdir}/Crystal

%files -n claws-mail-theme-Everaldo_Kids
%defattr(644,root,root,755)
%doc Everaldo_Kids/README
%{_themesdir}/Everaldo_Kids

%files -n claws-mail-theme-Gnomaws
%defattr(644,root,root,755)
%doc Gnomaws-*/{ChangeLog,README}
%{_themesdir}/Gnomaws-*

%files -n claws-mail-theme-Gnomeria
%defattr(644,root,root,755)
%doc Gnomeria/README
%{_themesdir}/Gnomeria

%files -n claws-mail-theme-Gorillaws
%defattr(644,root,root,755)
%doc Gorillaws/{ChangeLog,README}
%{_themesdir}/Gorillaws

%files -n claws-mail-theme-Graphitte
%defattr(644,root,root,755)
%doc Graphitte-*/README
%{_themesdir}/Graphitte-*

%files -n claws-mail-theme-GurUnix
%defattr(644,root,root,755)
%doc GurUnix/{ChangeLog,README}
%{_themesdir}/GurUnix

%files -n claws-mail-theme-Korillaws
%defattr(644,root,root,755)
%doc Korillaws/{ChangeLog,README}
%{_themesdir}/Korillaws

%files -n claws-mail-theme-Kovico
%defattr(644,root,root,755)
%{_themesdir}/Kovico-claws

%files -n claws-mail-theme-Logos
%defattr(644,root,root,755)
%{_themesdir}/Logos-*

%files -n claws-mail-theme-Mongrel
%defattr(644,root,root,755)
%{_themesdir}/mongrel

%files -n claws-mail-theme-Mongrel2
%defattr(644,root,root,755)
%{_themesdir}/mongrel2

%files -n claws-mail-theme-Mozilla
%defattr(644,root,root,755)
%doc mozilla/README
%{_themesdir}/mozilla

%files -n claws-mail-theme-New_Session
%defattr(644,root,root,755)
%{_themesdir}/New_Session

%files -n claws-mail-theme-OldDark
%defattr(644,root,root,755)
%{_themesdir}/Old_Dark_Theme

%files -n claws-mail-theme-Orbit-Claws
%defattr(644,root,root,755)
%doc orbit-claws/README
%{_themesdir}/orbit-claws

%files -n claws-mail-theme-Phoenity
%defattr(644,root,root,755)
%doc Phoenity/readme.txt
%{_themesdir}/Phoenity

%files -n claws-mail-theme-Plain_and_Bluish
%defattr(644,root,root,755)
%{_themesdir}/Plain_and_Bluish

%files -n claws-mail-theme-STW
%defattr(644,root,root,755)
%{_themesdir}/stw

%files -n claws-mail-theme-Skypilot-Clawssic
%defattr(644,root,root,755)
%doc Skypilot_Clawssic/README
%{_themesdir}/Skypilot_Clawssic

%files -n claws-mail-theme-Sylpholution
%defattr(644,root,root,755)
%doc Sylpholution/ChangeLog*
%{_themesdir}/Sylpholution

%files -n claws-mail-theme-SylZilla
%defattr(644,root,root,755)
%doc SylZilla/{ChangeLog,README}
%{_themesdir}/SylZilla

%files -n claws-mail-theme-TangoClaws
%defattr(644,root,root,755)
%doc TangoClaws-*/README
%{_themesdir}/TangoClaws-*

%files -n claws-mail-theme-XeNtish
%defattr(644,root,root,755)
%doc XeNtish/README
%{_themesdir}/XeNtish

%files -n claws-mail-theme-tml02c
%defattr(644,root,root,755)
%{_themesdir}/tml02c

%files -n claws-mail-theme-tom2
%defattr(644,root,root,755)
%doc tom_*/README
%{_themesdir}/tom_*
