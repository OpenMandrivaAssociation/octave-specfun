%global octpkg specfun

%global commit 8e53e97c2b1d7c5ef0c9ce5adc53a8c18f9a62b3

Summary:	Special functions for Octave
Name:		octave-%{octpkg}
Version:	1.1.0
Release:	1
# Use devlopment snapshot because last release is too old.
# hg clone http://hg.code.sf.net/p/octave/specfun octave-specfun
# rm -fr octave-specfun/{.hg,.hgignore}
# mv octave-specfun specfun-1.1.0
# tar cvzf specfun-1.1.0.tar.gz specfun-1.1.0/*
Source0:	http://downloads.sourceforge.net/octave/%{octpkg}-%{version}.tar.gz

License:	GPLv3+ and BSD
Group:		Sciences/Mathematics
Url:		https://octave.sourceforge.io/%{octpkg}/
BuildArch:	noarch

BuildRequires:	octave-devel >= 3.4.0

Requires:	octave(api) = %{octave_api}

Requires(post): octave
Requires(postun): octave

%description
Special functions including ellipitic functions, etc., for Octave.

This package is part of unmantained Octave-Forge collection.

%files
%license COPYING
%doc NEWS
%dir %{octpkgdir}
%{octpkgdir}/*

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{octpkg}-%{version}

# remove backup files
#find . -name \*~ -delete

# ellipj is now in Octave core
#rm -fr src

%build
%set_build_flags
%octave_pkg_build

%install
%octave_pkg_install

%check
%octave_pkg_check

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

