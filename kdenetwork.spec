%define	_Xdir		/usr/X11R6
%define _Xbin		%{_Xdir}/bin
%define _Xshare		%{_Xdir}/share
%define _Xlocale	%{_Xdir}/share/locale
%define _Xlib		%{_Xdir}/lib
%define _Xinclude	%{_Xdir}/include


Summary:     K Desktop Environment - network applications
Summary(pl): K Desktop Environment - aplikacje sieciowe
Name:        kdenetwork
Version:     1.1.1
Release:     2
Vendor:      The KDE Team
Source:      ftp://ftp.kde.org/pub/kde/stable/%{version}/distribution/tar/generic/source/%{name}-%{version}.tar.bz2
#Patch:       kmail.charset.patch
Group:       X11/KDE/Network
Group(pl):   X11/KDE
Copyright:   GPL
Requires:    qt >= 1.40, kdelibs = %{version}
BuildRoot:   /tmp/%{name}-%{version}-root

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
Summary:     KDE Archie clients
Summary(pl): Klient programu archie dla KDE
Group:       X11/KDE/Network
Group(pl):   X11/KDE/Sieci
Requires:    qt >= 1.40, kdelibs = %{version}

%description karchie
This is archie client for KDE.

%description -l pl karchie
Klient programu archie dla KDE.

%package kbiff
Summary:     KDE kbiff
Summary(pl): KDE kbiff
Group:       X11/KDE/Network
Group(pl):   X11/KDE/Sieci
Requires:    qt >= 1.40, kdelibs = %{version}

%description kbiff

%description -l pl kbiff

%package kfinger
Summary:     KDE finger client
Summary(pl): Klient programu 'finger' dla KDE
Group:       X11/KDE/Network
Group(pl):   X11/KDE/Sieci
Requires:    qt >= 1.40, kdelibs = %{version}

%description kfinger

%description -l pl kfinger

%package kmail
Summary:     KDE Mail client
Summary(pl): Program pocztowy KDE
Group:       X11/KDE/Network
Requires:    qt >= 1.40, kdelibs = %{version}

%description kmail
This is electronic mail client for KDE.
It is able to retrievie mail from POP3 accounts and from local mailboxes. 

This package contains version patched for better charset support.

%description -l pl kmail
Program pocztowy dla KDE.
Potrafi odczytywaæ pocztê z kont POP3 jak i lokalnych skrzynek.

Ten pakiet zawiera wersj± programu z poprawion± obs³ug± zestawów znaków.

%package knu
Summary:     KDE Network Utilities	
Summary(pl): Narzêdzia sieciowe KDE
Group:       X11/KDE/Network
Requires:    qt >= 1.40, kdelibs = %{version}, netkit-base

%description knu
Frontend to ping, host and traceroute utilities.

%description -l pl knu
Interfejs do narzêdzi: ping, host i traceroute.

%package korn 
Summary:     KDE 'biff' application
Summary(pl): Wska¼nik skrzynki pocztowej dla KDE
Group:       X11/KDE/Network
Requires:    qt >= 1.40, kdelibs = %{version}

%description korn
A simple program showing number of mails in your folders.

%description -l pl korn
Programik pokazuj±cy ilo¶æ wiadomo¶ci w wybranych folderach pocztowych.

%package kppp
Summary:     KDE PPP dialer	
Summary(pl): Program do po³±czeñ modemowych dla KDE
Group:       X11/KDE/Network
Requires:    qt >= 1.40, kdelibs = %{version}, ppp 

%description kppp
A PPPP dialer for KDE. It supports multiple accounts.

%description -l pl kppp
Program no nawi±zywania po³±czeñ modemowych pod KDE.
Posiada ³atwy interfejs i mo¿liwo¶æ zdefiniowania kilku kont.

%package krn
Summary:     KDE News Reader	
Summary(pl): Czytnik newsówd dla KDE
Group:       X11/KDE/Network
Requires:    qt >= 1.40, kdelibs = %{version}

%description krn
This is a news reader for KDE. It has threading and everything else
you need to be happy reading your news.

%description -l pl krn
Czytnik newsów dla KDE. Obs³uguje w±tki oraz killfile. 

%package ksirc
Summary:     KDE IRC client
Summary(pl): Klient IRC dla KDE
Group:       X11/KDE/Network
Group(pl):   X11/KDE/Sieci
Requires:    qt >= 1.40, kdelibs = %{version}

%description ksirc

%description -l pl ksirc

%package ktalkd
Summary:     KDE Mail client
Summary(pl): Program pocztowy KDE
Group:       X11/KDE/Network
Group(pl):   X11/KDE/Sieci
Requires:    qt >= 1.40, kdelibs = %{version}

%description ktalkd

%description -l pl ktalkd

%prep
%setup -q
#%patch -p1

%build
export KDEDIR=/usr/X11R6
# don't use -fno-exceptions - ksirc requires exceptions
CXXFLAGS="$RPM_OPT_FLAGS -Wall -fno-rtti" \
CFLAGS="$RPM_OPT_FLAGS -Wall" \
./configure %{_target} \
	--prefix=$KDEDIR \
 	--with-install-root=$RPM_BUILD_ROOT \
 	--with-pam="yes"
make KDEDIR=$KDEDIR

%install
rm -rf $RPM_BUILD_ROOT
export KDEDIR=/usr/X11R6
make RUN_KAPPFINDER=no prefix=$RPM_BUILD_ROOT$KDEDIR install

%find_lang karchie %{_builddir}/karchie.lang
%find_lang kbiff %{_builddir}/kbiff.lang
%find_lang kfinger %{_builddir}/kfinger.lang
%find_lang kmail %{_builddir}/kmail.lang
%find_lang knu %{_builddir}/knu.lang
%find_lang korn %{_builddir}/korn.lang
%find_lang kppp %{_builddir}/kppp.lang
%find_lang kppplogview %{_builddir}/kppplogview.lang
%find_lang krn %{_builddir}/krn.lang
%find_lang ksirc %{_builddir}/ksirc.lang
%find_lang pws %{_builddir}/pws.lang
%find_lang ktalkd %{_builddir}/ktalkd.lang
%find_lang kcmktalkd %{_builddir}/kcmktalkd/lang

%clean
rm -rf $RPM_BUILD_ROOT

#################################################
#             KARCHIE - checking OK
#################################################

%files karchie -f karchie.lang
%defattr(644, root, root, 755)

%config(missingok) /etc/X11/kde/karchierc
%config(missingok) /etc/X11/kde/applnk/Internet/karchie.kdelnk

%{_Xbin}/karchie

%lang(en) %{_Xshare}/kde/doc/HTML/en/karchie

%{_Xshare}/kde/icons/karchie.xpm
%{_Xshare}/kde/icons/mini/karchie.xpm

#################################################
#             KBIFF - checking OK
#################################################

%files kbiff -f kbiff.lang
%defattr(644, root, root, 755)

%config(missingok) /etc/X11/kde/applnk/Internet/kbiff.kdelnk

%{_Xbin}/kbiff

%{_Xshare}/kde/apps/kbiff

%lang(en) %{_Xshare}/kde/doc/HTML/en/kbiff

%{_Xshare}/kde/icons/kbiff.xpm
%{_Xshare}/kde/icons/mini/kbiff.xpm

#################################################
#             KFINGER - checking OK
#################################################

%files kfinger -f kfinger.lang
%defattr(644, root, root, 755)

%config(missingok) /etc/X11/kde/kfingerrc
%config(missingok) /etc/X11/kde/applnk/Internet/kfinger.kdelnk

%{_Xbin}/kfinger

%lang(en) %{_Xshare}/kde/doc/HTML/en/kfinger

%{_Xshare}/kde/toolbar

#################################################
#             KMAIL - checking OK
#################################################

%files kmail -f kmail.lang
%defattr(644, root, root, 755)

%config(missingok) /etc/X11/kde/applnk/Internet/KMail.kdelnk

%attr(755, root, root) /usr/X11R6/bin/kmail

%{_Xshare}/kde/apps/kmail

%lang(en) %{_Xshare}/kde/doc/HTML/en/kmail

%{_Xshare}/kde/icons/kmail.xpm
%{_Xshare}/kde/icons/mini/kmail.xpm

#################################################
#             KNU - checking OK
#################################################

%files knu -f knu
%defattr(644, root, root, 755)

%config(missingok) /etc/X11/kde/applnk/Internet/knu.kdelnk

%attr(755, root, root) /usr/X11R6/bin/knu

%lang(en) %{_Xshare}/kde/doc/HTML/en/knu

/usr/X11R6/share/kde/icons/mini/knu.xpm
/usr/X11R6/share/kde/icons/knu.xpm

#################################################
#             Korn - checking OK
#################################################

%files korn -f korn.lang
%defattr(644, root, root, 755)

%config(missingok) /etc/X11/kde/applnk/Internet/KOrn.kdelnk

%attr(755, root, root) /usr/X11R6/bin/korn

%lang(en) /usr/X11R6/share/kde/doc/HTML/en/korn

/usr/X11R6/share/kde/icons/mini/korn.xpm
/usr/X11R6/share/kde/icons/korn.xpm

#################################################
#             KPPP - checking OK
#################################################

%files kppp -f kppp  -f kppplogview
%defattr(644, root, root, 755)

%config(missingok) /etc/X11/kde/applnk/Internet/Kppp.kdelnk
%config(missingok) /etc/X11/kde/applnk/Internet/kppplogview.kdelnk

%attr(755, root, root) /usr/X11R6/bin/kppplogview
%attr(2755,root, uucp) /usr/X11R6/bin/kppp

/usr/X11R6/share/kde/apps/kppp

%lang(en) /usr/X11R6/share/kde/doc/HTML/en/kppp

/usr/X11R6/share/kde/icons/mini/kppp.xpm
/usr/X11R6/share/kde/icons/kppp.xpm

#################################################
#             KRN - checking OK
#################################################

%files krn -f krn.lang
%defattr(644, root, root, 755)

%config(missingok) /etc/X11/kde/applnk/Internet/Krn.kdelnk

%attr(755, root, root) /usr/X11R6/bin/krn
%attr(755, root, root) /usr/X11R6/bin/kdecode
%attr(755, root, root) /usr/X11R6/bin/newkrn

/usr/X11R6/share/kde/apps/krn

%lang(en) /usr/X11R6/share/kde/doc/HTML/en/krn

/usr/X11R6/share/kde/icons/mini/krn.xpm
/usr/X11R6/share/kde/icons/krn.xpm

#################################################
#             KSIRC - checking
#################################################

%files ksirc -f ksirc.lang -f pws.lang
%defattr(644, root, root, 755)

%config(missingok) /etc/X11/kde/applnk/Internet/ksirc.kdelnk
%config(missingok) /etc/X11/kde/applnk/Internet/pws.kdelnk

%attr(755, root, root) %{_Xbin}/ksirc
%attr(755, root, root) %{_Xbin}/dsirc
%attr(755, root, root) %{_Xbin}/ksticker
%attr(755, root, root) %{_Xbin}/mathpod

%{_Xlib}/ksirc

%attr(755, root, root) %{_Xlib}/libpuke*

%attr(755, root, root) %{_Xlib}/libkplunger*

%{_Xshare}/kde/apps/ksirc

%lang(en) %{_Xshare}/kde/doc/HTML/en/ksirc
%lang(en) %{_Xshare}/kde/doc/HTML/en/pws

%{_Xshare}/kde/icons/mini/pws.xpm
%{_Xshare}/kde/icons/ksirc.gif
%{_Xshare}/kde/icons/pws.xpm

#################################################
#             KTALKD - checking OK
#################################################

%files ktalkd -f ktalkd.lang -f kcmktalkd.lang
%defattr(644, root, root, 755)

%config(missingok) /etc/X11/kde/ktalkdrc
%config(missingok) /etc/X11/kde/applnk/Settings/Network/kcmktalkd.kdelnk

%{_Xbin}/kcmktalkd
%{_Xbin}/kotalkd
%{_Xbin}/ktalkd
%{_Xbin}/ktalkdlg
%{_Xbin}/mail.local

%lang(el) %{_Xshare}/kde/doc/HTML/el/ktalkd
%lang(en) %{_Xshare}/kde/doc/HTML/en/ktalkd
%lang(fr) %{_Xshare}/kde/doc/HTML/fr/ktalkd
%lang(it) %{_Xshare}/kde/doc/HTML/it/ktalkd

%{_Xshare}/kde/sounds/ktalkd.wav

%changelog
* Fri May 21 1999 Wojciech "Sas" Cieciwa <cieciwa@alpha.zarz.agh.edu.pl>
  [1.1.1-2]
- fixes problem with locale files uses '%find_lang' macro.

* Wed May 19 1999 Wojciech "Sas" Cieciwa <cieciwa@alpha.zarz.agh.edu.pl>
  [1.1.1-1]
- updated to version 1.1.1,
- removed wmconfig part from /etc/X11,

* Wed Dec  8 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.0-7]
- recompiled against libstdc++.so.2.9.

* Sun Oct 4 1998 Jacek Konieczny <jajcus@zeus.polsl.gliwice.pl>
  [1.0-4]
- created new spec based on kdebase.spec.
