%define	oname	geomcfly

Summary:	Geolocalized Metalinks created on the Fly
Name:		python-%{oname}
Version:	0.8.1
Release:	%mkrel 2
Source0:	%{oname}-%{version}.tar.gz
URL:		http://geomcfly.sourceforge.net/
License:	GPLv2+
Group:		Development/Python
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch
Requires:	python-geoip python-metalink

%description
This module is for creation of metalinks from a list of mirrors with their
preference relative to clients' geographical location.

While it's primary target of use is the Mandriva Linux distribution and
downloading of it's packages, it aims to be written in a generic and portable
way making it usable for other purposes as well.

%prep
%setup -q -n %{oname}-%{version}

%build

%install
rm -rf %{buildroot}
install -m644 %{oname}.py -D %{buildroot}%{python_sitelib}/%{oname}.py
install -m755 %{oname}.py.cgi -D %{buildroot}/var/www/cgi-bin/%{oname}.py.cgi
install -d %{buildroot}%{_localstatedir}/%{oname}
install -d %{buildroot}/var/run/%{oname}
touch %{buildroot}/var/run/%{oname}/lock

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{python_sitelib}/%{oname}.py
/var/www/cgi-bin/%{oname}.py.cgi
%attr(-,apache,apache) %{_localstatedir}/%{oname}
%attr(-,apache,apache) /var/run/%{oname}/lock
%ghost /var/run/%{oname}/lock

