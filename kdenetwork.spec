Summary:     K Desktop Environment - network applications
Summary(pl): K Desktop Environment - aplikacje sieciowe
Name:        kdenetwork
Version:     1.0
Release:     7
Vendor:      The KDE Team
Source:      ftp://ftp.kde.org/pub/kde/stable/%{version}/distribution/tar/generic/source/%{name}-%{version}.tar.gz
Patch:       kmail.charset.patch
Group:       X11/KDE/Network
Copyright:   GPL
Requires:    qt >= 1.40, kdelibs = %{version}
BuildRoot:   /tmp/%{name}-%{version}-root

%description
KDE network applications.
Package includes:
  KMail - e-mail client. Patched for proper charsets support
  KRN - news client
  KNU - network utilities (frontend to ping, host, traceroute)
  KORN - "biff" program
  KPPP - PPP dialer

%description -l pl
Aplikacje sieciowe KDE.
Pakiet zawiera:
  KMail - program pocztowy, z poprawion± obs³ug± zestawów znaków
  KRN - Program do czytania newsów
  KNU - Interfejs do ping'a, traceroute'a i host'a
  KORN - program pokazuj±cy stan skrzynek pocztowych
  KPPP - program do nawi±zywania po³±czeñ modemowych

%package -n kmail
Summary:     KDE Mail client
Summary(pl): Program pocztowy KDE
Group:       X11/KDE/Network
Requires:    qt >= 1.40, kdelibs = %{version}

%description -n kmail
This is electronic mail client for KDE.
It is able to retrievie mail from POP3 accounts and from local mailboxes. 

This package contains version patched for better charset support.

%description -l pl -n kmail
Program pocztowy dla KDE.
Potrafi odczytywaæ pocztê z kont POP3 jak i lokalnych skrzynek.

Ten pakiet zawiera wersj± programu z poprawion± obs³ug± zestawów znaków.

%package -n krn
Summary:     KDE News Reader	
Summary(pl): Czytnik newsówd dla KDE
Group:       X11/KDE/Network
Requires:    qt >= 1.40, kdelibs = %{version}

%description -n krn
This is a news reader for KDE. It has threading and everything else
you need to be happy reading your news.

%description -l pl -n krn
Czytnik newsów dla KDE. Obs³uguje w±tki oraz killfile. 

%package -n knu
Summary:     KDE Network Utilities	
Summary(pl): Narzêdzia sieciowe KDE
Group:       X11/KDE/Network
Requires:    qt >= 1.40, kdelibs = %{version}, netkit-base

%description -n knu
Frontend to ping, host and traceroute utilities.

%description -l pl -n knu
Interfejs do narzêdzi: ping, host i traceroute.

%package -n korn 
Summary:     KDE 'biff' application
Summary(pl): Wska¼nik skrzynki pocztowej dla KDE
Group:       X11/KDE/Network
Requires:    qt >= 1.40, kdelibs = %{version}

%description -n korn
A simple program showing number of mails in your folders.

%description -l pl -n korn
Programik pokazuj±cy ilo¶æ wiadomo¶ci w wybranych folderach pocztowych.

%package -n kppp
Summary:     KDE PPP dialer	
Summary(pl): Program do po³±czeñ modemowych dla KDE
Group:       X11/KDE/Network
Requires:    qt >= 1.40, kdelibs = %{version}, ppp 

%description -n kppp
A PPPP dialer for KDE. It supports multiple accounts.

%description -l pl -n kppp
Program no nawi±zywania po³±czeñ modemowych pod KDE.
Posiada ³atwy interfejs i mo¿liwo¶æ zdefiniowania kilku kont.

%prep
%setup -q
%patch -p1

%build
export KDEDIR=/usr/X11R6
CXXFLAGS="$RPM_OPT_FLAGS -Wall" CFLAGS="$RPM_OPT_FLAGS -Wall" \
./configure %{_target} \
	--prefix=$KDEDIR \
 	--with-install-root=$RPM_BUILD_ROOT \
 	--with-pam="yes"
make KDEDIR=$KDEDIR

%install
rm -rf $RPM_BUILD_ROOT
export KDEDIR=/usr/X11R6
make RUN_KAPPFINDER=no prefix=$RPM_BUILD_ROOT$KDEDIR install

# create wmconfig files
install -d $RPM_BUILD_ROOT/etc/X11/wmconfig
DIR=$PWD
cd $RPM_BUILD_ROOT/etc/X11/kde/applnk
for kdelnk in `find . -name "*.kdelnk"` ; do
  PKG=kde`basename $kdelnk|sed -e "s/\.kdelnk$//"`;
  SECT=`dirname $kdelnk|sed -e "s/^\.\/*//"`;
  kdelnk2wmconfig $PKG $kdelnk $RPM_BUILD_ROOT/etc/X11/wmconfig/$PKG KDE/$SECT pl
done
cd $DIR

%clean
rm -rf $RPM_BUILD_ROOT

#################################################
#             KMAIL
#################################################

%files -n kmail
%defattr(644, root, root, 755)
/usr/X11R6/share/kde/apps/kmail
/usr/X11R6/share/kde/icons/kmail.xpm
/usr/X11R6/share/kde/icons/mini/kmail.xpm
%config(missingok) /etc/X11/kde/applnk/Internet/KMail.kdelnk
%config(missingok) /etc/X11/wmconfig/kdeKMail
%lang(en) /usr/X11R6/share/kde/doc/HTML/en/kmail
%lang(cs) /usr/X11R6/share/locale/cs/LC_MESSAGES/kmail.mo
%lang(de) /usr/X11R6/share/locale/de/LC_MESSAGES/kmail.mo
%lang(el) /usr/X11R6/share/locale/el/LC_MESSAGES/kmail.mo
%lang(es) /usr/X11R6/share/locale/es/LC_MESSAGES/kmail.mo
%lang(fi) /usr/X11R6/share/locale/fi/LC_MESSAGES/kmail.mo
%lang(fr) /usr/X11R6/share/locale/fr/LC_MESSAGES/kmail.mo
%lang(hr) /usr/X11R6/share/locale/hr/LC_MESSAGES/kmail.mo
%lang(hu) /usr/X11R6/share/locale/hu/LC_MESSAGES/kmail.mo
%lang(it) /usr/X11R6/share/locale/it/LC_MESSAGES/kmail.mo
%lang(nl) /usr/X11R6/share/locale/nl/LC_MESSAGES/kmail.mo
%lang(no) /usr/X11R6/share/locale/no/LC_MESSAGES/kmail.mo
%lang(pl) /usr/X11R6/share/locale/pl/LC_MESSAGES/kmail.mo
%lang(pt) /usr/X11R6/share/locale/pt*/LC_MESSAGES/kmail.mo
%lang(ro) /usr/X11R6/share/locale/ro/LC_MESSAGES/kmail.mo
%lang(sk) /usr/X11R6/share/locale/sk/LC_MESSAGES/kmail.mo
%lang(zh) /usr/X11R6/share/locale/zh*/LC_MESSAGES/kmail.mo
%attr(755, root, root) /usr/X11R6/bin/kmail

#################################################
#             KRN
#################################################

%files -n krn
%defattr(644, root, root, 755)
/usr/X11R6/share/kde/apps/krn
/usr/X11R6/share/kde/icons/mini/krn.xpm
/usr/X11R6/share/kde/icons/krn.xpm
%config(missingok) /etc/X11/kde/applnk/Internet/Krn.kdelnk
%config(missingok) /etc/X11/wmconfig/kdeKrn
%lang(en) /usr/X11R6/share/kde/doc/HTML/en/krn
%lang(cs) /usr/X11R6/share/locale/cs/LC_MESSAGES/krn.mo
%lang(de) /usr/X11R6/share/locale/de/LC_MESSAGES/krn.mo
%lang(el) /usr/X11R6/share/locale/el/LC_MESSAGES/krn.mo
%lang(es) /usr/X11R6/share/locale/es/LC_MESSAGES/krn.mo
%lang(fi) /usr/X11R6/share/locale/fi/LC_MESSAGES/krn.mo
%lang(fr) /usr/X11R6/share/locale/fr/LC_MESSAGES/krn.mo
%lang(hr) /usr/X11R6/share/locale/hr/LC_MESSAGES/krn.mo
%lang(it) /usr/X11R6/share/locale/it/LC_MESSAGES/krn.mo
%lang(nl) /usr/X11R6/share/locale/nl/LC_MESSAGES/krn.mo
%lang(no) /usr/X11R6/share/locale/no/LC_MESSAGES/krn.mo
%lang(pl) /usr/X11R6/share/locale/pl/LC_MESSAGES/krn.mo
%lang(pt) /usr/X11R6/share/locale/pt*/LC_MESSAGES/krn.mo
%lang(ro) /usr/X11R6/share/locale/ro/LC_MESSAGES/krn.mo
%lang(sk) /usr/X11R6/share/locale/sk/LC_MESSAGES/krn.mo
%lang(zh) /usr/X11R6/share/locale/zh*/LC_MESSAGES/krn.mo
%attr(755, root, root) /usr/X11R6/bin/krn
%attr(755, root, root) /usr/X11R6/bin/kdecode

#################################################
#             KNU
#################################################

%files -n knu
%defattr(644, root, root, 755)
/usr/X11R6/share/kde/icons/mini/knu.xpm
/usr/X11R6/share/kde/icons/knu.xpm
%config(missingok) /etc/X11/kde/applnk/Internet/knu.kdelnk
%config(missingok) /etc/X11/wmconfig/kdeknu
%lang(en) /usr/X11R6/share/kde/doc/HTML/en/knu
%lang(cs) /usr/X11R6/share/locale/cs/LC_MESSAGES/knu.mo
%lang(de) /usr/X11R6/share/locale/de/LC_MESSAGES/knu.mo
%lang(el) /usr/X11R6/share/locale/el/LC_MESSAGES/knu.mo
%lang(es) /usr/X11R6/share/locale/es/LC_MESSAGES/knu.mo
%lang(fi) /usr/X11R6/share/locale/fi/LC_MESSAGES/knu.mo
%lang(fr) /usr/X11R6/share/locale/fr/LC_MESSAGES/knu.mo
%lang(hr) /usr/X11R6/share/locale/hr/LC_MESSAGES/knu.mo
%lang(hu) /usr/X11R6/share/locale/hu/LC_MESSAGES/knu.mo
%lang(it) /usr/X11R6/share/locale/it/LC_MESSAGES/knu.mo
%lang(nl) /usr/X11R6/share/locale/nl/LC_MESSAGES/knu.mo
%lang(no) /usr/X11R6/share/locale/no/LC_MESSAGES/knu.mo
%lang(pl) /usr/X11R6/share/locale/pl/LC_MESSAGES/knu.mo
%lang(pt) /usr/X11R6/share/locale/pt*/LC_MESSAGES/knu.mo
%lang(sk) /usr/X11R6/share/locale/sk/LC_MESSAGES/knu.mo
%lang(zh) /usr/X11R6/share/locale/zh*/LC_MESSAGES/knu.mo
%attr(755, root, root) /usr/X11R6/bin/knu

#################################################
#             Korn
#################################################

%files -n korn
%defattr(644, root, root, 755)
/usr/X11R6/share/kde/icons/mini/korn.xpm
/usr/X11R6/share/kde/icons/korn.xpm
%config(missingok) /etc/X11/kde/applnk/Internet/KOrn.kdelnk
%config(missingok) /etc/X11/wmconfig/kdeKOrn
%lang(en) /usr/X11R6/share/kde/doc/HTML/en/korn
%attr(755, root, root) /usr/X11R6/bin/korn

#################################################
#             KPPP
#################################################

%files -n kppp
%defattr(644, root, root, 755)
/usr/X11R6/share/kde/apps/kppp
/usr/X11R6/share/kde/icons/mini/kppp.xpm
/usr/X11R6/share/kde/icons/kppp.xpm
%config(missingok) /etc/X11/kde/applnk/Internet/Kppp.kdelnk
%config(missingok) /etc/X11/wmconfig/kdeKppp
%lang(en) /usr/X11R6/share/kde/doc/HTML/en/kppp
%lang(ca) /usr/X11R6/share/locale/ca/LC_MESSAGES/kppp.mo
%lang(cs) /usr/X11R6/share/locale/cs/LC_MESSAGES/kppp.mo
%lang(da) /usr/X11R6/share/locale/da/LC_MESSAGES/kppp.mo
%lang(de) /usr/X11R6/share/locale/de/LC_MESSAGES/kppp.mo
%lang(el) /usr/X11R6/share/locale/el/LC_MESSAGES/kppp.mo
%lang(es) /usr/X11R6/share/locale/es/LC_MESSAGES/kppp.mo
%lang(fi) /usr/X11R6/share/locale/fi/LC_MESSAGES/kppp.mo
%lang(fr) /usr/X11R6/share/locale/fr/LC_MESSAGES/kppp.mo
%lang(hr) /usr/X11R6/share/locale/hr/LC_MESSAGES/kppp.mo
%lang(it) /usr/X11R6/share/locale/it/LC_MESSAGES/kppp.mo
%lang(nl) /usr/X11R6/share/locale/nl/LC_MESSAGES/kppp.mo
%lang(no) /usr/X11R6/share/locale/no/LC_MESSAGES/kppp.mo
%lang(pl) /usr/X11R6/share/locale/pl/LC_MESSAGES/kppp.mo
%lang(pt) /usr/X11R6/share/locale/pt*/LC_MESSAGES/kppp.mo
%lang(ro) /usr/X11R6/share/locale/ro/LC_MESSAGES/kppp.mo
%lang(sk) /usr/X11R6/share/locale/sk/LC_MESSAGES/kppp.mo
%lang(zh) /usr/X11R6/share/locale/zh*/LC_MESSAGES/kppp.mo
%attr(755, root, root) /usr/X11R6/bin/kppplogview
%attr(2755,root, uucp) /usr/X11R6/bin/kppp

%changelog
* Wed Dec  8 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.0-7]
- recompiled against libstdc++.so.2.9.

* Sun Oct 4 1998 Jacek Konieczny <jajcus@zeus.polsl.gliwice.pl>
  [1.0-4]
- created new spec based on kdebase.spec.
