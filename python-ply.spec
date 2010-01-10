
Summary: Python Lex-Yacc
Name: python-ply
Version: 3.3
Release: %mkrel 1
License: LGPL
Group: Development/Python
Source0: http://www.dabeaz.com/ply/ply-%{version}.tar.bz2
URL: http://www.dabeaz.com/ply/
%py_requires -d
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}

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
%setup -qn ply-%{version}

%install
rm -fr %{buildroot}
python setup.py install --root=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc CHANGES README TODO doc example test
%python_sitelib/*.egg-info
%python_sitelib/ply
