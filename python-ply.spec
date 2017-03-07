Name:		python-ply
Version:	3.10
Release:	1
Group:		Development/Python
License:	BSD-like
Summary:	Python Lex-Yacc
Source0:	http://www.dabeaz.com/ply/ply-%{version}.tar.gz
URL:		http://www.dabeaz.com/ply/
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

%package -n	python2-ply
Summary:	Python 2.x version of the PLY lex/yacc implementation
Group:		Development/Python
BuildRequires:	pkgconfig(python2)

%description -n	python2-ply
Python 2.x version of ply.

PLY is an implementation of lex and yacc parsing tools for Python.

%prep
%setup -q -n ply-%{version}
mkdir python3
mv `ls |grep -v python3` python3
cp -a python3 python2

%build
cd python3
python setup.py build

cd ../python2
%{__python2} setup.py build

%install
cd python3
%{__python} setup.py install --root=%{buildroot}

cd ../python2
%{__python2} setup.py install --root=%{buildroot}

%files
%doc python3/CHANGES python3/TODO python3/doc python3/example python3/test
%py_puresitedir/ply
%py_puresitedir/*.egg-info

%files -n python2-ply
%doc python2/CHANGES python2/TODO python2/doc python2/example python2/test
%py2_puresitedir/ply
%py2_puresitedir/*.egg-info
