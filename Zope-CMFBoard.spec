%define		zope_subname	CMFBoard
Summary:	Portal discussion for Plone
Summary(pl.UTF-8):	Portal dyskusyjny dla Plone
Name:		Zope-%{zope_subname}
Version:	2.2.1
Release:	1
License:	GPL
Group:		Development/Tools
Source0:	http://dl.sourceforge.net/collective/%{zope_subname}-%{version}.tar.gz
# Source0-md5:	c9e758f81525e49a89871ba79af61588
URL:		http://www.cmfboard.org/
BuildRequires:	python
BuildRequires:	rpmbuild(macros) >= 1.268
Requires(post,postun):	/usr/sbin/installzopeproduct
%pyrequires_eq	python-modules
Requires:	Zope
Requires:	Zope-BTreeFolder2
Requires:	Zope-CMF
Requires:	Zope-CMFMessage
Requires:	Zope-CMFPlone >= 2.0
Requires:	Zope-PlacelessTranslationService
Requires:	Zope-PortalTransport
Requires:	Zope-archetypes >= 1.2.5
Requires:	python-Imaging
Requires:	python-PyXML
Conflicts:	CMF
Conflicts:	Plone
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Portal discussion for Plone.

%description -l pl.UTF-8
Portal dyskusyjny dla Plone.

%prep
%setup -q -n %{zope_subname}

%build
rm -rf skins/cmfboard/{personalize_form.pt,personalize_form.pt.properties}
rm -rf skins/cmfboard/fcMaillist/{register.py,validate_personalize.py,validate_registration.py}
rm -rf i18n/{build.bat,*.exe}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}

cp -af {Extensions,i18n,mailtemplates,skins,uihelpers,zpt,*.py,*.gif,version.txt} $RPM_BUILD_ROOT%{_datadir}/%{name}

%py_comp $RPM_BUILD_ROOT%{_datadir}/%{name}
%py_ocomp $RPM_BUILD_ROOT%{_datadir}/%{name}

# find $RPM_BUILD_ROOT -type f -name "*.py" -exec rm -rf {} \;;

%clean
rm -rf $RPM_BUILD_ROOT

%post
/usr/sbin/installzopeproduct %{_datadir}/%{name} %{zope_subname}
%service -q zope restart

%postun
if [ "$1" = "0" ]; then
	/usr/sbin/installzopeproduct -d %{zope_subname}
	%service -q zope restart
fi

%files
%defattr(644,root,root,755)
%doc docs/* CHANGES.txt CREDITS.txt README.txt TODO.txt BUGS.txt
%{_datadir}/%{name}
