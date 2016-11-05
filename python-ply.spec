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

BuildRequires:	pkgconfig(python3)
BuildRequires:	pkgconfig(python2)

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

%files -f python3/FILELIST
%doc python3/CHANGES python3/README.md python3/TODO python3/doc python3/example python3/test

#----------------------------------------------------------------------------

%package -n	python2-%{module}
Summary:	Python 2.x version of the PLY lex/yacc implementation
Group:		Development/Python
BuildRequires:	pkgconfig(python2)

%description -n	python2-%{module}
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

Python 2.x version of PLY.

%files -n python2-%{module} -f python2/FILELIST
%doc python2/CHANGES python2/README.md python2/TODO python2/doc python2/example python2/test

#----------------------------------------------------------------------------

%prep
%setup -q -n %{module}-%{version}
# fix file-not-utf8 warning
iconv -f iso8859-1 -t utf8 CHANGES > CHANGES.tmp
touch -r CHANGES CHANGES.tmp
mv -f CHANGES.tmp CHANGES

# set python2 and python3 branch
mkdir python3
mv `ls |grep -v python3` python3
cp -a python3 python2

# fix wrong-script-interpreter
sed -i "s|#!/usr/local/bin/python|#!%{__python}|"  python3/example/yply/yply.py
sed -i "s|#!/usr/local/bin/python|#!%{__python2}|" python2/example/yply/yply.py

sed -i "s|#!/usr/local/bin/python|#!%{__python}|"  python3/doc/makedoc.py
sed -i "s|#!/usr/local/bin/python|#!%{__python2}|"  python2/doc/makedoc.py

%build
# build python3 module
pushd python3
%{__python} setup.py build
popd

# build python2 module
pushd python2
%{__python2} setup.py build
popd

%install
# install python3 module
pushd python3
%{__python} setup.py install --root=%{buildroot} --record=FILELIST

# remove *.pyc files from FILELIST
%__sed -i '/\\*.pyc$/d' FILELIST
popd

# install python2 module
pushd python2
%{__python2} setup.py install --root=%{buildroot} --record=FILELIST

# remove *.pyc files from FILELIST
%__sed -i '/\\*.pyc$/d' FILELIST
popd

