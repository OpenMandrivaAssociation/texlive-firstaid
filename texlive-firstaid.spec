%global tl_name firstaid
%global tl_revision 79234

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	First aid for external LaTeX files and packages that need updating
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/required/firstaid
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/firstaid.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/firstaid.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/firstaid.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package contains some first aid for LaTeX packages or classes that
require updates because of internal changes to the LaTeX kernel that are
not yet reflected in the package's or class's code. The file
latex2e-first-aid-for-external-files.ltx provided by this package is
meant to be loaded during format generation and not by the user.

