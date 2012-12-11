Summary:	Simple DVD mastering GUI
Name:		tkdvd
Version:	4.0.9
Release:	%mkrel 2
License:	GPLv2+
Group:		Archiving/Cd burning
URL:		http://regis.damongeot.free.fr/tkdvd/
Source0:	http://regis.damongeot.free.fr/tkdvd/dl/%{name}-%{version}.tar.gz
BuildRequires:	imagemagick
# For macros
BuildRequires:	tcl-devel
Requires:	dvd+rw-tools tk tcl
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-buildroot

%description
TkDVD is a GUI for growisofs which is a part of dvd+rw-tools.  It allows
burnning DVD+R/RW, -R/W and DVD+R DL easily.

Features:
    * View the current command line passed to growisofs with options and
      file listing
    * Burn DVD from iso images
    * Create ISO images from files
    * Can overburn DVD
    * Support multi-sessions DVD
    * Add/delete/exclude file/directories and show current used space
    * can keep directory structure
    * options to choose iso9660 filesystem extension (like Joliet or
      RockRidge extensions)
    * Prevent burning if used space > DVD+R/RW capacity
    * show output of growisofs/mkisofs to view burned % and estimated
      remaining time

%prep
%setup -q -n %{name}
chmod 755 TkDVD.sh
chmod 644 icons/*.*
chmod 644 src/*.tcl
perl -p -i -e 's|\$\{source_directory\}|%{tcl_sitelib}/%{name}||g' TkDVD.sh src/*

%install
rm -fr %{buildroot}
mkdir -p %{buildroot}%{tcl_sitelib}/%{name}
cp TkDVD.sh %{buildroot}%{tcl_sitelib}/%{name}
cp -r src %{buildroot}%{tcl_sitelib}/%{name}
mkdir -p %{buildroot}%{_bindir}
ln -sf %{tcl_sitelib}/%{name}/TkDVD.sh %{buildroot}%{_bindir}/%{name}

#menu

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Name=TkDVD
Comment=%{summary}
Exec=%{_bindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=DiscBurning;Archiving;
EOF

#icons
mkdir -p %{buildroot}%{_iconsdir}/hicolor/{16x16,32x32,48x48}/apps
cp icons/%{name}-48.png %{buildroot}%{_iconsdir}/hicolor/48x48/apps/%{name}.png
cp icons/%{name}-32.png %{buildroot}%{_iconsdir}/hicolor/32x32/apps/%{name}.png
convert -size 16x16 icons/%{name}-48.png %{buildroot}%{_iconsdir}/hicolor/16x16/apps/%{name}.png

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post
%{update_menus}
%update_icon_cache hicolor
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%clean_icon_cache hicolor
%endif

%files
%defattr(-,root,root)
%doc ChangeLog FAQ README TODO
%{_bindir}/%{name}
%{tcl_sitelib}/%{name}
%{_datadir}/applications/*
%{_iconsdir}/hicolor/*/apps/%{name}.png


%changelog
* Sun Sep 20 2009 Thierry Vignaud <tvignaud@mandriva.com> 4.0.9-2mdv2010.0
+ Revision: 445481
- rebuild

* Fri Dec 05 2008 Adam Williamson <awilliamson@mandriva.org> 4.0.9-1mdv2009.1
+ Revision: 310820
- buildrequires tcl-devel (for macros)
- move to new location per policy
- new release 4.0.9

* Fri Aug 08 2008 Thierry Vignaud <tvignaud@mandriva.com> 4.0.8-2mdv2009.0
+ Revision: 269435
- rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Thu Apr 17 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 4.0.8-1mdv2009.0
+ Revision: 195384
- new version
- spec file clean
- put icons into f.do compiliant directory

  + Thierry Vignaud <tvignaud@mandriva.com>
    - drop old menu
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Fri Oct 26 2007 Jérôme Soyer <saispo@mandriva.org> 4.0.7-1mdv2008.1
+ Revision: 102336
- New release 4.0.7


* Mon Mar 12 2007 Jérôme Soyer <saispo@mandriva.org> 4.0.6-1mdv2007.1
+ Revision: 141635
- New version 4.0.6

* Sun Feb 18 2007 Jérôme Soyer <saispo@mandriva.org> 4.0.5-1mdv2007.1
+ Revision: 122264
- New release 4.0.5

* Tue Nov 14 2006 Lenny Cartier <lenny@mandriva.com> 4.0.4-1mdv2007.1
+ Revision: 84097
- Fix deletion of directories
- Update to 4.0.4
- Import tkdvd

* Thu Aug 17 2006 Austin Acton <austin@mandriva.org> 4.0.3-2mdv2007.0
- oops, fix menu

* Mon Aug 14 2006 Austin Acton <austin@mandriva.org> 4.0.3-1mdv2007.0
- 4.0.3
- xdg menu

* Tue Jun 27 2006 Austin Acton <austin@mandriva.org> 4.0.0-1mdk
- New release 4.0.0

* Mon Jan 16 2006 Lenny Cartier <lenny@mandriva.com> 3.10.1-1mdk
- 3.10.1

* Fri Dec 30 2005 Austin Acton <austin@mandriva.org> 3.10.0-1mdk
- New release 3.10.0

* Fri Nov 04 2005 Austin Acton <austin@mandriva.org> 3.8.4-1mdk
- New release 3.8.4

* Mon Oct 10 2005 Austin Acton <austin@mandriva.org> 3.8.2-1mdk
- New release 3.8.2

* Mon Aug 22 2005 Austin Acton <austin@mandriva.org> 3.8-1mdk
- New release 3.8

* Sat Aug 13 2005 Austin Acton <austin@mandriva.org> 3.7-1mdk
- New release 3.7

* Mon Jul 04 2005 Austin Acton <austin@mandriva.org> 3.5-1mdk
- New release 3.5

* Sun Feb 06 2005 Austin Acton <austin@mandrake.org> 3.4-1mdk
- 3.4

* Wed Jan 19 2005 Austin Acton <austin@mandrake.org> 3.2-1mdk
- 3.2

* Thu Jan 13 2005 Austin Acton <austin@mandrake.org> 3.1-1mdk
- initial package

