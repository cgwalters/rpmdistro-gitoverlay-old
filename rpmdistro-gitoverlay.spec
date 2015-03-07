Name:             rpmdistro-gitoverlay
Version:          2015.0
Release:          1%{?dist}
Summary:          Tool to maintain a layer of packages

Group:            Development/Languages
License:          LGPLv2+
URL:              https://github.com/cgwalters/rpmdistro-gitoverlay
# Generated via "git archive"
Source0:          %{name}-%{version}.tar.gz

BuildRequires:    autoconf automake libtool
BuildRequires:    PyYAML

Requires:         PyYAML
Requires:         git-core

%description
Maintain a layer of packages on top of a base distribution.

%prep
%autosetup -Sgit -q

%build
env NOCONFIGURE=1 ./autogen.sh
%configure --disable-silent-rules
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot} INSTALL="install -p -c"

%files
%{_bindir}/*
%{_libdir}/%{name}/
%{_datadir}/%{name}/
