# Conditional build:
#	--with		kmail_toolbars_patch	aplies patch assigning icons
#						to some toolbar buttons in kmail
Summary:	K Desktop Environment - network applications
Summary(es):	K Desktop Environment - aplicaciones de red
Summary(pl):	K Desktop Environment - aplikacje sieciowe
Summary(pt_BR):	K Desktop Environment - aplicações de rede
Name:		kdenetwork
Version:	3.0.3
Release:	2
Epoch:		8
License:	GPL
Vendor:		The KDE Team
Group:		X11/Applications
Source0:	ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-%{version}.tar.bz2
# generated from kde-i18n
Source1:	kde-i18n-%{name}-%{version}.tar.bz2
Patch0:		%{name}-am15.patch
Patch1:		%{name}-utmpx.patch
Patch2:		%{name}-use_sendmail.patch
%{?_with_kmail_toolbars_patch:Patch3: %{name}-kmail_toolbars.patch}
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	fam-devel
BuildRequires:	gettext-devel
BuildRequires:	kdelibs-devel >= %{version}
BuildRequires:	libtool
BuildRequires:	libxml2-progs
BuildRequires:	qt-devel >= 3.0.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_fontdir	/usr/share/fonts
%define		_htmldir	/usr/share/doc/kde/HTML

%description
KDE network applications. Package includes:
- KMail - e-mail client. Patched for proper charsets support
- KORN - "biff" program
- KPPP - PPP dialer
- KNODE - news client
- KSirc - IRC client
- KIT - AOL Instant Messenger
- KNewsticker - News Ticker
- Lanbrowser - LAN Browser
- KDict - Online dictionary client
- KXmlRpcd - XmlRpc Daemon
- KPF - Public fileserver applet
- KTalkd - takt daemon

%description -l pl
Aplikacje sieciowe KDE. Pakiet zawiera:
- KMail - program pocztowy, z poprawion± obs³ug± zestawów znaków
- KORN - program pokazuj±cy stan skrzynek pocztowych
- KPPP - program do nawi±zywania po³±czeñ modemowych
- KNODE - Program do czytania newsów
- KSirc - Klient IRC
- KIT - klient AOL Instant Messenger
- KNewsticker - News Ticker
- Lanbrowser - Przegl±darka LAN-u
- KDict - Klient s³ownika
- KXmlRpcd - Daemon XmlRpc
- KPF - Applet publicznego serwera plików
- KTalkd - Daemon Talk

%description -l pt_BR
Aplicações de Rede para o KDE.

Incluídos neste pacote:

kmail: leitor de correio knu: utilitários de rede korn: ferramenta de
monitoração da caixa de correio kppp: configuração fácil para conexão
PPP krn: leitor de notícias

%package kmail
Summary:	KDE Mail client
Summary(pl):	Program pocztowy KDE
Summary(pt_BR):	Cliente / leitor de e-mails para o KDE
Group:		X11/Applications
Requires:	kdelibs >= %{version}

%description kmail
This is electronic mail client for KDE. It is able to retrievie mail
from POP3 accounts and from local mailboxes.

This package contains version patched for better charset support.

%description kmail -l pl
Program pocztowy dla KDE. Potrafi odczytywaæ pocztê z kont POP3 jak i
lokalnych skrzynek.

Ten pakiet zawiera wersj± programu z poprawion± obs³ug± zestawów
znaków.

%description kmail -l pt_BR
Poderoso cliente / leitor de e-mails para o KDE.

%package korn
Summary:	KDE 'biff' application
Summary(pl):	Wska¼nik skrzynki pocztowej dla KDE
Summary(pt_BR):	Miniaplicativo de monitoração da caixa de correio
Group:		X11/Applications
Requires:	kdelibs >= %{version}

%description korn
A simple program showing number of mails in your folders.

%description korn -l pl
Programik pokazuj±cy ilo¶æ wiadomo¶ci w wybranych folderach
pocztowych.

%description korn -l pt_BR
Miniaplicativo de monitoração da caixa de correio.

%package kppp
Summary:	KDE PPP dialer
Summary(pl):	Program do po³±czeñ modemowych dla KDE
Summary(pt_BR):	O discador para Internet
Group:		X11/Applications
Requires:	kdelibs >= %{version}
Requires:	ppp

%description kppp
A PPPP dialer for KDE. It supports multiple accounts.

%description kppp -l pl
Program no nawi±zywania po³±czeñ modemowych pod KDE. Posiada ³atwy
interfejs i mo¿liwo¶æ zdefiniowania kilku kont.

%description kppp -l pt_BR
O discador para Internet.

%package knode
Summary:	KDE News Reader
Summary(pl):	Czytnik newsów dla KDE
Summary(pt_BR):	Leitor de notícias (news) do KDE
Group:		X11/Applications
Requires:	kdelibs >= %{version}

%description knode
This is a news reader for KDE. It has threading and everything else
you need to be happy reading your news.

%description knode -l pl
Czytnik newsów dla KDE. Obs³uguje w±tki oraz killfile.

%description knode -l pt_BR
Leitor de notícias (news) do KDE.

%package ksirc
Summary:	KDE IRC client
Summary(pl):	Klient IRC dla KDE
Summary(pt_BR):	Cliente de IRC do KDE
Group:		X11/Applications
Requires:	kdelibs >= %{version}

%description ksirc
KDE IRC client.

%description ksirc -l pl
Klient IRC dla KDE.

%description ksirc -l pt_BR
Cliente de IRC do KDE.

%package kit
Summary:	KDE AOL Instant Messenger
Summary(pl):	Klient AOL Instant Messenger dla KDE
Summary(pt_BR):	Comunicador que usa o protocolo AOL
Group:		X11/Applications
Requires:	kdelibs >= %{version}

%description kit
KDE AOL Instant Messenger.

%description kit -l pl
Klient AOL Instant Messenger dla KDE.

%description kit -l pt_BR
Comunicador que usa o protocolo AOL.

%package knewsticker
Summary:	KDE News Ticker
Summary(pl):	News Ticker dla KDE
Summary(pt_BR):	Miniaplicativo de exibição de notícias para o painel Kicker
Group:		X11/Applications
Requires:	kdelibs >= %{version}

%description knewsticker
KDE News Ticker.

%description knewsticker -l pl
News Ticker dla KDE.

%description knewsticker -l pt_BR
Miniaplicativo de exibição de notícias para o painel Kicker.

%package lanbrowser
Summary:	KDE LAN Browser
Summary(pl):	Przegl±darka LAN-u dla KDE
Group:		X11/Applications
Requires:	kdelibs >= %{version}

%description lanbrowser
KDE LAN Browser.

%description lanbrowser
Przegl±darka LAN-u dla KDE.

%package kdict
Summary:	Online dictionary client
Summary(pl):	Klient s³ownika
Group:		X11/Applications
Requires:	kdelibs >= %{version}
Provides:	kdict
Obsoletes:	kdict

%description kdict
Online dictionary client.

%description kdict -l pl
Klient s³ownika.

%description kdict -l pt_BR
kdict é um utilitário de dicionário que usa servidores dictd da
Internet.

%package kxmlrpcd
Summary:	KDE XmlRpc Daemon
Summary(pl):	Deamon XmlRpc dla KDE
Group:		X11/Applications
Requires:	kdelibs = %{version}

%description kxmlrpcd
KDE XmlRpc Daemon.

%description kxmlrpcd -l pl
Deamon XmlRpc dla KDE.

%package kpf
Summary:	Public fileserver applet
Summary(pl):	Applet publicznego serwera plików
Group:		X11/Applications
Requires:	kdelibs = %{version}

%description kpf
Public fileserver applet.

%description kpf -l pl
Applet publicznego serwera plików.

%package ktalkd
Summary:	Talk daemon
Summary(pl):	Daemon talk
Group:		X11/Applications
Requires:	kdelibs = %{version}

%description ktalkd
Talk daemon.

%description ktalkd -l pl
Daemon talk.

%package devel
Summary:	Header files and development documentation
Summary(pl):	Pliki nag³ówkowe i dokumentacja developerska
Summary(pt_BR):	Arquivos de inclusão para compilar aplicações que usem as bibliotecas do kdenetwork
Group:		X11/Development/Libraries
Requires:	kdelibs = %{version}

%description devel
Header files and development documentation.

%description devel -l pl
Pliki nag³ówkowe i dokumentacja developerska.

%description devel -l pt_BR
Arquivos de inclusão para compilar aplicações que usem as bibliotecas
do kdenetwork.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%if%{?_with_kmail_toolbars_patch:1}%{!?_with_kmail_toolbars_patch:0}
%patch3 -p1
%endif

%build
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir

kde_cv_utmp_file=/var/run/utmpx ; export kde_cv_utmp_file
%configure \
	--%{!?debug:dis}%{?debug:en}able-debug \
	--enable-kernel-threads \
	--with-pam="yes" \
	--enable-final
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_applnkdir}{/Settings/KDE,/Network/{Communications,Mail,News,Misc}}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

mv $RPM_BUILD_ROOT%{_applnkdir}/{Internet,Network/Mail}/KMail.desktop
mv $RPM_BUILD_ROOT%{_applnkdir}/{Internet,Network/News}/KNode.desktop
mv $RPM_BUILD_ROOT%{_applnkdir}/{Internet,Network/Mail}/KOrn.desktop
mv $RPM_BUILD_ROOT%{_applnkdir}/{Utilities,Network/Mail}/kmailcvt.desktop
mv $RPM_BUILD_ROOT%{_applnkdir}/{Internet,Network/Misc}/Kppp.desktop
mv $RPM_BUILD_ROOT%{_applnkdir}/{Internet,Network/Misc}/kit.desktop
mv $RPM_BUILD_ROOT%{_applnkdir}/{Internet,Network/News}/knewsticker-standalone.desktop
mv $RPM_BUILD_ROOT%{_applnkdir}/{Internet,Network/Misc}/kppplogview.desktop
mv $RPM_BUILD_ROOT%{_applnkdir}/{Internet,Network/Communications}/ksirc.desktop
mv $RPM_BUILD_ROOT%{_applnkdir}/Settings/[!K]* $RPM_BUILD_ROOT%{_applnkdir}/Settings/KDE/

bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT

%find_lang kdict --with-kde
%find_lang kdictapplet --with-kde
cat kdictapplet.lang >> kdict.lang
%find_lang knewsticker --with-kde
%find_lang kcmnewsticker --with-kde
cat kcmnewsticker.lang >> knewsticker.lang
%find_lang kpf --with-kde
%find_lang ktalkd --with-kde
%find_lang kcmktalkd --with-kde
cat kcmktalkd.lang >> ktalkd.lang
%find_lang lisa --with-kde
%find_lang kcmlanbrowser --with-kde
%find_lang kio_lan --with-kde
cat kcmlanbrowser.lang kio_lan.lang >> lisa.lang
%find_lang kit --with-kde
%find_lang kmail --with-kde
%find_lang kmailcvt --with-kde
cat kmailcvt.lang >> kmail.lang
%find_lang knode --with-kde
%find_lang korn --with-kde
%find_lang kppp --with-kde
%find_lang kppplogview --with-kde
cat kppplogview.lang >> kppp.lang
%find_lang ksirc --with-kde
%find_lang kxmlrpcd --with-kde
%find_lang kcmkxmlrpcd --with-kde
cat kcmkxmlrpcd.lang >> kxmlrpcd.lang
%find_lang libkdenetwork --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post   kdict -p /sbin/ldconfig
%postun kdict -p /sbin/ldconfig

%files -f libkdenetwork.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmimelib.la
%attr(755,root,root) %{_libdir}/libmimelib.so.*.*
%attr(755,root,root) %{_libdir}/libkdenetwork.la
%attr(755,root,root) %{_libdir}/libkdenetwork.so.*.*

%files kmail -f kmail.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kmail
%attr(755,root,root) %{_bindir}/kmailcvt
%{_applnkdir}/Network/Mail/KMail.desktop
%{_applnkdir}/Network/Mail/kmailcvt.desktop
%{_datadir}/apps/kmail
%{_pixmapsdir}/hicolor/*x*/apps/kmail*.png

%files korn -f korn.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/korn
%{_applnkdir}/Network/Mail/KOrn.desktop
%{_pixmapsdir}/hicolor/*x*/apps/korn.png

%files kppp -f kppp.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kppplogview
%attr(755,root,root) %{_bindir}/kppp
%{_applnkdir}/Network/Misc/Kppp.desktop
%{_applnkdir}/Network/Misc/kppplogview.desktop
%{_datadir}/apps/kppp
%{_pixmapsdir}/hicolor/*x*/apps/kppp.png

%files knode -f knode.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/knode
%{_applnkdir}/Network/News/KNode.desktop
%{_datadir}/apps/knode
%{_pixmapsdir}/hicolor/*x*/apps/knode.png

%files ksirc -f ksirc.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ksirc
%attr(755,root,root) %{_bindir}/dsirc
%attr(755,root,root) %{_libdir}/ksirc.*
%attr(755,root,root) %{_libdir}/libkntsrcfilepropsdlg.??
%{_applnkdir}/Network/Communications/ksirc.desktop
%{_datadir}/config/ksircrc
%{_datadir}/apps/ksirc
%{_datadir}/services/kntsrcfilepropsdlg.desktop
%{_pixmapsdir}/*/*/*/ksirc*

%files kit -f kit.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kit
%{_applnkdir}/Network/Misc/kit.desktop
%{_datadir}/apps/kit
%{_pixmapsdir}/hicolor/*x*/apps/kit.png

%files knewsticker -f knewsticker.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/knewstickerstub
%attr(755,root,root) %{_libdir}/kde3/knewsticker_applet.??
%attr(755,root,root) %{_libdir}/kde3/libkcm_newsticker.??
%{_applnkdir}/Settings/KDE/Personalization/kcmnewsticker.desktop
%{_applnkdir}/Settings/KDE/Network/kcmnewsticker.desktop
%{_applnkdir}/Network/News/knewsticker*.desktop
%{_applnkdir}/.hidden/knewstickerstub.desktop
%{_datadir}/services/knewsservice.protocol
%{_datadir}/apps/knewsticker
%{_datadir}/apps/kicker/applets/knewsticker.desktop
%{_datadir}/apps/kconf_update/*
%{_pixmapsdir}/hicolor/*x*/apps/knewsticker.png

%files lanbrowser -f lisa.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/reslisa
%attr(755,root,root) %{_bindir}/lisa
%attr(755,root,root) %{_libdir}/kde3/libkcm_lanbrowser.??
%attr(755,root,root) %{_libdir}/kio_lan.??
%{_applnkdir}/Settings/KDE/Network/lanbrowser.desktop
%{_datadir}/services/rlan.protocol
%{_datadir}/services/lan.protocol
%{_datadir}/apps/lisa
%{_datadir}/apps/konqueror/dirtree/remote/lan.desktop

%files kdict -f kdict.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kdict
%attr(755,root,root) %{_libdir}/kde3/kdictapplet.la
%attr(755,root,root) %{_libdir}/kde3/kdictapplet.so.*.*.*
%{_datadir}/apps/kdict
%{_datadir}/apps/kicker/applets/kdictapplet.desktop
%{_pixmapsdir}/*/*/*/kdict*
%{_applnkdir}/Utilities/kdict.desktop

%files kxmlrpcd -f kxmlrpcd.lang
%defattr(644,root,root,755)
%attr(755,root,root)%{_bindir}/kxmlrpcd
%{_libdir}/kxmlrpcd.??
%{_libdir}/kde3/libkcm_xmlrpcd.??
%{_libdir}/kde3/libkcm_kcmkxmlrpcd.??
%{_datadir}/services/kxmlrpcd.desktop
%{_applnkdir}/Settings/KDE/System/kcmkxmlrpcd.desktop

%files kpf -f kpf.lang
%defattr(644,root,root,755)
%{_libdir}/kde3/kpfapplet.??
%{_libdir}/kde3/kpfpropertiesdialogplugin.??
%{_datadir}/apps/kicker/applets/kpf*
%{_datadir}/services/kpfpropertiesdialogplugin.desktop
%{_pixmapsdir}/*/*/*/kpf*

%files ktalkd -f ktalkd.lang
%defattr(644,root,root,755)
%attr(755,root,root)%{_bindir}/k*talkd*
%{_libdir}/kde3/libkcm_ktalkd.??
%{_datadir}/config/ktalkd*
%{_datadir}/sounds/ktalkd*
%{_pixmapsdir}/*/*/*/ktalkd*
%{_applnkdir}/Settings/KDE/Network/kcmktalkd.desktop

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/kdictapplet.so
%attr(755,root,root) %{_libdir}/libmimelib.so
%attr(755,root,root) %{_libdir}/libkdenetwork.so
%{_includedir}/*
