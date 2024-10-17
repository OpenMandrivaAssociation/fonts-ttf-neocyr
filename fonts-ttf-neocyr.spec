%define pkgname neocyr

Summary:	Decorative typeface
Name:		fonts-ttf-neocyr
Version:	20110622
Release:	2
License:	OFL
Group:		System/Fonts/True type
URL:		https://openfontlibrary.org/font/neocyr
Source0:	%{pkgname}.zip
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch
BuildRequires:	freetype-tools
BuildRequires:	dos2unix

%description
Neocyr is a decorative typeface that includes Latin and Cyrillic characters.

%prep
%setup -q -c -n %{pkgname}-%{version}
dos2unix *.txt

%build

%install
%__rm -rf %{buildroot}

%__mkdir_p %{buildroot}%{_xfontdir}/TTF/neocyr

%__install -m 644 ttf/*.ttf %{buildroot}%{_xfontdir}/TTF/neocyr
ttmkfdir %{buildroot}%{_xfontdir}/TTF/neocyr -o %{buildroot}%{_xfontdir}/TTF/neocyr/fonts.dir
%__ln_s fonts.dir %{buildroot}%{_xfontdir}/TTF/neocyr/fonts.scale

%__mkdir_p %{buildroot}%_sysconfdir/X11/fontpath.d/
%__ln_s ../../..%{_xfontdir}/TTF/neocyr \
    %{buildroot}%_sysconfdir/X11/fontpath.d/ttf-neocyr:pri=50

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc FONTLOG.txt OFL.txt OFL-FAQ.txt
%dir %{_xfontdir}/TTF/neocyr
%{_xfontdir}/TTF/neocyr/*.ttf
%verify(not mtime) %{_datadir}/fonts/TTF/neocyr/fonts.dir
%{_xfontdir}/TTF/neocyr/fonts.scale
%{_sysconfdir}/X11/fontpath.d/ttf-neocyr:pri=50


%changelog
* Fri Dec 09 2011 Dmitry Mikhirev <dmikhirev@mandriva.org> 20110622-1mdv2012.0
+ Revision: 739493
- Update to 2011-06-22

* Fri Jul 22 2011 Sergey Zhemoitel <serg@mandriva.org> 1.0-1
+ Revision: 690989
- imported package fonts-ttf-neocyr

