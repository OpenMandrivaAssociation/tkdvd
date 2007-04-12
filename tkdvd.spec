%define name	tkdvd
%define version 4.0.6
%define release %mkrel 1

Name: 	 	%{name}
Summary: 	Simple DVD mastering GUI
Version: 	%{version}
Release: 	%{release}

Source:		http://regis.damongeot.free.fr/tkdvd/dl/%{name}-%{version}.tar.bz2
URL:		http://regis.damongeot.free.fr/tkdvd/
License:	GPL
Group:		Archiving/Cd burning
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	ImageMagick
Requires:	dvd+rw-tools tk tcl
BuildArch:	noarch

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
%setup -q -n %name
chmod 755 TkDVD.sh
chmod 644 icons/*.*
chmod 644 src/*.tcl
perl -p -i -e 's|\$\{source_directory\}|%{_datadir}/%name||g' TkDVD.sh src/*

%install
rm -fr %buildroot
mkdir -p %buildroot/%{_datadir}/%name
cp TkDVD.sh %buildroot/%{_datadir}/%name
cp -r src %buildroot/%{_datadir}/%name
mkdir -p %buildroot/%{_bindir}
ln -sf %{_datadir}/%name/TkDVD.sh %buildroot/%_bindir/%name

#menu
mkdir -p $RPM_BUILD_ROOT%{_menudir}
cat << EOF > $RPM_BUILD_ROOT%{_menudir}/%{name}
?package(%{name}): command="%{name}" icon="%{name}.png" needs="x11" title="TkDVD" longtitle="Simple DVD mastering GUI" section="System/Archiving/CD Burning" xdg="true"
EOF

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=TkDVD
Comment=%{summary}
Exec=%{_bindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=DiscBurning;Archiving;X-MandrivaLinux-Archiving-CDBurning;
EOF

#icons
mkdir -p $RPM_BUILD_ROOT/%_liconsdir
cp icons/%name-48.png $RPM_BUILD_ROOT/%_liconsdir/%name.png
mkdir -p $RPM_BUILD_ROOT/%_iconsdir
cp icons/%name-32.png $RPM_BUILD_ROOT/%_iconsdir/%name.png
mkdir -p $RPM_BUILD_ROOT/%_miconsdir
convert -size 16x16 icons/%name-48.png $RPM_BUILD_ROOT/%_miconsdir/%name.png

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_menus
		
%postun
%clean_menus

%files
%defattr(-,root,root)
%doc ChangeLog FAQ README TODO
%{_bindir}/%name
%{_datadir}/%name
%{_datadir}/applications/*
%{_menudir}/%name
%{_liconsdir}/%name.png
%{_iconsdir}/%name.png
%{_miconsdir}/%name.png


