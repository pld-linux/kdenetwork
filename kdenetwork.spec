Summary:	K Desktop Environment - network applications
Summary(es):	K Desktop Environment - aplicaciones de red
Summary(pl):	K Desktop Environment - aplikacje sieciowe
Summary(pt_BR):	K Desktop Environment - aplicaÁıes de rede
Name:		kdenetwork
Version:	2.2.2
Release:	3
Epoch:		8
License:	GPL
Vendor:		The KDE Team
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(es):	X11/Aplicaciones
Group(pl):	X11/Aplikacje
Group(pt_BR):	X11/AplicaÁıes
Group(pt):	X11/AplicaÁıes
Source0:	ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-%{version}.tar.bz2
Patch0:		%{name}-knewsticker-utf8.patch
Patch1:		%{name}-am15.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	kdelibs-devel >= %{version}
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_prefix 	/usr/X11R6
%define         _fontdir        /usr/share/fonts
%define         _htmldir        /usr/share/doc/kde/HTML

%description
KDE network applications. Package includes:
- KMail - e-mail client. Patched for proper charsets support
- KORN - "biff" program
- KPPP - PPP dialer
- KNODE - news client
- KSirc - IRC client
- KTalkd - takt daemon

%description -l es
%description -l pl
Aplikacje sieciowe KDE. Pakiet zawiera:
- KMail - program pocztowy, z poprawion± obs≥ug± zestawÛw znakÛw
- KORN - program pokazuj±cy stan skrzynek pocztowych
- KPPP - program do nawi±zywania po≥±czeÒ modemowych
- KNODE - Program do czytania newsÛw
- KSirc - IRC dla KDE
- KTalkd - talk daemon dla KDE

%description -l pt_BR
AplicaÁıes de Rede para o KDE.

IncluÌdos neste pacote:

kmail: leitor de correio knu: utilit·rios de rede korn: ferramenta de
monitoraÁ„o da caixa de correio kppp: configuraÁ„o f·cil para conex„o
PPP krn: leitor de notÌcias

%package kmail
Summary:	KDE Mail client
Summary(pl):	Program pocztowy KDE
Summary(pt_BR):	Cliente / leitor de e-mails para o KDE
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(es):	X11/Aplicaciones
Group(pl):	X11/Aplikacje
Group(pt_BR):	X11/AplicaÁıes
Group(pt):	X11/AplicaÁıes
Requires:	kdelibs >= %{version}

%description kmail
This is electronic mail client for KDE. It is able to retrievie mail
from POP3 accounts and from local mailboxes.

This package contains version patched for better charset support.

%description -l pl kmail
Program pocztowy dla KDE. Potrafi odczytywaÊ pocztÍ z kont POP3 jak i
lokalnych skrzynek.

Ten pakiet zawiera wersj± programu z poprawion± obs≥ug± zestawÛw
znakÛw.

%description -l pt_BR kmail
Poderoso cliente / leitor de e-mails para o KDE.

%package korn 
Summary:	KDE 'biff' application
Summary(pl):	Wskaºnik skrzynki pocztowej dla KDE
Summary(pt_BR):	Miniaplicativo de monitoraÁ„o da caixa de correio
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(es):	X11/Aplicaciones
Group(pl):	X11/Aplikacje
Group(pt_BR):	X11/AplicaÁıes
Group(pt):	X11/AplicaÁıes
Requires:	kdelibs >= %{version}

%description korn
A simple program showing number of mails in your folders.

%description -l pl korn
Programik pokazuj±cy ilo∂Ê wiadomo∂ci w wybranych folderach
pocztowych.

%description -l pt_BR korn
Miniaplicativo de monitoraÁ„o da caixa de correio.

%package kppp
Summary:	KDE PPP dialer	
Summary(pl):	Program do po≥±czeÒ modemowych dla KDE
Summary(pt_BR):	O discador para Internet
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(es):	X11/Aplicaciones
Group(pl):	X11/Aplikacje
Group(pt_BR):	X11/AplicaÁıes
Group(pt):	X11/AplicaÁıes
Requires:	kdelibs >= %{version}
Requires:	ppp 

%description kppp
A PPPP dialer for KDE. It supports multiple accounts.

%description -l pl kppp
Program no nawi±zywania po≥±czeÒ modemowych pod KDE. Posiada ≥atwy
interfejs i moøliwo∂Ê zdefiniowania kilku kont.

%description -l pt_BR kppp
O discador para Internet.

%package knode
Summary:	KDE News Reader	
Summary(pl):	Czytnik newsÛw dla KDE
Summary(pt_BR):	Leitor de notÌcias (news) do KDE
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(es):	X11/Aplicaciones
Group(pl):	X11/Aplikacje
Group(pt_BR):	X11/AplicaÁıes
Group(pt):	X11/AplicaÁıes
Requires:	kdelibs >= %{version}

%description knode
This is a news reader for KDE. It has threading and everything else
you need to be happy reading your news.

%description -l pl knode
Czytnik newsÛw dla KDE. Obs≥uguje w±tki oraz killfile.

%description -l pt_BR knode
Leitor de notÌcias (news) do KDE.

%package ksirc
Summary:	KDE IRC client
Summary(pl):	Klient IRC dla KDE
Summary(pt_BR):	Cliente de IRC do KDE
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(es):	X11/Aplicaciones
Group(pl):	X11/Aplikacje
Group(pt_BR):	X11/AplicaÁıes
Group(pt):	X11/AplicaÁıes
Requires:	kdelibs >= %{version}

%description ksirc
KDE IRC client.

%description -l pl ksirc
Klient IRC dla KDE.

%description -l pt_BR ksirc
Cliente de IRC do KDE.

%package kit
Summary:	KDE AOL Instant Messenger
Summary(pl):	Klient AOL Instant Messenger dla KDE
Summary(pt_BR):	Comunicador que usa o protocolo AOL
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(es):	X11/Aplicaciones
Group(pl):	X11/Aplikacje
Group(pt_BR):	X11/AplicaÁıes
Group(pt):	X11/AplicaÁıes
Requires:	kdelibs >= %{version}

%description kit
KDE AOL Instant Messenger.

%description -l pl kit
Klient AOL Instant Messenger dla KDE.

%description -l pt_BR kit
Comunicador que usa o protocolo AOL.

%package knewsticker
Summary:	KDE News Ticker
Summary(pt_BR):	Miniaplicativo de exibiÁ„o de notÌcias para o painel Kicker
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(es):	X11/Aplicaciones
Group(pl):	X11/Aplikacje
Group(pt_BR):	X11/AplicaÁıes
Group(pt):	X11/AplicaÁıes
Requires:	kdelibs >= %{version}

%description knewsticker
KDE News Ticker.

%description -l pt_BR knewsticker
Miniaplicativo de exibiÁ„o de notÌcias para o painel Kicker.

%package lanbrowser
Summary:	KDE Lan Browser
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(es):	X11/Aplicaciones
Group(pl):	X11/Aplikacje
Group(pt_BR):	X11/AplicaÁıes
Group(pt):	X11/AplicaÁıes
Requires:	kdelibs >= %{version}

%description lanbrowser
KDE Lan Browser.

%package kdict
Summary:	Online dictionary client
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(es):	X11/Aplicaciones
Group(pl):	X11/Aplikacje
Group(pt_BR):	X11/AplicaÁıes
Group(pt):	X11/AplicaÁıes
Requires:	kdelibs >= %{version}

%description kdict
Online dictionary client.

%description -l pt_BR kdict
kdict È um utilit·rio de dicion·rio que usa servidores dictd da
internet.

%package devel
Summary:	Header files and development documentation
Summary(pt_BR):	Arquivos de inclus„o para compilar aplicaÁıes que usem as bibliotecas do kdenetwork
Group:		X11/Development/Libraries
Group(de):	X11/Entwicklung/Libraries
Group(es):	X11/Desarrollo/Bibliotecas
Group(fr):	X11/Development/Librairies
Group(pl):	X11/Programowanie/Biblioteki
Group(pt_BR):	X11/Desenvolvimento/Bibliotecas
Group(ru):	X11/Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):	X11/Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…
Requires:	kdelibs = %{version}

%description devel
Header files and development documentation.

%description -l pt_BR devel
Arquivos de inclus„o para compilar aplicaÁıes que usem as bibliotecas
do kdenetwork.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir

%{__make} -f Makefile.cvs
%configure \
	--%{!?debug:dis}%{?debug:en}able-debug \
	--enable-kernel-threads \
 	--with-pam="yes"
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_applnkdir}/Network/{Communications,Mail,News,Misc}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install kmail/KMail.desktop		$RPM_BUILD_ROOT%{_applnkdir}/Network/Mail
install kmailcvt/kmailcvt.desktop	$RPM_BUILD_ROOT%{_applnkdir}/Network/Mail
install korn/KOrn.desktop		$RPM_BUILD_ROOT%{_applnkdir}/Network/Mail
install knode/KNode.desktop		$RPM_BUILD_ROOT%{_applnkdir}/Network/News
install ksirc/ksirc.desktop		$RPM_BUILD_ROOT%{_applnkdir}/Network/Communications
install kppp/Kppp.desktop 		$RPM_BUILD_ROOT%{_applnkdir}/Network/Misc
install kppp/logview/kppplogview.desktop 	$RPM_BUILD_ROOT%{_applnkdir}/Network/Misc
install kit/kit.desktop 		$RPM_BUILD_ROOT%{_applnkdir}/Network/Misc
install kdict/kdict.desktop		$RPM_BUILD_ROOT%{_applnkdir}/Network/Misc

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post   kdict  -p /sbin/ldconfig
%postun kdict -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmimelib.la
%attr(755,root,root) %{_libdir}/libmimelib.so.*.*
%attr(755,root,root) %{_libdir}/libkdenetwork.la
%attr(755,root,root) %{_libdir}/libkdenetwork.so.*.*

%files kmail
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kmail
%attr(755,root,root) %{_bindir}/kmailcvt
%{_applnkdir}/Network/Mail/KMail.desktop
%{_applnkdir}/Network/Mail/kmailcvt.desktop
%{_datadir}/apps/kmail
%{_htmldir}/en/kmail
%{_pixmapsdir}/hicolor/*x*/apps/kmail*.png

%files korn
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/korn
%{_applnkdir}/Network/Mail/KOrn.desktop
%{_htmldir}/en/korn
%{_pixmapsdir}/hicolor/*x*/apps/korn.png

%files kppp
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kppplogview
%attr(755,root,root) %{_bindir}/kppp
%{_applnkdir}/Network/Misc/Kppp.desktop
%{_applnkdir}/Network/Misc/kppplogview.desktop
%{_datadir}/apps/kppp
%{_htmldir}/en/kppp
%{_pixmapsdir}/hicolor/*x*/apps/kppp.png

%files knode
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/knode
%{_applnkdir}/Network/News/KNode.desktop
%{_datadir}/apps/knode
%{_htmldir}/en/knode
%{_pixmapsdir}/hicolor/*x*/apps/knode.png

%files ksirc
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ksirc
%attr(755,root,root) %{_bindir}/dsirc
%attr(755,root,root) %{_libdir}/ksirc.*
%attr(755,root,root) %{_libdir}/libkntsrcfilepropsdlg.??
%{_applnkdir}/Network/Communications/ksirc.desktop
%{_datadir}/config/ksircrc
%{_datadir}/apps/ksirc
%{_datadir}/services/kntsrcfilepropsdlg.desktop
%{_htmldir}/en/ksirc
%{_pixmapsdir}/hicolor/*x*/apps/ksirc.png

%files kit
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kit
%{_applnkdir}/Network/Misc/kit.desktop
%{_htmldir}/en/kit
%{_datadir}/apps/kit
%{_pixmapsdir}/hicolor/*x*/apps/kit.png

%files knewsticker
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/knewstickerstub
%attr(755,root,root) %{_bindir}/ksticker
%attr(755,root,root) %{_libdir}/lib*newsticker*
%{_applnkdir}/Settings/Personalization/kcmnewsticker.desktop
%{_applnkdir}/Settings/Network/kcmnewsticker.desktop
%{_applnkdir}/.hidden/knewstickerstub.desktop
%{_datadir}/services/knewsservice.protocol
%{_datadir}/apps/knewsticker
%{_datadir}/apps/kicker/applets/knewsticker.desktop
%{_datadir}/apps/kconf_update/*
%{_pixmapsdir}/hicolor/*x*/apps/knewsticker.png

%files lanbrowser
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/reslisa
%attr(755,root,root) %{_bindir}/lisa
%attr(755,root,root) %{_libdir}/lib*lanbrowser*
%attr(755,root,root) %{_libdir}/kio_lan.??
%{_applnkdir}/Settings/Network/lanbrowser.desktop
%{_datadir}/services/rlan.protocol
%{_datadir}/services/lan.protocol
%{_datadir}/apps/lisa
%{_datadir}/apps/konqueror/dirtree/remote/lan.desktop

%files kdict
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kdict
%attr(755,root,root) %{_libdir}/libkdictapplet.la
%attr(755,root,root) %{_libdir}/libkdictapplet.so.*.*
%{_datadir}/apps/kdict
%{_datadir}/apps/kicker/applets/kdictapplet.desktop
%{_pixmapsdir}/*/*/*/kdict*
%{_applnkdir}/Network/Misc/kdict.desktop

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libkdictapplet.so
%attr(755,root,root) %{_libdir}/libmimelib.so
%attr(755,root,root) %{_libdir}/libkdenetwork.so
%{_includedir}/*
