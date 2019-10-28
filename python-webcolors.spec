#
# Conditional build:
%bcond_without	python2	# CPython 2.x module
%bcond_without	python3	# CPython 3.x module
%bcond_without	doc	# Sphinx documentation
%bcond_without	tests	# unit tests

%define 	module	webcolors
Summary:	Library for working with sRGB color specifications as used in HTML and CSS
Summary(pl.UTF-8):	Biblioteka do pracy z definicjami kolorów sRGB używanymi w formatach HTML i CSS
Name:		python-%{module}
Version:	1.10
Release:	2
License:	BSD
Group:		Libraries/Python
#Source0Download: https://github.com/ubernostrum/webcolors/releases
Source0:	https://github.com/ubernostrum/webcolors/archive/%{version}/%{module}-%{version}.tar.gz
# Source0-md5:	195e37e745a77609aca47ea22b01d8b1
URL:		https://github.com/ubernostrum/webcolors
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
%if %{with tests}
BuildRequires:	python-six
%endif
%endif
%if %{with python3}
Requires:	python3-modules >= 1:3.5
%if %{with tests}
BuildRequires:	python3-six
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with doc}
BuildRequires:	python3-sphinx_rtd_theme
BuildRequires:	sphinx-pdg
%endif
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A library for working with color names and color value formats defined
by the HTML and CSS specifications for use in documents on the Web.

Support is included for the following formats (RGB colorspace only;
conversion to/from HSL can be handled by the colorsys module in the
Python standard library):
- Specification-defined color names
- Six-digit hexadecimal
- Three-digit hexadecimal
- Integer rgb() triplet
- Percentage rgb() triple

%description -l pl.UTF-8
Biblioteka do pracy z nazwami kolorów oraz formatami wartości kolorów
określonymi w specyfikacjach HTML i CSS, przeznaczonych do użycia w
dokumentach WWW.

Obsługiwane są następujące formaty (tylko przestrzeń nazw RGB;
konwersję do/z HSL można uzyskać korzystając z modułu colorsys
biblioteki standardowej Pythona):
- nazwy kolorów określone w specyfikacji
- sześciocyfrowe wartości szesnastkowe
- trzycyfrowe wartości szesnastkowe
- trójki całkowite rgb()
- trójki procentowe rgb()

%package -n python3-%{module}
Summary:	Library for working with sRGB color specifications as used in HTML and CSS
Summary(pl.UTF-8):	Biblioteka do pracy z definicjami kolorów sRGB używanymi w formatach HTML i CSS
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.5

%description -n python3-%{module}
A library for working with color names and color value formats defined
by the HTML and CSS specifications for use in documents on the Web.

Support is included for the following formats (RGB colorspace only;
conversion to/from HSL can be handled by the colorsys module in the
Python standard library):
- Specification-defined color names
- Six-digit hexadecimal
- Three-digit hexadecimal
- Integer rgb() triplet
- Percentage rgb() triple

%description -n python3-%{module} -l pl.UTF-8
Biblioteka do pracy z nazwami kolorów oraz formatami wartości kolorów
określonymi w specyfikacjach HTML i CSS, przeznaczonych do użycia w
dokumentach WWW.

Obsługiwane są następujące formaty (tylko przestrzeń nazw RGB;
konwersję do/z HSL można uzyskać korzystając z modułu colorsys
biblioteki standardowej Pythona):
- nazwy kolorów określone w specyfikacji
- sześciocyfrowe wartości szesnastkowe
- trzycyfrowe wartości szesnastkowe
- trójki całkowite rgb()
- trójki procentowe rgb()

%package apidocs
Summary:	Documentation for Python webcolors module
Summary(pl.UTF-8):	Dokumentacja do modułu Pythona webcolors
Group:		Documentation

%description apidocs
Documentation for Python webcolors module.

%description apidocs -l pl.UTF-8
Dokumentacja do modułu Pythona webcolors.

%prep
%setup -q -n %{module}-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
PYTHONPATH=$(pwd)/build-2/lib \
%{__python} -m unittest discover -s tests
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
PYTHONPATH=$(pwd)/build-3/lib \
%{__python3} -m unittest discover -s tests
%endif
%endif

%if %{with doc}
%{__make} -C docs html \
	SPHINXBUILD=sphinx-build-3
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py_sitescriptdir}/webcolors.py[co]
%{py_sitescriptdir}/webcolors-%{version}-*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py3_sitescriptdir}/webcolors.py
%{py3_sitescriptdir}/__pycache__/webcolors.cpython-*.py[co]
%{py3_sitescriptdir}/webcolors-%{version}-*.egg-info
%endif

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/_build/html/{_static,*.html,*.js}
%endif
