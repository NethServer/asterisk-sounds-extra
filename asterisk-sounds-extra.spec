#Workaround for 64 bit CPUs
%define _lib lib

Summary: Extra Sounds for Asterisk, The Open Source PBX
Name: asterisk-sounds-extra
Version: 1.5
Release: 2%{dist}
License: GPL
Group: Utilities/System
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Source10: http://downloads.digium.com/pub/telephony/sounds/releases/asterisk-extra-sounds-en-ulaw-%{version}.tar.gz
Source11: http://downloads.digium.com/pub/telephony/sounds/releases/asterisk-extra-sounds-en-alaw-%{version}.tar.gz
Source12: http://downloads.digium.com/pub/telephony/sounds/releases/asterisk-extra-sounds-en-g722-%{version}.tar.gz
Source13: http://downloads.digium.com/pub/telephony/sounds/releases/asterisk-extra-sounds-en-sln16-%{version}.tar.gz
BuildArch: noarch
URL: http://www.asterisk.org

%description
Asterisk is an open source PBX and telephony development platform.  Asterisk
can both replace a conventional PBX and act as a platform for the
development of custom telephony applications for the delivery of dynamic
content over a telephone; similar to how one can deliver dynamic content
through a web browser using CGI and a web server.

Asterisk supports a variety of telephony hardware including BRI, PRI, POTS,
and IP telephony clients using the Inter-Asterisk eXchange (IAX) protocol (e.g.
gnophone or miniphone).  For more information and a current list of supported
hardware, see http://www.asterisk.org


%package en-ulaw
Summary: Asterisk extra sounds - en - ulaw.
Group: Utilities/System
Provides: %{name} = %{version}-%{release}
Requires(pre): %{_sbindir}/groupadd
Requires(pre): %{_sbindir}/useradd

%pre en-ulaw
%{_sbindir}/groupadd -r asterisk &>/dev/null || :
%{_sbindir}/useradd -r -s /bin/bash -d /home/asterisk -c 'Asterisk User' -g asterisk asterisk &>/dev/null || :

%package en-alaw
Summary: Asterisk extra sounds - en - alaw.
Group: Utilities/System
Provides: %{name} = %{version}-%{release}
Requires(pre): %{_sbindir}/groupadd
Requires(pre): %{_sbindir}/useradd

%pre en-alaw
%{_sbindir}/groupadd -r asterisk &>/dev/null || :
%{_sbindir}/useradd -r -s /bin/bash -d /home/asterisk -c 'Asterisk User' -g asterisk asterisk &>/dev/null || :

%package en-wideband
Summary: Asterisk extra sounds - en - g722
Group: Utilities/System
Provides: %{name} = %{version}-%{release}
Requires(pre): %{_sbindir}/groupadd
Requires(pre): %{_sbindir}/useradd

%pre en-wideband
%{_sbindir}/groupadd -r asterisk &>/dev/null || :
%{_sbindir}/useradd -r -s /bin/bash -d /home/asterisk -c 'Asterisk User' -g asterisk asterisk &>/dev/null || :

%description en-ulaw
This package contains Asterisk extra sounds - en - ulaw.

%description en-alaw
This package contains Asterisk extra sounds - en - alaw.

%description en-wideband
This package contains Asterisk extra sounds - en - g722.

%prep

%build

%install
mkdir -p $RPM_BUILD_ROOT/var/lib/asterisk/sounds/en/

tar xof %SOURCE10 -C $RPM_BUILD_ROOT/var/lib/asterisk/sounds/en/
touch $RPM_BUILD_ROOT/var/lib/asterisk/sounds/.asterisk-extra-sounds-en-ulaw-%{version}

tar xof %SOURCE11 -C $RPM_BUILD_ROOT/var/lib/asterisk/sounds/en/
touch $RPM_BUILD_ROOT/var/lib/asterisk/sounds/.asterisk-extra-sounds-en-alaw-%{version}

tar xof %SOURCE12 -C $RPM_BUILD_ROOT/var/lib/asterisk/sounds/en/
touch $RPM_BUILD_ROOT/var/lib/asterisk/sounds/.asterisk-extra-sounds-en-g722-%{version}

tar xof %SOURCE13 -C $RPM_BUILD_ROOT/var/lib/asterisk/sounds/en/
touch $RPM_BUILD_ROOT/var/lib/asterisk/sounds/.asterisk-extra-sounds-en-sln16-%{version}

%post

%clean
cd $RPM_BUILD_DIR
%{__rm} -rf %{name}-%{version}
%{__rm} -rf /var/log/%{name}-sources-%{version}-%{release}.make.err
%{__rm} -rf $RPM_BUILD_ROOT

%files en-ulaw
%defattr(-, root, root)
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/en/*.ulaw
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/en/*/*.ulaw
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/en/extra-sounds-en.txt
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/en/CHANGES-asterisk-extra-en-%{version}
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/en/CREDITS-asterisk-extra-en-%{version}
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/en/LICENSE-asterisk-extra-en-%{version}
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/.asterisk-extra-sounds-en-ulaw-%{version}

%files en-alaw
%defattr(-, root, root)
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/en/*.alaw
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/en/*/*.alaw
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/en/extra-sounds-en.txt
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/en/CHANGES-asterisk-extra-en-%{version}
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/en/CREDITS-asterisk-extra-en-%{version}
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/en/LICENSE-asterisk-extra-en-%{version}
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/.asterisk-extra-sounds-en-alaw-%{version}

%files en-wideband
%defattr(-, root, root)
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/en/*.g722
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/en/*/*.g722
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/en/*.sln16
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/en/*/*.sln16
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/en/extra-sounds-en.txt
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/en/CHANGES-asterisk-extra-en-%{version}
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/en/CREDITS-asterisk-extra-en-%{version}
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/en/LICENSE-asterisk-extra-en-%{version}
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/.asterisk-extra-sounds-en-g722-%{version}
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/.asterisk-extra-sounds-en-sln16-%{version}
