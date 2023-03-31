Name:		texlive-firstaid
Version:	64892
Release:	2
Summary:	First aid for external LaTeX files and packages that need updating
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/firstaid
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/firstaid.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/firstaid.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/firstaid.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package contains some first aid for LaTeX packages or
classes that require updates because of internal changes to the
LaTeX kernel that are not yet reflected in the package's or
class's code. The file latex2e-first-aid-for-external-files.ltx
provided by this package is meant to be loaded during format
generation and not by the user.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/firstaid
%{_texmfdistdir}/tex/latex/firstaid
%doc %{_texmfdistdir}/doc/latex/firstaid

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
