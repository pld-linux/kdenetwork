
%define		_state		unstable
%define		_ver		3.1.90
%define		_snap		030623

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
# Source0-md5:	f6c0dacfaf4b3037e60d562445517e8a
Source2:	%{name}-lisa.init
Source3:        %{name}-lisa.sysconfig
Source4:        %{name}-lisarc
Patch0:		%{name}-utmpx.patch
Patch1:		%{name}-use_sendmail.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	fam-devel
BuildRequires:	gettext-devel
BuildRequires:	kdelibs-devel >= %{version}
BuildRequires:	libtool
BuildRequires:	libxml2-progs
BuildRequires:	openslp-devel
BuildRequires:	qt-devel >= 3.1
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_htmldir	%{_docdir}/kde/HTML
%define		_icondir	%{_datadir}/icons

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

%package kdict
Summary:	Online dictionary client
Summary(pl):	Klient s³ownika
License:	Artistic
Group:		X11/Applications
Requires:	kdebase-kicker >= %{version}
Provides:	kdict
Obsoletes:	%{name}-kmail
Obsoletes:	%{name}-knode
Obsoletes:	%{name}-korn

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
Requires:	kdelibs >= %{version}
Obsoletes:	%{name}-krfb < 9:3.1-6
Obsoletes:	%{name}-kmail
Obsoletes:	%{name}-knode
Obsoletes:	%{name}-korn

%description kinetd
An Internet daemon that starts network services on demand.

%description kinetd -l pl
Demon internetowy, który uruchamia na ¿±danie us³ugi sieciowe.

%package kget
Summary:	File Downloander
Summary(pl):	¦ci±gacz plików
Group:		X11/Applications
Requires:	kdebase-core >= %{version}
Obsoletes:	%{name}-kmail
Obsoletes:	%{name}-knode
Obsoletes:	%{name}-korn

%description kget
File Downloader.

%description kget -l pl
¦ci±gacz plików.

%package kit
Summary:	KDE AOL Instant Messenger
Summary(pl):	Klient AOL Instant Messenger dla KDE
Summary(pt_BR):	Comunicador que usa o protocolo AOL
License:	LGPL
Group:		X11/Applications
Requires:	kdebase-core >= %{version}
Obsoletes:	%{name}-kmail
Obsoletes:	%{name}-knode
Obsoletes:	%{name}-korn

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
Requires:	kdebase-kicker >= %{version}
Obsoletes:	%{name}-kmail
Obsoletes:	%{name}-knode
Obsoletes:	%{name}-korn

%description knewsticker
KDE News Ticker.

%description knewsticker -l pl
News Ticker dla KDE.

%description knewsticker -l pt_BR
Miniaplicativo de exibição de notícias para o painel Kicker.

%package kpf
Summary:	Public fileserver applet
Summary(pl):	Applet publicznego serwera plików
Group:		X11/Applications
Requires:	kdebase-kicker >= %{version}
Obsoletes:	%{name}-kmail
Obsoletes:	%{name}-knode
Obsoletes:	%{name}-korn

%description kpf
Public fileserver applet.

%description kpf -l pl
Applet publicznego serwera plików.

%package kppp
Summary:	KDE PPP dialer
Summary(pl):	Program do po³±czeñ modemowych dla KDE
Summary(pt_BR):	O discador para Internet
Group:		X11/Applications
Requires:	kdebase-core >= %{version}
Requires:	ppp
Obsoletes:	%{name}-kmail
Obsoletes:	%{name}-knode
Obsoletes:	%{name}-korn

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
Requires:	kdebase-core >= %{version}
Obsoletes:	%{name}-kmail
Obsoletes:	%{name}-knode
Obsoletes:	%{name}-korn

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
Requires:	kdebase-core >= %{version}
Requires:	%{name}-kinetd = %{epoch}:%{version}-%{release}
Obsoletes:	%{name}-kmail
Obsoletes:	%{name}-knode
Obsoletes:	%{name}-korn

%description krfb
Virtual Desktops.

%description krfb -l pl
Wirtualne biurka.

%package ktalkd
Summary:	Talk daemon
Summary(pl):	Daemon talk
Group:		X11/Applications
Requires:	kdebase-core >= %{version}
Obsoletes:	%{name}-kmail
Obsoletes:	%{name}-knode
Obsoletes:	%{name}-korn

%description ktalkd
Talk daemon.

%description ktalkd -l pl
Demon talk.

%package kwifimanager
Summary:	Wireless LAN
Summary(pl):	Bezprzewodowy LAN
Group:		X11/Applications
Requires:	kdelibs >= %{version}
Obsoletes:	%{name}-kmail
Obsoletes:	%{name}-knode
Obsoletes:	%{name}-korn

%description kwifimanager
Wireless LAN.

%description kwifimanager -l pl
Bezprzewodowy LAN.

%package kxmlrpcd
Summary:	KDE XmlRpc Daemon
Summary(pl):	Deamon XmlRpc dla KDE
Group:		X11/Applications
Requires:	kdelibs >= %{version}
Obsoletes:	%{name}-kmail
Obsoletes:	%{name}-knode
Obsoletes:	%{name}-korn

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
Obsoletes:	%{name}-kmail
Obsoletes:	%{name}-knode
Obsoletes:	%{name}-korn
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

%package rss-devel
Summary:	TODO
Summary(pl):	TODO
Group:		X11/Development/Libraries
Obsoletes:	%{name}-librss-devel

%description rss-devel
TODO.

%description rss-devel -l pl
TODO.

%prep
%setup -q -n %{name}-%{_snap}
%patch0 -p1
%patch1 -p1

%build

for plik in `find ./ -name *.desktop` ; do
	echo $plik
	sed -i -e "s/\[nb\]/\[no\]/g" $plik
done

%configure \
	--%{!?debug:dis}%{?debug:en}able-debug \
	--enable-final

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_appsdir=%{_applnkdir} \
	kde_htmldir=%{_htmldir}

install -d $RPM_BUILD_ROOT%{_sysconfdir}/{rc.d/init.d,sysconfig}

mv $RPM_BUILD_ROOT%{_applnkdir}/{Settings,KDE-Settings}

install %{SOURCE2} $RPM_BUILD_ROOT/etc/rc.d/init.d/lisa
install %{SOURCE3} $RPM_BUILD_ROOT/etc/sysconfig/lisa
install %{SOURCE4} $RPM_BUILD_ROOT%{_sysconfdir}/lisarc

cd $RPM_BUILD_ROOT%{_icondir}
mv {locolor,crystalsvg}/16x16/apps/krfb.png
cd -

%find_lang kdict		--with-kde
%find_lang kit			--with-kde
%find_lang knewsticker		--with-kde
%find_lang korn			--with-kde
%find_lang kpf			--with-kde
%find_lang kppp			--with-kde
%find_lang krfb			--with-kde
%find_lang ksirc		--with-kde
%find_lang ktalkd		--with-kde
%find_lang kcmtalkd		--with-kde
cat kcmtalkd.lang >> ktalkd.lang
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

%post	rss	-p /sbin/ldconfig
%postun	rss	-p /sbin/ldconfig

#%files kwifimanager
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
%{_desktopdir}/kdict.desktop
%{_icondir}/*/*/*/kdict*

%files kget
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kget
%{_libdir}/kde3/khtml_kget.la
%attr(755,root,root) %{_libdir}/kde3/khtml_kget.so
%{_datadir}/apps/kget
%{_datadir}/apps/khtml/kpartplugins/kget_plug_in.rc
%{_datadir}/mimelnk/application/x-kgetlist.desktop
%{_desktopdir}/kget.desktop
%{_icondir}/*/*/*/*kget*

%files kinetd
%defattr(644,root,root,755)
%{_libdir}/kde3/kded_kinetd.la
%attr(755,root,root) %{_libdir}/kde3/kded_kinetd.so
%{_datadir}/apps/kinetd
%{_datadir}/services/kded/kinetd.desktop
%{_datadir}/servicetypes/kinetdmodule.desktop

%files kit -f kit.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kit
%{_datadir}/apps/kit
%{_desktopdir}/kit.desktop
%{_icondir}/*/*/*/kit.png

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
%{_desktopdir}/knewsticker*.desktop
%{_icondir}/*/*/*/knewsticker.png

%files kpf -f kpf.lang
%defattr(644,root,root,755)
%{_libdir}/kde3/kpf_panelapplet.la
%attr(755,root,root) %{_libdir}/kde3/kpf_panelapplet.so
%{_libdir}/kde3/kpfpropertiesdialog.la
%attr(755,root,root) %{_libdir}/kde3/kpfpropertiesdialog.so
%{_datadir}/apps/kicker/applets/kpf*
%{_datadir}/services/kpfpropertiesdialogplugin.desktop
%{_icondir}/*/*/*/kpf*

%files kppp -f kppp.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kppplogview
%attr(755,root,root) %{_bindir}/kppp
%{_datadir}/apps/kppp
%{_desktopdir}/Kppp.desktop
%{_desktopdir}/kppplogview.desktop
%{_icondir}/*/*/*/kppp.png

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
%{_applnkdir}/KDE-Settings/Network/kcmkrfb.desktop
%{_desktopdir}/krfb.desktop
%{_desktopdir}/krdc.desktop
%{_icondir}/*/*/*/krdc*
%{_icondir}/[!l]*/*/*/krfb*

%files ksirc -f ksirc.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ksirc
%attr(755,root,root) %{_bindir}/dsirc
%{_libdir}/ksirc.la
%attr(755,root,root) %{_libdir}/ksirc.so
%{_libdir}/kde3/libkntsrcfilepropsdlg.la
%attr(755,root,root) %{_libdir}/kde3/libkntsrcfilepropsdlg.so
%{_datadir}/config/ksircrc
%{_datadir}/apps/ksirc
%{_datadir}/services/kntsrcfilepropsdlg.desktop
%{_desktopdir}/ksirc.desktop
%{_icondir}/[!l]*/*/*/ksirc*

%files ktalkd -f ktalkd.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ktalkd
%attr(755,root,root) %{_bindir}/ktalkdlg
%attr(755,root,root) %{_bindir}/mail.local
%{_libdir}/kde3/kcm_ktalkd.la
%attr(755,root,root) %{_libdir}/kde3/kcm_ktalkd.so
%{_datadir}/config/ktalkd*
%{_datadir}/sounds/ktalkd*
%{_applnkdir}/KDE-Settings/Network/kcmktalkd.desktop
%{_icondir}/*/*/*/ktalkd*

%files kxmlrpcd -f kxmlrpcd.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kxmlrpcd
%{_libdir}/kxmlrpcd.la
%attr(755,root,root) %{_libdir}/kxmlrpcd.so
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

%files rss-devel
%defattr(644,root,root,755)
%{_includedir}/rss                                                      
