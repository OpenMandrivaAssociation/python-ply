Name:		python-ply
Version:	3.4
Release:	2
Group:		Development/Python
License:	BSD-like
Summary:	Python Lex-Yacc
Source:		http://www.dabeaz.com/ply/ply-%{version}.tar.gz
URL:		http://www.dabeaz.com/ply/
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

%files
%doc CHANGES README TODO doc example test
%py_puresitedir/ply
%py_puresitedir/*.egg-info
