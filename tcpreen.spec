Summary:	tcpreen - TCP stream monitor tool
Summary(pl):	tcpreen - narzędzie monitorujące strumienie TCP
Name:		tcpreen
Version:	1.4.2
Release:	1
License:	GPL v2
Group:		Applications/Networking
Source0:	http://dl.sourceforge.net/tcpreen/%{name}-%{version}.tar.bz2
# Source0-md5:	a0d846d3ee587a41bb0749c5f2227475
Patch0:		%{name}-words.patch
URL:		http://www.simphalempin.com/dev/tcpreen/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
tcpreen is a tool to monitor and analyse data transmitted between a
client and server via a TCP connection.

%description -l pl
tcpreen jest narzędziem do monitorowania i analizowania danych
przesyłanych między klientem a serwerem z użyciem połączenia TCP.

%prep
%setup -q
%patch0 -p1

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
