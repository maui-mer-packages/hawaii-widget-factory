# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.27
# 

Name:       hawaii-widget-factory

# >> macros
# << macros

Summary:    Widget styles showcase
Version:    0.2.0.1.20140101.191d077
Release:    1
Group:      Applications/System
License:    BSD
URL:        https://github.com/mauios/hawaii-widget-factory.git
Source0:    hawaii-widget-factory-%{version}.tar.xz
Source100:  hawaii-widget-factory.yaml
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  cmake

%description
Showcase tool for testing new Qt and QtQuick Controls styles.

%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
cd upstream
# << build pre

%cmake .  \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DCMAKE_INSTALL_PREFIX=/usr

make %{?_smp_mflags}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
cd upstream
# << install pre
%make_install

# >> install post
# << install post

%files
%defattr(-,root,root,-)
%{_bindir}/widget-factory
# >> files
# << files
