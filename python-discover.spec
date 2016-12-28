#
# Conditional build:
%bcond_without	python2	# CPython 2.x module
%bcond_without	python3	# CPython 3.x module

Summary:	Test discovery for unittest (backport from Python 2.7)
Summary(pl.UTF-8):	Wykrywanie testów dla modułu unittest (backport z Pythona 2.7)
Name:		python-discover
Version:	0.4.0
Release:	2
License:	BSD
Group:		Development/Languages/Python
#Source0Download: https://pypi.python.org/simple/discover/
Source0:	https://pypi.python.org/packages/source/d/discover/discover-%{version}.tar.gz
# Source0-md5:	30bb643af4f5ea47fff572b5c346207d
URL:		https://pypi.python.org/pypi/discover/
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-devel >= 1:2.4
%endif
%if %{with python3}
BuildRequires:	python3-devel >= 1:3.2
%endif
Requires:	python-modules >= 1:2.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is the test discovery mechanism and ``load_tests`` protocol for
unittest backported from Python 2.7 to work with Python 2.4 or more
recent (including Python 3).

%description -l pl.UTF-8
Ten moduł zawiera mechanizm znajdowania testów oraz protokół
"load_tests" dla modułu unittest przeniesiony z Pythona 2.7 tak, aby
działał z Pythonem 2.4 i nowszymi (włącznie z Pythonem 3).

%package -n python3-discover
Summary:	Test discovery for unittest (backport from Python 2.7)
Summary(pl.UTF-8):	Wykrywanie testów dla modułu unittest (backport z Pythona 2.7)
Group:		Development/Languages/Python
Requires:	python3-modules >= 1:3.2

%description -n python3-discover
This is the test discovery mechanism and ``load_tests`` protocol for
unittest backported from Python 2.7 to work with Python 2.4 or more
recent (including Python 3).

%description -n python3-discover -l pl.UTF-8
Ten moduł zawiera mechanizm znajdowania testów oraz protokół
"load_tests" dla modułu unittest przeniesiony z Pythona 2.7 tak, aby
działał z Pythonem 2.4 i nowszymi (włącznie z Pythonem 3).

%prep
%setup -q -n discover-%{version}

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%{__mv} $RPM_BUILD_ROOT%{_bindir}/discover{,-2}
%py_postclean
%endif

%if %{with python3}
%py3_install

%{__mv} $RPM_BUILD_ROOT%{_bindir}/discover{,-3}
%endif

%if %{with python2}
ln -sf discover-2 $RPM_BUILD_ROOT%{_bindir}/discover
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc README.txt
%attr(755,root,root) %{_bindir}/discover
%attr(755,root,root) %{_bindir}/discover-2
%{py_sitescriptdir}/discover.py[co]
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/discover-%{version}-py*.egg-info
%endif
%endif

%if %{with python3}
%files -n python3-discover
%defattr(644,root,root,755)
%doc README.txt
%attr(755,root,root) %{_bindir}/discover-3
%{py3_sitescriptdir}/discover.py
%{py3_sitescriptdir}/__pycache__/discover.cpython-*.py[co]
%{py3_sitescriptdir}/discover-%{version}-py*.egg-info
%endif
