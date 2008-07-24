
Summary: Python Lex-Yacc
Name: python-ply
Version: 2.3
Release: %mkrel 3
License: LGPL
Group: Development/Python
Source0: http://www.dabeaz.com/ply/ply-%{version}.tar.bz2
URL: http://www.dabeaz.com/ply/
BuildRoot: %{_tmppath}/%{name}-buildroot
Requires: python
BuildRequires: python-devel
BuildArch: noarch

%description
PLY is yet another implementation of lex and yacc for Python. Although
several other parsing tools are available for Python, there are
several reasons why you might want to take a look at PLY:
- It uses LR-parsing which is reasonably efficient and well suited for
  larger grammars.
- PLY provides most of the standard lex/yacc features including
  support for empty productions, precedence rules, error recovery, and
  support for ambiguous grammars.
- PLY is extremely easy to use and provides very extensive error
  checking.

%prep
rm -rf $RPM_BUILD_ROOT

%setup -n ply-%{version}

%install
python setup.py install --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root,0755)
%doc CHANGES COPYING README TODO doc example test


