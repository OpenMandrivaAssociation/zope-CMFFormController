%define Product CMFFormController
%define product cmfformcontroller
%define name    zope-%{Product}
%define version 2.1.1
%define release %mkrel 3

%define zope_minver     2.6
%define zope_home       %{_prefix}/lib/zope
%define software_home   %{zope_home}/lib/python

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:    CMFFormController replaces the portal_form form validation mechanism from Plone
URL:        http://plone.org/products/%{product}
Source:     http://plone.org/products/%{product}/releases/%{version}/%{Product}-%{version}.tar.gz
License:    GPL
Group:      System/Servers
Requires:   zope >= %{zope_minver}
Requires:   zope-CMF >= 1.3
Epoch:      1
BuildArch:  noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
CMFFormController replaces the portal_form form validation
mechanism from Plone. It should work just fine in plain CMF as
well.

%prep
%setup -c -q

%build
# Not much, eh? :-)


%install
%{__rm} -rf %{buildroot}
%{__mkdir_p} %{buildroot}/%{software_home}/Products
%{__cp} -a * %{buildroot}%{software_home}/Products/


%clean
%{__rm} -rf %{buildroot}

%post
if [ "`%{_prefix}/bin/zopectl status`" != "daemon manager not running" ] ; then
        service zope restart
fi

%postun
if [ -f "%{_prefix}/bin/zopectl" ] && [ "`%{_prefix}/bin/zopectl status`" != "daemon manager not running" ] ; then
        service zope restart
fi

%files
%defattr(-,root,root)
%{software_home}/Products/*
