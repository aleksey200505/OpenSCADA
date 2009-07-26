#===== Generic Info ======
%define srcname openscada-%version
# bcond_with "--disable compiling"
# bcond_without "--enable compiling"
# ======== DAQ =========
%bcond_with diamondboards
%bcond_without dcon
%bcond_without modbus
%bcond_without soundcard
%bcond_without snmp
%bcond_without siemens
%bcond_without system
%bcond_without blockcalc
%bcond_without javalikecalc
%bcond_without logiclevel
%bcond_without daqgate
# ======== Protocol ========
%bcond_without selfsystem
# ========= DATA BASES =====
%bcond_with firebird
%bcond_without mysql
%bcond_without dbf
%bcond_without sqlite
# =========== ARH ===========
%bcond_without dbarch
%bcond_without fsarch
# ========== Web Interfaces ======
%bcond_without webcfg
%bcond_without webcfgd
%bcond_without webvision
# ========== HTTP Protocol =========
%bcond_without http
# ========== QT Interfaces ==========
# QT4 devel old in to CentOs
%if 0%{?rhel}
%bcond_with qtstarter
%bcond_with qtcfg
%bcond_with qtvision
%else
%bcond_without qtstarter
%bcond_without qtcfg
%bcond_without qtvision
%define _desktopdir %_datadir/applications
%define _iconsdir /usr/share/icons
%endif
# ========== Transports ==========
%bcond_without ssl
%bcond_without sockets
%bcond_without serial
# ========== Special ===========
%bcond_without flibcomplex
%bcond_without flibmath
%bcond_without flibsys
%bcond_without systemtests

# DIAMONDBOARDS - Only for x86_32
%ifarch x86_64
%if 0%{?with_diamondboards}
%{error: DIAMONDBOARDS support available only for %{ix86} target}
%endif
%endif

Summary: Open SCADA system project
Name: openscada
Version: 0.6.3.3
Release: 10%{?dist}
Source0: ftp://oscada.org.ua/OpenSCADA/0.6.3/openscada-%version.tar.gz
# Init scripts for fedora
Patch0: oscada.init.patch
License: GPLv2
Group: Applications/Engineering
URL: http://oscada.org.ua
BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
# has some x86-assembly includes
ExclusiveArch:  %{ix86} x86_64

BuildRequires: gettext
BuildRequires: gd-devel
BuildRequires: expat-devel
BuildRequires: sqlite-devel
BuildRequires: byacc
BuildRequires: bison
BuildRequires: portaudio-devel
%if 0%{?rhel}
BuildRequires: qt4-devel
%else
BuildRequires: qt-devel
%endif
BuildRequires: lm_sensors-devel
BuildRequires: openssl-devel
BuildRequires: fftw-devel
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtool
BuildRequires: desktop-file-utils
BuildRequires: sed
BuildRequires: chrpath

Requires(post): chkconfig
Requires(preun): chkconfig
Requires(preun): initscripts

%description
Open SCADA system. For access use account "root" and password "openscada".
%description -l ru_RU.UTF8
B:@KB0O SCADA A8AB5<0. ;O 4>ABC?0 8A?>;L7C9B5 70?8AL "root" 8 ?0@>;L
"openscada".
%description -l uk_UA.UTF8
V4:@8B0 SCADA A8AB5<0. ;O 4>ABC?C 28:>@8AB>2C9B5 70?8A "root" B0 ?0@>;L
"openscada".
%description -l de_DE.UTF8
Das offene SCADA System. Fuer den Zugang die Aufzeichnung "root" und das
Kennwort "openscada" benutzen.

%post
/sbin/ldconfig
/sbin/chkconfig --add openscadad

%postun -p /sbin/ldconfig

%preun
if [ $1 = 0 ]; then
 /sbin/service openscadad stop > /dev/null 2>&1
 /sbin/chkconfig --del openscadad
fi

%if 0%{?with_diamondboards}
%package DAQ-DiamondBoards
Summary: Open SCADA DAQ
Group: Applications/Engineering
Requires: %{name} = %{version}-%{release}
%description DAQ-DiamondBoards
The %name-DAQ-DiamondBoards allows access to Diamond systems DA boards.
Includes support of Athena board.
%description DAQ-DiamondBoards -l ru_RU.UTF8
0:5B %name-DAQ-DiamondBoards ?@54>AB02;O5B 4>ABC? : ?;0B0< A1>@0
40==KE D8@<K Diamond systems. :;NG05B ?>445@6:C A8AB5<=>9 ?;0BK
Athena.
%description DAQ-DiamondBoards -l uk_UA.UTF8
0:5B %name-DAQ-DiamondBoards =040T 4>ABC? 4> ?;0B 71>@C 40=8E DV@<8
Diamond systems. :;NG0T ?V4B@8<:C A8AB5<=>W ?;0B8 Athena.
%description DAQ-DiamondBoards -l de_DE.UTF8
Das Paket %name-DAQ-DiamondBoards ermoeglicht den Zugang zur
Datenerfassung der Firma Diamond systems.Es enthaelt die Unterstuetzung
der Systemplatte Athena.
%endif

%if 0%{?with_dcon}
%package DAQ-DCON
Summary: Open SCADA DAQ
Group: Applications/Engineering
Requires: %{name} = %{version}-%{release}
%description DAQ-DCON
The %name-DAQ-DCON allows realisation of DCON client service.
Supported I-7000 DCON protocol.
%description DAQ-DCON -l ru_RU.UTF8
0:5B %name-DAQ-DCON ?@54>AB02;O5B @50;870F8N :;85=BA:>3> A5@28A0
?@>B>:>;0 DCON. >445@68205BAO ?@>B>:>; I-7000 DCON.
%description DAQ-DCON -l uk_UA.UTF8
0:5B %name-DAQ-DCON =040T @50;V70FVN :;VT=BAL:>3> A5@2VAC DCON.
V4B@8<CTBLAO I-7000 DCON ?@>B>:>;.
%description DAQ-DCON -l de_DE.UTF8
Das Paket %name-DAQ-DCON ermoeglicht Verwirklichung des
Kundenservices des DCON-Protoklls. Unterstueuzung Prototkoll
I-7000 DCON.
%endif

%if 0%{?with_modbus}
%package DAQ-ModBus
Summary: Open SCADA DAQ
Group: Applications/Engineering
Requires: %{name} = %{version}-%{release}
%description DAQ-ModBus
The %name-DAQ-ModBus allows realisation of ModBus client service.
Supported Modbus/TCP, Modbus/RTU and Modbus/ASCII protocols.
%description DAQ-ModBus -l ru_RU.UTF8
0:5B %name-DAQ-ModBus ?@54>AB02;O5B @50;870F8N :;85=BA:>3> A5@28A0
?@>B>:>;0 ModBus. >445@6820NBAO Modbus/TCP, Modbus/RTU 8
Modbus/ASCII ?@>B>:>;K.
%description DAQ-ModBus -l uk_UA.UTF8
0:5B %name-DAQ-ModBus =040T @50;V70FVN :;VT=BAL:>3> ModBus A5@2VAC.
V4B@8<CNBLAO Modbus/TCP, Modbus/RTU B0 Modbus/ASCII ?@>B>:>;8.
%description DAQ-ModBus -l de_DE.UTF8
Das Paket %name-DAQ-ModBus emoeglicht Realisierung des Kundenservices des
ModBus - Protokolls. Unterstuetzt werden die Protokolle Modbus/TCP,
Modbus/RTU 8 Modbus/ASCII.
%endif

%if 0%{?with_soundcard}
%package DAQ-Soundcard
Summary: Open SCADA DAQ
Group: Applications/Engineering
Requires: %{name} = %{version}-%{release}
%description DAQ-Soundcard
The %name-DAQ-Soundcard allows access to sound card data.
%description DAQ-Soundcard -l ru_RU.UTF8
0:5B %name-DAQ-Soundcard ?@54>AB02;O5B 4>ABC? : 72C:>2>9 :0@B5.
%description DAQ-Soundcard -l uk_UA.UTF8
0:5B %name-DAQ-Soundcard =040T 4>ABC? 4> 40=8E 72C:>2>W :0@B8.
%description DAQ-Soundcard -l de_DE.UTF8
Das Paket %name-DAQ-Soundcard ermoeglicht den Zugang zur Schallkarte.
%endif

%if 0%{?with_snmp}
%package DAQ-SNMP
Summary: Open SCADA DAQ
Group: Applications/Engineering
BuildRequires: net-snmp-devel
Requires: %{name} = %{version}-%{release}
%description DAQ-SNMP
The %name-DAQ-SNMP allows realising of SNMP client service.
%description DAQ-SNMP -l ru_RU.UTF8
0:5B %name-DAQ-SNMP ?@54>AB02;O5B @50;870F8N :;85=BA:>3>
A5@28A0 ?@>B>:>;0 SNMP.
%description DAQ-SNMP -l uk_UA.UTF8
0:5B %name-DAQ-SNMP =040T @50;V70FVN :;VT=BAL:>3> SNMP A5@2VAC.
%description DAQ-SNMP -l de_DE.UTF8
Das Paket %name-DAQ-SNMP ermoeglicht Realisierung des Kundenservices
des SNMP - Protokolls.
%endif

%if 0%{?with_siemens}
%package DAQ-Siemens
Summary: Open SCADA DAQ
Group: Applications/Engineering
Requires: %{name} = %{version}-%{release}
%description DAQ-Siemens
The %name-DAQ-Siemens, allows data source Siemens PLC by CP of
Hilscher CIF cards using MPI protocol and library Libnodave
for other.
%description DAQ-Siemens -l ru_RU.UTF8
0:5B %name-DAQ-Siemens, ?@54>AB02;O5B 8AB>G=8: 40==KE  Siemens
?>A@54AB2>< :0@B Hilscher CIF A 8A?>;L7>20=85< ?@>B>:>;0 MPI 8
181;8>B5:8 Libnodave 4;O >AB0;L=>3>.
%description DAQ-Siemens -l uk_UA.UTF8
0:5B %name-DAQ-Siemens, =040T 465@5;> 40=8E  Siemens 70
4>?><>3>N :0@B Hilscher CIF 7 28:>@8AB0==O< ?@>B>:>;C MPI B0
1V1;V>B5:8 Libnodave 4;O V=H>3>.
%description DAQ-Siemens -l de_DE.UTF8
Das Paket %name-DAQ-Siemens, enthaelt die Datenquelle PLC Siemens
mittels der Karten Hilscher CIF durch Anwendung des MPI -
Protokolls und der Bibliothek Libnodave fuer Anderes.
%endif

%if 0%{?with_system}
%package DAQ-System
Summary: Open SCADA DAQ
Group: Applications/Engineering
Requires: %{name} = %{version}-%{release}
%description DAQ-System
The %name-DAQ-System, allow operation system data acquisition.
Support OS Linux data sources: HDDTemp, Sensors, Uptime, Memory, CPU and
other.
%description DAQ-System -l ru_RU.UTF8
0:5B %name-DAQ-System, ?@54>AB02;O5B A1>@ 40==KE >?5@0F8>==>9
A8AB5<K. >445@6820NBAO 8AB>G=8:8 40==KE ! Linux: HDDTemp, Sensors,
Uptime, Memory, CPU 8 4@C385.
%description DAQ-System -l uk_UA.UTF8
0:5B %name-DAQ-System, 040T 71V@ 40=8E >?5@0FV9=>W A8AB5<8.
V4B@8<CNBLAO 465@5;0 40=8E ! Linux: HDDTemp, Sensors, Uptime, Memory,
CPU B0 V=H5.
%description DAQ-System -l de_DE.UTF8
Das Paket %name-DAQ-System ermoeglicht Datenerfassung des
Operationssystems. Es werden die Datenquellen ! Linux: HDDTemp,
Sensors, Uptime, Memory, CPU und andere unterstuetzt.
%endif

%if 0%{?with_blockcalc}
%package DAQ-BlockCalc
Summary: Open SCADA DAQ
Group: Applications/Engineering
Requires: %{name} = %{version}-%{release}
%description DAQ-BlockCalc
The %name-DAQ-BlockCalc allows block based calculator.
%description DAQ-BlockCalc -l ru_RU.UTF8
0:5B %name-DAQ-BlockCalc, ?@54>AB02;O5B 1;>G=K9 2KG8A;8B5;L.
%description DAQ-BlockCalc -l uk_UA.UTF8
0:5B %name-DAQ-BlockCalc, =040T 1;>:>289 >1G8A;N20G.
%description DAQ-BlockCalc -l de_DE.UTF8
Das Paket %name-DAQ-BlockCalc gewaehrt den Blockrechner
%endif

%if 0%{?with_javalikecalc}
%package DAQ-JavaLikeCalc
Summary: Open SCADA DAQ
Group: Applications/Engineering
Requires: %{name} = %{version}-%{release}
%description DAQ-JavaLikeCalc
The %name-DAQ-JavaLikeCalc allows java-like based calculator and
function's libraries engine. User can create and modify function and
libraries.
%description DAQ-JavaLikeCalc -l ru_RU.UTF8
0:5B %name-DAQ-JavaLikeCalc, ?@54>AB02;O5B >A=>20==K5 =0 java ?>4>1=><
O7K:5 2KG8A;8B5;L 8 4286>: 181;8>B5:. >;L7>20B5;L <>65B A>74020BL 8
<>48D8F8@>20BL DC=:F88 8 181;8>B5:8.
%description DAQ-JavaLikeCalc -l uk_UA.UTF8
0:5B %name-DAQ-JavaLikeCalc, =040T 107>20=V =0 <>2V AE>6V9 =0 Java
>1G8A;N20G B0 4286>: 1V1;V>B5: DC=:FW. >@8ABC20G <>65 AB2>@N20B8 B0
<>48DV:C20B8 DC=:FVW B0 1V1;V>B5:8.
%description DAQ-JavaLikeCalc -l de_DE.UTF8
Das %name-DAQ-JavaLikeCalc, entaelt die auf java - aehnlicher Sprache
begruendeten Bibliothekenrechner und -laufer. Der Nutzer kann Funktionen
und Bibliotheken schaffen und modifizieren.
%endif

%if 0%{?with_logiclevel}
%package DAQ-LogicLevel
Summary: Open SCADA DAQ
Group: Applications/Engineering
Requires: %{name} = %{version}-%{release}
%description DAQ-LogicLevel
The %name-DAQ-LogicLevel allows logic level paramers.
%description DAQ-LogicLevel -l ru_RU.UTF8
0:5B %name-DAQ-LogicLevel, ?@54>AB02;O5B ;>38G5A:89 C@>25=L ?0@0<5B@>2.
%description DAQ-LogicLevel -l uk_UA.UTF8
0:5B %name-DAQ-LogicLevel, =040T ;>3VG=89 @V25=L ?0@0<5B@V2.
%description DAQ-LogicLevel -l de_DE.UTF8
Das Paket %name-DAQ-LogicLevel, enthaelt das logische Parameterlevel.
%endif

%if 0%{?with_daqgate}
%package DAQ-Gate
Summary: Open SCADA DAQ
Group: Applications/Engineering
Requires: %{name} = %{version}-%{release}
%description DAQ-Gate
The %name-DAQ-Gate, Allow to make gate data sources of remote
OpenSCADA station to local OpenSCADA station.
%description DAQ-Gate -l ru_RU.UTF8
0:5B %name-DAQ-Gate, ?>72>;O5B 2K?>;=OBL H;N7>20=85 8AB>G=8:>2
40==KE C40;Q==KE OpenSCADA AB0=F89 2 ;>:0;L=K5.
%description DAQ-Gate -l uk_UA.UTF8
0:5B %name-DAQ-Gate, 4>72>;OT H;N7C20B8 465@5;0 40=8E 2V440;5=8E
OpenSCADA AB0=FV9 4> ;>:0;L=8E.
%description DAQ-Gate -l de_DE.UTF8
Das Paket %name-DAQ-Gate, ermoeglicht das Einschleusen der Datenquellen der
entfernten OpenSCADA Stationen in die lokale.
%endif

%if 0%{?with_selfsystem}
%package Protocol-SelfSystem
Summary: Open SCADA Protocol
Group: Applications/Engineering
Requires: %{name} = %{version}-%{release}
%description Protocol-SelfSystem
The %name-Protocol-SelfSystem self OpenSCADA protocol, support
generic functions.
%description Protocol-SelfSystem -l ru_RU.UTF8
0:5B %name-Protocol-SelfSystem, c>1AB25==K9 ?@>B>:>; OpenSCADA,
?>445@68205B >A=>2=K5 DC=:F88.
%description Protocol-SelfSystem -l uk_UA.UTF8
0:5B %name-Protocol-SelfSystem, 2;0A=89 ?@>B>:>; OpenSCADA,
?V4B@8<CT >A=>2=V DC=:FVW.
%description Protocol-SelfSystem -l de_DE.UTF8
Das Paket %name-Protocol-SelfSystem, das eigene OpenSCADA -
Protokoll, unterstuetzt Hauptfunktionen
%endif

%if 0%{?with_firebird}
%package DB-FireBird
Summary: Open SCADA database
Group: Applications/Engineering
BuildRequires: firebird-devel
Requires: %{name} = %{version}-%{release}
%description DB-FireBird
The %name-DB-FireBird allow support of the DB FireBird.
%description DB-FireBird -l ru_RU.UTF8
0:5B %name-DB-FireBird, ?@54>AB02;O5B ?>445@6:C  FireBird.
%description DB-FireBird -l uk_UA.UTF8
0:5B %name-DB-FireBird, <>4C;L . 040T ?V4B@8<:C  FireBird.
%description DB-FireBird -l de_DE.UTF8
Das Paket %name-DB-FireBird Ermoegliht die FireBird Dateibasenunterstuetzung.
%endif

%if 0%{?with_mysql}
%package DB-MySQL
Summary: Open SCADA database
Group: Applications/Engineering
BuildRequires: mysql-devel
Requires: %{name} = %{version}-%{release}
%description DB-MySQL
The %name-DB-MySQL package allow support of the BD MySQL
%description DB-MySQL -l ru_RU.UTF8
0:5B %name-DB-MySQL, ?@54>AB02;O5B ?>445@6:C  MySQL.
%description DB-MySQL -l uk_UA.UTF8
0:5B %name-DB-MySQL, 040T ?V4B@8<:C  MySQL.
%description DB-MySQL -l de_DE.UTF8
Das Paket %name-DB-MySQL Ermoeglicht die MySQL-Dateibasenunterstuetzung.
%endif

%if 0%{?with_dbf}
%package DB-DBF
Summary: Open SCADA database
Group: Applications/Engineering
Requires: %{name} = %{version}-%{release}
%description DB-DBF
The %name-DB-DBF package allow support of the *.dbf files, version 3.0.
%description DB-DBF -l ru_RU.UTF8
0:5B %name-DB-DBF, ?@54>AB02;O5B ?>445@6:C *.dbf D09;>2, 25@A88 3.0..
%description DB-DBF -l uk_UA.UTF8
0:5B %name-DB-DBF, =040T ?V4B@8<:C *.dbf D09;V2, 25@AVW 3.0.
%description DB-DBF -l de_DE.UTF8
Das Paket %name-DB-DBF ermoeglicht die *.dbf Dateiunterstutzung, Versionen 3.0..
%endif

%if 0%{?with_sqlite}
%package DB-SQLite
Summary: Open SCADA bases
Group: Applications/Engineering
Requires: %{name} = %{version}-%{release}
%description DB-SQLite
The %name-DB-SQLite package allow support of the BD SQLite.
%description DB-SQLite -l ru_RU.UTF8
0:5B %name-DB-SQLite, ?@54>AB02;O5B ?>445@6:C  SQLite.
%description DB-SQLite -l uk_UA.UTF8
0:5B %name-DB-SQLite, =040T ?V4B@8<:C  SQLite.
%description DB-SQLite -l de_DE.UTF8
Das Paket %name-DB-SQLite ermoeglicht die DB SQLite - Unterstuetzung.
%endif

%if 0%{?with_dbarch}
%package ARH-DBArch
Summary: Open SCADA arch
Group: Applications/Engineering
Requires: %{name} = %{version}-%{release}
%description ARH-DBArch
The %name-ARH-DBArch package allow functions for messages and values
arhiving to DB.
%description ARH-DBArch -l ru_RU.UTF8
0:5B %name-ARH-DBArch, ?@54>AB02;O5B DC=:F88 0@E828@>20=8O A>>1I5=89 8
7=0G5=89 =0 .
%description ARH-DBArch -l uk_UA.UTF8
0:5B %name-ARH-DBArch, =040T DC=:FVW 0@EV20FVW ?>2V4><;5=L B0 7=0G5=L =0 .
%description ARH-DBArch -l de_DE.UTF8
Das Paket %name-ARH-DBArch gewaehrt Archivierungsfunktionen der Mitteilungen
und Bedeutungen fuer DB.
%endif

%if 0%{?with_fsarch}
%package ARH-FSArch
Summary: Open SCADA arch
Group: Applications/Engineering
Requires: %{name} = %{version}-%{release}
%description ARH-FSArch
The %name-ARH-FSArch allow functions for messages and values arhiving
to file system.
%description ARH-FSArch -l ru_RU.UTF8
0:5B %name-ARH-FSArch, ?@54>AB02;O5B DC=:F88 0@E828@>20=8O A>>1I5=89 8
7=0G5=89 =0 D09;>2CN A8AB5<C.
%description ARH-FSArch -l uk_UA.UTF8
0:5B %name-ARH-FSArch, =040T DC=:FVW 0@EV20FVW ?>2V4><;5=L B0 7=0G5=L =0
D09;>2C A8AB5<C.
%description ARH-FSArch -l de_DE.UTF8
Das Paket %name-ARH-FSArch gewaert Archivierungsfunktionen fuer Mitteilungen
und Bedeutungen fuer Dateisystem.
%endif

%if 0%{?with_webcfg}
%package UI-WebCfg
Summary: Open SCADA interfaces
Group: Applications/Engineering
Requires: %{name} = %{version}-%{release}
%description UI-WebCfg
The %name-UI-WebCfg allows the WEB based OpenSCADA system
configurator.
%description UI-WebCfg -l ru_RU.UTF8
0:5B %name-UI-WebCfg, ?@54>AB02;O5B WEB >A=>20==K9 :>=D83C@0B>@
A8AB5<K OpenSCADA.
%description UI-WebCfg -l uk_UA.UTF8
0:5B %name-UI-WebCfg, =040T WEB 107>20=89 :>=DV3C@0B>@ A8AB5<8
OpenSCADA.
%description UI-WebCfg -l de_DE.UTF8
Das Paket %name-UI-WebCfg ermoeglicht den WEB-begruendeten
OpenSCADA-Konfigurator.
%endif

%if 0%{?with_webcfgd}
%package UI-WebCfgd
Summary: Open SCADA interfaces
Group: Applications/Engineering
Requires: %{name} = %{version}-%{release}
%description UI-WebCfgd
The %name-UI-WebCfgd allows the dynamic WEB based OpenSCADA system
configurator. Use XHTML, CSS and JavaScript technologies.
%description UI-WebCfgd -l ru_RU.UTF8
0:5B %name-UI-WebCfgd, ?@54>AB02;O5B 48=0<8G5A:89 WEB >A=>20==K9
:>=D83C@0B>@. A?>;L7C5B XHTML, CSS 8 JavaScript B5E=>;>388.
%description UI-WebCfgd -l uk_UA.UTF8
0:5B %name-UI-WebCfgd, =040T 48=0<VG=89 WEB 107>20=89 :>=DV3C@0B>@.
8:>@8AB0=> XHTML, CSS B0 JavaScript B5E=>;>3VW.
%description UI-WebCfgd -l de_DE.UTF8
Das Paket %name-UI-WebCfgd ermoeglicht den dynamischen WEB-begruendeten
Konfigurator. Nutzt XHTML, CSS and JavaScript technologies aus.
%endif

%if 0%{?with_webvision}
%package UI-WebVision
Summary: Open SCADA interfaces
Group: Applications/Engineering
Requires: %{name} = %{version}-%{release}
%description UI-WebVision
The %name-UI-WebVision web operation user interface for visual control area
(VCA) projects playing.
%description UI-WebVision -l ru_UA.UTF8
0:5B %name-UI-WebVision, web @01>G89 ?>;L7>20B5;LA:89 8=B5@D59A 4;O
8A?>;=5=8O 287C0;L=KE A@54 C?@02;5=8O (!#)
%description UI-WebVision -l uk_RU.UTF8
0:5B %name-UI-WebVision, web @>1>G89 V=B5@D59A :>@8ABC20G0 4;O 28:>=0==O
2V7C0;L=>3> A5@54>28I0 :5@C20==O (!).
%description UI-WebVision -l de_DE.UTF8
Das Paket %name-UI-WebVision, web-Arbeitsnutzersinterface fuer Ausfuehrung
visueller Kontrollebereiche .
%endif

%if 0%{?with_http}
%package Protocol-HTTP
Summary: Open SCADA http
Group: Applications/Engineering
Requires: %{name} = %{version}-%{release}
%description Protocol-HTTP
The %name-Protocol-HTTP package allows support HTTP for WWW based UIs.
%description Protocol-HTTP -l ru_RU.UTF8
0:5B %name-Protocol-HTTP ?@54>AB02;O5B ?>445@6:C HTTP 4;O WWW >A=>20==KE
?>;L7>20B5;LA:8E 8=B5@D59A>2.
%description Protocol-HTTP -l uk_UA.UTF8
0:5B %name-Protocol-HTTP 040T ?V4B@8<:C HTTP 4;O WWW 107>7>20=8E
:>@8ABC20;L=8FL:8E V=B5@D59AV2.
%description Protocol-HTTP -l de_DE.UTF8
Das Paket %name-Protocol-HTTP ermoeglicht die HTTP-Unterstuetzung fuer die
WWW-basierenden Nutzersinterfaces .
%endif

%if 0%{?with_qtstarter}
%package UI-QTStarter
Summary: Open SCADA QT Starter
Group: Applications/Engineering
Requires: %{name} = %{version}-%{release}
%description UI-QTStarter
The %name-UI-QTStarter Allow QT GUI starter. It is single for
all QT GUI modules!.
%description UI-QTStarter -l ru_RU.UTF8
0:5B %name-UI-QTStarter @54>AB02;O5B QT GUI ?CA:0B5;L.
= O2;O5BAO 548=AB25==K< 4;O 2A5E QT GUI <>4C;59!
%description UI-QTStarter -l uk_UA.UTF8
0:5B %name-UI-QTStarter 040T QT GUI ?CA:0G. V= T >48= 4;O
CAVE QT GUI <>4C;V2!
%description UI-QTStarter -l de_DE.UTF8
Das Paket %name-UI-QTStarter  Enthaelt den QT GUI Starter.
Ist das einzige fuer alle QT GUI Module!
%endif

%if 0%{?with_qtcfg}
%package UI-QTCfg
Summary: Open SCADA QT interfaces
Group: Applications/Engineering
Requires: %{name} = %{version}-%{release}
%description UI-QTCfg
The %name-UI-QTCfg allows the QT based OpenSCADA system configurator.
%description UI-QTCfg -l ru_RU.UTF8
0:5B %name-UI-QTCfg ?@54>AB02;O5B QT >A=>20==K9 :>=D83C@0B>@ A8AB5<K
OpenSCADA.
%description UI-QTCfg -l uk_UA.UTF8
0:5B %name-UI-QTCfg <VAB8BL D09;8 QTCfg-:>=DV3C@0B>@C.
%description UI-QTCfg -l de_DE.UTF8
Das Paket %name-UI-QTCfg emrmoeglicht den QT-begruendeten
OpenSCADA-Systemkonfigurator.
%endif

%if 0%{?with_qtvision}
%package UI-QTVision
Summary: Open SCADA QT interfaces
Group: Applications/Engineering
Requires: %{name} = %{version}-%{release}
%description UI-QTVision
The %name-UI-QTVision package includes files visual operation user
interface.
%description UI-QTVision -l ru_RU.UTF8
0:5B %name-UI-QTVision 2:;NG05B D09;K @01>G53> ?>;L7>20B5;LA:>3>
8=B5@D59A0.
%description UI-QTVision -l uk_UA.UTF8
0:5B %name-UI-QTVision 2:;NG0T D09;8 @>1>G>3> V=B5@D59AC
:>@8ABC20G0.
%description UI-QTVision -l de_DE.UTF8
Das Paket %name-UI-QTVision enthaelt die Arbeitsnutzersinterfacedaten
%endif

%if 0%{?with_ssl}
%package Transport-SSL
Summary: Open SCADA transports
Group: Applications/Engineering
Requires: %{name} = %{version}-%{release}
%description Transport-SSL
The %name-Transport-SSL allows security socket layer based transport.
Used OpenSSL and supported SSLv2, SSLv3 and TLSv1.
%description Transport-SSL -l ru_RU.UTF8
0:5B %name-Transport-SSL ?@54>AB02;O5B B@0=A?>@B >A=>20==K9 =0 A;>5
157>?0A=KE A>:5B>2. A?>;L7C5BAO OpenSSL 8 ?>445@6820NBO SSLv2, SSLv3
and TLSv1.
%description Transport-SSL -l uk_UA.UTF8
0:5B %name-Transport-SSL =040T B@0=A?>@B 107>20=89 =0 157?5G=><C H0@V A>:5BV2.
 8:>@8AB0=> OpenSSL B0 ?V4B@8<CNBLAO SSLv2, SSLv3 and TLSv1.
%description Transport-SSL -l de_DE.UTF8
Das Paket %name-Transport-SSL enthaelt den auf der Schicht der unfallfesten
Sockets begruendeten Transport. Es werden OpenSSL benutzt und SSLv2, SSLv3
und TLSv1 unterstuetzt.
%endif

%if 0%{?with_sockets}
%package Transport-Sockets
Summary: Open SCADA transports
Group: Applications/Engineering
Requires: %{name} = %{version}-%{release}
%description Transport-Sockets
The %name-Transport-Sockets allows sockets based transport. Supports inet
and unix sockets. Inet socket uses TCP and UDP protocols.
%description Transport-Sockets -l ru_RU.UTF8
0:5B %name-Transport-Sockets ?54>AB02;O5B B@0=A?>@B >A=>20==K9 =0 A>:5B0E.
>445@6820NBAO 8=B5@=5B 8 UNIX A>:5BK. =B5@=5B A>:5B 8A?>;L7C5B TCP 8 UDP
?@>B>:>;K.
%description Transport-Sockets -l uk_UA.UTF8
0:5B %name-Transport-Sockets =040T B@0=A?>@B 107>20=89 =0 A>:5B0E.
V4B@8<CNBLAO V=B5@=5B B0 UNIX A>:5B8. =B5@=5B A>:5B 28:>@8AB>2CT TCP
B0 UDP ?@>B>:>;8.
%description Transport-Sockets -l de_DE.UTF8
Das Paket %name-Transport-Sockets ermoeglicht den auf Sockets begruendeten
Transport. Unterstuetzt werden Internet- und UNIX-Sockets. Internetsocket
benutzt TCP und UDP Protokolle.
%endif

%if 0%{?with_serial}
%package Transport-Serial
Summary: Open SCADA transports
Group: Applications/Engineering
Requires: %{name} = %{version}-%{release}
%description Transport-Serial
The %name-Transport-Serial, allow serial based interfaces. Used for
data exchanging through serial interfaces like RS232, RS485, GSM
and other.
%description Transport-Serial -l ru_RU.UTF8
0:5B %name-Transport-Serial, ?@54>AB02;O5B ?>A;54>20B5;L=K9 8=B5@D59A.
A?>;L7C5BAO 4;O >1<5=0 40==K<8 G5@57 ?>A;54>20B5;L=K5 8=B5@D59AK
B8?0 RS232, RS485, GSM 8 4@C3>5.
%description Transport-Serial -l uk_UA.UTF8
0:5B %name-Transport-Serial, =040T ?>A;V4>2=V V=B5@D59A8.
8:>@8AB>2CTBLAO 4;O >1<V=C 40=8<8 G5@57 ?>A;V4>2=V V=B5@D59AB8
B8?C RS232, RS485, GSM B0 V=H5.
%description Transport-Serial -l de_DE.UTF8
Das Paket %name-Transport-Serial, ermoeglicht konsequenten
Nutzersinterface. Wird fuer das Umtauschen von Daten durch konsequente
Interfaces wie RS232, RS485, GSM und andere benutzt.
%endif

%if 0%{?with_flibcomplex}
%package Special-FlibComplex1
Summary: Open SCADA special
Group: Applications/Engineering
Requires: %{name} = %{version}-%{release}
%description Special-FlibComplex1
The %name-Special-FlibComplex1 allows static function library
Complex1 (SCADA Complex1 functions).
%description Special-FlibComplex1 -l ru_RU.UTF8
0:5B %name-Special-FlibComplex1-Sockets ?@54>AB02;O5B AB0B8G5A:CN
181;8>B5:C DC=:F89 Complex1 (DC=:F88 SCADA Complex1).
%description Special-FlibComplex1 -l uk_UA.UTF8
0:5B %name-Special-FlibComplex1 =040T AB0B8G=C 1V1;V>B5:C DC=:FV9
Complex1 (DC=:FVW SCADA Complex1).
%description Special-FlibComplex1 -l de_DE.UTF8
Das Paket %name-Special-FlibComplex1s enthaelt statische
Bibliothek der Complex1-Funktionen (Funktionen SCADA Complex1).
%endif

%if 0%{?with_flibmath}
%package Special-FlibMath
Summary: Open SCADA special
Group: Applications/Engineering
Requires: %{name} = %{version}-%{release}
%description Special-FlibMath
The %name-Special-FlibMath allows mathematic static function library.
%description Special-FlibMath -l ru_RU.UTF8
0:5B %name-Special-FlibMath ?@54>AB02;O5B 181;8>B5:C AB0=40@B=KE
<0B5<0B8G5A:8E DC=:F89.
%description Special-FlibMath -l uk_UA.UTF8
0:5B %name-Special-FlibMath =040T AB0B8G=C 1V1;V>B5:C <0B5<0B8G=8E DC=:FV9.
%description Special-FlibMath -l de_DE.UTF8
The %name-Special-FlibMath : #Das Paket %name-Special-FlibMath enthaelt
Standardbibliothek der mathematischen Funktionen.
%endif

%if 0%{?with_flibsys}
%package Special-FlibSys
Summary: Open SCADA special
Group: Applications/Engineering
Requires: %{name} = %{version}-%{release}
%description Special-FlibSys
The %name-Special-FlibSys allows system API functions library
of the user programming area.
%description Special-FlibSys -l ru_RU.UTF8
0:5B %name-Special-FlibSys ?@54>AB02;O5B 2 A8AB5<C 181;8>B5:C
A8AB5<=>3> API A@54K ?>;L7>20B5;LA:>3> ?@>3@0<<8@>20=8O.
%description Special-FlibSys -l uk_UA.UTF8
0:5B %name-Special-FlibSys =040T 2 A8AB5<C 1V1;V>B5:C A8AB5<=>3> API
A5@54>28I0 ?@>3@0<C20==O :>@8ABC20G0.
%description Special-FlibSys -l de_DE.UTF8
Das Paket %name-Special-FlibSys ermoeglicht in das System die
Bibliothek der API-Systemprogrammierung des Nutzersbereiches.
%endif

%if 0%{?with_systemtests}
%package Special-SystemTests
Summary: Open SCADA special
Group: Applications/Engineering
Requires: %{name} = %{version}-%{release}
%description Special-SystemTests
The %name-Special-SystemTests allows the group tests for OpenSCADA system.
%description Special-SystemTests -l ru_RU.UTF8
0:5B %name-Special-SystemTests ?@54>AB02;O5B 3@C??C B5AB>2 4;O A8AB5<K
OpenSCADA.
%description Special-SystemTests -l uk_UA.UTF8
0:5B %name-Special-SystemTests =040T 3@C?C B5ABV2 4;O A8AB5<8 OpenSCADA.
%description Special-SystemTests -l de_DE.UTF8
Das Paket %name-Special-SystemTests enthaelt die Testgruppe fuer das
OpenSCADA-System
%endif

%package doc
Summary: Open SCADA documents
Group: Documentation
%description doc
The %name-doc package include documents files.
%description doc -l ru_RU.UTF8
0:5B %name-doc 2:;NG05B D09;K 4>:C<5=B0F88.
%description doc -l uk_UA.UTF8
0:5B %name-doc 2:;NG0T D09;8 4>:C<5=B0FVW.
%description doc -l de_DE.UTF8
Das Paket %name-doc enthaelt Dokumentationsdateien.

%package devel
Summary: Open SCADA development
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
%description devel
The %name-devel package includes library archives and include files.
%description devel -l ru_RU.UTF8
0:5B %name-devel 2:;NG05B 0@E82 181;8>B5: 8 2:;NG05<K5 D09;K.
%description devel -l uk_UA.UTF8
0:5B %name-devel 2:;NG0T 0@EV2 1V1;V>B5: B0 2:;NG0T<V D09;8.
%description devel -l de_DE.UTF8
Das Paket %name-devel enthaelt Bibliothekenarchiv und eingeschlossene
Dateien.

%package demo
Summary: Open SCADA demo data bases and config
Group: Applications/Engineering
Requires:%{name} = %{version}-%{release}
# ############### ARH ########################
%if 0%{?with_dbarch}
Requires:%{name}-ARH-DBArch = %{version}-%{release}
%endif
%if 0%{?with_fsarch}
Requires:%{name}-ARH-FSArch = %{version}-%{release}
%endif
# ############### Special ########################
%if 0%{?with_flibmath}
Requires:%{name}-Special-FlibMath = %{version}-%{release}
%endif
%if 0%{?with_flibcomplex}
Requires:%{name}-Special-FlibComplex1 = %{version}-%{release}
%endif
%if 0%{?with_flibsys}
Requires:%{name}-Special-FlibSys = %{version}-%{release}
%endif
%if 0%{?with_systemtests}
Requires:%{name}-Special-SystemTests = %{version}-%{release}
%endif
# ############### DAQ ########################
%if 0%{?with_blockcalc}
Requires:%{name}-DAQ-BlockCalc = %{version}-%{release}
%endif
%if 0%{?with_javalikecalc}
Requires:%{name}-DAQ-JavaLikeCalc = %{version}-%{release}
%endif
%if 0%{?with_logiclevel}
Requires:%{name}-DAQ-LogicLevel = %{version}-%{release}
%endif
%if 0%{?with_system}
Requires:%{name}-DAQ-System = %{version}-%{release}
%endif
%if 0%{?with_blockcalc}
Requires:%{name}-DAQ-BlockCalc = %{version}-%{release}
%endif
%if 0%{?with_daqgate}
Requires:%{name}-DAQ-Gate = %{version}-%{release}
%endif
# ############### HTTP ########################
%if 0%{?with_http}
Requires:%{name}-Protocol-HTTP = %{version}-%{release}
%endif
# ############### SelfSystem ########################
%if 0%{?with_selfsystem}
Requires:%{name}-Protocol-SelfSystem = %{version}-%{release}
%endif
# ############### Transport ########################
%if 0%{?with_sockets}
Requires:%{name}-Transport-Sockets = %{version}-%{release}
%endif
%if 0%{?with_ssl}
Requires:%{name}-Transport-SSL = %{version}-%{release}
%endif
%if 0%{?with_serial}
Requires:%{name}-Transport-Serial = %{version}-%{release}
%endif
# ############### GUI System ########################
%if 0%{?with_qtstarter}
Requires:%{name}-UI-QTStarter = %{version}-%{release}
%endif
%if 0%{?with_qtcfg}
Requires:%{name}-UI-QTCfg = %{version}-%{release}
%endif
%if 0%{?with_qtvision}
Requires:%{name}-UI-QTVision = %{version}-%{release}
%endif
# ############### Web Interfaces ########################
%if 0%{?with_webcfg}
Requires:%{name}-UI-WebCfg = %{version}-%{release}
%endif
%if 0%{?with_webcfgd}
Requires:%{name}-UI-WebCfgd = %{version}-%{release}
%endif
%if 0%{?with_webvision}
Requires:%{name}-UI-WebVision = %{version}-%{release}
%endif

%description demo
The %{name}-demo package includes demo data bases and configs.
For start use command <openscada_demo>. For access use account
"root" and password "openscada" or account "user" without password.
%description demo -l ru_RU.UTF8
0:5B %{name}-demo 2:;NG05B 45<>=AB@0F8>==K5 107K 40==KE 8 :>=D83C@0F88.
;O AB0@B0 8A?>;L7C9B5 :><0=4C <openscada_demo>. ;O 4>ABC?0 8A?>;L7C9B5 70?8AL
"root" 8 ?0@>;L "openscada" 8;8 70?8AL "user" 157 ?0@>;O.
%description demo -l uk_UA.UTF8
0:5B %{name}-demo 2:;NG0T 45<>=AB@0FV9=V 1078 40=8E B0 :>=DV3C@0FVW. ;O
AB0@BC 28:>@8AB>2C9B5 :><0=4C <openscada_demo>. ;O 4>ABC?C 28:>@8AB>2C9B5
70?8A "root" B0 ?0@>;L "openscada" 01> 70?8A "user" 157 ?0@>;O.
%description demo -l de_DE.UTF8
Das Paket %{name}-demo enthaelt Demodatenbanken und Konfigurationen. Fuers
Starten wird Kommando <openscada_demo> benutzt. Fuer den Zugang benutzen Sie
die Anschreibung "root" und das Kennwort "openscada" oder die Anschreibung
"user" ohne Kennwort.

%prep
%setup -q -n %{srcname}
%patch0 -p1 -b .fedora
%{__sed} -i 's|/usr/lib/|%{_libdir}/|' data/oscada*.xml

%build
CFLAGS="%{optflags}" CXXFLAGS="%{optflags}" \
  %configure --disable-static \
	%{!?with_dcon:--disable-DCON} \
	%{!?with_diamondboards:--disable-DiamondBoards} \
	%{!?with_mysql:--disable-MySQL} \
	%{!?with_firebird:--disable-FireBird} \
	%{?with_firebird:--with-firebird=%{_libdir}/firebird} \
	%{!?with_dbf:--disable-DBF} \
	%{!?with_sqlite:--disable-SQLite} \
	%{!?with_webcfg:--disable-WebCfg} \
	%{!?with_webcfgd:--disable-WebCfgD} \
	%{!?with_webvision:--disable-WebVision} \
	%{!?with_http:--disable-HTTP} \
	%{!?with_modbus:--disable-ModBus} \
	%{!?with_soundcard:--disable-SoundCard} \
	%{!?with_qtcfg:--disable-QTCfg} \
	%{!?with_qtvision:--disable-Vision} \
	%{!?with_ssl:--disable-SSL} \
	%{!?with_serial:--disable-Serial} \
	%{!?with_sockets:--disable-Sockets} \
	%{!?with_snmp:--disable-SNMP} \
	%{!?with_siemens:--disable-Siemens} \
	%{!?with_dbarch:--disable-DBArch} \
	%{!?with_fsarch:--disable-FSArch} \
	%{!?with_system:--disable-System} \
	%{!?with_blockcalc:--disable-BlockCalc} \
	%{!?with_javalikecalc:--disable-JavaLikeCalc} \
	%{!?with_logiclevel:--disable-LogicLev} \
	%{!?with_daqgate:--disable-DAQGate} \
	%{!?with_selfsystem:--disable-SelfSystem} \
	%{!?with_flibcomplex:--disable-FlibComplex1} \
	%{!?with_flibmath:--disable-FlibMath} \
	%{!?with_flibsys:-disable-FlibSYS} \
	%{!?with_systemtests:--disable-SelfSystem} \
	%{!?with_qtstarter:--disable-QTStarter}

make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install

# let's try to get rid of rpath
chrpath --delete %{buildroot}%{_bindir}/openscada

# remove static libs and libtool archives
rm -f %{buildroot}%{_libdir}/*.*a
rm -f %{buildroot}%{_libdir}/openscada/*.*a

install -m 755 -d %{buildroot}%{_includedir}/openscada/
install -m 644 *.h %{buildroot}%{_includedir}/openscada
install -m 644 src/*.h %{buildroot}%{_includedir}/openscada
install -m 644 -pD data/oscada.xml %{buildroot}%{_sysconfdir}/oscada.xml
install -m 644 -pD data/oscada_start.xml %{buildroot}%{_sysconfdir}/oscada_start.xml
install -m 755 -pD data/openscada_start %{buildroot}%{_bindir}/openscada_start
install -m 755 -pD data/oscada.init %{buildroot}%{_initrddir}/openscadad
install -m 755 -d %{buildroot}/var/spool/openscada/{DATA,icons}
install -m 644 data/icons/* %{buildroot}/var/spool/openscada/icons
install -m 755 -d %{buildroot}/var/spool/openscada/ARCHIVES/{MESS,VAL}
install -m 644 -pD demo/oscada_demo.xml %{buildroot}%{_sysconfdir}/oscada_demo.xml
install -m 755 -pD demo/openscada_demo %{buildroot}%{_bindir}/openscada_demo
%if 0%{?with_qtstarter}
install -m 644 -pD demo/openscada_demo.png %{buildroot}%_iconsdir/openscada_demo.png
install -m 644 -pD data/openscada.png %{buildroot}%_iconsdir/openscada.png
%endif
install -m 755 -d %{buildroot}/var/spool/openscada/DEMO
install -m 644 demo/*.db %{buildroot}/var/spool/openscada/DEMO

echo "OpenSCADA data dir" > %{buildroot}/var/spool/openscada/DATA/info
echo "OpenSCADA messages archive dir" > %{buildroot}/var/spool/openscada/ARCHIVES/MESS/info
echo "OpenSCADA values archive dir" > %{buildroot}/var/spool/openscada/ARCHIVES/VAL/info

# installation of *.desktop files
%if 0%{?with_qtstarter}
desktop-file-install --dir=%{buildroot}%_desktopdir data/openscada.desktop
desktop-file-install --dir=%{buildroot}%_desktopdir demo/openscada_demo.desktop
%endif

%find_lang %{name} --all-name

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/oscada.xml
%config(noreplace) %{_sysconfdir}/oscada_start.xml
%dir %{_libdir}/openscada
%dir %{_localstatedir}/spool/openscada
%dir %{_localstatedir}/spool/openscada/DATA
%dir %{_localstatedir}/spool/openscada/icons
%dir %{_localstatedir}/spool/openscada/ARCHIVES
%dir %{_localstatedir}/spool/openscada/ARCHIVES/MESS
%dir %{_localstatedir}/spool/openscada/ARCHIVES/VAL
%doc README README_ru COPYING ChangeLog
%{_initrddir}/openscadad
%{_bindir}/openscada
%{_bindir}/openscada_start
%{_libdir}/*.so.*
%{_libdir}/openscada/*.so

%{?with_diamondboards: %exclude %{_libdir}/openscada/daq_DiamondBoards.so}
%{?with_dcon: %exclude %{_libdir}/openscada/daq_DCON.so}
%{?with_modbus: %exclude %{_libdir}/openscada/daq_ModBus.so}
%{?with_soundcard: %exclude %{_libdir}/openscada/daq_SoundCard.so}
%{?with_snmp: %exclude %{_libdir}/openscada/daq_SNMP.so}
%{?with_siemens: %exclude %{_libdir}/openscada/daq_Siemens.so}
%{?with_system: %exclude %{_libdir}/openscada/daq_System.so}
%{?with_blockcalc: %exclude %{_libdir}/openscada/daq_BlockCalc.so}
%{?with_javalikecalc: %exclude %{_libdir}/openscada/daq_JavaLikeCalc.so}
%{?with_logiclevel: %exclude %{_libdir}/openscada/daq_LogicLev.so}
%{?with_daqgate: %exclude %{_libdir}/openscada/daq_DAQGate.so}
%{?with_selfsystem: %exclude %{_libdir}/openscada/prot_SelfSystem.so}
%{?with_firebird: %exclude %{_libdir}/openscada/bd_FireBird.so}
%{?with_mysql: %exclude %{_libdir}/openscada/bd_MySQL.so}
%{?with_dbf: %exclude %{_libdir}/openscada/bd_DBF.so}
%{?with_sqlite: %exclude %{_libdir}/openscada/bd_SQLite.so}
%{?with_dbarch: %exclude %{_libdir}/openscada/arh_DBArch.so}
%{?with_fsarch: %exclude %{_libdir}/openscada/arh_FSArch.so}
%{?with_webcfg: %exclude %{_libdir}/openscada/ui_WebCfg.so}
%{?with_webcfgd: %exclude %{_libdir}/openscada/ui_WebCfgD.so}
%{?with_webvision: %exclude %{_libdir}/openscada/ui_WebVision.so}
%{?with_http: %exclude %{_libdir}/openscada/prot_HTTP.so}
%{?with_qtcfg: %exclude %{_libdir}/openscada/ui_QTCfg.so}
%{?with_qtvision: %exclude %{_libdir}/openscada/ui_Vision.so}
%{?with_ssl: %exclude %{_libdir}/openscada/tr_SSL.so}
%{?with_sockets: %exclude %{_libdir}/openscada/tr_Sockets.so}
%{?with_ssl: %exclude %{_libdir}/openscada/tr_Serial.so}
%{?with_flibcomplex: %exclude %{_libdir}/openscada/spec_FLibComplex1.so}
%{?with_flibmath: %exclude %{_libdir}/openscada/spec_FLibMath.so}
%{?with_flibsys: %exclude %{_libdir}/openscada/spec_FLibSYS.so}
%{?with_systemtests: %exclude %{_libdir}/openscada/spec_SystemTests.so}

%{_localstatedir}/spool/openscada/DATA/info
%{_localstatedir}/spool/openscada/icons/*
%{_localstatedir}/spool/openscada/ARCHIVES/MESS/info
%{_localstatedir}/spool/openscada/ARCHIVES/VAL/info

%files doc
%defattr(-,root,root)
%doc doc/*.pdf doc/Modules

%if 0%{?with_diamondboards}
%files DAQ-DiamondBoards
%defattr(-,root,root)
%{_libdir}/openscada/daq_DiamondBoards.so
%endif

%if 0%{?with_dcon}
%files DAQ-DCON
%defattr(-,root,root)
%{_libdir}/openscada/daq_DCON.so
%endif

%if 0%{?with_modbus}
%files DAQ-ModBus
%defattr(-,root,root)
%{_libdir}/openscada/daq_ModBus.so
%endif

%if 0%{?with_soundcard}
%files DAQ-Soundcard
%defattr(-,root,root)
%{_libdir}/openscada/daq_SoundCard.so
%endif

%if 0%{?with_snmp}
%files DAQ-SNMP
%defattr(-,root,root)
%{_libdir}/openscada/daq_SNMP.so
%endif

%if 0%{?with_siemens}
%files DAQ-Siemens
%defattr(-,root,root)
%{_libdir}/openscada/daq_Siemens.so
%endif

%if 0%{?with_system}
%files DAQ-System
%defattr(-,root,root)
%{_libdir}/openscada/daq_System.so
%endif

%if 0%{?with_blockcalc}
%files DAQ-BlockCalc
%defattr(-,root,root)
%{_libdir}/openscada/daq_BlockCalc.so
%endif

%if 0%{?with_javalikecalc}
%files DAQ-JavaLikeCalc
%defattr(-,root,root)
%{_libdir}/openscada/daq_JavaLikeCalc.so
%endif

%if 0%{?with_logiclevel}
%files DAQ-LogicLevel
%defattr(-,root,root)
%{_libdir}/openscada/daq_LogicLev.so
%endif

%if 0%{?with_daqgate}
%files DAQ-Gate
%defattr(-,root,root)
%{_libdir}/openscada/daq_DAQGate.so
%endif

%if 0%{?with_selfsystem}
%files Protocol-SelfSystem
%defattr(-,root,root)
%{_libdir}/openscada/prot_SelfSystem.so
%endif

%if 0%{?with_firebird}
%files DB-FireBird
%defattr(-,root,root)
%{_libdir}/openscada/bd_FireBird.so
%endif

%if 0%{?with_mysql}
%files DB-MySQL
%defattr(-,root,root)
%{_libdir}/openscada/bd_MySQL.so
%endif

%if 0%{?with_dbf}
%files DB-DBF
%defattr(-,root,root)
%{_libdir}/openscada/bd_DBF.so
%endif

%if 0%{?with_sqlite}
%files DB-SQLite
%defattr(-,root,root)
%{_libdir}/openscada/bd_SQLite.so
%endif

%if 0%{?with_dbarch}
%files ARH-DBArch
%defattr(-,root,root)
%{_libdir}/openscada/arh_DBArch.so
%endif

%if 0%{?with_fsarch}
%files ARH-FSArch
%defattr(-,root,root)
%{_libdir}/openscada/arh_FSArch.so
%endif

%if 0%{?with_webcfg}
%files UI-WebCfg
%defattr(-,root,root)
%{_libdir}/openscada/ui_WebCfg.so
%endif

%if 0%{?with_webcfgd}
%files UI-WebCfgd
%defattr(-,root,root)
%{_libdir}/openscada/ui_WebCfgD.so
%endif

%if 0%{?with_webvision}
%files UI-WebVision
%defattr(-,root,root)
%{_libdir}/openscada/ui_WebVision.so
%endif

%if 0%{?with_http}
%files Protocol-HTTP
%defattr(-,root,root)
%{_libdir}/openscada/prot_HTTP.so
%endif

%if 0%{?with_qtstarter}
%files UI-QTStarter
%defattr(-,root,root)
%{_libdir}/openscada/ui_QTStarter.so
%_desktopdir/openscada.desktop
%_desktopdir/openscada_demo.desktop
%_iconsdir/openscada.png
%endif

%if 0%{?with_qtcfg}
%files UI-QTCfg
%defattr(-,root,root)
%{_libdir}/openscada/ui_QTCfg.so
%endif

%if 0%{?with_qtvision}
%files UI-QTVision
%defattr(-,root,root)
%{_libdir}/openscada/ui_Vision.so
%endif

%if 0%{?with_ssl}
%files Transport-SSL
%defattr(-,root,root)
%{_libdir}/openscada/tr_SSL.so
%endif

%if 0%{?with_sockets}
%files Transport-Sockets
%defattr(-,root,root)
%{_libdir}/openscada/tr_Sockets.so
%endif

%if 0%{?with_serial}
%files Transport-Serial
%defattr(-,root,root)
%{_libdir}/openscada/tr_Serial.so
%endif

%if 0%{?with_flibcomplex}
%files Special-FlibComplex1
%defattr(-,root,root)
%{_libdir}/openscada/spec_FLibComplex1.so
%endif

%if 0%{?with_flibmath}
%files Special-FlibMath
%defattr(-,root,root)
%{_libdir}/openscada/spec_FLibMath.so
%endif

%if 0%{?with_flibsys}
%files Special-FlibSys
%defattr(-,root,root)
%{_libdir}/openscada/spec_FLibSYS.so
%endif

%if 0%{?with_systemtests}
%files Special-SystemTests
%defattr(-,root,root)
%{_libdir}/openscada/spec_SystemTests.so
%endif

%files devel
%defattr(-,root,root)
%dir %{_includedir}/openscada
%{_libdir}/*.so
%{_includedir}/openscada/*

%files demo
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/oscada_demo.xml
%dir %{_localstatedir}/spool/openscada/DEMO
%{_bindir}/openscada_demo
%{_localstatedir}/spool/openscada/DEMO/*.db
%if 0%{?with_qtstarter}
%_desktopdir/openscada_demo.desktop
%_iconsdir/openscada_demo.png
%endif

%changelog
* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.3.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jul 14 2009 Popkov Aleksey <aleksey@oscada.org.ua> 0.6.3.3-9
- Adding %find_lang macros by Peter Lemenkov <lemenkov@gmail.com>
- Somes cosmetics.

* Tue Jun 30 2009 Popkov Aleksey <aleksey@oscada.org.ua> 0.6.3.3-8
- Added of dependences in to self package demo
- Fixed %preun section by Peter Lemenkov <lemenkov@gmail.com>
- Somes cosmetics.

* Wed Jun 19 2009 Popkov Aleksey <aleksey@oscada.org.ua> 0.6.3.3-7
- Fixed bugs maked by me.

* Wed Jun 18 2009 Popkov Aleksey <aleksey@oscada.org.ua> 0.6.3.3-6
- Workarounds for some bugs in rpmbuild by Peter Lemenkov <lemenkov@gmail.com>.

* Wed Jun 17 2009 Popkov Aleksey <aleksey@oscada.org.ua> 0.6.3.3-5
- Fixed critical bugs maked by me.

* Tue Jun 16 2009 Popkov Aleksey <aleksey@oscada.org.ua> 0.6.3.3-4
- Enabled Portaudio-devel library by Popkov Aleksey.

* Tue Jun 16 2009 Popkov Aleksey <aleksey@oscada.org.ua> 0.6.3.3-3
- Adapted spec file for dist 5E-epel by Popkov Aleksey
- Adapted spec file for dist 4E-epel by Popkov Aleksey (Not tested)
- Fixed oscada.init.patch for cases messages.

* Thu Jun 11 2009 Popkov Aleksey <aleksey@oscada.org.ua> 0.6.3.3-2
- Fixed incoherent-init-script-name warning of rename init scripts from oscadad to openscadad by Popkov Aleksey
- Fixed incoherent-subsys error of rename into init scripts from lockfile=/var/lock/subsys/oscadad to lockfile=/var/lock/subsys/openscadad by Popkov Aleksey.

* Wed Jun 10 2009 Popkov Aleksey <aleksey@oscada.org.ua> 0.6.3.3-1
- Release OpenSCADA 0.6.3.3.
- Added self modules of daq_DAQGate and tr_Serial.
- Adapted init script for fedora. oscada.init.patch.
- Translated description to Germany language by Popkova Irina.

* Mon Jun 8 2009 Popkov Aleksey <aleksey@oscada.org.ua> 0.6.3.3-0.1.svn902
- Prerelease OpenSCADA 0.6.3.3 (svn ver. 902)
- Fixed issue with find_lang
- Removal, of some unneded files by Peter Lemenkov <lemenkov@gmail.com>
- Translated description to German language by Popkova Irina.

* Thu Jun 4 2009 Popkov Aleksey <aleksey@oscada.org.ua> 0.6.3.3-0.1.svn901
- Prerelease OpenSCADA 0.6.3.3 (svn ver. 901)
- Translated description to German language by Popkova Irina.

* Wed Jun 3 2009 Popkov Aleksey <aleksey@oscada.org.ua> 0.6.3.3-0.1.svn899
- Adaptated for release OpenSCADA 0.6.3.3.

* Thu May 26 2009 Popkov Aleksey <aleksey@oscada.org.ua> 0.6.3.2-2
- OpenSCADA build for Fedora.
- Translated description to German language by Popkova Irina.

* Wed Mar 18 2009 Roman Savochenko <rom_as@diyaorg.dp.ua>
- OpenSCADA update 0.6.3.2 release build.

* Mon Feb 2 2009 Roman Savochenko <rom_as@diyaorg.dp.ua>
- OpenSCADA update 0.6.3.1 release build.

* Mon Dec 22 2008 Roman Savochenko <rom_as@diyaorg.dp.ua>
- Documentation pack is unified and separated to project info files and documentation.
- Dynamic librarie's links packing into main package and development is fixed.

* Thu Oct 02 2008 Roman Savochenko <rom_as@fromru.com>
- Package name simple changing allow is added.

* Thu Sep 18 2008 Roman Savochenko <rom_as@diyaorg.dp.ua>
- Update spec to build for ALTLinux Sisyphus.

* Wed Mar 26 2008 Roman Savochenko <rom_as@diyaorg.dp.ua>
- Rebuilded for support x86_64 several distributives and some build system bugs is fixed.

* Sat Mar 23 2008 Roman Savochenko <rom_as@diyaorg.dp.ua>
- menu files included

* Fri Sep 02 2005 Roman Savochenko <rom_as@fromru.com>
- replace testdate whith demo package
- rename xinetd script from openscada to oscadad
- add xinetd script to generic package

* Wed Mar 16 2005 Roman Savochenko <rom_as@fromru.com>
- add Athena board specific build

* Wed Nov 03 2004 Roman Savochenko <rom_as@fromru.com>
- move the message arhives data to /var/spool/%{name}/ARHIVE/MESS

* Tue Apr 06 2004 Roman Savochenko <rom_as@fromru.com>
- make 3 packages: OpenScada, OpenScada-devel, OpenScada-testdata
- add languages: ru, uk
- make packages from 'make -dist' package;

* Thu Oct 15 2003 Roman Savochenko <rom_as@fromru.com>
- Starting
