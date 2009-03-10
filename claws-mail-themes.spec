Summary:	Themes for Claws-Mail (metapackage)
Summary(pl.UTF-8):	Motywy dla programu Claws-Mail (metapakiet)
Name:		claws-mail-themes
Version:	20090225
Release:	1
License:	GPL
Group:		Themes
Source0:	http://www.claws-mail.org/themes/%{name}-%{version}.tar.gz
# Source0-md5:	678f0815f52c781c4dc3f227e861b582
URL:		http://www.claws-mail.org/themes.php
Requires:	claws-mail-theme-Achileus-noname = %{version}-%{release}
Requires:	claws-mail-theme-A_Ducks_Claw = %{version}-%{release}
Requires:	claws-mail-theme-Black = %{version}-%{release}
Requires:	claws-mail-theme-Blaue_Klaue = %{version}-%{release}
Requires:	claws-mail-theme-Blue_Anarchy = %{version}-%{release}
Requires:	claws-mail-theme-Buuf = %{version}-%{release}
Requires:	claws-mail-theme-Clawsola = %{version}-%{release}
Requires:	claws-mail-theme-Coons_Blue = %{version}-%{release}
Requires:	claws-mail-theme-Crystal = %{version}-%{release}
Requires:	claws-mail-theme-Everaldo_Kids = %{version}-%{release}
Requires:	claws-mail-theme-Gnomaws = %{version}-%{release}
Requires:	claws-mail-theme-Gnomeria = %{version}-%{release}
Requires:	claws-mail-theme-Gorillaws = %{version}-%{release}
Requires:	claws-mail-theme-Graphitte = %{version}-%{release}
Requires:	claws-mail-theme-GurUnix = %{version}-%{release}
Requires:	claws-mail-theme-Hash303030 = %{version}-%{release}
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
Requires:	claws-mail-theme-Skypilot-Clawssic = %{version}-%{release}
Requires:	claws-mail-theme-STW = %{version}-%{release}
Requires:	claws-mail-theme-Sylpholution = %{version}-%{release}
Requires:	claws-mail-theme-SylZilla = %{version}-%{release}
Requires:	claws-mail-theme-Tango = %{version}-%{release}
Requires:	claws-mail-theme-TangoClaws = %{version}-%{release}
Requires:	claws-mail-theme-TangoOrbit = %{version}-%{release}
Requires:	claws-mail-theme-tml02c = %{version}-%{release}
Requires:	claws-mail-theme-tom2 = %{version}-%{release}
Requires:	claws-mail-theme-UltimateClawsMail = %{version}-%{release}
Requires:	claws-mail-theme-XeNtish = %{version}-%{release}
Requires:	claws-mail-theme-ZX = %{version}-%{release}
Provides:	sylpheed-claws-themes = %{version}
Obsoletes:	sylpheed-claws-themes
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_themesdir	%{_datadir}/claws-mail/themes

%description
Themes for Claws-Mail (metapackage).

%description -l pl.UTF-8
Motywy dla programu Claws-Mail (metapakiet).

%package -n claws-mail-theme-Achileus-noname
Summary:	Achileus-noname theme for Claws-Mail
Summary(pl.UTF-8):	Motyw achileus-noname dla Claws-Mail
Group:		Themes
Requires:	claws-mail
Provides:	sylpheed-claws-theme-Achileus-noname
Obsoletes:	sylpheed-claws-theme-Achileus-noname
Conflicts:	sylpheed-claws-themes <= 2.3.0-1

%description -n claws-mail-theme-Achileus-noname
Achileus-noname theme for Claws-Mail.

%description -n claws-mail-theme-Achileus-noname -l pl.UTF-8
Motyw achileus-noname dla Claws-Mail.

%package -n claws-mail-theme-A_Ducks_Claw
Summary:	A_Ducks_Claw theme for Claws-Mail
Summary(pl.UTF-8):	Motyw A_Ducks_Claw dla Claws-Mail
Group:		Themes
Requires:	claws-mail

%description -n claws-mail-theme-A_Ducks_Claw
A_Ducks_Claw theme for Claws-Mail.

%description -n claws-mail-theme-A_Ducks_Claw -l pl.UTF-8
Motyw A_Ducks_Claw dla Claws-Mail.

%package -n claws-mail-theme-Black
Summary:	Black theme for Claws-Mail
Summary(pl.UTF-8):	Motyw black dla Claws-Mail
Group:		Themes
Requires:	claws-mail
Provides:	sylpheed-claws-theme-Black
Obsoletes:	sylpheed-claws-theme-Black
Conflicts:	sylpheed-claws-themes <= 2.3.0-1

%description -n claws-mail-theme-Black
Black theme for Claws-Mail.

%description -n claws-mail-theme-Black -l pl.UTF-8
Motyw black dla Claws-Mail.

%package -n claws-mail-theme-Blaue_Klaue
Summary:	Blaue_Klaue theme for Claws-Mail
Summary(pl.UTF-8):	Motyw Blaue_Klaue dla Claws-Mail
Group:		Themes
Requires:	claws-mail

%description -n claws-mail-theme-Blaue_Klaue
Blaue_Klaue theme for Claws-Mail.

%description -n claws-mail-theme-Blaue_Klaue -l pl.UTF-8
Motyw Blaue_Klaue dla Claws-Mail.

%package -n claws-mail-theme-Blue_Anarchy
Summary:	Blue anarchy theme for Claws-Mail
Summary(pl.UTF-8):	Motyw blue anarchy dla Claws-Mail
Group:		Themes
Requires:	claws-mail
Provides:	sylpheed-claws-theme-Blue_Anarchy
Obsoletes:	sylpheed-claws-theme-Blue_Anarchy
Conflicts:	sylpheed-claws-themes <= 2.3.0-1

%description -n claws-mail-theme-Blue_Anarchy
Blue anarchy theme for Claws-Mail.

%description -n claws-mail-theme-Blue_Anarchy -l pl.UTF-8
Motyw blue anarchy dla Claws-Mail.

%package -n claws-mail-theme-Buuf
Summary:	Buuf theme for Claws-Mail
Summary(pl.UTF-8):	Motyw buuf dla Claws-Mail
Group:		Themes
Requires:	claws-mail

%description -n claws-mail-theme-Buuf
Buuf theme for Claws-Mail.

%description -n claws-mail-theme-Buuf -l pl.UTF-8
Motyw buuf dla Claws-Mail.

%package -n claws-mail-theme-Clawsola
Summary:	Clawsola theme for Claws-Mail
Summary(pl.UTF-8):	Motyw Clawsola dla Claws-Mail
Group:		Themes
Requires:	claws-mail
Provides:	sylpheed-claws-theme-Clawsola
Obsoletes:	sylpheed-claws-theme-Clawsola
Conflicts:	sylpheed-claws-themes <= 2.3.0-1

%description -n claws-mail-theme-Clawsola
Clawsola theme for Claws-Mail.

%description -n claws-mail-theme-Clawsola -l pl.UTF-8
Motyw Clawsola dla Claws-Mail.

%package -n claws-mail-theme-Coons_Blue
Summary:	Coons_Blue theme for Claws-Mail
Summary(pl.UTF-8):	Motyw Coons_Blue dla Claws-Mail
Group:		Themes
Requires:	claws-mail

%description -n claws-mail-theme-Coons_Blue
Coons_Blue theme for Claws-Mail.

%description -n claws-mail-theme-Coons_Blue -l pl.UTF-8
Motyw Coons_Blue dla Claws-Mail.

%package -n claws-mail-theme-Crystal
Summary:	Crystal theme for Claws-Mail
Summary(pl.UTF-8):	Motyw Crystal dla Claws-Mail
Group:		Themes
Requires:	claws-mail
Provides:	sylpheed-claws-theme-Crystal
Obsoletes:	sylpheed-claws-theme-Crystal
Conflicts:	sylpheed-claws-themes <= 2.3.0-1

%description -n claws-mail-theme-Crystal
Crystal theme for Claws-Mail.

%description -n claws-mail-theme-Crystal -l pl.UTF-8
Motyw Crystal dla Claws-Mail.

%package -n claws-mail-theme-Everaldo_Kids
Summary:	Everaldo Kids theme for Claws-Mail
Summary(pl.UTF-8):	Motyw Everaldo Kids dla Claws-Mail
Group:		Themes
Requires:	claws-mail
Provides:	sylpheed-claws-theme-Everaldo_Kids
Obsoletes:	sylpheed-claws-theme-Everaldo_Kids
Conflicts:	sylpheed-claws-themes <= 2.3.0-1

%description -n	claws-mail-theme-Everaldo_Kids
Everaldo Kids theme for Claws-Mail.

%description -n claws-mail-theme-Everaldo_Kids -l pl.UTF-8
Motyw Everaldo Kids dla Claws-Mail.

%package -n claws-mail-theme-Gnomaws
Summary:	Gnomaws theme for Claws-Mail
Summary(pl.UTF-8):	Motyw Gnomaws dla Claws-Mail
Group:		Themes
Requires:	claws-mail
Provides:	sylpheed-claws-theme-Gnomaws
Obsoletes:	sylpheed-claws-theme-Gnomaws
Conflicts:	sylpheed-claws-themes <= 2.3.0-1

%description -n claws-mail-theme-Gnomaws
Gnomaws theme for Claws-Mail.

%description -n claws-mail-theme-Gnomaws -l pl.UTF-8
Motyw Gnomaws dla Claws-Mail.

%package -n claws-mail-theme-Gnomeria
Summary:	Gnomeria theme for Claws-Mail
Summary(pl.UTF-8):	Motyw Gnomeria dla Claws-Mail
Group:		Themes
Requires:	claws-mail
Provides:	sylpheed-claws-theme-Gnomeria
Obsoletes:	sylpheed-claws-theme-Gnomeria
Conflicts:	sylpheed-claws-themes <= 2.3.0-1

%description -n claws-mail-theme-Gnomeria
Gnomeria theme for Claws-Mail.

%description -n claws-mail-theme-Gnomeria -l pl.UTF-8
Motyw Gnomeria dla Claws-Mail.

%package -n claws-mail-theme-Gorillaws
Summary:	Gorillaws theme for Claws-Mail
Summary(pl.UTF-8):	Motyw Gorillaws dla Claws-Mail
Group:		Themes
Requires:	claws-mail
Provides:	sylpheed-claws-theme-Gorillaws
Obsoletes:	sylpheed-claws-theme-Gorillaws
Conflicts:	sylpheed-claws-themes <= 2.3.0-1

%description -n claws-mail-theme-Gorillaws
Gorillaws theme for Claws-Mail.

%description -n claws-mail-theme-Gorillaws -l pl.UTF-8
Motyw Gorillaws dla Claws-Mail.

%package -n claws-mail-theme-Graphitte
Summary:	Graphitte theme for Claws-Mail
Summary(pl.UTF-8):	Motyw Graphitte dla Claws-Mail
Group:		Themes
Requires:	claws-mail
Provides:	sylpheed-claws-theme-Graphitte
Obsoletes:	sylpheed-claws-theme-Graphitte
Conflicts:	sylpheed-claws-themes <= 2.3.0-1

%description -n claws-mail-theme-Graphitte
Graphitte theme for Claws-Mail.

%description -n claws-mail-theme-Graphitte -l pl.UTF-8
Motyw Graphitte dla Claws-Mail.

%package -n claws-mail-theme-GurUnix
Summary:	GurUnix theme for Claws-Mail
Summary(pl.UTF-8):	Motyw GurUnix dla Claws-Mail
Group:		Themes
Requires:	claws-mail
Provides:	sylpheed-claws-theme-GurUnix
Obsoletes:	sylpheed-claws-theme-GurUnix
Conflicts:	sylpheed-claws-themes <= 2.3.0-1

%description -n claws-mail-theme-GurUnix
GurUnix theme for Claws-Mail.

%description -n claws-mail-theme-GurUnix -l pl.UTF-8
Motyw GurUnix dla Claws-Mail.

%package -n claws-mail-theme-Hash303030
Summary:	Hash303030 theme for Claws-Mail
Summary(pl.UTF-8):	Motyw Hash303030 dla Claws-Mail
Group:		Themes
Requires:	claws-mail

%description -n claws-mail-theme-Hash303030
Hash303030 theme for Claws-Mail.

%description -n claws-mail-theme-Hash303030 -l pl.UTF-8
Motyw hash303030 dla Claws-Mail.

%package -n claws-mail-theme-Korillaws
Summary:	Korillaws theme for Claws-Mail
Summary(pl.UTF-8):	Motyw Korillaws dla Claws-Mail
Group:		Themes
Requires:	claws-mail
Provides:	sylpheed-claws-theme-Korillaws
Obsoletes:	sylpheed-claws-theme-Korillaws
Conflicts:	sylpheed-claws-themes <= 2.3.0-1

%description -n claws-mail-theme-Korillaws
Korillaws theme for Claws-Mail.

%description -n claws-mail-theme-Korillaws -l pl.UTF-8
Motyw Korillaws dla Claws-Mail.

%package -n claws-mail-theme-Kovico
Summary:	Kovico-claws theme for Claws-Mail
Summary(pl.UTF-8):	Motyw Kovico-claws dla Claws-Mail
Group:		Themes
Requires:	claws-mail
Provides:	sylpheed-claws-theme-Kovico
Obsoletes:	sylpheed-claws-theme-Kovico
Conflicts:	sylpheed-claws-themes <= 2.3.0-1

%description -n claws-mail-theme-Kovico
Kovico theme for Claws-Mail.

%description -n claws-mail-theme-Kovico -l pl.UTF-8
Motyw Kovico dla Claws-Mail.

%package -n claws-mail-theme-Logos
Summary:	Logos theme for Claws-Mail
Summary(pl.UTF-8):	Motyw Logos dla Claws-Mail
Group:		Themes
Requires:	claws-mail
Provides:	sylpheed-claws-theme-Logos
Obsoletes:	sylpheed-claws-theme-Logos
Conflicts:	sylpheed-claws-themes <= 2.3.0-1

%description -n claws-mail-theme-Logos
Logos theme for Claws-Mail.

%description -n claws-mail-theme-Logos -l pl.UTF-8
Motyw Logos dla Claws-Mail.

%package -n claws-mail-theme-Mongrel
Summary:	Mongrel theme for Claws-Mail
Summary(pl.UTF-8):	Motyw Mongrel dla Claws-Mail
Group:		Themes
Requires:	claws-mail
Provides:	sylpheed-claws-theme-Mongrel
Obsoletes:	sylpheed-claws-theme-Mongrel
Conflicts:	sylpheed-claws-themes <= 2.3.0-1

%description -n claws-mail-theme-Mongrel
Mongrel theme for Claws-Mail.

%description -n claws-mail-theme-Mongrel -l pl.UTF-8
Motyw Mongrel dla Claws-Mail.

%package -n claws-mail-theme-Mongrel2
Summary:	Mongrel2 theme for Claws-Mail
Summary(pl.UTF-8):	Motyw Mongrel2 dla Claws-Mail
Group:		Themes
Requires:	claws-mail
Provides:	sylpheed-claws-theme-Mongrel2
Obsoletes:	sylpheed-claws-theme-Mongrel2
Conflicts:	sylpheed-claws-themes <= 2.3.0-1

%description -n claws-mail-theme-Mongrel2
Mongrel2 theme for Claws-Mail.

%description -n claws-mail-theme-Mongrel2 -l pl.UTF-8
Motyw Mongrel2 dla Claws-Mail.

%package -n claws-mail-theme-Mozilla
Summary:	Mozilla theme for Claws-Mail
Summary(pl.UTF-8):	Motyw Mozilla dla Claws-Mail
Group:		Themes
Requires:	claws-mail
Provides:	sylpheed-claws-theme-Mozilla
Obsoletes:	sylpheed-claws-theme-Mozilla
Conflicts:	sylpheed-claws-themes <= 2.3.0-1

%description -n claws-mail-theme-Mozilla
Mozilla theme for Claws-Mail.

%description -n claws-mail-theme-Mozilla -l pl.UTF-8
Motyw Mozilla dla Claws-Mail.

%package -n claws-mail-theme-Navigator
Summary:	Navigator theme for Claws-Mail
Summary(pl.UTF-8):	Motyw Navigator dla Claws-Mail
Group:		Themes
Requires:	claws-mail

%description -n claws-mail-theme-Navigator
Navigator theme for Claws-Mail.

%description -n claws-mail-theme-Navigator -l pl.UTF-8
Motyw Navigator dla Claws-Mail.

%package -n claws-mail-theme-New_Session
Summary:	New Session theme for Claws-Mail
Summary(pl.UTF-8):	Motyw New Session dla Claws-Mail
Group:		Themes
Requires:	claws-mail
Provides:	sylpheed-claws-theme-New_Session
Obsoletes:	sylpheed-claws-theme-New_Session
Conflicts:	sylpheed-claws-themes <= 2.3.0-1

%description -n	claws-mail-theme-New_Session
New Session theme for Claws-Mail.

%description -n claws-mail-theme-New_Session -l pl.UTF-8
Motyw New Session dla Claws-Mail.

%package -n claws-mail-theme-OldDark
Summary:	OldDark theme for Claws-Mail
Summary(pl.UTF-8):	Motyw OldDark dla Claws-Mail
Group:		Themes
Requires:	claws-mail
Provides:	sylpheed-claws-theme-OldDark
Obsoletes:	sylpheed-claws-theme-OldDark
Conflicts:	sylpheed-claws-themes <= 2.3.0-1

%description -n claws-mail-theme-OldDark
OldDark theme for Claws-Mail.

%description -n claws-mail-theme-OldDark -l pl.UTF-8
Motyw OldDark dla Claws-Mail.

%package -n claws-mail-theme-Orbit-Claws
Summary:	Orbit-Claws theme for Claws-Mail
Summary(pl.UTF-8):	Motyw Orbit-Claws dla Claws-Mail
Group:		Themes
Requires:	claws-mail
Provides:	sylpheed-claws-theme-Orbit-Claws
Obsoletes:	sylpheed-claws-theme-Orbit-Claws
Conflicts:	sylpheed-claws-themes <= 2.3.0-1

%description -n claws-mail-theme-Orbit-Claws
Orbit-Claws theme for Claws-Mail.

%description -n claws-mail-theme-Orbit-Claws -l pl.UTF-8
Motyw Orbit-Claws dla Claws-Mail.

%package -n claws-mail-theme-Phoenity
Summary:	Phoenity theme for Claws-Mail
Summary(pl.UTF-8):	Motyw Phoenity dla Claws-Mail
Group:		Themes
Requires:	claws-mail
Provides:	sylpheed-claws-theme-Phoenity
Obsoletes:	sylpheed-claws-theme-Phoenity
Conflicts:	sylpheed-claws-themes <= 2.3.0-1

%description -n claws-mail-theme-Phoenity
Phoenity theme for Claws-Mail.

%description -n claws-mail-theme-Phoenity -l pl.UTF-8
Motyw Phoenity dla Claws-Mail.

%package -n claws-mail-theme-Plain_and_Bluish
Summary:	Plain and Bluish theme for Claws-Mail
Summary(pl.UTF-8):	Motyw Plain and Bluish dla Claws-Mail
Group:		Themes
Requires:	claws-mail
Provides:	sylpheed-claws-theme-Plain_and_Bluish
Obsoletes:	sylpheed-claws-theme-Plain_and_Bluish
Conflicts:	sylpheed-claws-themes <= 2.3.0-1

%description -n claws-mail-theme-Plain_and_Bluish
Plain and Bluish theme for Claws-Mail.

%description -n claws-mail-theme-Plain_and_Bluish -l pl.UTF-8
Motyw Plain and Bluish dla Claws-Mail.

%package -n claws-mail-theme-Skypilot-Clawssic
Summary:	Skypilot-Clawssic theme for Claws-Mail
Summary(pl.UTF-8):	Motyw Skypilot-Clawssic dla Claws-Mail
Group:		Themes
Requires:	claws-mail
Provides:	sylpheed-claws-theme-Skypilot-Clawssic
Obsoletes:	sylpheed-claws-theme-Skypilot-Clawssic
Conflicts:	sylpheed-claws-themes <= 2.3.0-1

%description -n claws-mail-theme-Skypilot-Clawssic
Skypilot-Clawssic theme for Claws-Mail.

%description -n claws-mail-theme-Skypilot-Clawssic -l pl.UTF-8
Motyw Skypilot-Clawssic dla Claws-Mail.

%package -n claws-mail-theme-STW
Summary:	STW theme for Claws-Mail
Summary(pl.UTF-8):	Motyw STW dla Claws-Mail
Group:		Themes
Requires:	claws-mail
Provides:	sylpheed-claws-theme-STW
Obsoletes:	sylpheed-claws-theme-STW
Conflicts:	sylpheed-claws-themes <= 2.3.0-1

%description -n claws-mail-theme-STW
STW theme for Claws-Mail.

%description -n claws-mail-theme-STW -l pl.UTF-8
Motyw STW dla Claws-Mail.

%package -n claws-mail-theme-Sylpholution
Summary:	Sylpholution theme for Claws-Mail
Summary(pl.UTF-8):	Motyw Sylpholution dla Claws-Mail
Group:		Themes
Requires:	claws-mail
Provides:	sylpheed-claws-theme-Sylpholution
Obsoletes:	sylpheed-claws-theme-Sylpholution
Conflicts:	sylpheed-claws-themes <= 2.3.0-1

%description -n claws-mail-theme-Sylpholution
Sylpholution theme for Claws-Mail.

%description -n claws-mail-theme-Sylpholution -l pl.UTF-8
Motyw Sylpholution dla Claws-Mail.

%package -n claws-mail-theme-SylZilla
Summary:	SylZilla theme for Claws-Mail
Summary(pl.UTF-8):	Motyw SylZilla dla Claws-Mail
Group:		Themes
Requires:	claws-mail
Provides:	sylpheed-claws-theme-SylZilla
Obsoletes:	sylpheed-claws-theme-SylZilla
Conflicts:	sylpheed-claws-themes <= 2.3.0-1

%description -n claws-mail-theme-SylZilla
SylZilla theme for Claws-Mail.

%description -n claws-mail-theme-SylZilla -l pl.UTF-8
Motyw SylZilla dla Claws-Mail.

%package -n claws-mail-theme-Tango
Summary:	Tango theme for Claws-Mail
Summary(pl.UTF-8):	Motyw Tango dla Claws-Mail
Group:		Themes
Requires:	claws-mail

%description -n claws-mail-theme-Tango
Tango theme for Claws-Mail.

%description -n claws-mail-theme-Tango -l pl.UTF-8
Motyw Tango dla Claws-Mail.

%package -n claws-mail-theme-TangoClaws
Summary:	TangoClaws theme for Claws-Mail
Summary(pl.UTF-8):	Motyw TangoClaws dla Claws-Mail
Group:		Themes
Requires:	claws-mail
Provides:	sylpheed-claws-theme-TangoClaws
Obsoletes:	sylpheed-claws-theme-TangoClaws
Conflicts:	sylpheed-claws-themes <= 2.3.0-1

%description -n claws-mail-theme-TangoClaws
TangoClaws theme for Claws-Mail.

%description -n claws-mail-theme-TangoClaws -l pl.UTF-8
Motyw TangoClaws dla Claws-Mail.

%package -n claws-mail-theme-TangoOrbit
Summary:	TangoOrbit theme for Claws-Mail
Summary(pl.UTF-8):	Motyw TangoOrbit dla Claws-Mail
Group:		Themes
Requires:	claws-mail

%description -n claws-mail-theme-TangoOrbit
TangoOrbit theme for Claws-Mail.

%description -n claws-mail-theme-TangoOrbit -l pl.UTF-8
Motyw TangoOrbit dla Claws-Mail.

%package -n claws-mail-theme-tml02c
Summary:	tml02c theme for Claws-Mail
Summary(pl.UTF-8):	Motyw tml02c dla Claws-Mail
Group:		Themes
Requires:	claws-mail
Provides:	sylpheed-claws-theme-tml02c
Obsoletes:	sylpheed-claws-theme-tml02c
Conflicts:	sylpheed-claws-themes <= 2.3.0-1

%description -n claws-mail-theme-tml02c
tml02c theme for Claws-Mail.

%description -n claws-mail-theme-tml02c -l pl.UTF-8
Motyw tml02c dla Claws-Mail.

%package -n claws-mail-theme-tom2
Summary:	tom2 theme for Claws-Mail
Summary(pl.UTF-8):	Motyw tom2 dla Claws-Mail
Group:		Themes
Requires:	claws-mail
Provides:	sylpheed-claws-theme-tom2
Obsoletes:	sylpheed-claws-theme-tom2
Conflicts:	sylpheed-claws-themes <= 2.3.0-1

%description -n	claws-mail-theme-tom2
tom2 theme for Claws-Mail.

%description -n claws-mail-theme-tom2 -l pl.UTF-8
Motyw tom2 dla Claws-Mail.

%package -n claws-mail-theme-UltimateClawsMail
Summary:	UltimateClawsMail theme for Claws-Mail
Summary(pl.UTF-8):	Motyw UltimateClawsMail dla Claws-Mail
Group:		Themes
Requires:	claws-mail

%description -n	claws-mail-theme-UltimateClawsMail
UltimateClawsMail theme for Claws-Mail.

%description -n claws-mail-theme-UltimateClawsMail -l pl.UTF-8
Motyw UltimateClawsMail dla Claws-Mail.

%package -n claws-mail-theme-XeNtish
Summary:	XeNtish theme for Claws-Mail
Summary(pl.UTF-8):	Motyw XeNtish dla Claws-Mail
Group:		Themes
Requires:	claws-mail
Provides:	sylpheed-claws-theme-XeNtish
Obsoletes:	sylpheed-claws-theme-XeNtish
Conflicts:	sylpheed-claws-themes <= 2.3.0-1

%description -n claws-mail-theme-XeNtish
XeNtish theme for Claws-Mail.

%description -n claws-mail-theme-XeNtish -l pl.UTF-8
Motyw XeNtish dla Claws-Mail.

%package -n claws-mail-theme-ZX
Summary:	ZX theme for Claws-Mail
Summary(pl.UTF-8):	Motyw ZX dla Claws-Mail
Group:		Themes
Requires:	claws-mail

%description -n	claws-mail-theme-ZX
ZX theme for Claws-Mail.

%description -n claws-mail-theme-ZX -l pl.UTF-8
Motyw ZX dla Claws-Mail.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_themesdir}

gzip -dc %{SOURCE0} | tar -x --strip-components=1 -C $RPM_BUILD_ROOT%{_themesdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)

%files -n claws-mail-theme-Achileus-noname
%defattr(644,root,root,755)
%{_themesdir}/achileus-noname

%files -n claws-mail-theme-A_Ducks_Claw
%defattr(644,root,root,755)
%{_themesdir}/A_Ducks_Claw

%files -n claws-mail-theme-Black
%defattr(644,root,root,755)
%{_themesdir}/black

%files -n claws-mail-theme-Blaue_Klaue
%defattr(644,root,root,755)
%{_themesdir}/Blaue_Klaue

%files -n claws-mail-theme-Blue_Anarchy
%defattr(644,root,root,755)
%{_themesdir}/blue_anarchy

%files -n claws-mail-theme-Buuf
%defattr(644,root,root,755)
%{_themesdir}/buuf

%files -n claws-mail-theme-Clawsola
%defattr(644,root,root,755)
%{_themesdir}/clawsola

%files -n claws-mail-theme-Coons_Blue
%defattr(644,root,root,755)
%{_themesdir}/Coons_Blue-*

%files -n claws-mail-theme-Crystal
%defattr(644,root,root,755)
%{_themesdir}/Crystal

%files -n claws-mail-theme-Everaldo_Kids
%defattr(644,root,root,755)
%{_themesdir}/Everaldo_Kids

%files -n claws-mail-theme-Gnomaws
%defattr(644,root,root,755)
%{_themesdir}/Gnomaws-*

%files -n claws-mail-theme-Gnomeria
%defattr(644,root,root,755)
%{_themesdir}/Gnomeria

%files -n claws-mail-theme-Gorillaws
%defattr(644,root,root,755)
%{_themesdir}/Gorillaws

%files -n claws-mail-theme-Graphitte
%defattr(644,root,root,755)
%{_themesdir}/Graphitte-*

%files -n claws-mail-theme-GurUnix
%defattr(644,root,root,755)
%{_themesdir}/GurUnix

%files -n claws-mail-theme-Hash303030
%defattr(644,root,root,755)
%{_themesdir}/hash303030

%files -n claws-mail-theme-Korillaws
%defattr(644,root,root,755)
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
%{_themesdir}/mozilla

%files -n claws-mail-theme-Navigator
%defattr(644,root,root,755)
%{_themesdir}/Navigator

%files -n claws-mail-theme-New_Session
%defattr(644,root,root,755)
%{_themesdir}/New_Session

%files -n claws-mail-theme-OldDark
%defattr(644,root,root,755)
%{_themesdir}/Old*

%files -n claws-mail-theme-Orbit-Claws
%defattr(644,root,root,755)
%{_themesdir}/orbit-claws

%files -n claws-mail-theme-Phoenity
%defattr(644,root,root,755)
%{_themesdir}/Phoenity

%files -n claws-mail-theme-Plain_and_Bluish
%defattr(644,root,root,755)
%{_themesdir}/Plain_and_Bluish

%files -n claws-mail-theme-Skypilot-Clawssic
%defattr(644,root,root,755)
%{_themesdir}/Skypilot*

%files -n claws-mail-theme-STW
%defattr(644,root,root,755)
%{_themesdir}/stw

%files -n claws-mail-theme-Sylpholution
%defattr(644,root,root,755)
%{_themesdir}/Sylpholution

%files -n claws-mail-theme-SylZilla
%defattr(644,root,root,755)
%{_themesdir}/SylZilla

%files -n claws-mail-theme-Tango
%defattr(644,root,root,755)
%{_themesdir}/Tango_v1.2

%files -n claws-mail-theme-TangoClaws
%defattr(644,root,root,755)
%{_themesdir}/TangoClaws-*

%files -n claws-mail-theme-TangoOrbit
%defattr(644,root,root,755)
%{_themesdir}/TangoOrbit

%files -n claws-mail-theme-tml02c
%defattr(644,root,root,755)
%{_themesdir}/tml02c

%files -n claws-mail-theme-tom2
%defattr(644,root,root,755)
%{_themesdir}/tom_2*

%files -n claws-mail-theme-UltimateClawsMail
%defattr(644,root,root,755)
%{_themesdir}/UltimateClawsMail*

%files -n claws-mail-theme-XeNtish
%defattr(644,root,root,755)
%{_themesdir}/XeNtish

%files -n claws-mail-theme-ZX
%defattr(644,root,root,755)
%{_themesdir}/ZX-*
