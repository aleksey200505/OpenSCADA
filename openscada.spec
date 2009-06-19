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
Release: 7%{?dist}
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

%description
Open SCADA system. For access use account "root" and password "openscada".
%description -l ru_RU.UTF8
Открытая SCADA система. Для доступа используйте запись "root" и пароль
"openscada".
%description -l uk_UA.UTF8
Відкрита SCADA система. Для доступу використовуйте запис "root" та пароль
"openscada".
%description -l de_DE.UTF8
Das offene SCADA System. Fuer den Zugang die Aufzeichnung "root" und das
Kennwort "openscada" benutzen.

%post
/sbin/ldconfig
/sbin/chkconfig --add openscadad
/sbin/chkconfig openscadad off

%postun -p /sbin/ldconfig

%preun
/sbin/chkconfig --del openscadad

%if 0%{?with_diamondboards}
%package DAQ-DiamondBoards
Summary: Open SCADA DAQ
Group: Applications/Engineering
Requires: %{name} = %{version}-%{release}
%description DAQ-DiamondBoards
The %name-DAQ-DiamondBoards allows access to Diamond systems DA boards.
Includes support of Athena board.
%description DAQ-DiamondBoards -l ru_RU.UTF8
Пакет %name-DAQ-DiamondBoards предоставляет доступ к платам сбора
данных фирмы Diamond systems. Включает поддержку системной платы
Athena.
%description DAQ-DiamondBoards -l uk_UA.UTF8
Пакет %name-DAQ-DiamondBoards надає доступ до плат збору даних фірми
Diamond systems. Включає підтримку системної плати Athena.
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
Пакет %name-DAQ-DCON предоставляет реализацию клиентского сервиса
протокола DCON. Поддерживается протокол I-7000 DCON.
%description DAQ-DCON -l uk_UA.UTF8
Пакет %name-DAQ-DCON надає реалізацію клієнтського сервісу DCON.
Підтримується I-7000 DCON протокол.
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
Пакет %name-DAQ-ModBus предоставляет реализацию клиентского сервиса
протокола ModBus. Поддерживаются Modbus/TCP, Modbus/RTU и
Modbus/ASCII протоколы.
%description DAQ-ModBus -l uk_UA.UTF8
Пакет %name-DAQ-ModBus надає реалізацію клієнтського ModBus сервісу.
Підтримуються Modbus/TCP, Modbus/RTU та Modbus/ASCII протоколи.
%description DAQ-ModBus -l de_DE.UTF8
Das Paket %name-DAQ-ModBus emoeglicht Realisierung des Kundenservices des
ModBus - Protokolls. Unterstuetzt werden die Protokolle Modbus/TCP,
Modbus/RTU и Modbus/ASCII.
%endif

%if 0%{?with_soundcard}
%package DAQ-Soundcard
Summary: Open SCADA DAQ
Group: Applications/Engineering
Requires: %{name} = %{version}-%{release}
%description DAQ-Soundcard
The %name-DAQ-Soundcard allows access to sound card data.
%description DAQ-Soundcard -l ru_RU.UTF8
Пакет %name-DAQ-Soundcard предоставляет доступ к звуковой карте.
%description DAQ-Soundcard -l uk_UA.UTF8
Пакет %name-DAQ-Soundcard надає доступ до даних звукової карти.
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
Пакет %name-DAQ-SNMP предоставляет реализацию клиентского
сервиса протокола SNMP.
%description DAQ-SNMP -l uk_UA.UTF8
Пакет %name-DAQ-SNMP надає реалізацію клієнтського SNMP сервісу.
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
Пакет %name-DAQ-Siemens, предоставляет источник данных ПЛК Siemens
посредством карт Hilscher CIF с использованием протокола MPI и
библиотеки Libnodave для остального.
%description DAQ-Siemens -l uk_UA.UTF8
Пакет %name-DAQ-Siemens, надає джерело даних ПЛК Siemens за
допомогою карт Hilscher CIF з використанням протоколу MPI та
бібліотеки Libnodave для іншого.
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
Пакет %name-DAQ-System, предоставляет сбор данных операционной
системы. Поддерживаются источники данных ОС Linux: HDDTemp, Sensors,
Uptime, Memory, CPU и другие.
%description DAQ-System -l uk_UA.UTF8
Пакет %name-DAQ-System, Надає збір даних операційної системи.
Підтримуються джерела даних ОС Linux: HDDTemp, Sensors, Uptime, Memory,
CPU та інше.
%description DAQ-System -l de_DE.UTF8
Das Paket %name-DAQ-System ermoeglicht Datenerfassung des
Operationssystems. Es werden die Datenquellen ОС Linux: HDDTemp,
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
Пакет %name-DAQ-BlockCalc, предоставляет блочный вычислитель.
%description DAQ-BlockCalc -l uk_UA.UTF8
Пакет %name-DAQ-BlockCalc, надає блоковий обчислювач.
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
Пакет %name-DAQ-JavaLikeCalc, предоставляет основанные на java подобном
языке вычислитель и движок библиотек. Пользователь может создавать и
модифицировать функции и библиотеки.
%description DAQ-JavaLikeCalc -l uk_UA.UTF8
Пакет %name-DAQ-JavaLikeCalc, надає базовані на мові схожій на Java
обчислювач та движок бібліотек функцї. Користувач може створювати та
модифікувати функції та бібліотеки.
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
Пакет %name-DAQ-LogicLevel, предоставляет логический уровень параметров.
%description DAQ-LogicLevel -l uk_UA.UTF8
Пакет %name-DAQ-LogicLevel, надає логічний рівень параметрів.
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
Пакет %name-DAQ-Gate, позволяет выполнять шлюзование источников
данных удалённых OpenSCADA станций в локальные.
%description DAQ-Gate -l uk_UA.UTF8
Пакет %name-DAQ-Gate, дозволяє шлюзувати джерела даних віддалених
OpenSCADA станцій до локальних.
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
Пакет %name-Protocol-SelfSystem, cобственный протокол OpenSCADA,
поддерживает основные функции.
%description Protocol-SelfSystem -l uk_UA.UTF8
Пакет %name-Protocol-SelfSystem, власний протокол OpenSCADA,
підтримує основні функції.
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
Пакет %name-DB-FireBird, предоставляет поддержку БД FireBird.
%description DB-FireBird -l uk_UA.UTF8
Пакет %name-DB-FireBird, модуль БД. Надає підтримку БД FireBird.
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
Пакет %name-DB-MySQL, предоставляет поддержку БД MySQL.
%description DB-MySQL -l uk_UA.UTF8
Пакет %name-DB-MySQL, Надає підтримку БД MySQL.
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
Пакет %name-DB-DBF, предоставляет поддержку *.dbf файлов, версии 3.0..
%description DB-DBF -l uk_UA.UTF8
Пакет %name-DB-DBF, надає підтримку *.dbf файлів, версії 3.0.
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
Пакет %name-DB-SQLite, предоставляет поддержку БД SQLite.
%description DB-SQLite -l uk_UA.UTF8
Пакет %name-DB-SQLite, надає підтримку БД SQLite.
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
Пакет %name-ARH-DBArch, предоставляет функции архивирования сообщений и
значений на БД.
%description ARH-DBArch -l uk_UA.UTF8
Пакет %name-ARH-DBArch, надає функції архівації повідомлень та значень на БД.
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
Пакет %name-ARH-FSArch, предоставляет функции архивирования сообщений и
значений на файловую систему.
%description ARH-FSArch -l uk_UA.UTF8
Пакет %name-ARH-FSArch, надає функції архівації повідомлень та значень на
файлову систему.
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
Пакет %name-UI-WebCfg, предоставляет WEB основанный конфигуратор
системы OpenSCADA.
%description UI-WebCfg -l uk_UA.UTF8
Пакет %name-UI-WebCfg, надає WEB базований конфігуратор системи
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
Пакет %name-UI-WebCfgd, предоставляет динамический WEB основанный
конфигуратор. Использует XHTML, CSS и JavaScript технологии.
%description UI-WebCfgd -l uk_UA.UTF8
Пакет %name-UI-WebCfgd, надає динамічний WEB базований конфігуратор.
Використано XHTML, CSS та JavaScript технології.
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
Пакет %name-UI-WebVision, web рабочий пользовательский интерфейс для
исполнения визуальных сред управления (СВУ)
%description UI-WebVision -l uk_RU.UTF8
Пакет %name-UI-WebVision, web робочий інтерфейс користувача для виконання
візуального середовища керування (СВК).
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
Пакет %name-Protocol-HTTP предоставляет поддержку HTTP для WWW основанных
пользовательских интерфейсов.
%description Protocol-HTTP -l uk_UA.UTF8
Пакет %name-Protocol-HTTP Надає підтримку HTTP для WWW базозованих
користувальницьких інтерфейсів.
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
Пакет %name-UI-QTStarter Предоставляет QT GUI пускатель.
Он является единственным для всех QT GUI модулей!
%description UI-QTStarter -l uk_UA.UTF8
Пакет %name-UI-QTStarter Надає QT GUI пускач. Він є один для
усіх QT GUI модулів!
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
Пакет %name-UI-QTCfg предоставляет QT основанный конфигуратор системы
OpenSCADA.
%description UI-QTCfg -l uk_UA.UTF8
Пакет %name-UI-QTCfg містить файли QTCfg-конфігуратору.
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
Пакет %name-UI-QTVision включает файлы рабочего пользовательского
интерфейса.
%description UI-QTVision -l uk_UA.UTF8
Пакет %name-UI-QTVision включає файли робочого інтерфейсу
користувача.
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
Пакет %name-Transport-SSL предоставляет транспорт основанный на слое
безопасных сокетов. Используется OpenSSL и поддерживаютя SSLv2, SSLv3
and TLSv1.
%description Transport-SSL -l uk_UA.UTF8
Пакет %name-Transport-SSL надає транспорт базований на безпечному шарі сокетів.
 Використано OpenSSL та підтримуються SSLv2, SSLv3 and TLSv1.
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
Пакет %name-Transport-Sockets педоставляет транспорт основанный на сокетах.
Поддерживаются интернет и UNIX сокеты. Интернет сокет использует TCP и UDP
протоколы.
%description Transport-Sockets -l uk_UA.UTF8
Пакет %name-Transport-Sockets надає транспорт базований на сокетах.
Підтримуються інтернет та UNIX сокети. Інтернет сокет використовує TCP
та UDP протоколи.
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
Пакет %name-Transport-Serial, предоставляет последовательный интерфейс.
Используется для обмена данными через последовательные интерфейсы
типа RS232, RS485, GSM и другое.
%description Transport-Serial -l uk_UA.UTF8
Пакет %name-Transport-Serial, надає послідовні інтерфейси.
Використовується для обміну даними через послідовні інтерфейсти
типу RS232, RS485, GSM та інше.
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
Пакет %name-Special-FlibComplex1-Sockets предоставляет статическую
библиотеку функций Complex1 (функции SCADA Complex1).
%description Special-FlibComplex1 -l uk_UA.UTF8
Пакет %name-Special-FlibComplex1 надає статичну бібліотеку функцій
Complex1 (функції SCADA Complex1).
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
Пакет %name-Special-FlibMath предоставляет библиотеку стандартных
математических функций.
%description Special-FlibMath -l uk_UA.UTF8
Пакет %name-Special-FlibMath надає статичну бібліотеку математичних функцій.
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
Пакет %name-Special-FlibSys предоставляет в систему библиотеку
системного API среды пользовательского программирования.
%description Special-FlibSys -l uk_UA.UTF8
Пакет %name-Special-FlibSys надає в систему бібліотеку системного API
середовища програмування користувача.
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
Пакет %name-Special-SystemTests предоставляет группу тестов для системы
OpenSCADA.
%description Special-SystemTests -l uk_UA.UTF8
Пакет %name-Special-SystemTests надає групу тестів для системи OpenSCADA.
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
Пакет %name-doc включает файлы документации.
%description doc -l uk_UA.UTF8
Пакет %name-doc включає файли документації.
%description doc -l de_DE.UTF8
Das Paket %name-doc enthaelt Dokumentationsdateien.

%package devel
Summary: Open SCADA development
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
%description devel
The %name-devel package includes library archives and include files.
%description devel -l ru_RU.UTF8
Пакет %name-devel включает архив библиотек и включаемые файлы.
%description devel -l uk_UA.UTF8
Пакет %name-devel включає архів бібліотек та включаємі файли.
%description devel -l de_DE.UTF8
Das Paket %name-devel enthaelt Bibliothekenarchiv und eingeschlossene
Dateien.

%package demo
Summary: Open SCADA demo data bases and config
Group: Applications/Engineering
Requires:%{name} = %{version}-%{release}
Requires:%{name}-ARH-DBArch = %{version}-%{release}
Requires:%{name}-ARH-FSArch = %{version}-%{release}

Requires:%{name}-Special-FlibMath = %{version}-%{release}
Requires:%{name}-Special-FlibComplex1 = %{version}-%{release}
Requires:%{name}-Special-FlibSys = %{version}-%{release}

Requires:%{name}-DAQ-BlockCalc = %{version}-%{release}
Requires:%{name}-DAQ-JavaLikeCalc = %{version}-%{release}
Requires:%{name}-DAQ-LogicLevel = %{version}-%{release}
Requires:%{name}-DAQ-System = %{version}-%{release}
Requires:%{name}-DAQ-BlockCalc = %{version}-%{release}
Requires:%{name}-DAQ-Gate = %{version}-%{release}

Requires:%{name}-Protocol-HTTP = %{version}-%{release}
Requires:%{name}-Protocol-SelfSystem = %{version}-%{release}

Requires:%{name}-Transport-Sockets = %{version}-%{release}
Requires:%{name}-Transport-SSL = %{version}-%{release}
Requires:%{name}-Transport-Serial = %{version}-%{release}

%if 0%{?with_qtstarter}
Requires:%{name}-UI-QTStarter = %{version}-%{release}
Requires:%{name}-UI-QTCfg = %{version}-%{release}
Requires:%{name}-UI-QTVision = %{version}-%{release}
%endif

Requires:%{name}-UI-WebCfg = %{version}-%{release}
Requires:%{name}-UI-WebCfgd = %{version}-%{release}
Requires:%{name}-UI-WebVision = %{version}-%{release}

%description demo
The %{name}-demo package includes demo data bases and configs.
For start use command <openscada_demo>. For access use account
"root" and password "openscada" or account "user" without password.
%description demo -l ru_RU.UTF8
Пакет %{name}-demo включает демонстрационные базы данных и конфигурации.
Для старта используйте команду <openscada_demo>. Для доступа используйте запись
"root" и пароль "openscada" или запись "user" без пароля.
%description demo -l uk_UA.UTF8
Пакет %{name}-demo включає демонстраційні бази даних та конфігурації. Для
старту використовуйте команду <openscada_demo>. Для доступу використовуйте
запис "root" та пароль "openscada" або запис "user" без пароля.
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

%clean
%{__rm} -rf %{buildroot}

%files
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
%{_initrddir}/openscadad
%{_bindir}/openscada
%{_bindir}/openscada_start
%doc README README_ru COPYING ChangeLog
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

%lang(de) %{_datadir}/locale/de/LC_MESSAGES/*
%lang(ru) %{_datadir}/locale/ru/LC_MESSAGES/*
%lang(uk) %{_datadir}/locale/uk/LC_MESSAGES/*
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
