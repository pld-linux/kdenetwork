Summary:	K Desktop Environment - network applications
Summary(pl):	K Desktop Environment - aplikacje sieciowe
Name:		kdenetwork
Version:	1.1.2
Release:	1
Vendor:		The KDE Team
Source:		ftp://ftp.kde.org/pub/kde/stable/%{version}/distribution/tar/generic/source/%{name}-%{version}.tar.bz2
#Patch:		kmail.charset.patch
Group:		X11/KDE/Networking
Group(pl):	X11/KDE/Sieciowe
Copyright:	GPL
Requires:	qt >= 1.40
Requires:	kdelibs = %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_prefix 	/usr/X11R6

%description
KDE network applications.
Package includes:
  KArchie - archie client 
  KBiff - 
  KFinger - finger client 
  KMail - e-mail client. Patched for proper charsets support
  KNU - network utilities (frontend to ping, host, traceroute)
  KORN - "biff" program
  KPPP - PPP dialer
  KRN - news client
  KSirc - IRC client
  KTalkd - takt daemon

%description -l pl
Aplikacje sieciowe KDE.
Pakiet zawiera:
  KArchie - klient dla wyszukiwarek archie
  KBiff - 
  KFinger - klient programu finger
  KMail - program pocztowy, z poprawion± obs³ug± zestawów znaków
  KNU - Interfejs do ping'a, traceroute'a i host'a
  KORN - program pokazuj±cy stan skrzynek pocztowych
  KPPP - program do nawi±zywania po³±czeñ modemowych
  KRN - Program do czytania newsów
  KSirc - IRC dla KDE
  KTalkd - talk daemon dla KDE

%package karchie
Summary:     	KDE Archie clients
Summary(pl): 	Klient programu archie dla KDE
Group:       	X11/KDE/Networking
Group(pl):   	X11/KDE/Sieciowe
Requires:    	qt >= 1.40
Requires:	kdelibs = %{version}

%description karchie
This is archie client for KDE.

%description -l pl karchie
Klient programu archie dla KDE.

%package kbiff
Summary:     	KDE kbiff
Summary(pl): 	KDE kbiff
Group:       	X11/KDE/Networking
Group(pl):   	X11/KDE/Sieciowe
Requires:    	qt >= 1.40
Requires:	kdelibs = %{version}

%description kbiff

%description -l pl kbiff

%package kfinger
Summary:     	KDE finger client
Summary(pl): 	Klient programu 'finger' dla KDE
Group:       	X11/KDE/Networking
Group(pl):   	X11/KDE/Sieciowe
Requires:    	qt >= 1.40
Requires:	kdelibs = %{version}

%description kfinger

%description -l pl kfinger

%package kmail
Summary:     	KDE Mail client
Summary(pl): 	Program pocztowy KDE
Group:       	X11/KDE/Networking
Requires:    	qt >= 1.40
Requires:	kdelibs = %{version}

%description kmail
This is electronic mail client for KDE.
It is able to retrievie mail from POP3 accounts and from local mailboxes. 

This package contains version patched for better charset support.

%description -l pl kmail
Program pocztowy dla KDE.
Potrafi odczytywaæ pocztê z kont POP3 jak i lokalnych skrzynek.

Ten pakiet zawiera wersj± programu z poprawion± obs³ug± zestawów znaków.

%package knu
Summary:     	KDE Network Utilities	
Summary(pl): 	Narzêdzia sieciowe KDE
Group:       	X11/KDE/Networking
Requires:    	qt >= 1.40
Requires:	kdelibs = %{version}
Requires:	inetdaemon

%description knu
Frontend to ping, host and traceroute utilities.

%description -l pl knu
Interfejs do narzêdzi: ping, host i traceroute.

%package korn 
Summary:     	KDE 'biff' application
Summary(pl): 	Wska¼nik skrzynki pocztowej dla KDE
Group:       	X11/KDE/Networking
Requires:    	qt >= 1.40
Requires:	kdelibs = %{version}

%description korn
A simple program showing number of mails in your folders.

%description -l pl korn
Programik pokazuj±cy ilo¶æ wiadomo¶ci w wybranych folderach pocztowych.

%package kppp
Summary:     	KDE PPP dialer	
Summary(pl): 	Program do po³±czeñ modemowych dla KDE
Group:       	X11/KDE/Networking
Requires:    	qt >= 1.40
Requires:	kdelibs = %{version}
Requires:	ppp 

%description kppp
A PPPP dialer for KDE. It supports multiple accounts.

%description -l pl kppp
Program no nawi±zywania po³±czeñ modemowych pod KDE.
Posiada ³atwy interfejs i mo¿liwo¶æ zdefiniowania kilku kont.

%package krn
Summary:     	KDE News Reader	
Summary(pl): 	Czytnik newsów dla KDE
Group:       	X11/KDE/Networking
Requires:    	qt >= 1.40
Requires:	kdelibs = %{version}

%description krn
This is a news reader for KDE. It has threading and everything else
you need to be happy reading your news.

%description -l pl krn
Czytnik newsów dla KDE. Obs³uguje w±tki oraz killfile. 

%package ksirc
Summary:     	KDE IRC client
Summary(pl): 	Klient IRC dla KDE
Group:       	X11/KDE/Networking
Group(pl):   	X11/KDE/Sieciowe
Requires:    	qt >= 1.40
Requires:	kdelibs = %{version}

%description ksirc

%description -l pl ksirc

%package ktalkd
Summary:     	KDE Mail client
Summary(pl): 	Program pocztowy KDE
Group:       	X11/KDE/Networking
Group(pl):   	X11/KDE/Sieciowe
Requires:    	qt >= 1.40
Requires:	kdelibs = %{version}

%description ktalkd

%description -l pl ktalkd

%prep
%setup -q
#%patch -p1

%build
export KDEDIR=%{_prefix}
CXXFLAGS="$RPM_OPT_FLAGS -Wall -fno-rtti" \
CFLAGS="$RPM_OPT_FLAGS -Wall" \
./configure %{_target_platform} \
	--prefix=$KDEDIR \
	--with-qt-dir=%{_prefix} \
 	--with-install-root=$RPM_BUILD_ROOT \
 	--with-pam="yes"
make KDEDIR=$KDEDIR

%install
rm -rf $RPM_BUILD_ROOT
export KDEDIR=%{_prefix}
make RUN_KAPPFINDER=no prefix=$RPM_BUILD_ROOT$KDEDIR install

%find_lang karchie
%find_lang kbiff
%find_lang kfinger
%find_lang kmail
%find_lang knu
%find_lang korn
%find_lang kppp
%find_lang kppplogview
%find_lang krn
%find_lang ksirc
%find_lang pws
%find_lang ktalkd
%find_lang kcmktalkd

%clean
rm -rf $RPM_BUILD_ROOT

#################################################
#             KARCHIE - checking OK
#################################################

%files karchie -f karchie.lang
%defattr(644,root,root,755)

%config(missingok) /etc/X11/kde/karchierc
%config(missingok) /etc/X11/kde/applnk/Internet/karchie.kdelnk

%{_bindir}/karchie

%{_datadir}/kde/doc/HTML/en/karchie

%{_datadir}/kde/icons/karchie.xpm
%{_datadir}/kde/icons/mini/karchie.xpm

#################################################
#             KBIFF - checking OK
#################################################

%files kbiff -f kbiff.lang
%defattr(644,root,root,755)

%config(missingok) /etc/X11/kde/applnk/Internet/kbiff.kdelnk

%{_bindir}/kbiff

%{_datadir}/kde/apps/kbiff

%{_datadir}/kde/doc/HTML/en/kbiff

%{_datadir}/kde/icons/kbiff.xpm
%{_datadir}/kde/icons/mini/kbiff.xpm

#################################################
#             KFINGER - checking OK
#################################################

%files kfinger -f kfinger.lang
%defattr(644,root,root,755)

%config(missingok) /etc/X11/kde/kfingerrc
%config(missingok) /etc/X11/kde/applnk/Internet/kfinger.kdelnk

%{_bindir}/kfinger

%{_datadir}/kde/doc/HTML/en/kfinger

%{_datadir}/kde/toolbar

#################################################
#             KMAIL - checking OK
#################################################

%files kmail -f kmail.lang
%defattr(644,root,root,755)

%config(missingok) /etc/X11/kde/applnk/Internet/KMail.kdelnk

%attr(755,root,root) %{_bindir}/kmail

%{_datadir}/kde/apps/kmail

%{_datadir}/kde/doc/HTML/en/kmail

%{_datadir}/kde/icons/kmail.xpm
%{_datadir}/kde/icons/mini/kmail.xpm

#################################################
#             KNU - checking OK
#################################################

%files knu -f knu.lang
%defattr(644,root,root,755)

%config(missingok) /etc/X11/kde/applnk/Internet/knu.kdelnk

%attr(755,root,root) %{_bindir}/knu

%{_datadir}/kde/doc/HTML/en/knu

%{_datadir}/kde/icons/mini/knu.xpm
%{_datadir}/kde/icons/knu.xpm

#################################################
#             Korn - checking OK
#################################################

%files korn -f korn.lang
%defattr(644,root,root,755)

%config(missingok) /etc/X11/kde/applnk/Internet/KOrn.kdelnk

%attr(755,root,root) %{_bindir}/korn

%{_datadir}/kde/doc/HTML/en/korn

%{_datadir}/kde/icons/mini/korn.xpm
%{_datadir}/kde/icons/korn.xpm

#################################################
#             KPPP - checking OK
#################################################

%files kppp -f kppp.lang  -f kppplogview.lang
%defattr(644,root,root,755)

%config(missingok) /etc/X11/kde/applnk/Internet/Kppp.kdelnk
%config(missingok) /etc/X11/kde/applnk/Internet/kppplogview.kdelnk

%attr(755, root, root) %{_bindir}/kppplogview
%attr(2755,root, uucp) %{_bindir}/kppp

%{_datadir}/kde/apps/kppp

%{_datadir}/kde/doc/HTML/en/kppp

%{_datadir}/kde/icons/mini/kppp.xpm
%{_datadir}/kde/icons/kppp.xpm

#################################################
#             KRN - checking OK
#################################################

%files krn -f krn.lang
%defattr(644,root,root,755)

%config(missingok) /etc/X11/kde/applnk/Internet/Krn.kdelnk

%attr(755,root,root) %{_bindir}/krn
%attr(755,root,root) %{_bindir}/kdecode
%attr(755,root,root) %{_bindir}/newkrn

%{_datadir}/kde/apps/krn

%{_datadir}/kde/doc/HTML/en/krn

%{_datadir}/kde/icons/mini/krn.xpm
%{_datadir}/kde/icons/krn.xpm

#################################################
#             KSIRC - checking
#################################################

%files ksirc -f ksirc.lang -f pws.lang
%defattr(644,root,root,755)

%config(missingok) /etc/X11/kde/applnk/Internet/ksirc.kdelnk

%attr(755,root,root) %{_bindir}/ksirc
%attr(755,root,root) %{_bindir}/dsirc
%attr(755,root,root) %{_bindir}/ksticker
%attr(755,root,root) %{_bindir}/mathpod

/usr/X11R6/lib/ksirc

/usr/X11R6/lib/libpuke*
/usr/X11R6/lib/libkplunger*

%{_datadir}/kde/apps/ksirc

%{_datadir}/kde/doc/HTML/en/ksirc
%{_datadir}/kde/doc/HTML/en/pws

%{_datadir}/kde/icons/mini/pws.xpm
%{_datadir}/kde/icons/ksirc.gif
%{_datadir}/kde/icons/pws.xpm

#################################################
#             KTALKD - checking OK
#################################################

%files ktalkd -f ktalkd.lang -f kcmktalkd.lang
%defattr(644,root,root,755)

%config(missingok) /etc/X11/kde/ktalkdrc
%config(missingok) /etc/X11/kde/applnk/Settings/Network/kcmktalkd.kdelnk

%{_bindir}/kcmktalkd
%{_bindir}/kotalkd
%{_bindir}/ktalkd
%{_bindir}/ktalkdlg
%{_bindir}/mail.local

%{_datadir}/kde/doc/HTML/en/ktalkd
%lang(el) %{_datadir}/kde/doc/HTML/el/ktalkd
%lang(fr) %{_datadir}/kde/doc/HTML/fr/ktalkd
%lang(it) %{_datadir}/kde/doc/HTML/it/ktalkd

%{_datadir}/kde/sounds/ktalkd.wav
