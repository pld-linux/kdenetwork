# Conditional build:
# _kmail_toolbars_patch		- aplies patch assigning icons
#				  to some toolbar buttons in kmail
# _with_pixmapsubdirs		- leave different depth/resolution icons
#
Summary:	K Desktop Environment - network applications
Summary(es):	K Desktop Environment - aplicaciones de red
Summary(ko):	K 데스크탑 환경 - 네트웍 응용 프로그램
Summary(pl):	K Desktop Environment - aplikacje sieciowe
Summary(pt_BR):	K Desktop Environment - aplica寤es de rede
Name:		kdenetwork
Version:	3.0.4
Release:	10
Epoch:		8
License:	GPL
Vendor:		The KDE Team
Group:		X11/Applications
Source0:	ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-%{version}.tar.bz2
# generated from kde-i18n
Source1:	kde-i18n-%{name}-%{version}.tar.bz2
Source2:	lisa.init
Source3:	lisa.sysconfig
Source4:	%{name}-lisarc
Patch0:		%{name}-use_sendmail.patch
Patch1:		%{name}-kmail_toolbars.patch
Patch2:		%{name}-fix-kio_lan.patch
Patch3:		%{name}-fix-sync-config-when-we-close-config-dialogbox.patch
Patch4:		%{name}-fix-kpgp-mem-leak.patch
Patch5:		%{name}-fix-copy-link-location.patch
Patch6:		%{name}-launch-spellchecking-config-when-it-didnot-configurate.patch
Patch7:		%{name}-disable-enable-ok-button-in-new-channel.patch
Patch8:		%{name}-no_versioned_modules.patch
# Security fix from 3.0.5
Patch9:		%{name}-lan.patch
Patch10:	%{name}-desktop.patch
# ported from lisa.spec
Patch11:	%{name}-lisa_net_auto_conf.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	awk
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

%define		no_install_post_chrpath		1
%define		_with_pixmapsubdirs		1

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
- KMail - program pocztowy, z poprawion� obs퀅g� zestaw�w znak�w
- KORN - program pokazuj켧y stan skrzynek pocztowych
- KPPP - program do nawi콄ywania po낢cze� modemowych
- KNODE - program do czytania news�w
- KSirc - klient IRC
- KIT - klient AOL Instant Messenger
- KNewsticker - News Ticker
- Lanbrowser - przegl켨arka LAN-u
- KDict - klient s쿽wnika
- KXmlRpcd - demon XmlRpc
- KPF - applet publicznego serwera plik�w
- KTalkd - demon Talk

%description -l pt_BR
Aplica寤es de Rede para o KDE.

Inclu�dos neste pacote:

kmail: leitor de correio knu: utilit�rios de rede korn: ferramenta de
monitora豫o da caixa de correio kppp: configura豫o f�cil para conex�o
PPP krn: leitor de not�cias

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
Program pocztowy dla KDE. Potrafi odczytywa� poczt� z kont POP3 jak i
lokalnych skrzynek.

Ten pakiet zawiera wersj� programu z poprawion� obs퀅g� zestaw�w
znak�w.

%description kmail -l pt_BR
Poderoso cliente / leitor de e-mails para o KDE.

%package korn
Summary:	KDE 'biff' application
Summary(pl):	Wska펝ik skrzynki pocztowej dla KDE
Summary(pt_BR):	Miniaplicativo de monitora豫o da caixa de correio
Group:		X11/Applications
Requires:	kdelibs >= %{version}

%description korn
A simple program showing number of mails in your folders.

%description korn -l pl
Programik pokazuj켧y ilo뜻 wiadomo턢i w wybranych folderach
pocztowych.

%description korn -l pt_BR
Miniaplicativo de monitora豫o da caixa de correio.

%package kppp
Summary:	KDE PPP dialer
Summary(ko):	KDE용 PPP 설정 도구
Summary(pl):	Program do po낢cze� modemowych dla KDE
Summary(pt_BR):	O discador para Internet
Group:		X11/Applications
Requires:	kdelibs >= %{version}
Requires:	ppp

%description kppp
A PPPP dialer for KDE. It supports multiple accounts.

%description kppp -l pl
Program no nawi콄ywania po낢cze� modemowych pod KDE. Posiada 쿪twy
interfejs i mo퓄iwo뜻 zdefiniowania kilku kont.

%description kppp -l pt_BR
O discador para Internet.

%package knode
Summary:	KDE News Reader
Summary(pl):	Czytnik news�w dla KDE
Summary(pt_BR):	Leitor de not�cias (news) do KDE
Group:		X11/Applications
Requires:	kdelibs >= %{version}

%description knode
This is a news reader for KDE. It has threading and everything else
you need to be happy reading your news.

%description knode -l pl
Czytnik news�w dla KDE. Obs퀅guje w켾ki oraz killfile.

%description knode -l pt_BR
Leitor de not�cias (news) do KDE.

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
License:	LGPL
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
Summary(pt_BR):	Miniaplicativo de exibi豫o de not�cias para o painel Kicker
Group:		X11/Applications
Requires:	kdelibs >= %{version}

%description knewsticker
KDE News Ticker.

%description knewsticker -l pl
News Ticker dla KDE.

%description knewsticker -l pt_BR
Miniaplicativo de exibi豫o de not�cias para o painel Kicker.

%package lanbrowser
Summary:	KDE LAN browser libraries
Summary(pl):	Biblioteki przegl켨arki LAN-u dla KDE
Group:		X11/Applications
Requires:	lisa
Requires:	kdelibs >= %{version}

%description lanbrowser
KDE LAN browser libraries.

%description lanbrowser -l pl
Biblioteki przegl켨arki LAN-u dla KDE.

%package lisa
Summary:	KDE LAN information server
Summary(pl):	Serwer informacji o LAN-ie dla KDE
Group:		Networking/Daemons
Requires(post,preun):/sbin/chkconfig
Obsoletes:	lisa
Provides:	lisa
Conflicts:	%{name}-lanbrowser <= 3.0.4-9

%description lisa
KDE LAN information server.

%description lisa -l pl
Serwer informacji o LAN-ie dla KDE.

%package kdict
Summary:	Online dictionary client
Summary(pl):	Klient s쿽wnika
License:	Artistic
Group:		X11/Applications
Requires:	kdelibs >= %{version}
Provides:	kdict
Obsoletes:	kdict

%description kdict
Online dictionary client.

%description kdict -l pl
Klient s쿽wnika.

%description kdict -l pt_BR
kdict � um utilit�rio de dicion�rio que usa servidores dictd da
Internet.

%package kxmlrpcd
Summary:	KDE XmlRpc Daemon
Summary(pl):	Deamon XmlRpc dla KDE
Group:		X11/Applications
Requires:	kdelibs = %{version}

%description kxmlrpcd
KDE XmlRpc Daemon.

%description kxmlrpcd -l pl
Demon XmlRpc dla KDE.

%package kpf
Summary:	Public fileserver applet
Summary(pl):	Applet publicznego serwera plik�w
Group:		X11/Applications
Requires:	kdelibs = %{version}

%description kpf
Public fileserver applet.

%description kpf -l pl
Applet publicznego serwera plik�w.

%package ktalkd
Summary:	Talk daemon
Summary(pl):	Daemon talk
Group:		X11/Applications
Requires:	kdelibs = %{version}

%description ktalkd
Talk daemon.

%description ktalkd -l pl
Demon talk.

%package devel
Summary:	Header files and development documentation
Summary(pl):	Pliki nag농wkowe i dokumentacja developerska
Summary(pt_BR):	Arquivos de inclus�o para compilar aplica寤es que usem as bibliotecas do kdenetwork
Group:		X11/Development/Libraries
Requires:	kdelibs = %{version}

%description devel
Header files and development documentation.

%description devel -l pl
Pliki nag농wkowe i dokumentacja developerska.

%description devel -l pt_BR
Arquivos de inclus�o para compilar aplica寤es que usem as bibliotecas
do kdenetwork.

%prep
%setup	-q
%patch0 -p1
%if%{?_with_kmail_toolbars_patch:1}%{!?_with_kmail_toolbars_patch:0}
%patch1 -p1
%endif
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1

%build
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir

kde_cv_utmp_file=/var/run/utmpx ; export kde_cv_utmp_file
%configure \
	--%{!?debug:dis}%{?debug:en}able-debug \
	--enable-kernel-threads \
	--with-pam="yes" \
	--disable-rpath \
	--enable-final
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_applnkdir}{/Settings/KDE,/Network/{Communications,Mail,News,Misc}} \
	$RPM_BUILD_ROOT{/etc/{rc.d/init.d,sysconfig},%{_sysconfdir},/usr/bin}

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

mv -f $RPM_BUILD_ROOT%{_pixmapsdir}{/hicolor/48x48/apps/*,}

mv -f $RPM_BUILD_ROOT%{_bindir}/{res,}lisa $RPM_BUILD_ROOT/usr/bin

install %{SOURCE2} $RPM_BUILD_ROOT/etc/rc.d/init.d/lisa
install %{SOURCE3} $RPM_BUILD_ROOT/etc/sysconfig/lisa
install %{SOURCE4} $RPM_BUILD_ROOT%{_sysconfdir}/lisarc

bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT

for f in `find $RPM_BUILD_ROOT%{_applnkdir} -name '.directory' -o -name '*.desktop'` ; do
	awk -v F=$f '/^Icon=/ && !/\.xpm$/ && !/\.png$/ { $0 = $0 ".png";} { print $0; } END { if(F == ".directory") print "Type=Directory"; }' < $f > $f.tmp
	mv -f $f{.tmp,}
done

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
cat kio_lan.lang >> kcmlanbrowser.lang
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

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post	kdict -p /sbin/ldconfig
%postun kdict -p /sbin/ldconfig

%post lisa
/sbin/chkconfig --add lisa
if [ -r /var/lock/subsys/lisa ]; then
	/etc/rc.d/init.d/lisa restart >&2
else
	echo "Run \"/etc/rc.d/init.d/lisa start\" to start Lisa daemon."
fi

%preun lisa
if [ "$1" = "0" ]; then
	if [ -r /var/lock/subsys/lisa ]; then
		/etc/rc.d/init.d/lisa stop >&2
	fi
	/sbin/chkconfig --del lisa
fi

%files -f libkdenetwork.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmimelib.so.*.*
%attr(755,root,root) %{_libdir}/libkdenetwork.so.*.*

%files kmail -f kmail.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kmail
%attr(755,root,root) %{_bindir}/kmailcvt
%{_applnkdir}/Network/Mail/KMail.desktop
%{_applnkdir}/Network/Mail/kmailcvt.desktop
%{_datadir}/apps/kmail
%{?_with_pixmapsubdirs:%{_pixmapsdir}/hicolor/*x*/apps/kmail*.png}
%{_pixmapsdir}/kmail*.png

%files korn -f korn.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/korn
%{_applnkdir}/Network/Mail/KOrn.desktop
%{?_with_pixmapsubdirs:%{_pixmapsdir}/hicolor/*x*/apps/korn.png}
%{_pixmapsdir}/korn.png

%files kppp -f kppp.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kppplogview
%attr(755,root,root) %{_bindir}/kppp
%{_applnkdir}/Network/Misc/Kppp.desktop
%{_applnkdir}/Network/Misc/kppplogview.desktop
%{_datadir}/apps/kppp
%{?_with_pixmapsubdirs:%{_pixmapsdir}/hicolor/*x*/apps/kppp.png}
%{_pixmapsdir}/kppp.png

%files knode -f knode.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/knode
%{_applnkdir}/Network/News/KNode.desktop
%{_datadir}/apps/knode
%{?_with_pixmapsubdirs:%{_pixmapsdir}/hicolor/*x*/apps/knode.png}
%{_pixmapsdir}/knode.png

%files ksirc -f ksirc.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ksirc
%attr(755,root,root) %{_bindir}/dsirc
%attr(755,root,root) %{_libdir}/ksirc.so
#%{_libdir}/ksirc.la
%attr(755,root,root) %{_libdir}/libkntsrcfilepropsdlg.so
#%{_libdir}/libkntsrcfilepropsdlg.la
%{_applnkdir}/Network/Communications/ksirc.desktop
%{_datadir}/config/ksircrc
%{_datadir}/apps/ksirc
%{_datadir}/services/kntsrcfilepropsdlg.desktop
%{?_with_pixmapsubdirs:%{_pixmapsdir}/*color/*x*/apps/ksirc.png}
%{_pixmapsdir}/ksirc.png

%files kit -f kit.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kit
%{_applnkdir}/Network/Misc/kit.desktop
%{_datadir}/apps/kit
%{?_with_pixmapsubdirs:%{_pixmapsdir}/hicolor/*x*/apps/kit.png}
%{_pixmapsdir}/kit.png

%files knewsticker -f knewsticker.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/knewstickerstub
%attr(755,root,root) %{_libdir}/kde3/knewsticker_applet.so
%{_libdir}/kde3/knewsticker_applet.la
%attr(755,root,root) %{_libdir}/kde3/libkcm_newsticker.so
%{_libdir}/kde3/libkcm_newsticker.la
%{_applnkdir}/Settings/KDE/Personalization/kcmnewsticker.desktop
%{_applnkdir}/Settings/KDE/Network/kcmnewsticker.desktop
%{_applnkdir}/Network/News/knewsticker*.desktop
%{_applnkdir}/.hidden/knewstickerstub.desktop
%{_datadir}/services/knewsservice.protocol
%{_datadir}/apps/knewsticker
%{_datadir}/apps/kicker/applets/knewsticker.desktop
%{_datadir}/apps/kconf_update/*
%{?_with_pixmapsubdirs:%{_pixmapsdir}/hicolor/*x*/apps/knewsticker.png}
%{_pixmapsdir}/knewsticker.png

%files lanbrowser -f kcmlanbrowser.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/libkcm_lanbrowser.so
%{_libdir}/kde3/libkcm_lanbrowser.la
%attr(755,root,root) %{_libdir}/kio_lan.so
%{_libdir}/kio_lan.la
%{_applnkdir}/Settings/KDE/Network/lanbrowser.desktop
%{_datadir}/services/rlan.protocol
%{_datadir}/services/lan.protocol
%{_datadir}/apps/lisa
%{_datadir}/apps/konqueror/dirtree/remote/lan.desktop

%files lisa -f lisa.lang
%defattr(644,root,root,755)
%attr(755,root,root) /usr/bin/reslisa
%attr(755,root,root) /usr/bin/lisa
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/lisarc
%config(noreplace) %verify(not size mtime md5) /etc/sysconfig/lisa
%attr(754,root,root) /etc/rc.d/init.d/lisa

%files kdict -f kdict.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kdict
%{_libdir}/kde3/kdictapplet.la
%attr(755,root,root) %{_libdir}/kde3/kdictapplet.so
%{_datadir}/apps/kdict
%{_datadir}/apps/kicker/applets/kdictapplet.desktop
%{_applnkdir}/Utilities/kdict.desktop
%{?_with_pixmapsubdirs:%{_pixmapsdir}/hicolor/*x*/apps/kdict.png}
%{_pixmapsdir}/kdict.png

%files kxmlrpcd -f kxmlrpcd.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kxmlrpcd
%attr(755,root,root) %{_libdir}/kxmlrpcd.so
%{_libdir}/kxmlrpcd.la
%attr(755,root,root) %{_libdir}/kde3/libkcm_xmlrpcd.so
%{_libdir}/kde3/libkcm_xmlrpcd.la
%attr(755,root,root) %{_libdir}/kde3/libkcm_kcmkxmlrpcd.so
%{_libdir}/kde3/libkcm_kcmkxmlrpcd.la
%{_datadir}/services/kxmlrpcd.desktop
%{_applnkdir}/Settings/KDE/System/kcmkxmlrpcd.desktop

%files kpf -f kpf.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/kpfapplet.so
%attr(755,root,root) %{_libdir}/kde3/kpfapplet.la
%attr(755,root,root) %{_libdir}/kde3/kpfpropertiesdialogplugin.so
%attr(755,root,root) %{_libdir}/kde3/kpfpropertiesdialogplugin.la
%{_datadir}/apps/kicker/applets/kpf*
%{_datadir}/services/kpfpropertiesdialogplugin.desktop
%{?_with_pixmapsubdirs:%{_pixmapsdir}/hicolor/*x*/apps/kpf*}
%{_pixmapsdir}/kpf*

%files ktalkd -f ktalkd.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/k*talkd*
%attr(755,root,root) %{_libdir}/kde3/libkcm_ktalkd.so
%{_libdir}/kde3/libkcm_ktalkd.la
%{_datadir}/config/ktalkd*
%{_datadir}/sounds/ktalkd*
%{_applnkdir}/Settings/KDE/Network/kcmktalkd.desktop
%{?_with_pixmapsubdirs:%{_pixmapsdir}/hicolor/*x*/apps/ktalkd*}
%{_pixmapsdir}/ktalkd*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmimelib.so
%attr(755,root,root) %{_libdir}/libkdenetwork.so
%{_libdir}/libmimelib.la
%{_libdir}/libkdenetwork.la
%{_includedir}/*
