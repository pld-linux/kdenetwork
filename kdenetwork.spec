
%bcond_with ggstatus	
# Use proper sstatus behaviour for gg (which means 
# losing some contactlist features in kopete due 
# to a design bug)

%bcond_without	loadmovie 
# Use this bcond (--without loadmovie) if you are using qt from 
# devel as it has a memleak in QMovie. Qt 3.2.3 is safe.

%bcond_without  i18n    # dont build i18n subpackage

%define		_state		stable
%define		_ver		3.2.0
#%%define		_snap		040110

Summary:	K Desktop Environment - network applications
Summary(es):	K Desktop Environment - aplicaciones de red
Summary(pl):	K Desktop Environment - aplikacje sieciowe
Summary(pt_BR):	K Desktop Environment - aplicações de rede
Name:		kdenetwork
Version:	%{_ver}
Release:	0.2
Epoch:		10
License:	GPL
Group:		X11/Libraries
#Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{_ver}/src/%{name}-%{version}.tar.bz2
Source0:	http://ep09.pld-linux.org/~djurban/kde/%{name}-%{version}.tar.bz2
# Source0-md5:	80d5a03ac950a7fac10bacbb122db11
%if %{with i18n}
Source1:        http://ep09.pld-linux.org/~djurban/kde/i18n/kde-i18n-%{name}-%{version}.tar.bz2
# Source1-md5:	1722734fd00114d8286d66b15dc86820f
%endif
Source2:	%{name}-lisa.init
Source3:	%{name}-lisa.sysconfig
Source4:	%{name}-lisarc
Patch0:		kde-common-utmpx.patch
Patch1:		%{name}-use_sendmail.patch
Patch2:		%{name}-vcategories.patch
Patch3:		%{name}-ggstatus.patch
Patch4:         %{name}-remove_loadmovie.patch
Patch5:         %{name}-dcoprss.patch
Patch6:         %{name}-libiw_27.patch
BuildRequires:	artsc-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	ed
BuildRequires:	fam-devel
BuildRequires:	gettext-devel
BuildRequires:	kdelibs-devel >= 9:%{version}
BuildRequires:	libgadu-devel >= 1.4
BuildRequires:	libiw-devel
BuildRequires:	libtool
BuildRequires:	libxml2-progs
BuildRequires:	libxslt-devel >= 1.0.7
BuildRequires:	openslp-devel
BuildRequires:	openssl-devel
BuildRequires:	pcre-devel
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	xmms-devel
BuildRequires:	xrender-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	libkopete_oscar.so.1

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
- KWiFiManager - wireless network manager

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
- KWiFiManager - zarz±dca sieci bezprzewodowej

%description -l pt_BR
Aplicações de Rede para o KDE.

Incluídos neste pacote:

kmail: leitor de correio knu: utilitários de rede korn: ferramenta de
monitoração da caixa de correio kppp: configuração fácil para conexão
PPP krn: leitor de notícias

%package devel
Summary:	kdenetwork header files
Summary(pl):	Pliki nag³ówkowe kdenetwork
Group:		X11/Development/Libraries
Requires:	kdelibs-devel >= 9:%{version}
Requires:	%{name}-libkopete_msn = %{epoch}:%{version}-%{release}
Requires:	%{name}-libkopete_oscar = %{epoch}:%{version}-%{release}
Requires:	%{name}-librss = %{epoch}:%{version}-%{release}
Obsoletes:	%{name}-librss-devel
Obsoletes:	%{name}-rss-devel

%description devel
kdenetwork header files.

%description devel -l pl
Pliki nag³ówkowe kdenetwork.

%description devel -l pt_BR
Arquivos de inclusão para compilar aplicações que usem as bibliotecas
do kdenetwork.

%package kdict
Summary:	Online dictionary client
Summary(pl):	Klient s³ownika
License:	Artistic
Group:		X11/Applications
Requires:	kdebase-core >= 9:%{version}
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
Requires:	%{name}-libkopete = %{epoch}:%{version}-%{release}
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

%package kopete-protocol-aim
Summary:	Adds AIM protocol support
Summary(pl):	Dodaje obs³ugê protoko³u AIM
Group:		X11/Applications/Networking
Requires:	%{name}-kopete = %{epoch}:%{version}-%{release}
Requires:	%{name}-libkopete_oscar = %{epoch}:%{version}-%{release}

%description kopete-protocol-aim
Adds AIM protocol support.

%description kopete-protocol-aim -l pl
Dodaje obs³ugê protoko³u AIM.

%package kopete-protocol-gg
Summary:	Adds GaduGadu protocol support
Summary(pl):	Dodaje obs³ugê protoko³u GaduGadu
Group:		X11/Applications/Networking
Requires:	%{name}-kopete = %{epoch}:%{version}-%{release}

%description kopete-protocol-gg
Adds GaguGadu protocol support.

%description kopete-protocol-gg -l pl
Dodaje obs³ugê protoko³u GaduGadu.

%package kopete-protocol-icq
Summary:	Adds ICQ protocol support
Summary(pl):	Dodaje obs³ugê protoko³u ICQ
Group:		X11/Applications/Networking
Requires:	%{name}-kopete = %{epoch}:%{version}-%{release}
Requires:	%{name}-libkopete_oscar = %{epoch}:%{version}-%{release}

%description kopete-protocol-icq
Adds ICQ protocol support.

%description kopete-protocol-icq -l pl
Dodaje obs³ugê protoko³u ICQ.

%package kopete-protocol-irc
Summary:	Adds IRC support
Summary(pl):	Dodaje obs³ugê IRC
Group:		X11/Applications/Networking
Requires:	%{name}-kopete = %{epoch}:%{version}-%{release}

%description kopete-protocol-irc
Adds IRC support.

%description kopete-protocol-irc -l pl
Dodaje obs³ugê IRC.

%package kopete-protocol-jabber
Summary:	Adds Jabber protocol support
Summary(pl):	Dodaje obs³ugê protoko³u Jabber
Group:		X11/Applications/Networking
Requires:	%{name}-kopete = %{epoch}:%{version}-%{release}

%description kopete-protocol-jabber
Adds Jabber protocol support.

%description kopete-protocol-jabber -l pl
Dodaje obs³ugê protoko³u Jabber.

%package kopete-protocol-msn
Summary:	Adds MSN protocol support
Summary(pl):	Dodaje obs³ugê protoko³u MSN
Group:		X11/Applications/Networking
Requires:	%{name}-kopete = %{epoch}:%{version}-%{release}
Requires:	%{name}-libkopete_msn = %{epoch}:%{version}-%{release}

%description kopete-protocol-msn
Adds MSN protocol support.

%description kopete-protocol-msn -l pl
Dodaje obs³ugê protoko³u MSN.

%package kopete-protocol-sms
Summary:	Adds SMS contact support
Summary(pl):	Dodaje obs³ugê kontaktów SMS
Group:		X11/Applications/Networking
Requires:	%{name}-kopete = %{epoch}:%{version}-%{release}

%description kopete-protocol-sms
Adds SMS contact support.

%description kopete-protocol-sms -l pl
Dodaje obs³ugê kontaktów SMS.

%package kopete-protocol-testbed
Summary:	Adds Testbed protocol support
Summary(pl):	Dodaje obs³ugê protoko³u testbed
Group:		X11/Applications/Networking
Requires:	%{name}-kopete = %{epoch}:%{version}-%{release}

%description kopete-protocol-testbed
Adds Testbed protocol support.

%description kopete-protocol-testbed -l pl
Dodaje obs³ugê protoko³u testbed.

%package kopete-protocol-winpopup
Summary:	Adds winpopup messaging support
Summary(pl):	Dodaje obs³ugê komunikacji via winpopup
Group:		X11/Applications/Networking
Requires:	%{name}-kopete = %{epoch}:%{version}-%{release}

%description kopete-protocol-winpopup
Adds winpopup messaging support.

%description kopete-protocol-winpopup -l pl
Dodaje obs³ugê komunikacji via winpopup.

%package kopete-protocol-yahoo
Summary:	Adds yahoo protocol support
Summary(pl):	Dodaje obs³ugê protoko³u yahoo
Group:		X11/Applications/Networking
Requires:	%{name}-kopete = %{epoch}:%{version}-%{release}

%description kopete-protocol-yahoo
Adds yahoo protocol support.

%description kopete-protocol-yahoo -l pl
Dodaje obs³ugê protoko³u yahoo.

%package kopete-tool-autoaway
Summary:	An autoaway plugin
Summary(pl):	Wtyczka automatycznego przej¶cia w stan zajêty
Group:		X11/Applications/Networking
Requires:	%{name}-kopete = %{epoch}:%{version}-%{release}

%description kopete-tool-autoaway
Automatically changes status to away. Conditions are configurable.

%description kopete-tool-autoaway -l pl
Automatycznie zmienia status na zajêty. Warunki, po zaistnieniu
których ma nastapiæ, s± konfigurowalne.

%package kopete-tool-autoreplace
Summary:	Autoreplaces some text you can choose
Summary(pl):	Wtyczka automatycznej zamiany tekstu
Group:		X11/Applications/Networking
Requires:	%{name}-kopete = %{epoch}:%{version}-%{release}

%description kopete-tool-autoreplace
Autoreplaces some text you can choose.

%description kopete-tool-autoreplace -l pl
Wtyczka automatycznej zamiany tekstu.

%package kopete-tool-conectionstatus
Summary:	Internet connection detector
Summary(pl):	Wykrywacz po³±czeñ internetowych
Group:		X11/Applications/Networking
Requires:	%{name}-kopete = %{epoch}:%{version}-%{release}

%description kopete-tool-conectionstatus
Automatically detects whether the internet connection is available or
not.

%description kopete-tool-conectionstatus -l pl
Automatycznie sprawdza czy dostêpne jest po³±czenie do internetu czy
nie.

%package kopete-tool-contactnotes
Summary:	Add personal notes to your contacts
Summary(pl):	Dodawanie notatek do kontaktów
Group:		X11/Applications/Networking
Requires:	%{name}-kopete = %{epoch}:%{version}-%{release}

%description kopete-tool-contactnotes
Allows adding personal notes to your contacts.

%description kopete-tool-contactnotes -l pl
Umo¿liwia dodawanie notatek do kontaktów.

%package kopete-tool-cryptography
Summary:	Messages encryptor
Summary(pl):	Program do szyfrowania wiadomo¶ci
Group:		X11/Applications/Networking
Requires:	%{name}-kopete = %{epoch}:%{version}-%{release}

%description kopete-tool-cryptography
OpenPGP messages encryptor.

%description kopete-tool-cryptography -l pl
Program do szyfrowania wiadomo¶ci przy pomocy OpenPGP.

%package kopete-tool-highlight
Summary:	A highlighter plugin
Summary(pl):	Wtyczka podkre¶laj±ca wybrane teksty
Group:		X11/Applications/Networking
Requires:	%{name}-kopete = %{epoch}:%{version}-%{release}

%description kopete-tool-highlight
A highlighter plugin.

%package kopete-tool-history
Summary:	A history plugin
Summary(pl):	Wtyczka obs³uguj±ca historiê rozmów
Group:		X11/Applications/Networking
Requires:	%{name}-kopete = %{epoch}:%{version}-%{release}

%description kopete-tool-history
A history plugin.

%description kopete-tool-history -l pl
Wtyczka obs³uguj±ca historiê rozmów.

%package kopete-tool-importer
Summary:	Contact importer
Summary(pl):	Importer kontaktów
Group:		X11/Applications/Networking
Requires:	%{name}-kopete = %{epoch}:%{version}-%{release}

%description kopete-tool-importer
Allows importing contacts from other IM's.

%description kopete-tool-importer -l pl
Umo¿liwia importowanie kontaktów z innych komunikatorów.

%package kopete-tool-nowlistening
Summary:	Playlist informer
Summary(pl):	Informator o playliscie
Group:		X11/Applications/Networking
Requires:	%{name}-kopete = %{epoch}:%{version}-%{release}
Requires:	xmms >= 1.0.0
Requires:	kdemultimedia-noatun >= 3.1
Requires:	kdemultimedia-kscd >= 3.1

%package kopete-tool-motionaway
Summary:	Sets away status when not detecting movement near the computer
Summary(pl):	Zmienia status na zajêty je¶li nie wykrywa ruchu wokó³ komputera
Group:		X11/Applications/Networking
Requires:	%{name}-kopete = %{epoch}:%{version}-%{release}

%description kopete-tool-motionaway
This plugin sets away status when not detecting movement near the
computer.

%description kopete-tool-motionaway -l pl
Ta wtyczka zmienia status na zajêty je¶li nie wykrywa ruchu wokó³
komputera.

%description kopete-tool-nowlistening
This plugin tells selected live chats what you're currently listening
to in xmms/kscd/noatun.

%description kopete-tool-nowlistening -l pl
Ta wtyczka wypisuje podczas rozmow nazwê aktualnie s³uchanej piosenki
w xmms/kscd/noatun.

%package kopete-tool-spellcheck
Summary:	A spell checking plugin.
Summary(pl):	Wtyczka sprawdzaj±ca pisownie.
Group:		X11/Applications/Networking
Requires:	%{name}-kopete = %{epoch}:%{version}-%{release}

%description kopete-tool-spellcheck
A spell checking plugin.

%description kopete-tool-spellcheck -l pl
Wtyczka sprawdzaj±ca pisownie.

%package kopete-tool-texteffect
Summary:	A plugin that adds nice effects to your messages
Summary(pl):	Wtyczka dodaj±ca ³adne efekty do twoich wiadomo¶ci
Group:		X11/Applications/Networking
Requires:	%{name}-kopete = %{epoch}:%{version}-%{release}

%description kopete-tool-texteffect
A plugin that adds nice effects to your messages.

%description kopete-tool-texteffect -l pl
Wtyczka dodaj±ca ³adne efekty do twoich wiadomo¶ci.

%package kopete-tool-translator
Summary:	Uses babelfish to translate messages
Summary(pl):	Wykorzystuje babelfish do t³umaczenia wiadomo¶ci
Group:		X11/Applications/Networking
Requires:	%{name}-kopete = %{epoch}:%{version}-%{release}

%description kopete-tool-translator
This plugin uses babelfish to translate messages.

%description kopete-tool-translator -l pl
Ta wtyczka wykorzystuje babelfish do t³umaczenia wiadomo¶ci.

%package kopete-tool-webpresence
Summary:	Web contactlist presenter
Summary(pl):	Wy¶wietlacz listy kontaktów na WWW
Group:		X11/Applications/Networking
Requires:	%{name}-kopete = %{epoch}:%{version}-%{release}
Requires:	libxml2 >= 2.4.8
Requires:	libxslt >= 1.0.7

%description kopete-tool-webpresence
This plugin shows the status of (parts of) your contactlist on a
webpage.

%description kopete-tool-webpresence -l pl
Ta wtyczka pokazuje status (ca³ej lub cze¶ci) listy kontaktów na
stronie WWW.

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
Requires:	wireless-tools

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

%package libkopete
Summary:	A kopete library
Summary(pl):	Bibliotek kopete
Group:		X11/Libraries
Requires:	kdelibs >= 9:%{version}
Obsoletes:	%{name}-kopete < 10:3.1.93.031114-3

%description libkopete
A kopete library.

%description libkopete -l pl
Bibliotek kopete.

%package libkopete_msn
Summary:	MSN protocol shared library
Summary(pl):	Biblioteka wspó³dzielona dla protoko³u MSN
Group:		X11/Libraries
Requires:	%{name}-libkopete = %{epoch}:%{version}-%{release}
Obsoletes:	%{name}-kopete-protocol-msn < 10:3.1.93.031114-3

%description libkopete_msn
MSN protocol shared library.

%description libkopete_msn -l pl
Biblioteka wspó³dzielona dla protoko³u MSN.

%package libkopete_oscar
Summary:	Adds OSCAR protocol support
Summary(pl):	Dodaje obs³ugê protoko³u OSCAR
Group:		X11/Applications/Networking
Requires:	%{name}-libkopete = %{epoch}:%{version}-%{release}
Obsoletes:	%{name}-kopete-protocol-oscar < 10:3.1.93.031114-3

%description libkopete_oscar
A shared library which adds OSCAR protocol support needed eg. by
aim and icq.

%description libkopete_oscar -l pl
Biblioteka dodaj±ca obs³ugê protoko³u OSCAR uzywanego m. innymi
przez aim i icq.

%package librss
Summary:	A rss library
Summary(pl):	Bibliotek rss
Group:		X11/Libraries
Requires:	kdelibs >= 9:%{version}
Obsoletes:	%{name}-rss < 10:3.1.93.031114-3

%description librss
A kopete rss.

%description librss -l pl
Bibliotek rss.

%package rss
Summary:	TODO
Summary(pl):	TODO
Group:		X11/Applications
Requires:	%{name}-librss = %{epoch}:%{version}-%{release}

%description rss
TODO.

%description rss -l pl
TODO.

%package kdict-i18n
Summary:	Internationalization and localization files for kdict
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kdict
Group:	X11/Applications
Requires:	%{name}-kdict = %{epoch}:%{version}-%{release}
Obsoletes:	kde-i18n-Affrikaans
Obsoletes:	kde-i18n-Afrikaans
Obsoletes:	kde-i18n-Arabic
Obsoletes:	kde-i18n-Azerbaijani
Obsoletes:	kde-i18n-Bulgarian
Obsoletes:	kde-i18n-Bosnian
Obsoletes:	kde-i18n-Catalan
Obsoletes:	kde-i18n-Czech
Obsoletes:	kde-i18n-Danish
Obsoletes:	kde-i18n-German
Obsoletes:	kde-i18n-Greek
Obsoletes:	kde-i18n-English_UK
Obsoletes:	kde-i18n-British
Obsoletes:	kde-i18n-Esperanto
Obsoletes:	kde-i18n-Spanish
Obsoletes:	kde-i18n-Estonian
Obsoletes:	kde-i18n-Finnish
Obsoletes:	kde-i18n-French
Obsoletes:	kde-i18n-Hebrew
Obsoletes:	kde-i18n-Hindi
Obsoletes:	kde-i18n-Croatian
Obsoletes:	kde-i18n-Hungarian
Obsoletes:	kde-i18n-Indonesian
Obsoletes:	kde-i18n-Icelandic
Obsoletes:	kde-i18n-Italian
Obsoletes:	kde-i18n-Japanese
Obsoletes:	kde-i18n-Korean
Obsoletes:	kde-i18n-Lithuanian
Obsoletes:	kde-i18n-Latvian
Obsoletes:	kde-i18n-Maltese
Obsoletes:	kde-i18n-Malay
Obsoletes:	kde-i18n-Mongolian
Obsoletes:	kde-i18n-Dutch
Obsoletes:	kde-i18n-Norwegian
Obsoletes:	kde-i18n-Norwegian_Bokmaal
Obsoletes:	kde-i18n-Norwegian_Bookmal
Obsoletes:	kde-i18n-Norwegian_Nynorsk
Obsoletes:	kde-i18n-Polish
Obsoletes:	kde-i18n-Portugnese
Obsoletes:	kde-i18n-Portuguese
Obsoletes:	kde-i18n-Brazil
Obsoletes:	kde-i18n-Brazil_Portugnese
Obsoletes:	kde-i18n-Brazil_Portuguese
Obsoletes:	kde-i18n-Romanian
Obsoletes:	kde-i18n-Russian
Obsoletes:	kde-i18n-Slovak
Obsoletes:	kde-i18n-Slovenian
Obsoletes:	kde-i18n-Serbian
Obsoletes:	kde-i18n-Swedish
Obsoletes:	kde-i18n-Tamil
Obsoletes:	kde-i18n-Thai
Obsoletes:	kde-i18n-Turkish
Obsoletes:	kde-i18n-Ukrainian
Obsoletes:	kde-i18n-Uzbek
Obsoletes:	kde-i18n-Venda
Obsoletes:	kde-i18n-Vietnamese
Obsoletes:	kde-i18n-Xhosa
Obsoletes:	kde-i18n-Simplified_Chinese
Obsoletes:	kde-i18n-Chinese
Obsoletes:	kde-i18n-Chinese-Big5
Obsoletes:	kde-i18n-Zulu
Obsoletes:	kde-i18n-kdelibs
Obsoletes:	kde-i18n

%description kdict-i18n
Internationalization and localization files for kdict.

%description -l pl kdict-i18n
Pliki umiêdzynarodawiaj±ce dla kdict.

%package kinetd-i18n
Summary:	Internationalization and localization files for kinetd
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kinetd
Group:	X11/Applications
Requires:	%{name}-kdict = %{epoch}:%{version}-%{release}
Obsoletes:	kde-i18n-Affrikaans
Obsoletes:	kde-i18n-Afrikaans
Obsoletes:	kde-i18n-Arabic
Obsoletes:	kde-i18n-Azerbaijani
Obsoletes:	kde-i18n-Bulgarian
Obsoletes:	kde-i18n-Bosnian
Obsoletes:	kde-i18n-Catalan
Obsoletes:	kde-i18n-Czech
Obsoletes:	kde-i18n-Danish
Obsoletes:	kde-i18n-German
Obsoletes:	kde-i18n-Greek
Obsoletes:	kde-i18n-English_UK
Obsoletes:	kde-i18n-British
Obsoletes:	kde-i18n-Esperanto
Obsoletes:	kde-i18n-Spanish
Obsoletes:	kde-i18n-Estonian
Obsoletes:	kde-i18n-Finnish
Obsoletes:	kde-i18n-French
Obsoletes:	kde-i18n-Hebrew
Obsoletes:	kde-i18n-Hindi
Obsoletes:	kde-i18n-Croatian
Obsoletes:	kde-i18n-Hungarian
Obsoletes:	kde-i18n-Indonesian
Obsoletes:	kde-i18n-Icelandic
Obsoletes:	kde-i18n-Italian
Obsoletes:	kde-i18n-Japanese
Obsoletes:	kde-i18n-Korean
Obsoletes:	kde-i18n-Lithuanian
Obsoletes:	kde-i18n-Latvian
Obsoletes:	kde-i18n-Maltese
Obsoletes:	kde-i18n-Malay
Obsoletes:	kde-i18n-Mongolian
Obsoletes:	kde-i18n-Dutch
Obsoletes:	kde-i18n-Norwegian
Obsoletes:	kde-i18n-Norwegian_Bokmaal
Obsoletes:	kde-i18n-Norwegian_Bookmal
Obsoletes:	kde-i18n-Norwegian_Nynorsk
Obsoletes:	kde-i18n-Polish
Obsoletes:	kde-i18n-Portugnese
Obsoletes:	kde-i18n-Portuguese
Obsoletes:	kde-i18n-Brazil
Obsoletes:	kde-i18n-Brazil_Portugnese
Obsoletes:	kde-i18n-Brazil_Portuguese
Obsoletes:	kde-i18n-Romanian
Obsoletes:	kde-i18n-Russian
Obsoletes:	kde-i18n-Slovak
Obsoletes:	kde-i18n-Slovenian
Obsoletes:	kde-i18n-Serbian
Obsoletes:	kde-i18n-Swedish
Obsoletes:	kde-i18n-Tamil
Obsoletes:	kde-i18n-Thai
Obsoletes:	kde-i18n-Turkish
Obsoletes:	kde-i18n-Ukrainian
Obsoletes:	kde-i18n-Uzbek
Obsoletes:	kde-i18n-Venda
Obsoletes:	kde-i18n-Vietnamese
Obsoletes:	kde-i18n-Xhosa
Obsoletes:	kde-i18n-Simplified_Chinese
Obsoletes:	kde-i18n-Chinese
Obsoletes:	kde-i18n-Chinese-Big5
Obsoletes:	kde-i18n-Zulu
Obsoletes:	kde-i18n-kdelibs
Obsoletes:	kde-i18n

%description kinetd-i18n
Internationalization and localization files for kinetd.

%description -l pl kinetd-i18n
Pliki umiêdzynarodawiaj±ce dla kinetd.

%package kdenetwork-i18n
Summary:	Common internationalization and localization files for kdenetwork
Summary(pl):	Wspó³dzielone pliki umiêdzynarodawiaj±ce dla kdenetwork
Group:	X11/Applications
Requires:	%{name}-kdict = %{epoch}:%{version}-%{release}
Obsoletes:	kde-i18n-Affrikaans
Obsoletes:	kde-i18n-Afrikaans
Obsoletes:	kde-i18n-Arabic
Obsoletes:	kde-i18n-Azerbaijani
Obsoletes:	kde-i18n-Bulgarian
Obsoletes:	kde-i18n-Bosnian
Obsoletes:	kde-i18n-Catalan
Obsoletes:	kde-i18n-Czech
Obsoletes:	kde-i18n-Danish
Obsoletes:	kde-i18n-German
Obsoletes:	kde-i18n-Greek
Obsoletes:	kde-i18n-English_UK
Obsoletes:	kde-i18n-British
Obsoletes:	kde-i18n-Esperanto
Obsoletes:	kde-i18n-Spanish
Obsoletes:	kde-i18n-Estonian
Obsoletes:	kde-i18n-Finnish
Obsoletes:	kde-i18n-French
Obsoletes:	kde-i18n-Hebrew
Obsoletes:	kde-i18n-Hindi
Obsoletes:	kde-i18n-Croatian
Obsoletes:	kde-i18n-Hungarian
Obsoletes:	kde-i18n-Indonesian
Obsoletes:	kde-i18n-Icelandic
Obsoletes:	kde-i18n-Italian
Obsoletes:	kde-i18n-Japanese
Obsoletes:	kde-i18n-Korean
Obsoletes:	kde-i18n-Lithuanian
Obsoletes:	kde-i18n-Latvian
Obsoletes:	kde-i18n-Maltese
Obsoletes:	kde-i18n-Malay
Obsoletes:	kde-i18n-Mongolian
Obsoletes:	kde-i18n-Dutch
Obsoletes:	kde-i18n-Norwegian
Obsoletes:	kde-i18n-Norwegian_Bokmaal
Obsoletes:	kde-i18n-Norwegian_Bookmal
Obsoletes:	kde-i18n-Norwegian_Nynorsk
Obsoletes:	kde-i18n-Polish
Obsoletes:	kde-i18n-Portugnese
Obsoletes:	kde-i18n-Portuguese
Obsoletes:	kde-i18n-Brazil
Obsoletes:	kde-i18n-Brazil_Portugnese
Obsoletes:	kde-i18n-Brazil_Portuguese
Obsoletes:	kde-i18n-Romanian
Obsoletes:	kde-i18n-Russian
Obsoletes:	kde-i18n-Slovak
Obsoletes:	kde-i18n-Slovenian
Obsoletes:	kde-i18n-Serbian
Obsoletes:	kde-i18n-Swedish
Obsoletes:	kde-i18n-Tamil
Obsoletes:	kde-i18n-Thai
Obsoletes:	kde-i18n-Turkish
Obsoletes:	kde-i18n-Ukrainian
Obsoletes:	kde-i18n-Uzbek
Obsoletes:	kde-i18n-Venda
Obsoletes:	kde-i18n-Vietnamese
Obsoletes:	kde-i18n-Xhosa
Obsoletes:	kde-i18n-Simplified_Chinese
Obsoletes:	kde-i18n-Chinese
Obsoletes:	kde-i18n-Chinese-Big5
Obsoletes:	kde-i18n-Zulu
Obsoletes:	kde-i18n-kdelibs
Obsoletes:	kde-i18n

%description kdenetwork-i18n
Internationalization and localization files for kdenetwork.

%description -l pl kdenetwork-i18n
Pliki umiêdzynarodawiaj±ce dla kdenetwork.



%package kget-i18n
Summary:	Internationalization and localization files for kget
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kget
Group:	X11/Applications
Requires:	%{name}-kget = %{epoch}:%{version}-%{release}
Obsoletes:	kde-i18n-Affrikaans
Obsoletes:	kde-i18n-Afrikaans
Obsoletes:	kde-i18n-Arabic
Obsoletes:	kde-i18n-Azerbaijani
Obsoletes:	kde-i18n-Bulgarian
Obsoletes:	kde-i18n-Bosnian
Obsoletes:	kde-i18n-Catalan
Obsoletes:	kde-i18n-Czech
Obsoletes:	kde-i18n-Danish
Obsoletes:	kde-i18n-German
Obsoletes:	kde-i18n-Greek
Obsoletes:	kde-i18n-English_UK
Obsoletes:	kde-i18n-British
Obsoletes:	kde-i18n-Esperanto
Obsoletes:	kde-i18n-Spanish
Obsoletes:	kde-i18n-Estonian
Obsoletes:	kde-i18n-Finnish
Obsoletes:	kde-i18n-French
Obsoletes:	kde-i18n-Hebrew
Obsoletes:	kde-i18n-Hindi
Obsoletes:	kde-i18n-Croatian
Obsoletes:	kde-i18n-Hungarian
Obsoletes:	kde-i18n-Indonesian
Obsoletes:	kde-i18n-Icelandic
Obsoletes:	kde-i18n-Italian
Obsoletes:	kde-i18n-Japanese
Obsoletes:	kde-i18n-Korean
Obsoletes:	kde-i18n-Lithuanian
Obsoletes:	kde-i18n-Latvian
Obsoletes:	kde-i18n-Maltese
Obsoletes:	kde-i18n-Malay
Obsoletes:	kde-i18n-Mongolian
Obsoletes:	kde-i18n-Dutch
Obsoletes:	kde-i18n-Norwegian
Obsoletes:	kde-i18n-Norwegian_Bokmaal
Obsoletes:	kde-i18n-Norwegian_Bookmal
Obsoletes:	kde-i18n-Norwegian_Nynorsk
Obsoletes:	kde-i18n-Polish
Obsoletes:	kde-i18n-Portugnese
Obsoletes:	kde-i18n-Portuguese
Obsoletes:	kde-i18n-Brazil
Obsoletes:	kde-i18n-Brazil_Portugnese
Obsoletes:	kde-i18n-Brazil_Portuguese
Obsoletes:	kde-i18n-Romanian
Obsoletes:	kde-i18n-Russian
Obsoletes:	kde-i18n-Slovak
Obsoletes:	kde-i18n-Slovenian
Obsoletes:	kde-i18n-Serbian
Obsoletes:	kde-i18n-Swedish
Obsoletes:	kde-i18n-Tamil
Obsoletes:	kde-i18n-Thai
Obsoletes:	kde-i18n-Turkish
Obsoletes:	kde-i18n-Ukrainian
Obsoletes:	kde-i18n-Uzbek
Obsoletes:	kde-i18n-Venda
Obsoletes:	kde-i18n-Vietnamese
Obsoletes:	kde-i18n-Xhosa
Obsoletes:	kde-i18n-Simplified_Chinese
Obsoletes:	kde-i18n-Chinese
Obsoletes:	kde-i18n-Chinese-Big5
Obsoletes:	kde-i18n-Zulu
Obsoletes:	kde-i18n-kdelibs
Obsoletes:	kde-i18n

%description kget-i18n
Internationalization and localization files for kget.

%description -l pl kget-i18n
Pliki umiêdzynarodawiaj±ce dla kget.

%package knewsticker-i18n
Summary:	Internationalization and localization files for knewsticker
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla knewsticker
Group:	X11/Applications
Requires:	%{name}-knewsticker = %{epoch}:%{version}-%{release}
Obsoletes:	kde-i18n-Affrikaans
Obsoletes:	kde-i18n-Afrikaans
Obsoletes:	kde-i18n-Arabic
Obsoletes:	kde-i18n-Azerbaijani
Obsoletes:	kde-i18n-Bulgarian
Obsoletes:	kde-i18n-Bosnian
Obsoletes:	kde-i18n-Catalan
Obsoletes:	kde-i18n-Czech
Obsoletes:	kde-i18n-Danish
Obsoletes:	kde-i18n-German
Obsoletes:	kde-i18n-Greek
Obsoletes:	kde-i18n-English_UK
Obsoletes:	kde-i18n-British
Obsoletes:	kde-i18n-Esperanto
Obsoletes:	kde-i18n-Spanish
Obsoletes:	kde-i18n-Estonian
Obsoletes:	kde-i18n-Finnish
Obsoletes:	kde-i18n-French
Obsoletes:	kde-i18n-Hebrew
Obsoletes:	kde-i18n-Hindi
Obsoletes:	kde-i18n-Croatian
Obsoletes:	kde-i18n-Hungarian
Obsoletes:	kde-i18n-Indonesian
Obsoletes:	kde-i18n-Icelandic
Obsoletes:	kde-i18n-Italian
Obsoletes:	kde-i18n-Japanese
Obsoletes:	kde-i18n-Korean
Obsoletes:	kde-i18n-Lithuanian
Obsoletes:	kde-i18n-Latvian
Obsoletes:	kde-i18n-Maltese
Obsoletes:	kde-i18n-Malay
Obsoletes:	kde-i18n-Mongolian
Obsoletes:	kde-i18n-Dutch
Obsoletes:	kde-i18n-Norwegian
Obsoletes:	kde-i18n-Norwegian_Bokmaal
Obsoletes:	kde-i18n-Norwegian_Bookmal
Obsoletes:	kde-i18n-Norwegian_Nynorsk
Obsoletes:	kde-i18n-Polish
Obsoletes:	kde-i18n-Portugnese
Obsoletes:	kde-i18n-Portuguese
Obsoletes:	kde-i18n-Brazil
Obsoletes:	kde-i18n-Brazil_Portugnese
Obsoletes:	kde-i18n-Brazil_Portuguese
Obsoletes:	kde-i18n-Romanian
Obsoletes:	kde-i18n-Russian
Obsoletes:	kde-i18n-Slovak
Obsoletes:	kde-i18n-Slovenian
Obsoletes:	kde-i18n-Serbian
Obsoletes:	kde-i18n-Swedish
Obsoletes:	kde-i18n-Tamil
Obsoletes:	kde-i18n-Thai
Obsoletes:	kde-i18n-Turkish
Obsoletes:	kde-i18n-Ukrainian
Obsoletes:	kde-i18n-Uzbek
Obsoletes:	kde-i18n-Venda
Obsoletes:	kde-i18n-Vietnamese
Obsoletes:	kde-i18n-Xhosa
Obsoletes:	kde-i18n-Simplified_Chinese
Obsoletes:	kde-i18n-Chinese
Obsoletes:	kde-i18n-Chinese-Big5
Obsoletes:	kde-i18n-Zulu
Obsoletes:	kde-i18n-kdelibs
Obsoletes:	kde-i18n

%description knewsticker-i18n
Internationalization and localization files for knewsticker.

%description -l pl knewsticker-i18n
Pliki umiêdzynarodawiaj±ce dla knewsticker.

%package kopete-i18n
Summary:	Internationalization and localization files for kopete
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kopete
Group:	X11/Applications
Requires:	%{name}-kopete = %{epoch}:%{version}-%{release}
Obsoletes:	kde-i18n-Affrikaans
Obsoletes:	kde-i18n-Afrikaans
Obsoletes:	kde-i18n-Arabic
Obsoletes:	kde-i18n-Azerbaijani
Obsoletes:	kde-i18n-Bulgarian
Obsoletes:	kde-i18n-Bosnian
Obsoletes:	kde-i18n-Catalan
Obsoletes:	kde-i18n-Czech
Obsoletes:	kde-i18n-Danish
Obsoletes:	kde-i18n-German
Obsoletes:	kde-i18n-Greek
Obsoletes:	kde-i18n-English_UK
Obsoletes:	kde-i18n-British
Obsoletes:	kde-i18n-Esperanto
Obsoletes:	kde-i18n-Spanish
Obsoletes:	kde-i18n-Estonian
Obsoletes:	kde-i18n-Finnish
Obsoletes:	kde-i18n-French
Obsoletes:	kde-i18n-Hebrew
Obsoletes:	kde-i18n-Hindi
Obsoletes:	kde-i18n-Croatian
Obsoletes:	kde-i18n-Hungarian
Obsoletes:	kde-i18n-Indonesian
Obsoletes:	kde-i18n-Icelandic
Obsoletes:	kde-i18n-Italian
Obsoletes:	kde-i18n-Japanese
Obsoletes:	kde-i18n-Korean
Obsoletes:	kde-i18n-Lithuanian
Obsoletes:	kde-i18n-Latvian
Obsoletes:	kde-i18n-Maltese
Obsoletes:	kde-i18n-Malay
Obsoletes:	kde-i18n-Mongolian
Obsoletes:	kde-i18n-Dutch
Obsoletes:	kde-i18n-Norwegian
Obsoletes:	kde-i18n-Norwegian_Bokmaal
Obsoletes:	kde-i18n-Norwegian_Bookmal
Obsoletes:	kde-i18n-Norwegian_Nynorsk
Obsoletes:	kde-i18n-Polish
Obsoletes:	kde-i18n-Portugnese
Obsoletes:	kde-i18n-Portuguese
Obsoletes:	kde-i18n-Brazil
Obsoletes:	kde-i18n-Brazil_Portugnese
Obsoletes:	kde-i18n-Brazil_Portuguese
Obsoletes:	kde-i18n-Romanian
Obsoletes:	kde-i18n-Russian
Obsoletes:	kde-i18n-Slovak
Obsoletes:	kde-i18n-Slovenian
Obsoletes:	kde-i18n-Serbian
Obsoletes:	kde-i18n-Swedish
Obsoletes:	kde-i18n-Tamil
Obsoletes:	kde-i18n-Thai
Obsoletes:	kde-i18n-Turkish
Obsoletes:	kde-i18n-Ukrainian
Obsoletes:	kde-i18n-Uzbek
Obsoletes:	kde-i18n-Venda
Obsoletes:	kde-i18n-Vietnamese
Obsoletes:	kde-i18n-Xhosa
Obsoletes:	kde-i18n-Simplified_Chinese
Obsoletes:	kde-i18n-Chinese
Obsoletes:	kde-i18n-Chinese-Big5
Obsoletes:	kde-i18n-Zulu
Obsoletes:	kde-i18n-kdelibs
Obsoletes:	kde-i18n

%description kopete-i18n
Internationalization and localization files for kopete.

%description -l pl kopete-i18n
Pliki umiêdzynarodawiaj±ce dla kopete.

%package kpf-i18n
Summary:	Internationalization and localization files for kpf
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kpf
Group:	X11/Applications
Requires:	%{name}-kpf = %{epoch}:%{version}-%{release}
Obsoletes:	kde-i18n-Affrikaans
Obsoletes:	kde-i18n-Afrikaans
Obsoletes:	kde-i18n-Arabic
Obsoletes:	kde-i18n-Azerbaijani
Obsoletes:	kde-i18n-Bulgarian
Obsoletes:	kde-i18n-Bosnian
Obsoletes:	kde-i18n-Catalan
Obsoletes:	kde-i18n-Czech
Obsoletes:	kde-i18n-Danish
Obsoletes:	kde-i18n-German
Obsoletes:	kde-i18n-Greek
Obsoletes:	kde-i18n-English_UK
Obsoletes:	kde-i18n-British
Obsoletes:	kde-i18n-Esperanto
Obsoletes:	kde-i18n-Spanish
Obsoletes:	kde-i18n-Estonian
Obsoletes:	kde-i18n-Finnish
Obsoletes:	kde-i18n-French
Obsoletes:	kde-i18n-Hebrew
Obsoletes:	kde-i18n-Hindi
Obsoletes:	kde-i18n-Croatian
Obsoletes:	kde-i18n-Hungarian
Obsoletes:	kde-i18n-Indonesian
Obsoletes:	kde-i18n-Icelandic
Obsoletes:	kde-i18n-Italian
Obsoletes:	kde-i18n-Japanese
Obsoletes:	kde-i18n-Korean
Obsoletes:	kde-i18n-Lithuanian
Obsoletes:	kde-i18n-Latvian
Obsoletes:	kde-i18n-Maltese
Obsoletes:	kde-i18n-Malay
Obsoletes:	kde-i18n-Mongolian
Obsoletes:	kde-i18n-Dutch
Obsoletes:	kde-i18n-Norwegian
Obsoletes:	kde-i18n-Norwegian_Bokmaal
Obsoletes:	kde-i18n-Norwegian_Bookmal
Obsoletes:	kde-i18n-Norwegian_Nynorsk
Obsoletes:	kde-i18n-Polish
Obsoletes:	kde-i18n-Portugnese
Obsoletes:	kde-i18n-Portuguese
Obsoletes:	kde-i18n-Brazil
Obsoletes:	kde-i18n-Brazil_Portugnese
Obsoletes:	kde-i18n-Brazil_Portuguese
Obsoletes:	kde-i18n-Romanian
Obsoletes:	kde-i18n-Russian
Obsoletes:	kde-i18n-Slovak
Obsoletes:	kde-i18n-Slovenian
Obsoletes:	kde-i18n-Serbian
Obsoletes:	kde-i18n-Swedish
Obsoletes:	kde-i18n-Tamil
Obsoletes:	kde-i18n-Thai
Obsoletes:	kde-i18n-Turkish
Obsoletes:	kde-i18n-Ukrainian
Obsoletes:	kde-i18n-Uzbek
Obsoletes:	kde-i18n-Venda
Obsoletes:	kde-i18n-Vietnamese
Obsoletes:	kde-i18n-Xhosa
Obsoletes:	kde-i18n-Simplified_Chinese
Obsoletes:	kde-i18n-Chinese
Obsoletes:	kde-i18n-Chinese-Big5
Obsoletes:	kde-i18n-Zulu
Obsoletes:	kde-i18n-kdelibs
Obsoletes:	kde-i18n

%description kpf-i18n
Internationalization and localization files for kpf.

%description -l pl kpf-i18n
Pliki umiêdzynarodawiaj±ce dla kpf.

%package kppp-i18n
Summary:	Internationalization and localization files for kppp
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kppp
Group:	X11/Applications
Requires:	%{name}-kppp = %{epoch}:%{version}-%{release}
Obsoletes:	kde-i18n-Affrikaans
Obsoletes:	kde-i18n-Afrikaans
Obsoletes:	kde-i18n-Arabic
Obsoletes:	kde-i18n-Azerbaijani
Obsoletes:	kde-i18n-Bulgarian
Obsoletes:	kde-i18n-Bosnian
Obsoletes:	kde-i18n-Catalan
Obsoletes:	kde-i18n-Czech
Obsoletes:	kde-i18n-Danish
Obsoletes:	kde-i18n-German
Obsoletes:	kde-i18n-Greek
Obsoletes:	kde-i18n-English_UK
Obsoletes:	kde-i18n-British
Obsoletes:	kde-i18n-Esperanto
Obsoletes:	kde-i18n-Spanish
Obsoletes:	kde-i18n-Estonian
Obsoletes:	kde-i18n-Finnish
Obsoletes:	kde-i18n-French
Obsoletes:	kde-i18n-Hebrew
Obsoletes:	kde-i18n-Hindi
Obsoletes:	kde-i18n-Croatian
Obsoletes:	kde-i18n-Hungarian
Obsoletes:	kde-i18n-Indonesian
Obsoletes:	kde-i18n-Icelandic
Obsoletes:	kde-i18n-Italian
Obsoletes:	kde-i18n-Japanese
Obsoletes:	kde-i18n-Korean
Obsoletes:	kde-i18n-Lithuanian
Obsoletes:	kde-i18n-Latvian
Obsoletes:	kde-i18n-Maltese
Obsoletes:	kde-i18n-Malay
Obsoletes:	kde-i18n-Mongolian
Obsoletes:	kde-i18n-Dutch
Obsoletes:	kde-i18n-Norwegian
Obsoletes:	kde-i18n-Norwegian_Bokmaal
Obsoletes:	kde-i18n-Norwegian_Bookmal
Obsoletes:	kde-i18n-Norwegian_Nynorsk
Obsoletes:	kde-i18n-Polish
Obsoletes:	kde-i18n-Portugnese
Obsoletes:	kde-i18n-Portuguese
Obsoletes:	kde-i18n-Brazil
Obsoletes:	kde-i18n-Brazil_Portugnese
Obsoletes:	kde-i18n-Brazil_Portuguese
Obsoletes:	kde-i18n-Romanian
Obsoletes:	kde-i18n-Russian
Obsoletes:	kde-i18n-Slovak
Obsoletes:	kde-i18n-Slovenian
Obsoletes:	kde-i18n-Serbian
Obsoletes:	kde-i18n-Swedish
Obsoletes:	kde-i18n-Tamil
Obsoletes:	kde-i18n-Thai
Obsoletes:	kde-i18n-Turkish
Obsoletes:	kde-i18n-Ukrainian
Obsoletes:	kde-i18n-Uzbek
Obsoletes:	kde-i18n-Venda
Obsoletes:	kde-i18n-Vietnamese
Obsoletes:	kde-i18n-Xhosa
Obsoletes:	kde-i18n-Simplified_Chinese
Obsoletes:	kde-i18n-Chinese
Obsoletes:	kde-i18n-Chinese-Big5
Obsoletes:	kde-i18n-Zulu
Obsoletes:	kde-i18n-kdelibs
Obsoletes:	kde-i18n

%description kppp-i18n
Internationalization and localization files for kppp.

%description -l pl kppp-i18n
Pliki umiêdzynarodawiaj±ce dla kppp.

%package krfb-i18n
Summary:	Internationalization and localization files for krfb
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla krfb
Group:	X11/Applications
Requires:	%{name}-krfb = %{epoch}:%{version}-%{release}
Obsoletes:	kde-i18n-Affrikaans
Obsoletes:	kde-i18n-Afrikaans
Obsoletes:	kde-i18n-Arabic
Obsoletes:	kde-i18n-Azerbaijani
Obsoletes:	kde-i18n-Bulgarian
Obsoletes:	kde-i18n-Bosnian
Obsoletes:	kde-i18n-Catalan
Obsoletes:	kde-i18n-Czech
Obsoletes:	kde-i18n-Danish
Obsoletes:	kde-i18n-German
Obsoletes:	kde-i18n-Greek
Obsoletes:	kde-i18n-English_UK
Obsoletes:	kde-i18n-British
Obsoletes:	kde-i18n-Esperanto
Obsoletes:	kde-i18n-Spanish
Obsoletes:	kde-i18n-Estonian
Obsoletes:	kde-i18n-Finnish
Obsoletes:	kde-i18n-French
Obsoletes:	kde-i18n-Hebrew
Obsoletes:	kde-i18n-Hindi
Obsoletes:	kde-i18n-Croatian
Obsoletes:	kde-i18n-Hungarian
Obsoletes:	kde-i18n-Indonesian
Obsoletes:	kde-i18n-Icelandic
Obsoletes:	kde-i18n-Italian
Obsoletes:	kde-i18n-Japanese
Obsoletes:	kde-i18n-Korean
Obsoletes:	kde-i18n-Lithuanian
Obsoletes:	kde-i18n-Latvian
Obsoletes:	kde-i18n-Maltese
Obsoletes:	kde-i18n-Malay
Obsoletes:	kde-i18n-Mongolian
Obsoletes:	kde-i18n-Dutch
Obsoletes:	kde-i18n-Norwegian
Obsoletes:	kde-i18n-Norwegian_Bokmaal
Obsoletes:	kde-i18n-Norwegian_Bookmal
Obsoletes:	kde-i18n-Norwegian_Nynorsk
Obsoletes:	kde-i18n-Polish
Obsoletes:	kde-i18n-Portugnese
Obsoletes:	kde-i18n-Portuguese
Obsoletes:	kde-i18n-Brazil
Obsoletes:	kde-i18n-Brazil_Portugnese
Obsoletes:	kde-i18n-Brazil_Portuguese
Obsoletes:	kde-i18n-Romanian
Obsoletes:	kde-i18n-Russian
Obsoletes:	kde-i18n-Slovak
Obsoletes:	kde-i18n-Slovenian
Obsoletes:	kde-i18n-Serbian
Obsoletes:	kde-i18n-Swedish
Obsoletes:	kde-i18n-Tamil
Obsoletes:	kde-i18n-Thai
Obsoletes:	kde-i18n-Turkish
Obsoletes:	kde-i18n-Ukrainian
Obsoletes:	kde-i18n-Uzbek
Obsoletes:	kde-i18n-Venda
Obsoletes:	kde-i18n-Vietnamese
Obsoletes:	kde-i18n-Xhosa
Obsoletes:	kde-i18n-Simplified_Chinese
Obsoletes:	kde-i18n-Chinese
Obsoletes:	kde-i18n-Chinese-Big5
Obsoletes:	kde-i18n-Zulu
Obsoletes:	kde-i18n-kdelibs
Obsoletes:	kde-i18n

%description krfb-i18n
Internationalization and localization files for krfb.

%description -l pl krfb-i18n
Pliki umiêdzynarodawiaj±ce dla krfb.

%package ksirc-i18n
Summary:	Internationalization and localization files for ksirc
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla ksirc
Group:	X11/Applications
Requires:	%{name}-ksirc = %{epoch}:%{version}-%{release}
Obsoletes:	kde-i18n-Affrikaans
Obsoletes:	kde-i18n-Afrikaans
Obsoletes:	kde-i18n-Arabic
Obsoletes:	kde-i18n-Azerbaijani
Obsoletes:	kde-i18n-Bulgarian
Obsoletes:	kde-i18n-Bosnian
Obsoletes:	kde-i18n-Catalan
Obsoletes:	kde-i18n-Czech
Obsoletes:	kde-i18n-Danish
Obsoletes:	kde-i18n-German
Obsoletes:	kde-i18n-Greek
Obsoletes:	kde-i18n-English_UK
Obsoletes:	kde-i18n-British
Obsoletes:	kde-i18n-Esperanto
Obsoletes:	kde-i18n-Spanish
Obsoletes:	kde-i18n-Estonian
Obsoletes:	kde-i18n-Finnish
Obsoletes:	kde-i18n-French
Obsoletes:	kde-i18n-Hebrew
Obsoletes:	kde-i18n-Hindi
Obsoletes:	kde-i18n-Croatian
Obsoletes:	kde-i18n-Hungarian
Obsoletes:	kde-i18n-Indonesian
Obsoletes:	kde-i18n-Icelandic
Obsoletes:	kde-i18n-Italian
Obsoletes:	kde-i18n-Japanese
Obsoletes:	kde-i18n-Korean
Obsoletes:	kde-i18n-Lithuanian
Obsoletes:	kde-i18n-Latvian
Obsoletes:	kde-i18n-Maltese
Obsoletes:	kde-i18n-Malay
Obsoletes:	kde-i18n-Mongolian
Obsoletes:	kde-i18n-Dutch
Obsoletes:	kde-i18n-Norwegian
Obsoletes:	kde-i18n-Norwegian_Bokmaal
Obsoletes:	kde-i18n-Norwegian_Bookmal
Obsoletes:	kde-i18n-Norwegian_Nynorsk
Obsoletes:	kde-i18n-Polish
Obsoletes:	kde-i18n-Portugnese
Obsoletes:	kde-i18n-Portuguese
Obsoletes:	kde-i18n-Brazil
Obsoletes:	kde-i18n-Brazil_Portugnese
Obsoletes:	kde-i18n-Brazil_Portuguese
Obsoletes:	kde-i18n-Romanian
Obsoletes:	kde-i18n-Russian
Obsoletes:	kde-i18n-Slovak
Obsoletes:	kde-i18n-Slovenian
Obsoletes:	kde-i18n-Serbian
Obsoletes:	kde-i18n-Swedish
Obsoletes:	kde-i18n-Tamil
Obsoletes:	kde-i18n-Thai
Obsoletes:	kde-i18n-Turkish
Obsoletes:	kde-i18n-Ukrainian
Obsoletes:	kde-i18n-Uzbek
Obsoletes:	kde-i18n-Venda
Obsoletes:	kde-i18n-Vietnamese
Obsoletes:	kde-i18n-Xhosa
Obsoletes:	kde-i18n-Simplified_Chinese
Obsoletes:	kde-i18n-Chinese
Obsoletes:	kde-i18n-Chinese-Big5
Obsoletes:	kde-i18n-Zulu
Obsoletes:	kde-i18n-kdelibs
Obsoletes:	kde-i18n

%description ksirc-i18n
Internationalization and localization files for ksirc.

%description -l pl ksirc-i18n
Pliki umiêdzynarodawiaj±ce dla ksirc.

%package ktalkd-i18n
Summary:	Internationalization and localization files for ktalkd
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla ktalkd
Group:	X11/Applications
Requires:	%{name}-ktalkd = %{epoch}:%{version}-%{release}
Obsoletes:	kde-i18n-Affrikaans
Obsoletes:	kde-i18n-Afrikaans
Obsoletes:	kde-i18n-Arabic
Obsoletes:	kde-i18n-Azerbaijani
Obsoletes:	kde-i18n-Bulgarian
Obsoletes:	kde-i18n-Bosnian
Obsoletes:	kde-i18n-Catalan
Obsoletes:	kde-i18n-Czech
Obsoletes:	kde-i18n-Danish
Obsoletes:	kde-i18n-German
Obsoletes:	kde-i18n-Greek
Obsoletes:	kde-i18n-English_UK
Obsoletes:	kde-i18n-British
Obsoletes:	kde-i18n-Esperanto
Obsoletes:	kde-i18n-Spanish
Obsoletes:	kde-i18n-Estonian
Obsoletes:	kde-i18n-Finnish
Obsoletes:	kde-i18n-French
Obsoletes:	kde-i18n-Hebrew
Obsoletes:	kde-i18n-Hindi
Obsoletes:	kde-i18n-Croatian
Obsoletes:	kde-i18n-Hungarian
Obsoletes:	kde-i18n-Indonesian
Obsoletes:	kde-i18n-Icelandic
Obsoletes:	kde-i18n-Italian
Obsoletes:	kde-i18n-Japanese
Obsoletes:	kde-i18n-Korean
Obsoletes:	kde-i18n-Lithuanian
Obsoletes:	kde-i18n-Latvian
Obsoletes:	kde-i18n-Maltese
Obsoletes:	kde-i18n-Malay
Obsoletes:	kde-i18n-Mongolian
Obsoletes:	kde-i18n-Dutch
Obsoletes:	kde-i18n-Norwegian
Obsoletes:	kde-i18n-Norwegian_Bokmaal
Obsoletes:	kde-i18n-Norwegian_Bookmal
Obsoletes:	kde-i18n-Norwegian_Nynorsk
Obsoletes:	kde-i18n-Polish
Obsoletes:	kde-i18n-Portugnese
Obsoletes:	kde-i18n-Portuguese
Obsoletes:	kde-i18n-Brazil
Obsoletes:	kde-i18n-Brazil_Portugnese
Obsoletes:	kde-i18n-Brazil_Portuguese
Obsoletes:	kde-i18n-Romanian
Obsoletes:	kde-i18n-Russian
Obsoletes:	kde-i18n-Slovak
Obsoletes:	kde-i18n-Slovenian
Obsoletes:	kde-i18n-Serbian
Obsoletes:	kde-i18n-Swedish
Obsoletes:	kde-i18n-Tamil
Obsoletes:	kde-i18n-Thai
Obsoletes:	kde-i18n-Turkish
Obsoletes:	kde-i18n-Ukrainian
Obsoletes:	kde-i18n-Uzbek
Obsoletes:	kde-i18n-Venda
Obsoletes:	kde-i18n-Vietnamese
Obsoletes:	kde-i18n-Xhosa
Obsoletes:	kde-i18n-Simplified_Chinese
Obsoletes:	kde-i18n-Chinese
Obsoletes:	kde-i18n-Chinese-Big5
Obsoletes:	kde-i18n-Zulu
Obsoletes:	kde-i18n-kdelibs
Obsoletes:	kde-i18n

%description ktalkd-i18n
Internationalization and localization files for ktalkd.

%description -l pl ktalkd-i18n
Pliki umiêdzynarodawiaj±ce dla ktalkd.

%package kwifimanager-i18n
Summary:	Internationalization and localization files for kwifimanager
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kwifimanager
Group:	X11/Applications
Requires:	%{name}-kwifimanager = %{epoch}:%{version}-%{release}
Obsoletes:	kde-i18n-Affrikaans
Obsoletes:	kde-i18n-Afrikaans
Obsoletes:	kde-i18n-Arabic
Obsoletes:	kde-i18n-Azerbaijani
Obsoletes:	kde-i18n-Bulgarian
Obsoletes:	kde-i18n-Bosnian
Obsoletes:	kde-i18n-Catalan
Obsoletes:	kde-i18n-Czech
Obsoletes:	kde-i18n-Danish
Obsoletes:	kde-i18n-German
Obsoletes:	kde-i18n-Greek
Obsoletes:	kde-i18n-English_UK
Obsoletes:	kde-i18n-British
Obsoletes:	kde-i18n-Esperanto
Obsoletes:	kde-i18n-Spanish
Obsoletes:	kde-i18n-Estonian
Obsoletes:	kde-i18n-Finnish
Obsoletes:	kde-i18n-French
Obsoletes:	kde-i18n-Hebrew
Obsoletes:	kde-i18n-Hindi
Obsoletes:	kde-i18n-Croatian
Obsoletes:	kde-i18n-Hungarian
Obsoletes:	kde-i18n-Indonesian
Obsoletes:	kde-i18n-Icelandic
Obsoletes:	kde-i18n-Italian
Obsoletes:	kde-i18n-Japanese
Obsoletes:	kde-i18n-Korean
Obsoletes:	kde-i18n-Lithuanian
Obsoletes:	kde-i18n-Latvian
Obsoletes:	kde-i18n-Maltese
Obsoletes:	kde-i18n-Malay
Obsoletes:	kde-i18n-Mongolian
Obsoletes:	kde-i18n-Dutch
Obsoletes:	kde-i18n-Norwegian
Obsoletes:	kde-i18n-Norwegian_Bokmaal
Obsoletes:	kde-i18n-Norwegian_Bookmal
Obsoletes:	kde-i18n-Norwegian_Nynorsk
Obsoletes:	kde-i18n-Polish
Obsoletes:	kde-i18n-Portugnese
Obsoletes:	kde-i18n-Portuguese
Obsoletes:	kde-i18n-Brazil
Obsoletes:	kde-i18n-Brazil_Portugnese
Obsoletes:	kde-i18n-Brazil_Portuguese
Obsoletes:	kde-i18n-Romanian
Obsoletes:	kde-i18n-Russian
Obsoletes:	kde-i18n-Slovak
Obsoletes:	kde-i18n-Slovenian
Obsoletes:	kde-i18n-Serbian
Obsoletes:	kde-i18n-Swedish
Obsoletes:	kde-i18n-Tamil
Obsoletes:	kde-i18n-Thai
Obsoletes:	kde-i18n-Turkish
Obsoletes:	kde-i18n-Ukrainian
Obsoletes:	kde-i18n-Uzbek
Obsoletes:	kde-i18n-Venda
Obsoletes:	kde-i18n-Vietnamese
Obsoletes:	kde-i18n-Xhosa
Obsoletes:	kde-i18n-Simplified_Chinese
Obsoletes:	kde-i18n-Chinese
Obsoletes:	kde-i18n-Chinese-Big5
Obsoletes:	kde-i18n-Zulu
Obsoletes:	kde-i18n-kdelibs
Obsoletes:	kde-i18n

%description kwifimanager-i18n
Internationalization and localization files for kwifimanager.

%description -l pl kwifimanager-i18n
Pliki umiêdzynarodawiaj±ce dla kwifimanager.

%package lanbrowser-i18n
Summary:	Internationalization and localization files for lanbrowser
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla lanbrowser
Group:	X11/Applications
Requires:	%{name}-lanbrowser = %{epoch}:%{version}-%{release}
Obsoletes:	kde-i18n-Affrikaans
Obsoletes:	kde-i18n-Afrikaans
Obsoletes:	kde-i18n-Arabic
Obsoletes:	kde-i18n-Azerbaijani
Obsoletes:	kde-i18n-Bulgarian
Obsoletes:	kde-i18n-Bosnian
Obsoletes:	kde-i18n-Catalan
Obsoletes:	kde-i18n-Czech
Obsoletes:	kde-i18n-Danish
Obsoletes:	kde-i18n-German
Obsoletes:	kde-i18n-Greek
Obsoletes:	kde-i18n-English_UK
Obsoletes:	kde-i18n-British
Obsoletes:	kde-i18n-Esperanto
Obsoletes:	kde-i18n-Spanish
Obsoletes:	kde-i18n-Estonian
Obsoletes:	kde-i18n-Finnish
Obsoletes:	kde-i18n-French
Obsoletes:	kde-i18n-Hebrew
Obsoletes:	kde-i18n-Hindi
Obsoletes:	kde-i18n-Croatian
Obsoletes:	kde-i18n-Hungarian
Obsoletes:	kde-i18n-Indonesian
Obsoletes:	kde-i18n-Icelandic
Obsoletes:	kde-i18n-Italian
Obsoletes:	kde-i18n-Japanese
Obsoletes:	kde-i18n-Korean
Obsoletes:	kde-i18n-Lithuanian
Obsoletes:	kde-i18n-Latvian
Obsoletes:	kde-i18n-Maltese
Obsoletes:	kde-i18n-Malay
Obsoletes:	kde-i18n-Mongolian
Obsoletes:	kde-i18n-Dutch
Obsoletes:	kde-i18n-Norwegian
Obsoletes:	kde-i18n-Norwegian_Bokmaal
Obsoletes:	kde-i18n-Norwegian_Bookmal
Obsoletes:	kde-i18n-Norwegian_Nynorsk
Obsoletes:	kde-i18n-Polish
Obsoletes:	kde-i18n-Portugnese
Obsoletes:	kde-i18n-Portuguese
Obsoletes:	kde-i18n-Brazil
Obsoletes:	kde-i18n-Brazil_Portugnese
Obsoletes:	kde-i18n-Brazil_Portuguese
Obsoletes:	kde-i18n-Romanian
Obsoletes:	kde-i18n-Russian
Obsoletes:	kde-i18n-Slovak
Obsoletes:	kde-i18n-Slovenian
Obsoletes:	kde-i18n-Serbian
Obsoletes:	kde-i18n-Swedish
Obsoletes:	kde-i18n-Tamil
Obsoletes:	kde-i18n-Thai
Obsoletes:	kde-i18n-Turkish
Obsoletes:	kde-i18n-Ukrainian
Obsoletes:	kde-i18n-Uzbek
Obsoletes:	kde-i18n-Venda
Obsoletes:	kde-i18n-Vietnamese
Obsoletes:	kde-i18n-Xhosa
Obsoletes:	kde-i18n-Simplified_Chinese
Obsoletes:	kde-i18n-Chinese
Obsoletes:	kde-i18n-Chinese-Big5
Obsoletes:	kde-i18n-Zulu
Obsoletes:	kde-i18n-kdelibs
Obsoletes:	kde-i18n

%description lanbrowser-i18n
Internationalization and localization files for lanbrowser.

%description -l pl lanbrowser-i18n
Pliki umiêdzynarodawiaj±ce dla lanbrowser.


%package rss-i18n
Summary:	Internationalization and localization files for rss
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla rss
Group:	X11/Applications
Requires:	%{name}-kdict = %{epoch}:%{version}-%{release}
Obsoletes:	kde-i18n-Affrikaans
Obsoletes:	kde-i18n-Afrikaans
Obsoletes:	kde-i18n-Arabic
Obsoletes:	kde-i18n-Azerbaijani
Obsoletes:	kde-i18n-Bulgarian
Obsoletes:	kde-i18n-Bosnian
Obsoletes:	kde-i18n-Catalan
Obsoletes:	kde-i18n-Czech
Obsoletes:	kde-i18n-Danish
Obsoletes:	kde-i18n-German
Obsoletes:	kde-i18n-Greek
Obsoletes:	kde-i18n-English_UK
Obsoletes:	kde-i18n-British
Obsoletes:	kde-i18n-Esperanto
Obsoletes:	kde-i18n-Spanish
Obsoletes:	kde-i18n-Estonian
Obsoletes:	kde-i18n-Finnish
Obsoletes:	kde-i18n-French
Obsoletes:	kde-i18n-Hebrew
Obsoletes:	kde-i18n-Hindi
Obsoletes:	kde-i18n-Croatian
Obsoletes:	kde-i18n-Hungarian
Obsoletes:	kde-i18n-Indonesian
Obsoletes:	kde-i18n-Icelandic
Obsoletes:	kde-i18n-Italian
Obsoletes:	kde-i18n-Japanese
Obsoletes:	kde-i18n-Korean
Obsoletes:	kde-i18n-Lithuanian
Obsoletes:	kde-i18n-Latvian
Obsoletes:	kde-i18n-Maltese
Obsoletes:	kde-i18n-Malay
Obsoletes:	kde-i18n-Mongolian
Obsoletes:	kde-i18n-Dutch
Obsoletes:	kde-i18n-Norwegian
Obsoletes:	kde-i18n-Norwegian_Bokmaal
Obsoletes:	kde-i18n-Norwegian_Bookmal
Obsoletes:	kde-i18n-Norwegian_Nynorsk
Obsoletes:	kde-i18n-Polish
Obsoletes:	kde-i18n-Portugnese
Obsoletes:	kde-i18n-Portuguese
Obsoletes:	kde-i18n-Brazil
Obsoletes:	kde-i18n-Brazil_Portugnese
Obsoletes:	kde-i18n-Brazil_Portuguese
Obsoletes:	kde-i18n-Romanian
Obsoletes:	kde-i18n-Russian
Obsoletes:	kde-i18n-Slovak
Obsoletes:	kde-i18n-Slovenian
Obsoletes:	kde-i18n-Serbian
Obsoletes:	kde-i18n-Swedish
Obsoletes:	kde-i18n-Tamil
Obsoletes:	kde-i18n-Thai
Obsoletes:	kde-i18n-Turkish
Obsoletes:	kde-i18n-Ukrainian
Obsoletes:	kde-i18n-Uzbek
Obsoletes:	kde-i18n-Venda
Obsoletes:	kde-i18n-Vietnamese
Obsoletes:	kde-i18n-Xhosa
Obsoletes:	kde-i18n-Simplified_Chinese
Obsoletes:	kde-i18n-Chinese
Obsoletes:	kde-i18n-Chinese-Big5
Obsoletes:	kde-i18n-Zulu
Obsoletes:	kde-i18n-kdelibs
Obsoletes:	kde-i18n

%description rss-i18n
Internationalization and localization files for rss.

%description -l pl rss-i18n
Pliki umiêdzynarodawiaj±ce dla rss.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%{?with_ggstatus:%patch3 -p1}
%{?without_loadmovie:%patch4 -p0}
%patch5 -p1
%patch6 -p1

%build
cp /usr/share/automake/config.sub admin
%{__make} -f admin/Makefile.common cvs

%configure \
	--disable-rpath \
	--with-qt-libraries=%{_libdir} \
	--enable-final

%{__make}

%install
#rm -rf $RPM_BUILD_ROOT
#
##%{__make} install \
#	DESTDIR=$RPM_BUILD_ROOT \
#	kde_htmldir=%{_kdedocdir}

##%if %{with i18n}
#if [ -f "%{SOURCE1}" ] ; then
#	bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT
#	for f in $RPM_BUILD_ROOT%{_datadir}/locale/*/LC_MESSAGES/*.mo; do
#		if [ "`file $f | sed -e 's/.*,//' -e 's/message.*//'`" -le 1 ] ; then
#			rm -f $f
#		fi
#	done
#else
#	echo "No i18n sources found and building --with i18n. FIXIT!"
#	exit 1
#fi
#
##%endif

#install -d $RPM_BUILD_ROOT%{_sysconfdir}/{rc.d/init.d,sysconfig}
#
#install %{SOURCE2} $RPM_BUILD_ROOT/etc/rc.d/init.d/lisa
#install %{SOURCE3} $RPM_BUILD_ROOT/etc/sysconfig/lisa
#install %{SOURCE4} $RPM_BUILD_ROOT%{_sysconfdir}/lisarc

#mv $RPM_BUILD_ROOT%{_datadir}/applnk/Internet/kopete.desktop \
#   $RPM_BUILD_ROOT%{_desktopdir}/kde
#
#cd $RPM_BUILD_ROOT%{_iconsdir}
#mv {locolor,crystalsvg}/16x16/apps/krfb.png
#cd -
#


%find_lang kdict		--with-kde
%find_lang kget			--with-kde
%find_lang knewsticker		--with-kde
%find_lang kopete		--with-kde
%find_lang kpf			--with-kde
%find_lang kppp			--with-kde
%find_lang krdc			--with-kde
%find_lang krfb			--with-kde
cat krdc.lang >> krfb.lang
%find_lang ksirc		--with-kde
%find_lang kwifimanager		--with-kde
%find_lang lisa			--with-kde
%find_lang lanbrowser		--with-kde
cat lanbrowser.lang >> lisa.lang

%if %{with i18n}
##%find_lang kcmkxmlrpcd		--with-kde
%find_lang ktalkd		--with-kde
%find_lang kcmtalkd		--with-kde
%find_lang kcmktalkd             --with-kde
cat kcmtalkd.lang >> ktalkd.lang
cat kcmktalkd.lang >> ktalkd.lang

%find_lang kcm_krfb             --with-kde
cat kcm_krfb.lang >> krfb.lang

%find_lang kcmlanbrowser           --with-kde
cat kcmlanbrowser.lang >> lisa.lang
%find_lang kio_lan           --with-kde
cat kio_lan.lang >> lisa.lang

%find_lang kppplogview       --with-kde
cat kppplogview.lang >> kppp.lang


%find_lang kwireless            --with-kde
cat kwireless.lang >> kwifimanager.lang
%find_lang kcmwifi            --with-kde
cat kcmwifi.lang >> kwifimanager.lang

%find_lang kdictapplet        --with-kde
cat kdictapplet.lang >> kdict.lang

%find_lang dcopservice       --with-kde
%find_lang desktop_kdenetwork           --with-kde
%find_lang kinetd               --with-kde

%endif

files="kdict \
kget \
knewsticker \
kopete \
kpf \
kppp \
krfb \
ksirc \
kwifimanager \
lisa"

for i in $files; do
	> ${i}_en.lang
	grep en\/ ${i}.lang|grep -v apidocs >> ${i}_en.lang
	grep -v apidocs $i.lang|grep -v en\/ > ${i}.lang.1
	mv ${i}.lang.1 ${i}.lang
done
				
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

%post	libkopete	-p /sbin/ldconfig
%postun	libkopete	-p /sbin/ldconfig

%post	libkopete_msn	-p /sbin/ldconfig
%postun	libkopete_msn	-p /sbin/ldconfig

%post	libkopete_oscar	-p /sbin/ldconfig
%postun	libkopete_oscar	-p /sbin/ldconfig

%post	librss		-p /sbin/ldconfig
%postun	librss		-p /sbin/ldconfig

%if %{with i18n}
%files kdict-i18n -f kdict.lang
%files kget-i18n -f kget.lang
%files knewsticker-i18n -f knewsticker.lang
%files kopete-i18n -f kopete.lang
%files kpf-i18n -f kpf.lang
%files kppp-i18n -f kppp.lang
%files krfb-i18n -f krfb.lang
%files ksirc-i18n -f ksirc.lang
%files ktalkd-i18n -f ktalkd.lang
%files kwifimanager-i18n -f kwifimanager.lang
%files lanbrowser-i18n -f lisa.lang
%files kinetd-i18n -f kinetd.lang
%files kdenetwork-i18n -f desktop_kdenetwork.lang
%files rss-i18n -f dcopservice.lang


%endif

%files devel
%defattr(644,root,root,755)
%{_includedir}/rss
%{_libdir}/libkopete.so
%{_libdir}/libkopete_msn_shared.so
%{_libdir}/libkopete_oscar.so
%{_libdir}/librss.so

%files kdict -f kdict_en.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kdict
%{_libdir}/kde3/kdict_panelapplet.la
%attr(755,root,root) %{_libdir}/kde3/kdict_panelapplet.so
%{_datadir}/apps/kdict
%{_datadir}/apps/kicker/applets/kdictapplet.desktop
%{_desktopdir}/kde/kdict.desktop
%{_iconsdir}/*/*/*/kdict*

%files kget -f kget_en.lang
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

%files knewsticker -f knewsticker_en.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/knewstickerstub
%{_libdir}/kde3/knewsticker_panelapplet.la
%attr(755,root,root) %{_libdir}/kde3/knewsticker_panelapplet.so
%{_datadir}/apps/knewsticker
%{_datadir}/apps/kicker/applets/knewsticker.desktop
%{_datadir}/apps/kconf_update/kn*
%{_datadir}/applnk/.hidden/knewstickerstub.desktop
%{_desktopdir}/kde/knewsticker*.desktop
%{_iconsdir}/*/*/*/knewsticker.png

%files kopete -f kopete_en.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kconf_update_bin/kopete-account-kconf_update
%attr(755,root,root) %{_libdir}/kconf_update_bin/kopete-pluginloader2-kconf_update
%attr(755,root,root) %{_bindir}/kopete
%{_libdir}/kde3/kcm_kopete_accountconfig.la
%attr(755,root,root) %{_libdir}/kde3/kcm_kopete_accountconfig.so
%{_libdir}/kde3/kcm_kopete_appearanceconfig.la
%attr(755,root,root) %{_libdir}/kde3/kcm_kopete_appearanceconfig.so
%{_libdir}/kde3/kcm_kopete_autoreplace.la
%attr(755,root,root) %{_libdir}/kde3/kcm_kopete_autoreplace.so
%{_libdir}/kde3/kcm_kopete_behaviorconfig.la
%attr(755,root,root) %{_libdir}/kde3/kcm_kopete_behaviorconfig.so
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
%dir %{_datadir}/apps/kopete/icons
%dir %{_datadir}/apps/kopete/icons/crystalsvg
%dir %{_datadir}/apps/kopete/icons/crystalsvg/*
%dir %{_datadir}/apps/kopete/icons/crystalsvg/*/*
%{_datadir}/apps/kopete/icons/crystalsvg/*/*/admin_icon.png
%{_datadir}/apps/kopete/icons/crystalsvg/*/*/aol_icon.png
%{_datadir}/apps/kopete/icons/crystalsvg/*/*/dt_icon.png
%{_datadir}/apps/kopete/icons/crystalsvg/*/*/emoticon.png
%{_datadir}/apps/kopete/icons/crystalsvg/*/*/free_icon.png
%{_datadir}/apps/kopete/icons/crystalsvg/*/*/kopeteavailable.png
%{_datadir}/apps/kopete/icons/crystalsvg/*/*/kopeteaway.png
%{_datadir}/apps/kopete/icons/crystalsvg/*/*/metacontact_away.png
%{_datadir}/apps/kopete/icons/crystalsvg/*/*/metacontact_offline.png
%{_datadir}/apps/kopete/icons/crystalsvg/*/*/metacontact_online.png
%{_datadir}/apps/kopete/icons/crystalsvg/*/*/metacontact_unknown.png
%{_datadir}/apps/kopete/icons/crystalsvg/*/*/newmsg.png
%{_datadir}/apps/kopete/icons/crystalsvg/*/*/newmessage.mng
%{_datadir}/apps/kopete/icons/crystalsvg/*/*/status_unknown.png
%dir %{_datadir}/apps/kopete/pics
%{_datadir}/apps/kopete/pics/emoticons
%{_datadir}/apps/kopete/styles
%dir %{_datadir}/apps/kopeterichtexteditpart
%{_datadir}/apps/kopeterichtexteditpart/kopeterichtexteditpartfull.rc
%{_datadir}/apps/kopeterichtexteditpart/kopeterichtexteditpartsimple.rc
%{_datadir}/services/chatwindow.desktop
%{_datadir}/services/kopete_accountconfig.desktop
%{_datadir}/services/kopete_appearanceconfig.desktop
%{_datadir}/services/kopete_behaviorconfig.desktop
%{_datadir}/servicetypes/kopeteplugin.desktop
%{_datadir}/servicetypes/kopeteprotocol.desktop
%{_datadir}/servicetypes/kopeteui.desktop
%{_datadir}/sounds/Kopete_Event.ogg
%{_datadir}/sounds/Kopete_Received.ogg
%{_datadir}/sounds/Kopete_Sent.ogg
%{_datadir}/sounds/Kopete_User_is_Online.ogg
%{_desktopdir}/kde/kopete.desktop
%{_iconsdir}/crystalsvg/*/apps/kopete.png

%files kopete-protocol-aim
%defattr(644,root,root,755)
%{_libdir}/kde3/kopete*aim*.la
%attr(755,root,root) %{_libdir}/kde3/kopete*aim*.so
%{_datadir}/apps/kopete/icons/crystalsvg/*/*/aim*
%{_datadir}/services/kopete_aim.desktop

%files kopete-protocol-gg
%defattr(644,root,root,755)
%{_libdir}/kde3/kopete*gadu*.la
%attr(755,root,root) %{_libdir}/kde3/kopete*gadu*.so
%{_datadir}/apps/kopete/icons/crystalsvg/*/*/gadu*
%{_datadir}/apps/kopete/icons/crystalsvg/*/*/gg*
%{_datadir}/services/kopete_gadu.desktop

%files kopete-protocol-icq
%defattr(644,root,root,755)
%{_libdir}/kde3/kopete*icq*.la
%attr(755,root,root) %{_libdir}/kde3/kopete*icq*.so
%{_datadir}/apps/kopete/icons/crystalsvg/*/*/icq*
%{_datadir}/services/kopete_icq.desktop

%files kopete-protocol-irc
%defattr(644,root,root,755)
%{_libdir}/kde3/kopete*irc*.la
%attr(755,root,root) %{_libdir}/kde3/kopete*irc*.so
%{_datadir}/apps/kopete/icons/crystalsvg/*/*/irc*
%{_datadir}/services/kopete_irc.desktop
#%%{_datadir}/apps/kopete/pics/irc_connecting.mng

%files kopete-protocol-jabber
%defattr(644,root,root,755)
%{_libdir}/kde3/kopete*jabber*.la
%attr(755,root,root) %{_libdir}/kde3/kopete*jabber*.so
%{_datadir}/apps/kopete/icons/crystalsvg/*/*/jabber*
%{_datadir}/services/kopete_jabber.desktop

%files kopete-protocol-msn
%defattr(644,root,root,755)
%{_libdir}/kde3/kcm_kopete_msn.la
%attr(755,root,root) %{_libdir}/kde3/kcm_kopete_msn.so
%{_libdir}/kde3/kopete*msn*.la
%attr(755,root,root) %{_libdir}/kde3/kopete*msn*.so
%{_datadir}/apps/kopete/icons/crystalsvg/*/*/msn*
%{_datadir}/services/kconfiguredialog/kopete_msn_config.desktop
%{_datadir}/services/kopete_msn.desktop

%files kopete-protocol-sms
%defattr(644,root,root,755)
%{_libdir}/kde3/kopete*sms*.la
%attr(755,root,root) %{_libdir}/kde3/kopete*sms*.so
%{_datadir}/apps/kopete/icons/crystalsvg/*/*/sms*
%{_datadir}/services/kopete_sms.desktop

#%files kopete-protocol-testbed
#%defattr(644,root,root,755)
#%{_libdir}/kde3/kopete_testbed.la
#%attr(755,root,root) %{_libdir}/kde3/kopete_testbed.so
#%{_datadir}/apps/kopete/icons/crystalsvg/*/*/testbed*
#%{_datadir}/services/kopete_testbed.desktop

#%files kopete-protocol-winpopup
#%defattr(644,root,root,755)
#%attr(755,root,root) %{_bindir}/winpopup*.sh
#%{_libdir}/kde3/kcm_kopete_wp.la
#%attr(755,root,root) %{_libdir}/kde3/kcm_kopete_wp.so
#%{_libdir}/kde3/kopete*wp*.la
#%attr(755,root,root) %{_libdir}/kde3/kopete*wp*.so
#%{_datadir}/apps/kopete/icons/crystalsvg/*/*/wp*
#%{_datadir}/services/kconfiguredialog/kopete_wp_config.desktop
#%{_datadir}/services/kopete_wp.desktop

%files kopete-protocol-yahoo
%defattr(644,root,root,755)
%{_libdir}/kde3/kopete_yahoo.la
%attr(755,root,root) %{_libdir}/kde3/kopete_yahoo.so
%{_datadir}/apps/kopete/icons/*/*/*/yahoo*
%{_datadir}/services/kopete_yahoo.desktop

%files kopete-tool-autoreplace
%defattr(644,root,root,755)
%{_libdir}/kde3/kcm_kopete_autoreplace.la
%attr(755,root,root) %{_libdir}/kde3/kcm_kopete_autoreplace.so
%{_libdir}/kde3/kopete*autoreplace*.la
%attr(755,root,root) %{_libdir}/kde3/kopete*autoreplace*.so
%{_datadir}/apps/kopete/icons/crystalsvg/*/*/autoreplace.png
%{_datadir}/services/kopete_autoreplace.desktop
%{_datadir}/services/kconfiguredialog/kopete_autoreplace_config.desktop

%files kopete-tool-conectionstatus
%defattr(644,root,root,755)
%{_libdir}/kde3/kopete*connectionstatus*.la
%attr(755,root,root) %{_libdir}/kde3/kopete*connectionstatus*.so
%{_datadir}/services/kopete_connectionstatus.desktop

%files kopete-tool-contactnotes
%defattr(644,root,root,755)
%{_libdir}/kde3/kopete*contactnotes*.la
%attr(755,root,root) %{_libdir}/kde3/kopete*contactnotes*.so
%{_datadir}/apps/kopete_contactnotes
%{_datadir}/services/kopete_contactnotes.desktop

%files kopete-tool-cryptography
%defattr(644,root,root,755)
%{_libdir}/kde3/kcm_kopete_cryptography.la
%attr(755,root,root) %{_libdir}/kde3/kcm_kopete_cryptography.so
%{_libdir}/kde3/kopete*cryptography*.la
%attr(755,root,root) %{_libdir}/kde3/kopete*cryptography*.so
%{_datadir}/apps/kopete_cryptography
%{_datadir}/services/kopete_cryptography.desktop
%{_datadir}/services/kconfiguredialog/kopete_cryptography_config.desktop

%files kopete-tool-highlight
%defattr(644,root,root,755)
%{_libdir}/kde3/kcm_kopete_highlight.la
%attr(755,root,root) %{_libdir}/kde3/kcm_kopete_highlight.so
%{_libdir}/kde3/kopete*highlight*.la
%attr(755,root,root) %{_libdir}/kde3/kopete*highlight*.so
%{_datadir}/apps/kopete/icons/crystalsvg/*/*/highlight.png
%{_datadir}/services/kopete_highlight.desktop
%{_datadir}/services/kconfiguredialog/kopete_highlight_config.desktop

%files kopete-tool-history
%defattr(644,root,root,755)
%{_libdir}/kde3/kcm_kopete_history.la
%attr(755,root,root) %{_libdir}/kde3/kcm_kopete_history.so
%{_libdir}/kde3/kopete*history*.la
%attr(755,root,root) %{_libdir}/kde3/kopete*history*.so
%{_datadir}/apps/kopete_history
%{_datadir}/services/kopete_history.desktop
%{_datadir}/services/kconfiguredialog/kopete_history_config.desktop

#%files kopete-tool-motionaway
#%defattr(644,root,root,755)
#%{_libdir}/kde3/kcm_kopete_motionaway.la
#%attr(755,root,root) %{_libdir}/kde3/kcm_kopete_motionaway.so
#%{_libdir}/kde3/kopete*motionaway*.la
#%attr(755,root,root) %{_libdir}/kde3/kopete*motionaway*.so
#%{_datadir}/services/kconfiguredialog/kopete_motionaway_config.desktop
#%{_datadir}/services/motionaway.desktop

%files kopete-tool-nowlistening
%defattr(644,root,root,755)
%{_libdir}/kde3/kcm_kopete_nowlistening.la
%attr(755,root,root) %{_libdir}/kde3/kcm_kopete_nowlistening.so
%{_libdir}/kde3/kopete*nowlistening*.la
%attr(755,root,root) %{_libdir}/kde3/kopete*nowlistening*.so
%{_datadir}/services/kconfiguredialog/kopete_nowlistening_config.desktop
%{_datadir}/services/kopete_nowlistening.desktop

#%%files kopete-tool-spellcheck
#%%defattr(644,root,root,755)
#%%{_libdir}/kde3/kopete*spellcheck*.la
#%%attr(755,root,root) %{_libdir}/kde3/kopete*spellcheck*.so
#%%{_datadir}/services/spellcheck.desktop

%files kopete-tool-texteffect
%defattr(644,root,root,755)
%{_libdir}/kde3/kcm_kopete_texteffect.la
%attr(755,root,root) %{_libdir}/kde3/kcm_kopete_texteffect.so
%{_libdir}/kde3/kopete*texteffect*.la
%attr(755,root,root) %{_libdir}/kde3/kopete*texteffect*.so
%{_datadir}/apps/kopete/icons/crystalsvg/*/*/texteffect.png
%{_datadir}/services/kconfiguredialog/kopete_texteffect_config.desktop
%{_datadir}/services/kopete_texteffect.desktop

%files kopete-tool-translator
%defattr(644,root,root,755)
%{_libdir}/kde3/kcm_kopete_translator.la
%attr(755,root,root) %{_libdir}/kde3/kcm_kopete_translator.so
%{_libdir}/kde3/kopete*translator*.la
%attr(755,root,root) %{_libdir}/kde3/kopete*translator*.so
%{_datadir}/apps/kopete_translator
%{_datadir}/services/kconfiguredialog/kopete_translator_config.desktop
%{_datadir}/services/kopete_translator.desktop

%files kopete-tool-webpresence
%defattr(644,root,root,755)
%{_libdir}/kde3/kcm_kopete_webpresence.la
%attr(755,root,root) %{_libdir}/kde3/kcm_kopete_webpresence.so
%{_libdir}/kde3/kopete*webpresence*.la
%attr(755,root,root) %{_libdir}/kde3/kopete*webpresence*.so
%dir %{_datadir}/apps/kopete/webpresence
%{_datadir}/apps/kopete/webpresence/webpresencedefault.xsl
%{_datadir}/apps/kopete/webpresence/wpimages.xsl
%{_datadir}/services/kconfiguredialog/kopete_webpresence_config.desktop
%{_datadir}/services/kopete_webpresence.desktop

%files kpf -f kpf_en.lang
%defattr(644,root,root,755)
%{_libdir}/kde3/kpf_panelapplet.la
%attr(755,root,root) %{_libdir}/kde3/kpf_panelapplet.so
%{_libdir}/kde3/kpfpropertiesdialog.la
%attr(755,root,root) %{_libdir}/kde3/kpfpropertiesdialog.so
%{_datadir}/apps/kicker/applets/kpfapplet.desktop
%{_datadir}/services/kpfpropertiesdialogplugin.desktop
%{_iconsdir}/*/*/*/kpf*

%files kppp -f kppp_en.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kppplogview
%attr(755,root,root) %{_bindir}/kppp
%{_datadir}/apps/kppp
%{_desktopdir}/kde/Kppp.desktop
%{_desktopdir}/kde/kppplogview.desktop
%{_iconsdir}/*/*/*/kppp.png

%files krfb -f krfb_en.lang
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

%files ksirc -f ksirc_en.lang
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

%files ktalkd -f ktalkd_en.lang
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

#%files kxmlrpcd -f kxmlrpcd.lang
#%defattr(644,root,root,755)
#%attr(755,root,root) %{_bindir}/kxmlrpcd
#%{_libdir}/libkdeinit_kxmlrpcd.la
#%attr(755,root,root) %{_libdir}/libkdeinit_kxmlrpcd.so
#%{_libdir}/kde3/kxmlrpcd.la
#%attr(755,root,root) %{_libdir}/kde3/kxmlrpcd.so
#%{_libdir}/kde3/kcm_xmlrpcd.la
#%attr(755,root,root) %{_libdir}/kde3/kcm_xmlrpcd.so
#%{_datadir}/services/kxmlrpcd.desktop

%files kwifimanager -f kwifimanager_en.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kwifimanager
%{_libdir}/libkwireless.la
%attr(755,root,root) %{_libdir}/libkwireless.so
%{_libdir}/kde3/kcm_kwifimanager.la
%attr(755,root,root) %{_libdir}/kde3/kcm_kwifimanager.so
%{_datadir}/apps/kicker/applets/kwireless.desktop
%{_datadir}/apps/kwifimanager
%{_datadir}/applications/kde/kcmwifi.desktop
%{_datadir}/applications/kde/kwifimanager.desktop

%files lanbrowser -f lisa_en.lang
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
%{_datadir}/applnk/.hidden/kcmkiolan.desktop
%{_datadir}/applnk/.hidden/kcmlisa.desktop
%{_datadir}/applnk/.hidden/kcmreslisa.desktop

%files libkopete
%defattr(644,root,root,755)
%{_libdir}/libkopete.la
%attr(755,root,root) %{_libdir}/libkopete.so.*.*.*

%files libkopete_msn
%defattr(644,root,root,755)
%{_libdir}/libkopete_msn_shared.la
%attr(755,root,root) %{_libdir}/libkopete_msn_shared.so.*.*.*

%files libkopete_oscar
%defattr(644,root,root,755)
%{_libdir}/libkopete_oscar.la
%attr(755,root,root) %{_libdir}/libkopete_oscar.so.*.*.*

%files librss
%defattr(644,root,root,755)
%{_libdir}/librss.la
%attr(755,root,root) %{_libdir}/librss.so.*.*.*

%files rss
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/feedbrowser
%attr(755,root,root) %{_bindir}/rssclient
%attr(755,root,root) %{_bindir}/rssservice
%{_datadir}/services/rssservice.desktop
