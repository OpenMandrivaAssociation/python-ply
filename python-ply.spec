Name:		python-ply
Version:	3.4
Release:	%mkrel 1
Group:		Development/Python
License:	BSD-like
Summary:	Python Lex-Yacc
Source:		http://www.dabeaz.com/ply/ply-%{version}.tar.gz
URL:		http://www.dabeaz.com/ply/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch
BuildRequires:	python-devel

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

%prep
%setup -q -n ply-%{version}

%build
%__python setup.py build

%install
%__python setup.py install --root=%{buildroot}

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc CHANGES README TODO doc example test
%py_puresitedir/ply
%py_puresitedir/*.egg-info


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

