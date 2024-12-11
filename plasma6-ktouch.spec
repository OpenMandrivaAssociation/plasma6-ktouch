%define git 20240218
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
%define stable %([ "$(echo %{version} |cut -d. -f3)" -ge 70 ] && echo -n un; echo -n stable)

Summary:	A program for learning touch typing
Name:		plasma6-ktouch
Version:	24.11.90
Release:	%{?git:0.%{git}.}1
License:	GPLv2+ and GFDL
Group:		Graphical desktop/KDE
Url:		https://edu.kde.org/ktouch
%if 0%{?git:1}
Source0:	https://invent.kde.org/education/ktouch/-/archive/%{gitbranch}/ktouch-%{gitbranchd}.tar.bz2#/ktouch-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/ktouch-%{version}.tar.xz
%endif
BuildRequires:	pkgconfig(xkbfile)
BuildRequires:	pkgconfig(xcb-xkb)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xcb)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6Network)
BuildRequires:	cmake(Qt6Qml)
BuildRequires:	cmake(Qt6Quick)
BuildRequires:	cmake(Qt6QuickWidgets)
BuildRequires:	cmake(Qt6Sql)
BuildRequires:	cmake(Qt6Test)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6Xml)
BuildRequires:	cmake(Qt6QuickControls2)
BuildRequires:	cmake(KF6Completion)
BuildRequires:	cmake(KF6ConfigWidgets)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6IconThemes)
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF6Declarative)
BuildRequires:	cmake(KF6DocTools)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6ItemViews)
BuildRequires:	cmake(KF6KCMUtils)
BuildRequires:	cmake(KF6TextWidgets)
BuildRequires:	cmake(KF6WidgetsAddons)
BuildRequires:	cmake(KF6WindowSystem)
BuildRequires:	cmake(KF6XmlGui)
Requires:	kqtquickcharts

%description
KTouch is a program for learning touch typing. KTouch is a way to learn
to type on a keyboard quickly and correctly. Every finger has its place
on the keyboard with associated keys to press.

KTouch helps you learn to touch typing by providing you with something
to write. KTouch can also help you to remember what fingers to use.

%files -f ktouch.lang
%{_datadir}/applications/org.kde.ktouch.desktop
%{_datadir}/ktouch
%{_bindir}/ktouch
%{_datadir}/metainfo/*.xml
%{_datadir}/config.kcfg/ktouch.kcfg
%{_iconsdir}/*/*/apps/ktouch.*
%doc %{_mandir}/man1/ktouch.1.*

#----------------------------------------------------------------------

%prep
%autosetup -p1 -n ktouch-%{?git:%{gitbranchd}}%{!?git:%{version}}

%build
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja
%ninja

%install
%ninja_install -C build
%find_lang ktouch --with-html --with-man
