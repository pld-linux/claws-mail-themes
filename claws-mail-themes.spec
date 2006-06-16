Summary:	Themes for Sylpheed-Claws (metapackage)
Summary(pl):	Motywy dla programu Sylpheed-Claws (metapakiet)
Name:		sylpheed-claws-themes
Version:	20060615
Release:	1
License:	GPL
Group:		Themes
Source0:	http://dl.sourceforge.net/sylpheed-claws/%{name}-%{version}.tar.bz2
# Source0-md5:	0c60eb6302f097fe3fec769ade7c8e9d
URL:		http://www.sylpheed-claws.net/themes.php
Requires:	sylpheed-claws-theme-Achileus-noname
Requires:	sylpheed-claws-theme-Black
Requires:	sylpheed-claws-theme-Blue_Anarchy
Requires:	sylpheed-claws-theme-Clawsola
Requires:	sylpheed-claws-theme-Crystal
Requires:	sylpheed-claws-theme-Everaldo_Kids
Requires:	sylpheed-claws-theme-Gnomaws
Requires:	sylpheed-claws-theme-Gnomeria
Requires:	sylpheed-claws-theme-Gorillaws
Requires:	sylpheed-claws-theme-Graphitte
Requires:	sylpheed-claws-theme-GurUnix
Requires:	sylpheed-claws-theme-Korillaws
Requires:	sylpheed-claws-theme-Kovico
Requires:	sylpheed-claws-theme-Logos
Requires:	sylpheed-claws-theme-Mongrel
Requires:	sylpheed-claws-theme-Mongrel2
Requires:	sylpheed-claws-theme-Mozilla
Requires:	sylpheed-claws-theme-New_Session
Requires:	sylpheed-claws-theme-OldDark
Requires:	sylpheed-claws-theme-Orbit-Claws
Requires:	sylpheed-claws-theme-Phoenity
Requires:	sylpheed-claws-theme-Plain_and_Bluish
Requires:	sylpheed-claws-theme-STW
Requires:	sylpheed-claws-theme-Skypilot-Clawssic
Requires:	sylpheed-claws-theme-Sylpholution
Requires:	sylpheed-claws-theme-SylZilla
Requires:	sylpheed-claws-theme-TangoClaws
Requires:	sylpheed-claws-theme-XeNtish
Requires:	sylpheed-claws-theme-tml02c
Requires:	sylpheed-claws-theme-tom2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_themesdir	%{_datadir}/sylpheed-claws/themes

%description
Themes for Sylpheed-Claws (metapackage).

%description -l pl
Motywy dla programu Sylpheed-Claws (metapakiet).

%package -n sylpheed-claws-theme-Achileus-noname
Summary:	Achileus-noname theme for Sylpheed-Claws
Summary(pl):	Motyw Achileus-noname dla Sylpheed-Claws
Group:		Themes
Requires:	sylpheed-claws
Conflicts:	sylpheed-claws-themes <= 2.3.0-1

%description -n sylpheed-claws-theme-Achileus-noname
Achileus-noname theme for Sylpheed-Claws.

%description -n sylpheed-claws-theme-Achileus-noname -l pl
Motyw Achileus-noname dla Sylpheed-Claws.

%package -n sylpheed-claws-theme-Black
Summary:	Black theme for Sylpheed-Claws
Summary(pl):	Motyw Black dla Sylpheed-Claws
Group:		Themes
Requires:       sylpheed-claws
Conflicts:      sylpheed-claws-themes <= 2.3.0-1

%description -n sylpheed-claws-theme-Black
Black theme for Sylpheed-Claws.

%description -n sylpheed-claws-theme-Black -l pl
Motyw Black dla Sylpheed-Claws.

%package -n sylpheed-claws-theme-Blue_Anarchy
Summary:	Blue Anarchy theme for Sylpheed-Claws
Summary(pl):	Motyw Blue Anarchy dla Sylpheed-Claws
Group:		Themes
Requires:       sylpheed-claws
Conflicts:      sylpheed-claws-themes <= 2.3.0-1

%description -n sylpheed-claws-theme-Blue_Anarchy
Blue Anarchy theme for Sylpheed-Claws.

%description -n sylpheed-claws-theme-Blue_Anarchy -l pl
Motyw Blue Anarchy dla Sylpheed-Claws.

%package -n sylpheed-claws-theme-Clawsola
Summary:	Clawsola theme for Sylpheed-Claws
Summary(pl):	Motyw Clawsola dla Sylpheed-Claws
Group:		Themes
Requires:       sylpheed-claws
Conflicts:      sylpheed-claws-themes <= 2.3.0-1

%description -n sylpheed-claws-theme-Clawsola
Clawsola theme for Sylpheed-Claws.

%description -n sylpheed-claws-theme-Clawsola -l pl
Motyw Clawsola dla Sylpheed-Claws.

%package -n sylpheed-claws-theme-Crystal
Summary:	Crystal theme for Sylpheed-Claws
Summary(pl):	Motyw Crystal dla Sylpheed-Claws
Group:		Themes
Requires:       sylpheed-claws
Conflicts:      sylpheed-claws-themes <= 2.3.0-1

%description -n sylpheed-claws-theme-Crystal
Crystal theme for Sylpheed-Claws.

%description -n sylpheed-claws-theme-Crystal -l pl
Motyw Crystal dla Sylpheed-Claws.

%package -n sylpheed-claws-theme-Everaldo_Kids
Summary:	Everaldo Kids theme for Sylpheed-Claws
Summary(pl):	Motyw Everaldo Kids dla Sylpheed-Claws
Group:		Themes
Requires:       sylpheed-claws
Conflicts:      sylpheed-claws-themes <= 2.3.0-1

%description -n	sylpheed-claws-theme-Everaldo_Kids
Everaldo Kids theme for Sylpheed-Claws.

%description -n sylpheed-claws-theme-Everaldo_Kids -l pl
Motyw Everaldo Kids dla Sylpheed-Claws.

%package -n sylpheed-claws-theme-Gnomaws
Summary:	Gnomaws theme for Sylpheed-Claws
Summary(pl):	Motyw Gnomaws dla Sylpheed-Claws
Group:		Themes
Requires:       sylpheed-claws
Conflicts:      sylpheed-claws-themes <= 2.3.0-1

%description -n sylpheed-claws-theme-Gnomaws
Gnomaws theme for Sylpheed-Claws.

%description -n sylpheed-claws-theme-Gnomaws -l pl
Motyw Gnomaws dla Sylpheed-Claws.

%package -n sylpheed-claws-theme-Gnomeria
Summary:	Gnomeria theme for Sylpheed-Claws
Summary(pl):	Motyw Gnomeria dla Sylpheed-Claws
Group:		Themes
Requires:       sylpheed-claws
Conflicts:      sylpheed-claws-themes <= 2.3.0-1

%description -n sylpheed-claws-theme-Gnomeria
Gnomeria theme for Sylpheed-Claws.

%description -n sylpheed-claws-theme-Gnomeria -l pl
Motyw Gnomeria dla Sylpheed-Claws.

%package -n sylpheed-claws-theme-Gorillaws
Summary:	Gorillaws theme for Sylpheed-Claws
Summary(pl):	Motyw Gorillaws dla Sylpheed-Claws
Group:		Themes
Requires:       sylpheed-claws
Conflicts:      sylpheed-claws-themes <= 2.3.0-1

%description -n sylpheed-claws-theme-Gorillaws
Gorillaws theme for Sylpheed-Claws.

%description -n sylpheed-claws-theme-Gorillaws -l pl
Motyw Gorillaws dla Sylpheed-Claws.

%package -n sylpheed-claws-theme-Graphitte
Summary:	Graphitte theme for Sylpheed-Claws
Summary(pl):	Motyw Graphitte dla Sylpheed-Claws
Group:		Themes
Requires:       sylpheed-claws
Conflicts:      sylpheed-claws-themes <= 2.3.0-1

%description -n sylpheed-claws-theme-Graphitte
Graphitte theme for Sylpheed-Claws.

%description -n sylpheed-claws-theme-Graphitte -l pl
Motyw Graphitte dla Sylpheed-Claws.

%package -n sylpheed-claws-theme-GurUnix
Summary:	GurUnix theme for Sylpheed-Claws
Summary(pl):	Motyw GurUnix dla Sylpheed-Claws
Group:		Themes
Requires:       sylpheed-claws
Conflicts:      sylpheed-claws-themes <= 2.3.0-1

%description -n sylpheed-claws-theme-GurUnix
GurUnix theme for Sylpheed-Claws.

%description -n sylpheed-claws-theme-GurUnix -l pl
Motyw GurUnix dla Sylpheed-Claws.

%package -n sylpheed-claws-theme-Korillaws
Summary:	Korillaws theme for Sylpheed-Claws
Summary(pl):	Motyw Korillaws dla Sylpheed-Claws
Group:		Themes
Requires:       sylpheed-claws
Conflicts:      sylpheed-claws-themes <= 2.3.0-1

%description -n sylpheed-claws-theme-Korillaws
Korillaws theme for Sylpheed-Claws.

%description -n sylpheed-claws-theme-Korillaws -l pl
Motyw Korillaws dla Sylpheed-Claws.

%package -n sylpheed-claws-theme-Kovico
Summary:	Kovico theme for Sylpheed-Claws
Summary(pl):	Motyw Kovico dla Sylpheed-Claws
Group:		Themes
Requires:       sylpheed-claws
Conflicts:      sylpheed-claws-themes <= 2.3.0-1

%description -n sylpheed-claws-theme-Kovico
Kovico theme for Sylpheed-Claws.

%description -n sylpheed-claws-theme-Kovico -l pl
Motyw Kovico dla Sylpheed-Claws.

%package -n sylpheed-claws-theme-Logos
Summary:	Logos theme for Sylpheed-Claws
Summary(pl):	Motyw Logos dla Sylpheed-Claws
Group:		Themes
Requires:       sylpheed-claws
Conflicts:      sylpheed-claws-themes <= 2.3.0-1

%description -n sylpheed-claws-theme-Logos
Logos theme for Sylpheed-Claws.

%description -n sylpheed-claws-theme-Logos -l pl
Motyw Logos dla Sylpheed-Claws.

%package -n sylpheed-claws-theme-Mongrel
Summary:	Mongrel theme for Sylpheed-Claws
Summary(pl):	Motyw Mongrel dla Sylpheed-Claws
Group:		Themes
Requires:       sylpheed-claws
Conflicts:      sylpheed-claws-themes <= 2.3.0-1

%description -n sylpheed-claws-theme-Mongrel
Mongrel theme for Sylpheed-Claws.

%description -n sylpheed-claws-theme-Mongrel -l pl
Motyw Mongrel dla Sylpheed-Claws.

%package -n sylpheed-claws-theme-Mongrel2
Summary:	Mongrel2 theme for Sylpheed-Claws
Summary(pl):	Motyw Mongrel2 dla Sylpheed-Claws
Group:		Themes
Requires:       sylpheed-claws
Conflicts:      sylpheed-claws-themes <= 2.3.0-1

%description -n sylpheed-claws-theme-Mongrel2
Mongrel2 theme for Sylpheed-Claws.

%description -n sylpheed-claws-theme-Mongrel2 -l pl
Motyw Mongrel2 dla Sylpheed-Claws.

%package -n sylpheed-claws-theme-Mozilla
Summary:	Mozilla theme for Sylpheed-Claws
Summary(pl):	Motyw Mozilla dla Sylpheed-Claws
Group:		Themes
Requires:       sylpheed-claws
Conflicts:      sylpheed-claws-themes <= 2.3.0-1

%description -n sylpheed-claws-theme-Mozilla
Mozilla theme for Sylpheed-Claws.

%description -n sylpheed-claws-theme-Mozilla -l pl
Motyw Mozilla dla Sylpheed-Claws.

%package -n sylpheed-claws-theme-New_Session
Summary:	New Session theme for Sylpheed-Claws
Summary(pl):	Motyw New Session dla Sylpheed-Claws
Group:		Themes
Requires:       sylpheed-claws
Conflicts:      sylpheed-claws-themes <= 2.3.0-1

%description -n	sylpheed-claws-theme-New_Session
New Session theme for Sylpheed-Claws.

%description -n sylpheed-claws-theme-New_Session -l pl
Motyw New Session dla Sylpheed-Claws.

%package -n sylpheed-claws-theme-OldDark
Summary:	OldDark theme for Sylpheed-Claws
Summary(pl):	Motyw OldDark dla Sylpheed-Claws
Group:		Themes
Requires:       sylpheed-claws
Conflicts:      sylpheed-claws-themes <= 2.3.0-1

%description -n sylpheed-claws-theme-OldDark
OldDark theme for Sylpheed-Claws.

%description -n sylpheed-claws-theme-OldDark -l pl
Motyw OldDark dla Sylpheed-Claws.

%package -n sylpheed-claws-theme-Orbit-Claws
Summary:	Orbit-Claws theme for Sylpheed-Claws
Summary(pl):	Motyw Orbit-Claws dla Sylpheed-Claws
Group:		Themes
Requires:       sylpheed-claws
Conflicts:      sylpheed-claws-themes <= 2.3.0-1

%description -n sylpheed-claws-theme-Orbit-Claws
Orbit-Claws theme for Sylpheed-Claws.

%description -n sylpheed-claws-theme-Orbit-Claws -l pl
Motyw Orbit-Claws dla Sylpheed-Claws.

%package -n sylpheed-claws-theme-Phoenity
Summary:	Phoenity theme for Sylpheed-Claws
Summary(pl):	Motyw Phoenity dla Sylpheed-Claws
Group:		Themes
Requires:       sylpheed-claws
Conflicts:      sylpheed-claws-themes <= 2.3.0-1

%description -n sylpheed-claws-theme-Phoenity
Phoenity theme for Sylpheed-Claws.

%description -n sylpheed-claws-theme-Phoenity -l pl
Motyw Phoenity dla Sylpheed-Claws.

%package -n sylpheed-claws-theme-Plain_and_Bluish
Summary:	Plain and Bluish theme for Sylpheed-Claws
Summary(pl):	Motyw Plain and Bluish dla Sylpheed-Claws
Group:		Themes
Requires:       sylpheed-claws
Conflicts:      sylpheed-claws-themes <= 2.3.0-1

%description -n sylpheed-claws-theme-Plain_and_Bluish
Plain and Bluish theme for Sylpheed-Claws.

%description -n sylpheed-claws-theme-Plain_and_Bluish -l pl
Motyw Plain and Bluish dla Sylpheed-Claws.

%package -n sylpheed-claws-theme-STW
Summary:	STW theme for Sylpheed-Claws
Summary(pl):	Motyw STW dla Sylpheed-Claws
Group:		Themes
Requires:       sylpheed-claws
Conflicts:      sylpheed-claws-themes <= 2.3.0-1

%description -n sylpheed-claws-theme-STW
STW theme for Sylpheed-Claws.

%description -n sylpheed-claws-theme-STW -l pl
Motyw STW dla Sylpheed-Claws.

%package -n sylpheed-claws-theme-Skypilot-Clawssic
Summary:	Skypilot-Clawssic theme for Sylpheed-Claws
Summary(pl):	Motyw Skypilot-Clawssic dla Sylpheed-Claws
Group:		Themes
Requires:       sylpheed-claws
Conflicts:      sylpheed-claws-themes <= 2.3.0-1

%description -n sylpheed-claws-theme-Skypilot-Clawssic
Skypilot-Clawssic theme for Sylpheed-Claws.

%description -n sylpheed-claws-theme-Skypilot-Clawssic -l pl
Motyw Skypilot-Clawssic dla Sylpheed-Claws.

%package -n sylpheed-claws-theme-Sylpholution
Summary:	Sylpholution theme for Sylpheed-Claws
Summary(pl):	Motyw Sylpholution dla Sylpheed-Claws
Group:		Themes
Requires:       sylpheed-claws
Conflicts:      sylpheed-claws-themes <= 2.3.0-1

%description -n sylpheed-claws-theme-Sylpholution
Sylpholution theme for Sylpheed-Claws.

%description -n sylpheed-claws-theme-Sylpholution -l pl
Motyw Sylpholution dla Sylpheed-Claws.

%package -n sylpheed-claws-theme-SylZilla
Summary:	SylZilla theme for Sylpheed-Claws
Summary(pl):	Motyw SylZilla dla Sylpheed-Claws
Group:		Themes
Requires:       sylpheed-claws
Conflicts:      sylpheed-claws-themes <= 2.3.0-1

%description -n sylpheed-claws-theme-SylZilla
SylZilla theme for Sylpheed-Claws.

%description -n sylpheed-claws-theme-SylZilla -l pl
Motyw SylZilla dla Sylpheed-Claws.

%package -n sylpheed-claws-theme-TangoClaws
Summary:	TangoClaws theme for Sylpheed-Claws
Summary(pl):	Motyw TangoClaws dla Sylpheed-Claws
Group:		Themes
Requires:       sylpheed-claws	
Conflicts:      sylpheed-claws-themes <= 2.3.0-1

%description -n sylpheed-claws-theme-TangoClaws
TangoClaws theme for Sylpheed-Claws.

%description -n sylpheed-claws-theme-TangoClaws -l pl
Motyw TangoClaws dla Sylpheed-Claws.

%package -n sylpheed-claws-theme-XeNtish
Summary:	XeNtish theme for Sylpheed-Claws
Summary(pl):	Motyw XeNtish dla Sylpheed-Claws
Group:		Themes
Requires:       sylpheed-claws
Conflicts:      sylpheed-claws-themes <= 2.3.0-1

%description -n sylpheed-claws-theme-XeNtish
XeNtish theme for Sylpheed-Claws.

%description -n sylpheed-claws-theme-XeNtish -l pl
Motyw XeNtish dla Sylpheed-Claws.

%package -n sylpheed-claws-theme-tml02c
Summary:	tml02c theme for Sylpheed-Claws
Summary(pl):	Motyw tml02c dla Sylpheed-Claws
Group:		Themes
Requires:       sylpheed-claws
Conflicts:      sylpheed-claws-themes <= 2.3.0-1

%description -n sylpheed-claws-theme-tml02c
tml02c theme for Sylpheed-Claws.

%description -n sylpheed-claws-theme-tml02c -l pl
Motyw tml02c dla Sylpheed-Claws.

%package -n sylpheed-claws-theme-tom2
Summary:	tom2 theme for Sylpheed-Claws
Summary(pl):	Motyw tom2 dla Sylpheed-Claws
Group:		Themes
Requires:       sylpheed-claws
Conflicts:      sylpheed-claws-themes <= 2.3.0-1

%description -n	sylpheed-claws-theme-tom2
tom2 theme for Sylpheed-Claws.

%description -n sylpheed-claws-theme-tom2 -l pl
Motyw tom2 dla Sylpheed-Claws.

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

%files -n sylpheed-claws-theme-Achileus-noname
%defattr(644,root,root,755)
%{_themesdir}/achileus-noname

%files -n sylpheed-claws-theme-Black
%defattr(644,root,root,755)
%doc black/README
%{_themesdir}/black

%files -n sylpheed-claws-theme-Blue_Anarchy
%defattr(644,root,root,755)
%doc blue_anarchy/Readme.txt
%{_themesdir}/blue_anarchy

%files -n sylpheed-claws-theme-Clawsola
%defattr(644,root,root,755)
%doc clawsola/{ChangeLog,README}
%{_themesdir}/clawsola

%files -n sylpheed-claws-theme-Crystal
%defattr(644,root,root,755)
%{_themesdir}/Crystal

%files -n sylpheed-claws-theme-Everaldo_Kids
%defattr(644,root,root,755)
%doc Everaldo_Kids/ReadMe
%{_themesdir}/Everaldo_Kids

%files -n sylpheed-claws-theme-Gnomaws
%defattr(644,root,root,755)
%doc Gnomaws-*/{ChangeLog,README}
%{_themesdir}/Gnomaws-*

%files -n sylpheed-claws-theme-Gnomeria
%defattr(644,root,root,755)
%doc Gnomeria/README
%{_themesdir}/Gnomeria

%files -n sylpheed-claws-theme-Gorillaws
%defattr(644,root,root,755)
%doc Gorillaws/{ChangeLog,README}
%{_themesdir}/Gorillaws

%files -n sylpheed-claws-theme-Graphitte
%defattr(644,root,root,755)
%doc Graphitte-*/README
%{_themesdir}/Graphitte-*

%files -n sylpheed-claws-theme-GurUnix
%defattr(644,root,root,755)
%doc GurUnix/{ChangeLog,README.txt}
%{_themesdir}/GurUnix

%files -n sylpheed-claws-theme-Korillaws
%defattr(644,root,root,755)
%doc Korillaws/{ChangeLog,README}
%{_themesdir}/Korillaws

%files -n sylpheed-claws-theme-Kovico
%defattr(644,root,root,755)
%{_themesdir}/Kovico-sylpheed

%files -n sylpheed-claws-theme-Logos
%defattr(644,root,root,755)
%{_themesdir}/Logos-*

%files -n sylpheed-claws-theme-Mongrel
%defattr(644,root,root,755)
%{_themesdir}/mongrel

%files -n sylpheed-claws-theme-Mongrel2
%defattr(644,root,root,755)
%{_themesdir}/mongrel2

%files -n sylpheed-claws-theme-Mozilla
%defattr(644,root,root,755)
%doc mozilla/README
%{_themesdir}/mozilla

%files -n sylpheed-claws-theme-New_Session
%defattr(644,root,root,755)
%doc New_Session/Readme.txt
%{_themesdir}/New_Session

%files -n sylpheed-claws-theme-OldDark
%defattr(644,root,root,755)
%{_themesdir}/Old_Dark_Theme

%files -n sylpheed-claws-theme-Orbit-Claws
%defattr(644,root,root,755)
%doc orbit-claws/README
%{_themesdir}/orbit-claws

%files -n sylpheed-claws-theme-Phoenity
%defattr(644,root,root,755)
%doc Phoenity/readme.txt
%{_themesdir}/Phoenity

%files -n sylpheed-claws-theme-Plain_and_Bluish
%defattr(644,root,root,755)
%{_themesdir}/Plain_and_Bluish

%files -n sylpheed-claws-theme-STW
%defattr(644,root,root,755)
%{_themesdir}/stw

%files -n sylpheed-claws-theme-Skypilot-Clawssic
%defattr(644,root,root,755)
%doc Skypilot_Clawssic/README
%{_themesdir}/Skypilot_Clawssic

%files -n sylpheed-claws-theme-Sylpholution
%defattr(644,root,root,755)
%doc Sylpholution/ChangeLog*
%{_themesdir}/Sylpholution

%files -n sylpheed-claws-theme-SylZilla
%defattr(644,root,root,755)
%doc SylZilla/{ChangeLog,README}
%{_themesdir}/SylZilla

%files -n sylpheed-claws-theme-TangoClaws
%defattr(644,root,root,755)
%doc TangoClaws-*/README
%{_themesdir}/TangoClaws-*

%files -n sylpheed-claws-theme-XeNtish
%defattr(644,root,root,755)
%doc XeNtish/README
%{_themesdir}/XeNtish

%files -n sylpheed-claws-theme-tml02c
%defattr(644,root,root,755)
%{_themesdir}/tml02c

%files -n sylpheed-claws-theme-tom2
%defattr(644,root,root,755)
%doc tom_*/README
%{_themesdir}/tom_*
