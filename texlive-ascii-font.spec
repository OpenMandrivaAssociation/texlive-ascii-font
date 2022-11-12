Name:		texlive-ascii-font
Version:	29989
Release:	1
Summary:	Use the ASCII "font" in LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/ascii
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ascii-font.r29989.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ascii-font.doc.r29989.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ascii-font.source.r29989.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides glyph and font access commands so that
LaTeX users can use the ASCII glyphs in their documents. The
ASCII font is encoded according to the IBM PC Code Page 437 C0
Graphics. This package replaces any early LaTeX 2.09 package
and "font" by R. Ramasubramanian and R.W.D. Nickalls.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/map/dvips/ascii-font/ascii.map
%{_texmfdistdir}/fonts/tfm/public/ascii-font/ASCII.tfm
%{_texmfdistdir}/fonts/type1/public/ascii-font/ASCII.pfb
%{_texmfdistdir}/tex/latex/ascii-font/ascii.sty
%doc %{_texmfdistdir}/doc/fonts/ascii-font/README.TEXLIVE
#- source
%doc %{_texmfdistdir}/source/fonts/ascii-font/ascii.dtx
%doc %{_texmfdistdir}/source/fonts/ascii-font/ascii.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc source %{buildroot}%{_texmfdistdir}
