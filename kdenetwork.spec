%define		REV	20000418
Summary:	K Desktop Environment - network applications
Summary(pl):	K Desktop Environment - aplikacje sieciowe
Name:		kdenetwork
Version:	2.0
Release:	1.pre_%{REV}
Vendor:		The KDE Team
Source:		ftp://ftp.kde.org/pub/kde/snapshots/current/%{name}-%{REV}.tar.bz2
#Patch:		kmail.charset.patch
Group:		X11/KDE/Networking
Group(pl):	X11/KDE/Sieciowe
Copyright:	GPL
BuildRequires:	qt >= 2.1
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

%package libsearch
Summary:	KDE search library
Summary(pl):	xxx
Group:		X11/KDE/Networking
Group(pl):	X11/KDE/Sieciowe
Requires:	qt>= 2.1
Requires:	kdelibs = %{version}
%description libsearch
%description -l pl libsearch

%package caitoo
Summary:	KDE subpackage
Summary(pl):	Pakiet pomocniczy dla KDE 
Group:		X11/KDE/Networking
Group(pl):	X11/KDE/Sieciowe
Requires:	qt >= 2.1
Requires:	kdelibs = %{version}
%description caitoo
%description -l pl caitoo

%package karchie
Summary:     	KDE Archie clients
Summary(pl): 	Klient programu archie dla KDE
Group:       	X11/KDE/Networking
Group(pl):   	X11/KDE/Sieciowe
Requires:    	qt >= 2.1
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
Requires:    	qt >= 2.1
Requires:	kdelibs = %{version}

%description kbiff

%description -l pl kbiff

%package kfinger
Summary:     	KDE finger client
Summary(pl): 	Klient programu 'finger' dla KDE
Group:       	X11/KDE/Networking
Group(pl):   	X11/KDE/Sieciowe
Requires:    	qt >= 2.1
Requires:	kdelibs = %{version}

%description kfinger

%description -l pl kfinger

%package kmail
Summary:     	KDE Mail client
Summary(pl): 	Program pocztowy KDE
Group:       	X11/KDE/Networking
Requires:    	qt >= 2.1
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
Requires:    	qt >= 2.1
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
Requires:    	qt >= 2.1
Requires:	kdelibs = %{version}

%description korn
A simple program showing number of mails in your folders.

%description -l pl korn
Programik pokazuj±cy ilo¶æ wiadomo¶ci w wybranych folderach pocztowych.

%package kppp
Summary:     	KDE PPP dialer	
Summary(pl): 	Program do po³±czeñ modemowych dla KDE
Group:       	X11/KDE/Networking
Requires:    	qt >= 2.1
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
Requires:    	qt >= 2.1
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
Requires:    	qt >= 2.1
Requires:	kdelibs = %{version}

%description ksirc

%description -l pl ksirc

%package ktalkd
Summary:     	KDE Mail client
Summary(pl): 	Program pocztowy KDE
Group:       	X11/KDE/Networking
Group(pl):   	X11/KDE/Sieciowe
Requires:    	qt >= 2.1
Requires:	kdelibs = %{version}

%description ktalkd

%description -l pl ktalkd

%prep
%setup -q -n %{name}
#%patch -p1

%build
KDEDIR=%{_prefix}
CXXFLAGS="$RPM_OPT_FLAGS -Wall"
CFLAGS="$RPM_OPT_FLAGS -Wall"
LDFLAGS="-s"
export KDEDIR CXXFLAGS CFLAGS LDFLAGS
%configure \
	--prefix=$KDEDIR \
	--with-qt-dir=%{_prefix} \
 	--with-install-root=$RPM_BUILD_ROOT \
 	--with-pam="yes"
%{__make} KDEDIR=$KDEDIR

%install
rm -rf $RPM_BUILD_ROOT
export KDEDIR=%{_prefix}
%{__make} RUN_KAPPFINDER=no prefix=$RPM_BUILD_ROOT$KDEDIR install

%find_lang caitoo
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

%post libsearch
/sbin/ldconfig

%postun libsearch
/sbin/ldconfig

%post ksirc
/sbin/ldconfig

%postun ksirc
/sbin/ldconfig
#################################################
#             CAITOO
#################################################
%files caitoo -f caitoo.lang
%defattr(644,root,root,755)

%config(missingok) %{_applnkdir}/Internet/caitoo.desktop

%attr(755,root,root) %{_bindir}/caitoo

%attr(644,root,root) %{_includedir}/caitoo*.h

%{_datadir}/apps/caitoo

%{_datadir}/icons/locolor/*x*/apps/caitoo.png

#################################################
#             KARCHIE - checking OK
#################################################

%files karchie -f karchie.lang
%defattr(644,root,root,755)

%config(missingok) %{_datadir}/config//karchierc
%config(missingok) {_applnkdir}/Internet/karchie.kdelnk

%attr(755,root,root) %{_bindir}/karchie

%{_datadir}/icons/locolor/*x*/apps/karchie.png
%{_datadir}/icons/hicolor/*x*/apps/karchie.png

#################################################
#             KBIFF - checking OK
#################################################

%files kbiff -f kbiff.lang
%defattr(644,root,root,755)

%config(missingok) %{_applnkdir}/Internet/kbiff.kdelnk

%attr(755,root,root) %{_bindir}/kbiff

%{_datadir}/apps/kbiff

%{_datadir}/icons/locolor/*x*/apps/kbiff.png
%{_datadir}/icons/hicolor/*x*/apps/kbiff.png

#################################################
#             KFINGER - checking OK
#################################################

%files kfinger -f kfinger.lang
%defattr(644,root,root,755)

%config(missingok) %{_datadir}/config/kfingerrc
%config(missingok) %{_applnkdir}/Internet/kfinger.kdelnk

%attr(755,root,root) %{_bindir}/kfinger

%{_datadir}/toolbar

#################################################
#             KMAIL - checking OK
#################################################

%files kmail -f kmail.lang
%defattr(644,root,root,755)

%config(missingok) %{_applnkdir}/Internet/KMail.kdelnk

%attr(755,root,root) %{_bindir}/kmail

%attr(644,root,root) %{_includedir}/kmail*.h

%{_datadir}/apps/kmail

%{_datadir}/icons/locolor/*x*/apps/kmail.png
%{_datadir}/icons/hicolor/*x*/apps/kmail.png

#################################################
#             KNU - checking OK
#################################################

%files knu -f knu.lang
%defattr(644,root,root,755)

%config(missingok) %{_applnkdir}/Internet/knu.kdelnk

%attr(755,root,root) %{_bindir}/knu

%{_datadir}/icons/locolor/*x*/apps/knu.png

#################################################
#             Korn - checking OK
#################################################

%files korn -f korn.lang
%defattr(644,root,root,755)

%config(missingok) %{_applnkdir}/Internet/KOrn.kdelnk

%attr(755,root,root) %{_bindir}/korn

%{_datadir}/icons/locolor/*x*/apps/korn.png
%{_datadir}/icons/hicolor/*x*/apps/korn.png

#################################################
#             KPPP - checking OK
#################################################

%files kppp -f kppp.lang  -f kppplogview.lang
%defattr(644,root,root,755)

%config(missingok) %{_applnkdir}/Internet/Kppp.kdelnk
%config(missingok) %{_applnkdir}/Internet/kppplogview.kdelnk

%attr(755, root, root) %{_bindir}/kppplogview
%attr(2755,root, uucp) %{_bindir}/kppp

%{_datadir}/apps/kppp

%{_datadir}/icons/locolor/*x*/apps/kppp.png
%{_datadir}/icons/hicolor/*x*/apps/kppp.png

#################################################
#             KRN - checking OK
#################################################

%files krn -f krn.lang
%defattr(644,root,root,755)

%config(missingok) %{_applnkdir}/Internet/Krn.kdelnk

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

%config(missingok) %{_applnkdir}/Internet/ksirc.kdelnk

%attr(755,root,root) %{_bindir}/ksirc
%attr(755,root,root) %{_bindir}/dsirc
%attr(755,root,root) %{_bindir}/ksticker
%attr(755,root,root) %{_bindir}/mathpod

%{_libdir}/ksirc

%attr(644,root,root) %{_libdir}/libplunger.a
%attr(755,root,root) %{_libdir}/libpuke.la
%attr(755,root,root) %{_libdir}/libpuke.so.*.*.*

%{_datadir}/apps/ksirc

%{_datadir}/icons/locolor/*x*/apps/ksirc.png
%{_datadir}/icons/locolor/*x*/apps/pws.png
%{_datadir}/icons/hicolor/*x*/apps/ksirc.png

#################################################
#             KTALKD - checking OK
#################################################

%files ktalkd -f ktalkd.lang -f kcmktalkd.lang
%defattr(644,root,root,755)

%config(missingok) %{_datadir}/config/ktalkdrc
%config(missingok) %{_applnkdir}/Settings/Network/kcmktalkd.kdelnk

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

#################################################
#             LIBSEARCH
#################################################
%files libsearch
%defattr(644,root,root,755)

%attr(644,root,root) %{_includedir}/ftpsearch.h
%attr(644,root,root) %{_includedir}/kping.h
%attr(644,root,root) %{_includedir}/newssearch.h
%attr(644,root,root) %{_includedir}/websearch.h

%attr(755,root,root) %{_libdir}/libsearch.la
%attr(755,root,root) %{_libdir}/libsearch.so.*.*.*

%{_datadir}/apps/libsearch
