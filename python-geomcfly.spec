%define	oname	geomcfly

Summary:	Geolocalized Metalinks created on the Fly
Name:		python-%{oname}
Version:	0.8.1
Release:	7
Source0:	%{oname}-%{version}.tar.gz
URL:		http://geomcfly.sourceforge.net/
License:	GPLv2+
Group:		Development/Python
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
install -m644 %{oname}.py -D %{buildroot}%{python_sitelib}/%{oname}.py
install -m755 %{oname}.py.cgi -D %{buildroot}/var/www/cgi-bin/%{oname}.py.cgi
install -d %{buildroot}%{_localstatedir}/lib/%{oname}
install -d %{buildroot}/var/run/%{oname}
touch %{buildroot}/var/run/%{oname}/lock

%files
%{python_sitelib}/%{oname}.py
/var/www/cgi-bin/%{oname}.py.cgi
%attr(-,apache,apache) %{_localstatedir}/lib/%{oname}
%ghost %attr(-,apache,apache) /var/run/%{oname}/lock



%changelog
* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.8.1-6mdv2010.0
+ Revision: 430844
- rebuild

* Fri Aug 01 2008 Thierry Vignaud <tv@mandriva.org> 0.8.1-5mdv2009.0
+ Revision: 259615
- rebuild

* Fri Jul 25 2008 Thierry Vignaud <tv@mandriva.org> 0.8.1-4mdv2009.0
+ Revision: 247420
- rebuild

  + Pixel <pixel@mandriva.com>
    - adapt to %%_localstatedir now being /var instead of /var/lib (#22312)

* Fri Feb 01 2008 Per Ã˜yvind Karlsen <peroyvind@mandriva.org> 0.8.1-2mdv2008.1
+ Revision: 160963
- rebuild since rpm 4.4.2.2 previously hosed python macros

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - wrap too long description

* Wed Nov 28 2007 Per Ã˜yvind Karlsen <peroyvind@mandriva.org> 0.8.1-1mdv2008.1
+ Revision: 113597
- import python-geomcfly


* Wed Nov 28 2007 Per Øyvind Karlsen <pkarlsen@mandriva.com> 0.8.1-1mdv2008.1
- 0.8.1

* Wed Nov 27 2007 Per Øyvind Karlsen <pkarlsen@mandriva.com> 0.8-1mdv2008.1
- Initial release
