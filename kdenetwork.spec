%define 	sver    beta1
Summary:	K Desktop Environment - network applications
Summary(pl):	K Desktop Environment - aplikacje sieciowe
Name:		kdenetwork
Version:	2.2
Release:        0.%{sver}.1
Vendor:		The KDE Team
Source:		ftp://ftp.kde.org/pub/kde/unstable/%{version}%{sver}/src/%{name}-%{version}%{sver}.tar.bz2
Group:          X11/Applications
Copyright:	GPL
BuildRequires:	qt-devel >= 2.2.2
BuildRequires:	kdelibs-devel >= %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_prefix 	/usr/X11R6
%define         _fontdir        /usr/share/fonts
%define         _htmldir        %{_datadir}/doc/kde/HTML

%description
KDE network applications.
Package includes:
  KMail - e-mail client. Patched for proper charsets support
  KORN - "biff" program
  KPPP - PPP dialer
  KNODE - news client
  KSirc - IRC client
  KTalkd - takt daemon

%description -l pl
Aplikacje sieciowe KDE.
Pakiet zawiera:
  KMail - program pocztowy, z poprawion± obs³ug± zestawów znaków
  KORN - program pokazuj±cy stan skrzynek pocztowych
  KPPP - program do nawi±zywania po³±czeñ modemowych
  KNODE - Program do czytania newsów
  KSirc - IRC dla KDE
  KTalkd - talk daemon dla KDE

%package kmail
Summary:     	KDE Mail client
Summary(pl): 	Program pocztowy KDE
Group:       	X11/Applications
Requires:	kdelibs >= %{version}

%description kmail
This is electronic mail client for KDE.
It is able to retrievie mail from POP3 accounts and from local mailboxes. 

This package contains version patched for better charset support.

%description -l pl kmail
Program pocztowy dla KDE.
Potrafi odczytywaæ pocztê z kont POP3 jak i lokalnych skrzynek.

Ten pakiet zawiera wersj± programu z poprawion± obs³ug± zestawów znaków.

%package korn 
Summary:     	KDE 'biff' application
Summary(pl): 	Wska¼nik skrzynki pocztowej dla KDE
Group:       	X11/Applications
Requires:	kdelibs >= %{version}

%description korn
A simple program showing number of mails in your folders.

%description -l pl korn
Programik pokazuj±cy ilo¶æ wiadomo¶ci w wybranych folderach pocztowych.

%package kppp
Summary:     	KDE PPP dialer	
Summary(pl): 	Program do po³±czeñ modemowych dla KDE
Group:       	X11/Applications
Requires:	kdelibs >= %{version}
Requires:	ppp 

%description kppp
A PPPP dialer for KDE. It supports multiple accounts.

%description -l pl kppp
Program no nawi±zywania po³±czeñ modemowych pod KDE.
Posiada ³atwy interfejs i mo¿liwo¶æ zdefiniowania kilku kont.

%package knode
Summary:     	KDE News Reader	
Summary(pl): 	Czytnik newsów dla KDE
Group:       	X11/Applications
Requires:	kdelibs >= %{version}

%description knode
This is a news reader for KDE. It has threading and everything else
you need to be happy reading your news.

%description -l pl knode
Czytnik newsów dla KDE. Obs³uguje w±tki oraz killfile. 

%package ksirc
Summary:     	KDE IRC client
Summary(pl): 	Klient IRC dla KDE
Group:       	X11/Applications
Requires:	kdelibs >= %{version}

%description ksirc

%description -l pl ksirc

%package kit
Summary:     	KDE AOL Instant Messenger
Summary(pl): 	Klient AOL Instant Messenger dla KDE
Group:       	X11/Applications
Requires:	kdelibs >= %{version}

%description kit

%description -l pl kit

%package knewsticker
Summary:     	KDE News Ticker
Group:       	X11/Applications
Requires:	kdelibs >= %{version}

%description knewsticker

%description -l pl knewsticker

%package lanbrowser
Summary:     	KDE Lan Browser
Group:       	X11/Applications
Requires:	kdelibs >= %{version}

%description lanbrowser

%description -l pl lanbrowser


%prep
%setup -q -n %{name}-%{version}%{sver}
%build
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir

%configure2_13 \
	--with-qt-dir=%{_prefix} \
 	--with-install-root=$RPM_BUILD_ROOT \
 	--with-pam="yes"
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_applnkdir}/Network/{Communications,Mail,News,Misc}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install kmail/KMail.desktop		$RPM_BUILD_ROOT%{_applnkdir}/Network/Mail
install korn/KOrn.desktop		$RPM_BUILD_ROOT%{_applnkdir}/Network/Mail
install knode/KNode.desktop		$RPM_BUILD_ROOT%{_applnkdir}/Network/News
install ksirc/ksirc.desktop		$RPM_BUILD_ROOT%{_applnkdir}/Network/Communications
install kppp/Kppp.desktop 		$RPM_BUILD_ROOT%{_applnkdir}/Network/Misc
install kppp/logview/kppplogview.desktop 	$RPM_BUILD_ROOT%{_applnkdir}/Network/Misc
install kit/kit.desktop 		$RPM_BUILD_ROOT%{_applnkdir}/Network/Misc
install korn/KOrn.desktop		$RPM_BUILD_ROOT%{_applnkdir}/Network/Misc

%clean
rm -rf $RPM_BUILD_ROOT

%files kmail
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kmail
%attr(755,root,root) %{_bindir}/kmailcvt
%{_applnkdir}/Network/Mail/KMail.desktop
%{_datadir}/apps/kmail
%{_includedir}/kmail*.h
%{_datadir}/doc/kde/HTML/en/kmail
%{_pixmapsdir}/hicolor/*x*/apps/kmail.png

%files korn
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/korn
%{_applnkdir}/Network/Mail/KOrn.desktop
%{_datadir}/doc/kde/HTML/en/korn
%{_pixmapsdir}/hicolor/*x*/apps/korn.png

%files kppp
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kppplogview
%attr(755,root,root) %{_bindir}/kppp
%{_applnkdir}/Network/Misc/Kppp.desktop
%{_applnkdir}/Network/Misc/kppplogview.desktop
%{_datadir}/apps/kppp
%{_datadir}/doc/kde/HTML/en/kppp
%{_pixmapsdir}/hicolor/*x*/apps/kppp.png

%files knode
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/knode
%{_applnkdir}/Network/News/KNode.desktop
%{_datadir}/apps/knode
%{_datadir}/doc/kde/HTML/en/knode
%{_pixmapsdir}/hicolor/*x*/apps/knode.png

%files ksirc
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ksirc
%attr(755,root,root) %{_bindir}/dsirc
%attr(755,root,root) %{_bindir}/ksticker
%attr(755,root,root) %{_libdir}/ksirc.*
%{_applnkdir}/Network/Communications/ksirc.desktop
%{_datadir}/config/ksircrc
%{_datadir}/apps/ksirc
%{_datadir}/doc/kde/HTML/en/ksirc
%{_pixmapsdir}/hicolor/*x*/apps/ksirc.png

%files kit
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kit
%{_applnkdir}/Network/Misc/kit.desktop
%{_datadir}/doc/kde/HTML/en/kit
%{_pixmapsdir}/hicolor/*x*/apps/kit.png

%files knewsticker
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/knewstickerstub
%attr(755,root,root) %{_bindir}/ksticker
%attr(755,root,root) %{_libdir}/lib*newsticker*
%{_applnkdir}/Settings/Personalization/kcmnewsticker.desktop
%{_applnkdir}/.hidden/knewstickerstub.desktop
%{_datadir}/services/knewsservice.protocol
%{_datadir}/apps/knewsticker
%{_datadir}/apps/kicker/applets/knewsticker.desktop
%{_pixmapsdir}/hicolor/*x*/apps/knewsticker.png

%files lanbrowser
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/reslisa
%attr(755,root,root) %{_bindir}/lisa
%attr(755,root,root) %{_libdir}/lib*lanbrowser*
%attr(755,root,root) %{_libdir}/kio_lan.so
%{_applnkdir}/Settings/Network/lanbrowser.desktop
%{_datadir}/services/rlan.protocol
%{_datadir}/services/lan.protocol
%{_datadir}/apps/lisa
%{_datadir}/apps/konqueror/dirtree/remote/lan.desktop
