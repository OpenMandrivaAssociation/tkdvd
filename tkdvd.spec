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
