Summary:	K Desktop Environment - network applications
Summary(es):	K Desktop Environment - aplicaciones de red
Summary(pl):	K Desktop Environment - aplikacje sieciowe
Summary(pt_BR):	K Desktop Environment - aplicações de rede
Name:		kdenetwork
Version:	2.2.2
Release:	3
Epoch:		8
License:	GPL
Vendor:		The KDE Team
Group:		X11/Applications
Source0:	ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-%{version}.tar.bz2
Patch0:		%{name}-knewsticker-utf8.patch
Patch1:		%{name}-am15.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	kdelibs-devel >= %{version}
BuildRequires:	libtool
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
- KTalkd - takt daemon

%description -l pl
Aplikacje sieciowe KDE. Pakiet zawiera:
- KMail - program pocztowy, z poprawion± obs³ug± zestawów znaków
- KORN - program pokazuj±cy stan skrzynek pocztowych
- KPPP - program do nawi±zywania po³±czeñ modemowych
- KNODE - Program do czytania newsów
- KSirc - IRC dla KDE
- KTalkd - talk daemon dla KDE

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

%description lanbrowser -l pl
Przegl±darka LAN-u dla KDE.

%package kdict
Summary:	Online dictionary client
Summary(pl):	Klient s³ownika
License:	Artistic
Group:		X11/Applications
Requires:	kdelibs >= %{version}

%description kdict
Online dictionary client.

%description kdict -l pl
Klient s³ownika.

%description kdict -l pt_BR
kdict é um utilitário de dicionário que usa servidores dictd da
Internet.

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
%setup	-q
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
install kppp/Kppp.desktop		$RPM_BUILD_ROOT%{_applnkdir}/Network/Misc
install kppp/logview/kppplogview.desktop	$RPM_BUILD_ROOT%{_applnkdir}/Network/Misc
install kit/kit.desktop			$RPM_BUILD_ROOT%{_applnkdir}/Network/Misc
install kdict/kdict.desktop		$RPM_BUILD_ROOT%{_applnkdir}/Network/Misc

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post	kdict -p /sbin/ldconfig
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
