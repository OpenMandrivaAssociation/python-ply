%define	module ply

Summary:	Python Lex-Yacc
Name:		python-ply
Version:	3.9
Release:	1
License:	BSD
Group:		Development/Python
URL:		http://www.dabeaz.com/%{module}/
Source0:	http://www.dabeaz.com/%{module}/%{module}-%{version}.tar.gz
BuildArch:	noarch

BuildRequires:	pkgconfig(python2)
BuildRequires:	pkgconfig(python3)

%description
PLY is an implementation of lex and yacc parsing tools for Python.

In a nutshell, PLY is nothing more than a straightforward lex/yacc
implementation. Here is a list of its essential features:

 * It's implemented entirely in Python.
 * It uses LR-parsing which is reasonably efficient and well suited
   for larger grammars.
 * PLY provides most of the standard lex/yacc features including support
   for empty productions, precedence rules, error recovery, and support
   for ambiguous grammars.
 * PLY is straightforward to use and provides very extensive error checking.
 * PLY doesn't try to do anything more or less than provide the basic
   lex/yacc functionality. In other words, it's not a large parsing
   framework or a component of some larger system.

The original version of PLY was developed in 2001 for use in an
Introduction to Compilers course where students used it to build a
compiler for a simple Pascal-like language. Because of its use in an
instructional setting, a lot of work went into providing extensive
error checking. In addition, this experience was used to sort out
common usability problems. Since then, a variety of incremental
improvements have been made to the system. PLY-3.0 adds support for
Python 3.0 and gives PLY's internals a much needed overhaul.

%files -f python2/FILELIST
%doc python2/CHANGES python2/README.md python2/TODO python2/doc python2/example python2/test

#----------------------------------------------------------------------------

%package -n	python3-%{module}
Summary:	Python 2.x version of the PLY lex/yacc implementation
Group:		Development/Python

%description -n	python3-%{module}
PLY is an implementation of lex and yacc parsing tools for Python.

In a nutshell, PLY is nothing more than a straightforward lex/yacc
implementation. Here is a list of its essential features:

 * It's implemented entirely in Python.
 * It uses LR-parsing which is reasonably efficient and well suited
   for larger grammars.
 * PLY provides most of the standard lex/yacc features including support
   for empty productions, precedence rules, error recovery, and support
   for ambiguous grammars.
 * PLY is straightforward to use and provides very extensive error checking.
 * PLY doesn't try to do anything more or less than provide the basic
   lex/yacc functionality. In other words, it's not a large parsing
   framework or a component of some larger system.

The original version of PLY was developed in 2001 for use in an
Introduction to Compilers course where students used it to build a
compiler for a simple Pascal-like language. Because of its use in an
instructional setting, a lot of work went into providing extensive
error checking. In addition, this experience was used to sort out
common usability problems. Since then, a variety of incremental
improvements have been made to the system. PLY-3.0 adds support for
Python 3.0 and gives PLY's internals a much needed overhaul.

Python 3.x version of PLY.

%files -n python3-%{module} -f python3/FILELIST
%doc python3/CHANGES python3/README.md python3/TODO python3/doc python3/example python3/test

#----------------------------------------------------------------------------

%prep
%setup -q -n %{module}-%{version}
# fix file-not-utf8 warning
iconv -f iso8859-1 -t utf8 CHANGES > CHANGES.tmp
touch -r CHANGES CHANGES.tmp
mv -f CHANGES.tmp CHANGES

# set python2 and python3 branch
mkdir python2
mv `ls |grep -v python2` python2
cp -a python2 python3

# fix wrong-script-interpreter
sed -i "s|#!/usr/local/bin/python|#!%{__python}|"  python2/example/yply/yply.py
sed -i "s|#!/usr/local/bin/python|#!%{__python3}|" python3/example/yply/yply.py

sed -i "s|#!/usr/local/bin/python|#!%{__python}|"  python2/doc/makedoc.py
sed -i "s|#!/usr/local/bin/python|#!%{__python3}|" python3/doc/makedoc.py

%build
# build python2 module
pushd python2
%{__python} setup.py build
popd

# build python3 module
pushd python3
%{__python3} setup.py build
popd

%install
# install python2 module
pushd python2
%{__python} setup.py install --root=%{buildroot} --record=FILELIST

# remove *.pyc files from FILELIST
%__sed -i '/\\*.pyc$/d' FILELIST
popd

# install python3 module
pushd python3
%{__python3} setup.py install --root=%{buildroot} --record=FILELIST

# remove *.pyc files from FILELIST
%__sed -i '/\\*.pyc$/d' FILELIST
popd

%changelog
* Wed Apr 20 2011 Paulo Andrade <pcpa@mandriva.com.br> 3.4-1mdv2011.0
+ Revision: 656088
- Update to latest upstream release

* Sat Oct 30 2010 Shlomi Fish <shlomif@mandriva.org> 3.3-2mdv2011.0
+ Revision: 590565
- New release - rebuild for python 2.7

* Sun Jan 10 2010 Guillaume Rousse <guillomovitch@mandriva.org> 3.3-1mdv2010.1
+ Revision: 489357
- new version

* Tue Jun 09 2009 Guillaume Rousse <guillomovitch@mandriva.org> 3.1-1mdv2010.0
+ Revision: 384253
- update to new version 3.1

* Sat Jan 03 2009 Funda Wang <fwang@mandriva.org> 2.5-2mdv2009.1
+ Revision: 323927
- clean spec

* Sat Nov 22 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.5-1mdv2009.1
+ Revision: 305847
- update to new version 2.5

* Fri Aug 01 2008 Thierry Vignaud <tv@mandriva.org> 2.3-4mdv2009.0
+ Revision: 259742
- rebuild

* Fri Jul 25 2008 Thierry Vignaud <tv@mandriva.org> 2.3-3mdv2009.0
+ Revision: 247588
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 2.3-1mdv2008.1
+ Revision: 136456
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Fri Feb 23 2007 Gaëtan Lehmann <glehmann@mandriva.org> 2.3-1mdv2007.0
+ Revision: 124895
- 2.3

* Thu Nov 30 2006 Gaëtan Lehmann <glehmann@mandriva.org> 2.2-1mdv2007.1
+ Revision: 88998
- sync sources
- 2.2
  drop patch 1
- 1.8
- Import python-ply

* Fri May 26 2006 Gaetan Lehmann <gaetan.lehmann@jouy.inra.fr> 1.7-1mdv2007.0
- New release 1.7
- update url

* Wed Apr 26 2006 Nicolas L�cureuil <neoclust@mandriva.org> 1.5-3mdk
- Add BuildRequires
- use mkrel

* Sun Dec 05 2004 Michael Scherer <misc@mandrake.org> 1.5-2mdk
- Rebuild for new python

* Wed Sep 01 2004 Lenny Cartier <lenny@mandrakesoft.com> 1.5-1mdk
- from Gaetan Lehmann <glehmann@netcourrier.com> :
	- Create package from scratch for mandrake system

