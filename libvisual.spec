%define smallversion 0.4

Name:           libvisual
Version:        0.4.0
Release:        9.1%{?dist}
Summary:        Abstraction library for audio visualisation plugins

Group:          Applications/Multimedia
License:        LGPLv2+
URL:            http://libvisual.sf.net
Source0:        http://dl.sf.net/libvisual/libvisual-0.4.0.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  xorg-x11-proto-devel

# https://bugzilla.redhat.com/show_bug.cgi?id=435771
Patch0:         libvisual-0.4.0-better-altivec-detection.patch
Patch1:         libvisual-0.4.0-inlinedefineconflict.patch


%description
Libvisual is an abstraction library that comes between applications and
audio visualisation plugins.

Often when it comes to audio visualisation plugins or programs that create
visuals they do depend on a player or something else, basically there is no
general framework that enable application developers to easy access cool
audio visualisation plugins. Libvisual wants to change this by providing
an interface towards plugins and applications, through this easy to use
interface applications can easily access plugins and since the drawing is
done by the application it also enables the developer to draw the visual
anywhere he wants.

%package        devel
Summary:        Development files for libvisual
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}

%description    devel
Libvisual is an abstraction library that comes between applications and
audio visualisation plugins.

This package contains the files needed to build an application with libvisual.

%prep
%setup -q
%patch0 -p1 -b .altivec-detection
%patch1 -p1 -b .inlinedefineconflict

%build
%ifarch i386
export CFLAGS="${RPM_OPT_FLAGS} -mmmx"
%endif
%configure
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name "*.la" -exec rm -f {} ';'

%find_lang %{name}-%{smallversion}


%clean
rm -rf $RPM_BUILD_ROOT


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files -f %{name}-%{smallversion}.lang
%defattr(-,root,root,-)
%doc AUTHORS COPYING ChangeLog NEWS README TODO
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root,-)
%doc README NEWS TODO AUTHORS
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/%{name}-%{smallversion}


%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 0.4.0-9.1
- Rebuilt for RHEL 6

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Mar 07 2009 Caolán McNamara <caolanm@redhat.com> - 0.4.0-8
- defining inline causes problems trying to build against libvisual headers, 
  e.g. libvisual-plugins

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Mar 11 2008 - Bastien Nocera <bnocera@redhat.com> - 0.4.0-6
- Better Altivec detection, code from David Woodhouse

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.4.0-5
- Autorebuild for GCC 4.3

* Sun Aug 26 2007 Aurelien Bompard <abompard@fedoraproject.org> 0.4.0-4
- fix license tag

* Wed Aug 30 2006 Aurelien Bompard <abompard@fedoraproject.org> 0.4.0-3
- rebuild

* Sat Jul 08 2006 Aurelien Bompard <abompard@fedoraproject.org> 0.4.0-2
- bump release

* Thu Jul 06 2006 Aurelien Bompard <abompard@fedoraproject.org> 0.4.0-1
- version 0.4.0
- drop Patch0 (applied upstream)

* Tue Feb 21 2006 Aurelien Bompard <gauret[AT]free.fr> 0.2.0-8
- fix dependency for modular X

* Tue Feb 21 2006 Aurelien Bompard <gauret[AT]free.fr> 0.2.0-7
- rebuild for FC5

* Wed Jun 15 2005 Aurelien Bompard <gauret[AT]free.fr> 0.2.0-6
- rebuild

* Wed Jun 15 2005 Aurelien Bompard <gauret[AT]free.fr> 0.2.0-5
- fix build for GCC4

* Thu Jun  9 2005 Michael Schwendt <mschwendt[AT]users.sf.net> 0.2.0-4
- use dist tag for all-arch-rebuild

* Thu Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net> 0.2.0-3
- rebuilt

* Mon Feb 14 2005 David Woodhouse <dwmw2@infradead.org> 0.2.0-2
- Fix bogus #if where #ifdef was meant

* Thu Feb 10 2005 Aurelien Bompard <gauret[AT]free.fr> 0.2.0-1
- version 0.2.0
- drop patch

* Sat Nov 27 2004 Aurelien Bompard <gauret[AT]free.fr> 0:0.1.7-0.fdr.1
- version 0.1.7

* Thu Oct 21 2004 Aurelien Bompard <gauret[AT]free.fr> 0:0.1.6-0.fdr.2
- Apply Adrian Reber's suggestions in bug 2182

* Tue Sep 28 2004 Aurelien Bompard <gauret[AT]free.fr> 0:0.1.6-0.fdr.1
- Initial RPM release.
