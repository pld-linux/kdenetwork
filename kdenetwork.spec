
%define		_state		unstable
%define		_ver		3.1.92
%define		_snap		030930

Summary:	K Desktop Environment - network applications
Summary(es):	K Desktop Environment - aplicaciones de red
Summary(pl):	K Desktop Environment - aplikacje sieciowe
Summary(pt_BR):	K Desktop Environment - aplicações de rede
Name:		kdenetwork
Version:	%{_ver}.%{_snap}
Release:	1
Epoch:		10
License:	GPL
Group:		X11/Libraries
#Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{_ver}/src/%{name}-%{version}.tar.bz2
Source0:	http://www.kernel.pl/~adgor/kde/%{name}-%{_snap}.tar.bz2
# Source0-md5:	12b53a31adfd7ddc5b4f044a920e4028
Source2:	%{name}-lisa.init
Source3:        %{name}-lisa.sysconfig
Source4:        %{name}-lisarc
Patch0:		%{name}-utmpx.patch
Patch1:		%{name}-use_sendmail.patch
Patch2:		%{name}-vcategories.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	fam-devel
BuildRequires:	gettext-devel
BuildRequires:	kdelibs-devel >= 9:%{version}
BuildRequires:	libtool
BuildRequires:	libxml2-progs
BuildRequires:	openslp-devel
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		no_install_post_chrpath		1

%description
KDE network applications. Package includes:
- KDict - Online dictionary client
- KGet - file downloader
- KIT - AOL Instant Messenger
- KMail - e-mail client. Patched for proper charsets support
- KNewsticker - News Ticker
- KNODE - news client
- KORN - "biff" program
- KPF - Public fileserver applet
- KPPP - PPP dialer
- KRFB - virtual desktops
- KSirc - IRC client
- KTalkd - takt daemon
- KXmlRpcd - XmlRpc Daemon
- Lanbrowser - LAN Browser

%description -l pl
Aplikacje sieciowe KDE. Pakiet zawiera:
- KDict - klient s³ownika
- KGet - ¦ciagacz plików
- KIT - klient AOL Instant Messenger
- KMail - program pocztowy, z poprawion± obs³ug± zestawów znaków
- KORN - program pokazuj±cy stan skrzynek pocztowych
- KPF - applet publicznego serwera plików
- KPPP - program do nawi±zywania po³±czeñ modemowych
- KNewsticker - News Ticker
- KNODE - program do czytania newsów
- KRFB - wirtualne biurka
- KSirc - klient IRC
- KTalkd - demon Talk
- KXmlRpcd - demon XmlRpc
- Lanbrowser - przegl±darka LAN-u

%description -l pt_BR
Aplicações de Rede para o KDE.

Incluídos neste pacote:

kmail: leitor de correio knu: utilitários de rede korn: ferramenta de
monitoração da caixa de correio kppp: configuração fácil para conexão
PPP krn: leitor de notícias

%package devel
Summary:	TODO
Summary(pl):	TODO
Group:		X11/Development/Libraries
Requires:	%{name}-kopete = %{epoch}:%{version}-%{release}
Requires:	%{name}-rss = %{epoch}:%{version}-%{release}
Obsoletes:	%{name}-librss-devel
Obsoletes:	%{name}-rss-devel

%description devel
TODO.

%description devel -l pl
TODO.

%package kdict
Summary:	Online dictionary client
Summary(pl):	Klient s³ownika
License:	Artistic
Group:		X11/Applications
Requires:	kdebase-kicker >= 9:%{version}
Provides:	kdict

%description kdict
Online dictionary client.

%description kdict -l pl
Klient s³ownika.

%description kdict -l pt_BR
kdict é um utilitário de dicionário que usa servidores dictd da
Internet.

%package kinetd
Summary:	KDE Internet Daemon
Summary(pl):	Demon internetowy KDE
Group:		X11/Applications
Requires:	kdelibs >= 9:%{version}
Obsoletes:	%{name}-krfb < 9:3.1-6

%description kinetd
An Internet daemon that starts network services on demand.

%description kinetd -l pl
Demon internetowy, który uruchamia na ¿±danie us³ugi sieciowe.

%package kget
Summary:	File Downloander
Summary(pl):	¦ci±gacz plików
Group:		X11/Applications
Requires:	kdebase-core >= 9:%{version}

%description kget
File Downloader.

%description kget -l pl
¦ci±gacz plików.

%package knewsticker
Summary:	KDE News Ticker
Summary(pl):	News Ticker dla KDE
Summary(pt_BR):	Miniaplicativo de exibição de notícias para o painel Kicker
Group:		X11/Applications
Requires:	kdebase-kicker >= 9:%{version}

%description knewsticker
KDE News Ticker.

%description knewsticker -l pl
News Ticker dla KDE.

%description knewsticker -l pt_BR
Miniaplicativo de exibição de notícias para o painel Kicker.

%package kopete
Summary:	Multi-protocol plugin-based instant messenger
Summary(pl):	Komunikator obs³uguj±cy wiele protoko³ów
Group:		X11/Applications
Requires:	kdebase-core >= 9:%{version}
Obsoletes:	kopete
Obsoletes:	kopete-plugin-tools-autoaway
Obsoletes:	kopete-plugin-tools-autoreplace
Obsoletes:	kopete-plugin-tools-conectionstatus
Obsoletes:	kopete-plugin-tools-contactnotes
Obsoletes:	kopete-plugin-tools-cryptography
Obsoletes:	kopete-plugin-tools-history
Obsoletes:	kopete-plugin-tools-highlight
Obsoletes:	kopete-plugin-tools-importer
Obsoletes:	kopete-plugin-tools-nowlistening
Obsoletes:	kopete-plugin-tools-motionaway
Obsoletes:	kopete-plugin-tools-spellcheck
Obsoletes:	kopete-plugin-tools-texteffect
Obsoletes:	kopete-plugin-tools-translator
Obsoletes:	kopete-plugin-tools-webpresence
Obsoletes:	kopete-plugin-protocols-aim
Obsoletes:	kopete-plugin-protocols-gg
Obsoletes:	kopete-plugin-protocols-icq
Obsoletes:	kopete-plugin-protocols-irc
Obsoletes:	kopete-plugin-protocols-jabber
Obsoletes:	kopete-plugin-protocols-msn
Obsoletes:	kopete-plugin-protocols-oscar
Obsoletes:	kopete-plugin-protocols-sms
Obsoletes:	kopete-plugin-protocols-winpopup
Obsoletes:	kopete-plugin-protocols-yahoo


%description kopete
Kopete is a flexible and extendable multiple protocol instant
messaging system designed as a plugin-based system. All protocols are
plugins and allow modular installment, configuration, and usage
without the main application knowing anything about the plugin being
loaded. The goal of Kopete is to provide users with a standard and
easy to use interface between all of their instant messaging systems,
but at the same time also providing developers with the ease of
writing plugins to support a new protocol. The core Kopete development
team provides a handful of plugins that most users can use, in
addition to templates for new developers to base a plugin off of.

%description kopete -l pl
Kopete to rozszerzalny i rozbudowywalny komunikator obs³uguj±cy wiele
protoko³ów, zaprojektowany w oparciu o wtyczki. Wszystkie protoko³y s±
wtyczkami, co pozwala na modularn± instalacjê, konfiguracjê i u¿ywanie
bez potrzeby obs³ugi ³adowanych wtyczek w g³ównej aplikacji. Celem
Kopete jest wyposa¿enie u¿ytkowników w standardowy i ³atwy w u¿yciu
interfejs pomiêdzy wszystkimi systemami komunikatorów, a jednocze¶nie
zapewenienie programistom ³atwo¶ci pisania wtyczek obs³uguj±cych nowe
protoko³y. Za³oga programistów Kopete udostêpnia podrêczny zestaw
wtyczek u¿ywanych przez wiêkszo¶æ u¿ytkowników oraz szablony dla
nowych programistów, na których mo¿na opieraæ nowe wtyczki.

%package kpf
Summary:	Public fileserver applet
Summary(pl):	Applet publicznego serwera plików
Group:		X11/Applications
Requires:	kdebase-kicker >= 9:%{version}

%description kpf
Public fileserver applet.

%description kpf -l pl
Applet publicznego serwera plików.

%package kppp
Summary:	KDE PPP dialer
Summary(pl):	Program do po³±czeñ modemowych dla KDE
Summary(pt_BR):	O discador para Internet
Group:		X11/Applications
Requires:	kdebase-core >= 9:%{version}
Requires:	ppp

%description kppp
A PPPP dialer for KDE. It supports multiple accounts.

%description kppp -l pl
Program no nawi±zywania po³±czeñ modemowych pod KDE. Posiada ³atwy
interfejs i mo¿liwo¶æ zdefiniowania kilku kont.

%description kppp -l pt_BR
O discador para Internet.

%package ksirc
Summary:	KDE IRC client
Summary(pl):	Klient IRC dla KDE
Summary(pt_BR):	Cliente de IRC do KDE
Group:		X11/Applications
Requires:	kdebase-core >= 9:%{version}

%description ksirc
KDE IRC client.

%description ksirc -l pl
Klient IRC dla KDE.

%description ksirc -l pt_BR
Cliente de IRC do KDE.

%package krfb
Summary:	Virtual Desktops
Summary(pl):	Wirtualne biurka
Group:		X11/Applications
Requires:	kdebase-core >= 9:%{version}
Requires:	%{name}-kinetd = %{epoch}:%{version}-%{release}

%description krfb
Virtual Desktops.

%description krfb -l pl
Wirtualne biurka.

%package ktalkd
Summary:	Talk daemon
Summary(pl):	Daemon talk
Group:		X11/Applications
Requires:	kdebase-core >= 9:%{version}

%description ktalkd
Talk daemon.

%description ktalkd -l pl
Demon talk.

%package kwifimanager
Summary:	Wireless LAN
Summary(pl):	Bezprzewodowy LAN
Group:		X11/Applications
Requires:	kdelibs >= 9:%{version}

%description kwifimanager
Wireless LAN.

%description kwifimanager -l pl
Bezprzewodowy LAN.

%package kxmlrpcd
Summary:	KDE XmlRpc Daemon
Summary(pl):	Deamon XmlRpc dla KDE
Group:		X11/Applications
Requires:	kdelibs >= 9:%{version}

%description kxmlrpcd
KDE XmlRpc Daemon.

%description kxmlrpcd -l pl
Demon XmlRpc dla KDE.

%package lanbrowser
Summary:	KDE LAN Browser
Summary(pl):	Przegl±darka LAN-u dla KDE
Group:		X11/Applications
Requires:	konqueror >= %{version}
Obsoletes:	%{name}-lisa
Obsoletes:	lisa
Provides:	lisa

%description lanbrowser
KDE LAN Browser.

%description lanbrowser -l pl
Przegl±darka LAN-u dla KDE.

%package rss
Summary:	TODO
Summary(pl):	TODO
Group:		X11/Libraries
Obsoletes:	%{name}-librss

%description rss
TODO.

%description rss -l pl
TODO.


###################################
#        BEGIN KOPETE
###################################


%package kopete-plugin-tools-autoaway
Summary:        An autoaway plugin
Summary(pl):    Wtyczka automatycznego przej¶cia w stan zajêty
Group:          X11/Applications/Networking
Requires:       %{name}-kopete = %{epoch}:%{version}-%{release}

%description kopete-plugin-tools-autoaway
Automatically changes status to away. Conditions are configurable.

%description kopete-plugin-tools-autoaway -l pl
Automatycznie zmienia status na zajêty. Warunki, po zaistnieniu
których ma nastapiæ, s± konfigurowalne.

%package kopete-plugin-tools-autoreplace
Summary:        Autoreplaces some text you can choose
Summary(pl):    Wtyczka automatycznej zamiany tekstu
Group:          X11/Applications/Networking
Requires:       %{name}-kopete = %{epoch}:%{version}-%{release}

%description kopete-plugin-tools-autoreplace
Autoreplaces some text you can choose.

%description kopete-plugin-tools-autoreplace -l pl
Wtyczka automatycznej zamiany tekstu.


%package kopete-plugin-tools-conectionstatus
Summary:        Internet connection detector
Summary(pl):    Wykrywacz po³±czeñ internetowych
Group:          X11/Applications/Networking
Requires:       %{name}-kopete = %{epoch}:%{version}-%{release}

%description kopete-plugin-tools-conectionstatus
Automatically detects whether the internet connection is available or
not.

%description kopete-plugin-tools-conectionstatus -l pl
Automatycznie sprawdza czy dostêpne jest po³±czenie do internetu czy
nie.

%package kopete-plugin-tools-contactnotes
Summary:        Add personal notes to your contacts
Summary(pl):    Dodawanie notatek do kontaktów
Group:          X11/Applications/Networking
Requires:       %{name}-kopete = %{epoch}:%{version}-%{release}

%description kopete-plugin-tools-contactnotes
Allows adding personal notes to your contacts.

%description kopete-plugin-tools-contactnotes  -l pl
Umo¿liwia dodawanie notatek do kontaktów.

%package kopete-plugin-tools-cryptography
Summary:        Messages encryptor
Summary(pl):    Program do szyfrowania wiadomo¶ci
Group:          X11/Applications/Networking
Requires:       %{name}-kopete = %{epoch}:%{version}-%{release}

%description kopete-plugin-tools-cryptography
OpenPGP messages encryptor.

%description kopete-plugin-tools-cryptography -l pl
Program do szyfrowania wiadomo¶ci przy pomocy OpenPGP.


%package kopete-plugin-tools-history
Summary:        A history plugin
Summary(pl):    Wtyczka obs³uguj±ca historiê rozmów
Group:          X11/Applications/Networking
Requires:       %{name}-kopete = %{epoch}:%{version}-%{release}

%description kopete-plugin-tools-history
A history plugin.

%description kopete-plugin-tools-history -l pl
Wtyczka obs³uguj±ca historiê rozmów.

%package kopete-plugin-tools-highlight
Summary:        A highlighter plugin
Summary(pl):    Wtyczka podkre¶laj±ca wybrane teksty
Group:          X11/Applications/Networking
Requires:       %{name}-kopete = %{epoch}:%{version}-%{release}

%description kopete-plugin-tools-highlight
A highlighter plugin.

%package kopete-plugin-tools-importer
Summary:        Contact importer
Summary(pl):    Importer kontaktów
Group:          X11/Applications/Networking
Requires:       %{name}-kopete = %{epoch}:%{version}-%{release}

%description kopete-plugin-tools-importer
Allows importing contacts from other IM's.

%description kopete-plugin-tools-importer -l pl
Umo¿liwia importowanie kontaktów z innych komunikatorów.

%package kopete-plugin-tools-nowlistening
Summary:        Playlist informer
Summary(pl):    Informator o playliscie
Group:          X11/Applications/Networking
Requires:       %{name}-kopete = %{epoch}:%{version}-%{release}
Requires:       xmms >= 1.0.0
Requires:       kdemultimedia-noatun >= 3.1
Requires:       kdemultimedia-kscd >= 3.1

%description kopete-plugin-tools-nowlistening
This plugin tells selected live chats what you're currently listening
to in xmms/kscd/noatun.

%description kopete-plugin-tools-nowlistening -l pl
Ta wtyczka wypisuje podczas rozmow nazwê aktualnie s³uchanej piosenki
w xmms/kscd/noatun.

%package kopete-plugin-tools-motionaway
Summary:        Sets away status when not detecting movement near the computer
Summary(pl):    Zmienia status na zajêty je¶li nie wykrywa ruchu wokó³ komputera
Group:          X11/Applications/Networking
Requires:       %{name}-kopete = %{epoch}:%{version}-%{release}

%description kopete-plugin-tools-motionaway
This plugin sets away status when not detecting movement near the
computer.

%description kopete-plugin-tools-motionaway -l pl
Ta wtyczka zmienia status na zajêty je¶li nie wykrywa ruchu wokó³
komputera.


%package kopete-plugin-tools-spellcheck
Summary:        A spell checking plugin.
Summary(pl):    Wtyczka sprawdzaj±ca pisownie.
Group:          X11/Applications/Networking
Requires:       %{name}-kopete = %{epoch}:%{version}-%{release}

%description kopete-plugin-tools-spellcheck
A spell checking plugin.

%description kopete-plugin-tools-spellcheck -l pl
Wtyczka sprawdzaj±ca pisownie.


%package kopete-plugin-tools-texteffect
Summary:        A plugin that adds nice effects to your messages
Summary(pl):    Wtyczka dodaj±ca ³adne efekty do twoich wiadomo¶ci
Group:          X11/Applications/Networking
Requires:       %{name}-kopete = %{epoch}:%{version}-%{release}

%description kopete-plugin-tools-texteffect
A plugin that adds nice effects to your messages.

%description kopete-plugin-tools-texteffect -l pl
Wtyczka dodaj±ca ³adne efekty do twoich wiadomo¶ci.

%package kopete-plugin-tools-translator
Summary:        Uses babelfish to translate messages
Summary(pl):    Wykorzystuje babelfish do t³umaczenia wiadomo¶ci
Group:          X11/Applications/Networking
Requires:       %{name}-kopete = %{epoch}:%{version}-%{release}

%description kopete-plugin-tools-translator
This plugin uses babelfish to translate messages.

%description kopete-plugin-tools-translator -l pl
Ta wtyczka wykorzystuje babelfish do t³umaczenia wiadomo¶ci.


%package kopete-plugin-tools-webpresence
Summary:        Web contactlist presenter
Summary(pl):    Wy¶wietlacz listy kontaktów na WWW
Group:          X11/Applications/Networking
Requires:       %{name}-kopete = %{epoch}:%{version}-%{release}
Requires:       libxml2 >= 2.4.8
Requires:       libxslt >= 1.0.7

%description kopete-plugin-tools-webpresence
This plugin shows the status of (parts of) your contactlist on a
webpage.

%description kopete-plugin-tools-webpresence -l pl
Ta wtyczka pokazuje status (ca³ej lub cze¶ci) listy kontaktów na
stronie WWW.

%package kopete-plugin-protocols-aim
Summary:        Adds AIM protocol support
Summary(pl):    Dodaje obs³ugê protoko³u AIM
Group:          X11/Applications/Networking
Requires:       %{name}-kopete = %{epoch}:%{version}-%{release}

%description kopete-plugin-protocols-aim
Adds AIM protocol support.

%description kopete-plugin-protocols-aim -l pl
Dodaje obs³ugê protoko³u AIM.

%package kopete-plugin-protocols-gg
Summary:        Adds GaduGadu protocol support
Summary(pl):    Dodaje obs³ugê protoko³u GaduGadu
Group:          X11/Applications/Networking
Requires:       %{name}-kopete = %{epoch}:%{version}-%{release}

%description kopete-plugin-protocols-gg
Adds GaguGadu protocol support.

%description kopete-plugin-protocols-gg -l pl
Dodaje obs³ugê protoko³u GaduGadu.
#1
%package kopete-plugin-protocols-icq
Summary:        Adds ICQ protocol support
Summary(pl):    Dodaje obs³ugê protoko³u ICQ
Group:          X11/Applications/Networking
Requires:       %{name}-kopete = %{epoch}:%{version}-%{release}

%description kopete-plugin-protocols-icq
Adds ICQ protocol support.

%description kopete-plugin-protocols-icq -l pl
Dodaje obs³ugê protoko³u ICQ.

%package kopete-plugin-protocols-irc
Summary:        Adds IRC support
Summary(pl):    Dodaje obs³ugê IRC
Group:          X11/Applications/Networking
Requires:       %{name}-kopete = %{epoch}:%{version}-%{release}

%description kopete-plugin-protocols-irc
Adds IRC support.

%description kopete-plugin-protocols-irc -l pl
Dodaje obs³ugê IRC.

%package kopete-plugin-protocols-jabber
Summary:        Adds Jabber protocol support
Summary(pl):    Dodaje obs³ugê protoko³u Jabber
Group:          X11/Applications/Networking
Requires:       %{name}-kopete = %{epoch}:%{version}-%{release}
Requires:       libpsi >= 20021108

%description kopete-plugin-protocols-jabber
Adds Jabber protocol support.

%description kopete-plugin-protocols-jabber -l pl
Dodaje obs³ugê protoko³u Jabber.

%package kopete-plugin-protocols-msn
Summary:        Adds MSN protocol support
Summary(pl):    Dodaje obs³ugê protoko³u MSN
Group:          X11/Applications/Networking
Requires:       %{name}-kopete = %{epoch}:%{version}-%{release}

%description kopete-plugin-protocols-msn
Adds MSN protocol support.

%description kopete-plugin-protocols-msn -l pl
Dodaje obs³ugê protoko³u MSN.

%package kopete-plugin-protocols-testbed
Summary:        Adds Testbed protocol support
Summary(pl):    Dodaje obs³ugê protoko³u testbed
Group:          X11/Applications/Networking
Requires:       %{name}-kopete = %{epoch}:%{version}-%{release}

%description kopete-plugin-protocols-testbed
Adds Testbed protocol support.

%description kopete-plugin-protocols-testbed -l pl
Dodaje obs³ugê protoko³u testbed.

%package kopete-plugin-protocols-oscar
Summary:        Adds OSCAR protocol support
Summary(pl):    Dodaje obs³ugê protoko³u OSCAR
Group:          X11/Applications/Networking
Requires:       %{name}-kopete = %{epoch}:%{version}-%{release}

%description kopete-plugin-protocols-oscar
Adds OSCAR protocol support.

%description kopete-plugin-protocols-oscar -l pl
Dodaje obs³ugê protoko³u OSCAR.

%package kopete-plugin-protocols-sms
Summary:        Adds SMS contact support
Summary(pl):    Dodaje obs³ugê kontaktów SMS
Group:          X11/Applications/Networking
Requires:       %{name}-kopete = %{epoch}:%{version}-%{release}

%description kopete-plugin-protocols-sms
Adds SMS contact support.

%description kopete-plugin-protocols-sms -l pl
Dodaje obs³ugê kontaktów SMS.

%package kopete-plugin-protocols-winpopup
Summary:        Adds winpopup messaging support
Summary(pl):    Dodaje obs³ugê komunikacji via winpopup
Group:          X11/Applications/Networking
Requires:       %{name}-kopete = %{epoch}:%{version}-%{release}

%description kopete-plugin-protocols-winpopup
Adds winpopup messaging support.

%description kopete-plugin-protocols-winpopup -l pl
Dodaje obs³ugê komunikacji via winpopup.

%package kopete-plugin-protocols-yahoo
Summary:        Adds yahoo protocol support
Summary(pl):    Dodaje obs³ugê protoko³u yahoo
Group:          X11/Applications/Networking
Requires:       %{name}-kopete = %{epoch}:%{version}-%{release}

%description kopete-plugin-protocols-yahoo
Adds yahoo protocol support.

%description kopete-plugin-protocols-yahoo -l pl
Dodaje obs³ugê protoko³u yahoo.


###################################

%prep
%setup -q -n %{name}-%{_snap}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build

for plik in `find ./ -name *.desktop` ; do
	echo $plik
	sed -i -e "s/\[nb\]/\[no\]/g" $plik
done

%{__make} -f admin/Makefile.common cvs

#export DO_NOT_COMPILE=kopete

%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_appsdir=%{_applnkdir} \
	kde_htmldir=%{_docdir}/kde/HTML

install -d $RPM_BUILD_ROOT%{_sysconfdir}/{rc.d/init.d,sysconfig}

install %{SOURCE2} $RPM_BUILD_ROOT/etc/rc.d/init.d/lisa
install %{SOURCE3} $RPM_BUILD_ROOT/etc/sysconfig/lisa
install %{SOURCE4} $RPM_BUILD_ROOT%{_sysconfdir}/lisarc

mv $RPM_BUILD_ROOT%{_applnkdir}/Internet/kopete.desktop \
    $RPM_BUILD_ROOT%{_desktopdir}/kde

cd $RPM_BUILD_ROOT%{_iconsdir}
mv {locolor,crystalsvg}/16x16/apps/krfb.png
cd -

%find_lang kdict		--with-kde
%find_lang knewsticker		--with-kde
%find_lang kopete		--with-kde
%find_lang kpf			--with-kde
%find_lang kppp			--with-kde
%find_lang krdc			--with-kde
%find_lang krfb			--with-kde
cat krdc.lang >> krfb.lang
%find_lang ksirc		--with-kde
%find_lang ktalkd		--with-kde
%find_lang kcmtalkd		--with-kde
cat kcmtalkd.lang >> ktalkd.lang
%find_lang kwifimanager		--with-kde
%find_lang kxmlrpcd		--with-kde
%find_lang lisa			--with-kde
%find_lang lanbrowser		--with-kde
cat lanbrowser.lang >> lisa.lang

%clean
rm -rf $RPM_BUILD_ROOT

%post lanbrowser
/sbin/chkconfig --add lisa
if [ -r /var/lock/subsys/lisa ]; then
	/etc/rc.d/init.d/lisa restart >&2
else
	echo "Run \"/etc/rc.d/init.d/lisa start\" to start Lisa daemon."
fi

%preun lanbrowser
if [ "$1" = "0" ]; then
	if [ -r /var/lock/subsys/lisa ]; then
		/etc/rc.d/init.d/lisa stop >&2
	fi
	/sbin/chkconfig --del lisa
fi

%post	kopete	-p /sbin/ldconfig
%postun	kopete	-p /sbin/ldconfig

%post	rss	-p /sbin/ldconfig
%postun	rss	-p /sbin/ldconfig

%files devel
%defattr(644,root,root,755)
%{_includedir}/rss                                                      
#%%{_libdir}/libkopete.so
#%%{_libdir}/libkopete_msn.so
#%%{_libdir}/libkopete_oscar.so
%{_libdir}/librss.so

#%files kwifimanager -f kwifimanager.lang
#%defattr(644,root,root,755)
#%{_libdir}/kde3/kcm_kwifimanager.la
#%attr(755,root,root) %{_libdir}/kde3/kcm_kwifimanager.so
#%{_applnkdir}/KDE-Settings/Network/kcmwifi.desktop

%files kdict -f kdict.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kdict
%{_libdir}/kde3/kdict_panelapplet.la
%attr(755,root,root) %{_libdir}/kde3/kdict_panelapplet.so
%{_datadir}/apps/kdict
%{_datadir}/apps/kicker/applets/kdictapplet.desktop
%{_desktopdir}/kde/kdict.desktop
%{_iconsdir}/*/*/*/kdict*

%files kget
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kget
%{_libdir}/kde3/khtml_kget.la
%attr(755,root,root) %{_libdir}/kde3/khtml_kget.so
%{_datadir}/apps/kget
%{_datadir}/apps/khtml/kpartplugins/kget_plug_in.rc
%{_datadir}/mimelnk/application/x-kgetlist.desktop
%{_desktopdir}/kde/kget.desktop
%{_iconsdir}/*/*/*/*kget*

%files kinetd
%defattr(644,root,root,755)
%{_libdir}/kde3/kded_kinetd.la
%attr(755,root,root) %{_libdir}/kde3/kded_kinetd.so
%{_datadir}/apps/kinetd
%{_datadir}/services/kded/kinetd.desktop
%{_datadir}/servicetypes/kinetdmodule.desktop

#%files kit -f kit.lang
#%defattr(644,root,root,755)
#%attr(755,root,root) %{_bindir}/kit
#%{_datadir}/apps/kit
#%{_desktopdir}/kde/kit.desktop
#%{_iconsdir}/*/*/*/kit.png

%files knewsticker -f knewsticker.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/knewstickerstub
%{_libdir}/kde3/knewsticker_panelapplet.la
%attr(755,root,root) %{_libdir}/kde3/knewsticker_panelapplet.so
%{_libdir}/kde3/kcm_knewsticker.la
%attr(755,root,root) %{_libdir}/kde3/kcm_knewsticker.so
%{_datadir}/apps/knewsticker
%{_datadir}/apps/kicker/applets/knewsticker.desktop
%{_datadir}/apps/kconf_update/kn*
%{_applnkdir}/.hidden/knewstickerstub.desktop
%{_applnkdir}/.hidden/kcmnewsticker.desktop
%{_desktopdir}/kde/knewsticker*.desktop
%{_iconsdir}/*/*/*/knewsticker.png

%files kopete -f kopete.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kconf_update_bin/kopete-account-kconf_update
%attr(755,root,root) %{_bindir}/kconf_update_bin/kopete-pluginloader2-kconf_update
%attr(755,root,root) %{_bindir}/kopete
#%%attr(755,root,root) %{_bindir}/winpopup-install.sh
#%%attr(755,root,root) %{_bindir}/winpopup-send.sh
#%%{_libdir}/libkopete.la
%attr(755,root,root) %{_libdir}/libkopete.so.*.*.*
%{_libdir}/kde3/kcm_kopete_accountconfig.la
%attr(755,root,root) %{_libdir}/kde3/kcm_kopete_accountconfig.so
%{_libdir}/kde3/kcm_kopete_appearanceconfig.la
%attr(755,root,root) %{_libdir}/kde3/kcm_kopete_appearanceconfig.so
%{_libdir}/kde3/kcm_kopete_autoreplace.la
%attr(755,root,root) %{_libdir}/kde3/kcm_kopete_autoreplace.so
%{_libdir}/kde3/kcm_kopete_behaviorconfig.la
%attr(755,root,root) %{_libdir}/kde3/kcm_kopete_behaviorconfig.so
%attr(755,root,root) %{_libdir}/kde3/kcm_kopete_pluginconfig.so
%{_libdir}/kde3/kcm_kopete_pluginconfig.la
%{_libdir}/kde3/libkrichtexteditpart.la
%attr(755,root,root) %{_libdir}/kde3/libkrichtexteditpart.so
%{_libdir}/kde3/kopete_chatwindow.la
%attr(755,root,root) %{_libdir}/kde3/kopete_chatwindow.so
%{_datadir}/apps/kconf_update/kopete-account-kconf_update.sh
%{_datadir}/apps/kconf_update/kopete-account-kconf_update.upd
%{_datadir}/apps/kconf_update/kopete-pluginloader.pl
%{_datadir}/apps/kconf_update/kopete-pluginloader.upd
%{_datadir}/apps/kconf_update/kopete-pluginloader2.sh
%{_datadir}/apps/kconf_update/kopete-pluginloader2.upd
%dir %{_datadir}/apps/kopete
%{_datadir}/apps/kopete/*rc
%{_datadir}/apps/kopete/styles/*
%{_datadir}/apps/kopete/pics/emoticons
%{_datadir}/apps/kopeterichtexteditpart/kopeterichtexteditpartfull.rc
%{_datadir}/apps/kopeterichtexteditpart/kopeterichtexteditpartsimple.rc
%{_datadir}/services/chatwindow.desktop
%{_datadir}/services/kopete_accountconfig.desktop
%{_datadir}/services/kopete_appearanceconfig.desktop
%{_datadir}/services/kopete_behaviorconfig.desktop
%{_datadir}/services/kopete_pluginconfig.desktop
%{_datadir}/servicetypes/kopeteplugin.desktop
%{_datadir}/servicetypes/kopeteprotocol.desktop
%{_datadir}/servicetypes/kopeteui.desktop
%{_datadir}/sounds/Kopete_Event.ogg
%{_datadir}/sounds/Kopete_Received.ogg
%{_datadir}/sounds/Kopete_Sent.ogg
%{_datadir}/sounds/Kopete_User_is_Online.ogg
%{_desktopdir}/kde/kopete.desktop
%{_iconsdir}/crystalsvg/*/apps/kopete.png
%{_datadir}/apps/kopete/icons/crystalsvg/*/*/kopete*
%{_datadir}/apps/kopete/icons/crystalsvg/*/*/metacontact*
%{_datadir}/apps/kopete/icons/crystalsvg/*/*/newmsg.png
%{_datadir}/apps/kopete/icons/crystalsvg/*/*/emoticon.png
%{_datadir}/apps/kopete/icons/crystalsvg/*/*/status_unknown.png
%{_datadir}/apps/kopete/pics/newmessage.mng


##################################
#      KOPETE SUBPKGS
#################################


%files kopete-plugin-tools-autoreplace
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/kopete*autoreplace*.so
%{_libdir}/kde3/kopete*autoreplace*.la
%{_libdir}/kde3/kcm_kopete_autoreplace.la
%attr(755,root,root) %{_libdir}/kde3/kcm_kopete_autoreplace.so
%{_datadir}/services/autoreplace.desktop
%{_datadir}/apps/kopete/icons/crystalsvg/*/*/autoreplace.png
%{_datadir}/services/kconfiguredialog/kopete_autoreplace_config.desktop

%files kopete-plugin-tools-conectionstatus
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/kopete*connectionstatus*.so
%{_libdir}/kde3/kopete*connectionstatus*.la
%{_datadir}/services/connectionstatus.desktop

%files kopete-plugin-tools-contactnotes
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/kopete*contactnotes*.so
%{_libdir}/kde3/kopete*contactnotes*.la
%{_datadir}/services/contactnotes.desktop

%files kopete-plugin-tools-cryptography
%defattr(644,root,root,755)
%{_datadir}/services/kconfiguredialog/kopete_cryptography_config.desktop
%{_libdir}/kde3/kcm_kopete_cryptography.la
%attr(755,root,root) %{_libdir}/kde3/kcm_kopete_cryptography.so
%attr(755,root,root) %{_libdir}/kde3/kopete*cryptography*.so
%{_libdir}/kde3/kopete*cryptography*.la
%{_datadir}/services/cryptography.desktop

%files kopete-plugin-tools-history
%defattr(644,root,root,755)
%{_datadir}/services/kconfiguredialog/kopete_history_config.desktop
%{_libdir}/kde3/kcm_kopete_history.la
%attr(755,root,root) %{_libdir}/kde3/kcm_kopete_history.so
%attr(755,root,root) %{_libdir}/kde3/kopete*history*.so
%{_libdir}/kde3/kopete*history*.la
%{_datadir}/services/history.desktop
##%{_datadir}/apps/kopete/icons/crystalsvg/*/*/history.png

%files kopete-plugin-tools-highlight
%defattr(644,root,root,755)
%{_datadir}/services/kconfiguredialog/kopete_highlight_config.desktop
%{_libdir}/kde3/kcm_kopete_highlight.la
%attr(755,root,root) %{_libdir}/kde3/kcm_kopete_highlight.so
%attr(755,root,root) %{_libdir}/kde3/kopete*highlight*.so
%{_libdir}/kde3/kopete*highlight*.la
%{_datadir}/services/highlight.desktop
%{_datadir}/apps/kopete/icons/crystalsvg/*/*/highlight.png

%files kopete-plugin-tools-nowlistening
%defattr(644,root,root,755)
%{_datadir}/services/kconfiguredialog/kopete_nowlistening_config.desktop
%attr(755,root,root)  %{_libdir}/kde3/kopete*nowlistening*.so
%{_libdir}/kde3/kcm_kopete_nowlistening.la
%attr(755,root,root) %{_libdir}/kde3/kcm_kopete_nowlistening.so
%{_libdir}/kde3/kopete*nowlistening*.la
%{_datadir}/services/nowlistening.desktop

%files kopete-plugin-tools-motionaway
%defattr(644,root,root,755)
%{_datadir}/services/kconfiguredialog/kopete_motionaway_config.desktop
%attr(755,root,root) %{_libdir}/kde3/kopete*motionaway*.so
%{_libdir}/kde3/kcm_kopete_motionaway.la
%attr(755,root,root) %{_libdir}/kde3/kcm_kopete_motionaway.so
%{_libdir}/kde3/kopete*motionaway*.la
%{_datadir}/services/motionaway.desktop

#%%files kopete-plugin-tools-spellcheck
#%%defattr(644,root,root,755)
#%%attr(755,root,root) %{_libdir}/kde3/kopete*spellcheck*.so
#%%{_libdir}/kde3/kopete*spellcheck*.la
#%%{_datadir}/services/spellcheck.desktop


%files kopete-plugin-tools-texteffect
%defattr(644,root,root,755)
%{_datadir}/services/kconfiguredialog/kopete_texteffect_config.desktop
%attr(755,root,root) %{_libdir}/kde3/kopete*texteffect*.so
%{_libdir}/kde3/kcm_kopete_texteffect.la
%attr(755,root,root) %{_libdir}/kde3/kcm_kopete_texteffect.so
%{_libdir}/kde3/kopete*texteffect*.la
%{_datadir}/services/texteffect.desktop
%{_datadir}/apps/kopete/icons/crystalsvg/*/*/texteffect.png

%files kopete-plugin-tools-translator
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/kopete*translator*.so
%{_datadir}/services/kconfiguredialog/kopete_translator_config.desktop
%{_libdir}/kde3/kcm_kopete_translator.la
%attr(755,root,root) %{_libdir}/kde3/kcm_kopete_translator.so
%{_libdir}/kde3/kopete*translator*.la
%{_datadir}/services/translator.desktop

%files kopete-plugin-tools-webpresence
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/kopete*webpresence*.so
%{_libdir}/kde3/kcm_kopete_webpresence.la
%{_datadir}/services/kconfiguredialog/kopete_webpresence_config.desktop
%attr(755,root,root) %{_libdir}/kde3/kcm_kopete_webpresence.so
%{_libdir}/kde3/kopete*webpresence*.la
%{_datadir}/services/webpresence.desktop
%{_datadir}/apps/kopete/webpresence/webpresencedefault.xsl
%{_datadir}/apps/kopete/webpresence/wpimages.xsl

%files kopete-plugin-protocols-aim
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/kopete*aim*.so
%{_libdir}/kde3/kopete*aim*.la
%{_datadir}/services/aim.desktop
%{_datadir}/apps/kopete/icons/crystalsvg/*/*/aim*
%{_datadir}/apps/kopete/pics/aim*

%files kopete-plugin-protocols-gg
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/kopete*gadu*.so
%{_libdir}/kde3/kopete*gadu*.la
%{_datadir}/services/gadu.desktop
%{_datadir}/apps/kopete/icons/crystalsvg/*/*/gadu*
%{_datadir}/apps/kopete/pics/gg*
%{_datadir}/apps/kopete/icons/crystalsvg/*/*/gg*

%files kopete-plugin-protocols-icq
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/kopete*icq*.so
%{_libdir}/kde3/kopete*icq*.la
%{_datadir}/services/icq.desktop
%{_datadir}/apps/kopete/icons/crystalsvg/*/*/icq*
%{_datadir}/apps/kopete/pics/icq*

%files kopete-plugin-protocols-irc
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/kopete*irc*.so
%{_libdir}/kde3/kopete*irc*.la
%{_datadir}/services/irc.desktop
%{_datadir}/apps/kopete/icons/crystalsvg/*/*/irc*
%{_datadir}/apps/kopete/pics/irc_connecting.mng

%files kopete-plugin-protocols-jabber
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/kopete*jabber*.so
%{_libdir}/kde3/kopete*jabber*.la
%{_datadir}/services/jabber.desktop
%{_datadir}/apps/kopete/pics/jabber*
%{_datadir}/apps/kopete/icons/crystalsvg/*/*/jabber*

%files kopete-plugin-protocols-msn
%defattr(644,root,root,755)
#%%{_libdir}/libkopete_msn.la
%{_datadir}/services/kconfiguredialog/kopete_msn_config.desktop
%{_libdir}/kde3/kcm_kopete_msn.la
%attr(755,root,root) %{_libdir}/kde3/kcm_kopete_msn.so
%attr(755,root,root) %{_libdir}/libkopete_msn.so.*.*.*
%attr(755,root,root) %{_libdir}/kde3/kopete*msn*.so
%{_libdir}/kde3/kopete*msn*.la
%{_datadir}/services/msn.desktop
%{_datadir}/apps/kopete/pics/msn*
%{_datadir}/apps/kopete/icons/crystalsvg/*/*/msn*

%files kopete-plugin-protocols-oscar
%defattr(644,root,root,755)
#%%{_libdir}/libkopete_oscar.la
%attr(755,root,root) %{_libdir}/libkopete_oscar.so.*.*.*
%{_datadir}/apps/kopete/icons/crystalsvg/*/*/*_icon.png

%files kopete-plugin-protocols-sms
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/kopete*sms*.so
%{_libdir}/kde3/kopete*sms*.la
%{_datadir}/services/sms.desktop
%{_datadir}/apps/kopete/icons/crystalsvg/*/*/sms*

#%%files kopete-plugin-protocols-yahoo
#%%defattr(644,root,root,755)
#%%attr(755,root,root) %{_libdir}/kde3/kopete_yahoo*.so
#%%{_libdir}/kde3/kopete_yahoo*.la
#%%{_datadir}/services/yahoo.desktop
#%%{_datadir}/apps/kopete/icons/*/*/*/yahoo*

%files kopete-plugin-protocols-winpopup
%defattr(644,root,root,755)
%{_libdir}/kde3/kcm_kopete_wp.la
%attr(755,root,root) %{_libdir}/kde3/kcm_kopete_wp.so
%attr(755,root,root) %{_bindir}/winpopup*.sh
%attr(755,root,root) %{_libdir}/kde3/kopete*wp*.so
%{_libdir}/kde3/kopete*wp*.la
%{_datadir}/services/wp.desktop
%{_datadir}/apps/kopete/icons/crystalsvg/*/*/wp*
%{_datadir}/services/kconfiguredialog/kopete_wp_config.desktop

%files kopete-plugin-protocols-testbed
%{_libdir}/kde3/kopete_testbed.la
%attr(755,root,root) %{_libdir}/kde3/kopete_testbed.so
%{_datadir}/services/testbed.desktop
%{_datadir}/apps/kopete/icons/crystalsvg/*/*/testbed*


###################################



%files kpf -f kpf.lang
%defattr(644,root,root,755)
%{_libdir}/kde3/kpf_panelapplet.la
%attr(755,root,root) %{_libdir}/kde3/kpf_panelapplet.so
%{_libdir}/kde3/kpfpropertiesdialog.la
%attr(755,root,root) %{_libdir}/kde3/kpfpropertiesdialog.so
%{_datadir}/apps/kicker/applets/kpf*
%{_datadir}/services/kpfpropertiesdialogplugin.desktop
%{_iconsdir}/*/*/*/kpf*

%files kppp -f kppp.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kppplogview
%attr(755,root,root) %{_bindir}/kppp
%{_datadir}/apps/kppp
%{_desktopdir}/kde/Kppp.desktop
%{_desktopdir}/kde/kppplogview.desktop
%{_iconsdir}/*/*/*/kppp.png

%files krfb -f krfb.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/krdc
%attr(755,root,root) %{_bindir}/krfb
%attr(755,root,root) %{_bindir}/krfb_httpd
%{_libdir}/kde3/kcm_krfb.la
%attr(755,root,root) %{_libdir}/kde3/kcm_krfb.so
%{_datadir}/apps/krdc
%{_datadir}/apps/krfb
%{_datadir}/services/kinetd_krfb.desktop
%{_datadir}/services/kinetd_krfb_httpd.desktop
%{_datadir}/services/rdp.protocol
%{_datadir}/services/vnc.protocol
%{_desktopdir}/kde//kcmkrfb.desktop
%{_desktopdir}/kde/krfb.desktop
%{_desktopdir}/kde/krdc.desktop
%{_iconsdir}/*/*/*/krdc*
%{_iconsdir}/[!l]*/*/*/krfb*

%files ksirc -f ksirc.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ksirc
%attr(755,root,root) %{_bindir}/dsirc
%{_libdir}/libkdeinit_ksirc.la
%attr(755,root,root) %{_libdir}/libkdeinit_ksirc.so
%{_libdir}/kde3/ksirc.la
%attr(755,root,root) %{_libdir}/kde3/ksirc.so
%{_libdir}/kde3/libkntsrcfilepropsdlg.la
%attr(755,root,root) %{_libdir}/kde3/libkntsrcfilepropsdlg.so
%{_datadir}/config/ksircrc
%{_datadir}/apps/ksirc
%{_datadir}/services/kntsrcfilepropsdlg.desktop
%{_desktopdir}/kde/ksirc.desktop
%{_iconsdir}/[!l]*/*/*/ksirc*

%files ktalkd -f ktalkd.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ktalkd
%attr(755,root,root) %{_bindir}/ktalkdlg
%attr(755,root,root) %{_bindir}/mail.local
%{_libdir}/kde3/kcm_ktalkd.la
%attr(755,root,root) %{_libdir}/kde3/kcm_ktalkd.so
%{_datadir}/config/ktalkdrc
%{_datadir}/sounds/ktalkd.wav
%{_desktopdir}/kde/kcmktalkd.desktop
%{_iconsdir}/*/*/*/ktalkd.png

%files kxmlrpcd -f kxmlrpcd.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kxmlrpcd
%{_libdir}/libkdeinit_kxmlrpcd.la
%attr(755,root,root) %{_libdir}/libkdeinit_kxmlrpcd.so
%{_libdir}/kde3/kxmlrpcd.la
%attr(755,root,root) %{_libdir}/kde3/kxmlrpcd.so
%{_libdir}/kde3/kcm_xmlrpcd.la
%attr(755,root,root) %{_libdir}/kde3/kcm_xmlrpcd.so
%{_datadir}/services/kxmlrpcd.desktop

%files lanbrowser -f lisa.lang
%defattr(644,root,root,755)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/lisarc
%config(noreplace) %verify(not size mtime md5) /etc/sysconfig/lisa
%attr(754,root,root) /etc/rc.d/init.d/lisa
%attr(755,root,root) %{_bindir}/reslisa
%attr(755,root,root) %{_bindir}/lisa
%{_libdir}/kde3/kio_lan.la
%attr(755,root,root) %{_libdir}/kde3/kio_lan.so
%{_libdir}/kde3/kcm_lanbrowser.la
%attr(755,root,root) %{_libdir}/kde3/kcm_lanbrowser.so
%{_datadir}/services/rlan.protocol
%{_datadir}/services/lan.protocol
%{_datadir}/apps/lisa
%{_datadir}/apps/konqueror/dirtree/remote/lan.desktop
%{_applnkdir}/.hidden/kcmkiolan.desktop
%{_applnkdir}/.hidden/kcmlisa.desktop
%{_applnkdir}/.hidden/kcmreslisa.desktop

%files rss
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/feedbrowser
%attr(755,root,root) %{_bindir}/rssclient
%attr(755,root,root) %{_bindir}/rssservice
%{_libdir}/librss.la                                                      
%attr(755,root,root) %{_libdir}/librss.so.*.*.*    
%{_datadir}/services/rssservice.desktop
