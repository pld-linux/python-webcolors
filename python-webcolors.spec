%define 	module	webcolors
Summary:	A library for working with color names and color value formats defined by the HTML and CSS specifications for use in documents on the Web
Name:		python-%module
Version:	1.3.1
Release:	1
License:	BSD License
Group:		Development/Languages
URL:		http://www.bitbucket.org/ubernostrum/webcolors/overview/
Source0:	http://bitbucket.org/ubernostrum/%{module}/downloads/%{module}-%{version}.tar.gz
# Source0-md5:	aeb4f33be6c26ec7f76a78c2d88cfb0c
BuildRequires:	rpmbuild(macros) >= 1.219
BuildRequires:	sed >= 4.0
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

%prep
%setup -q -n %{module}-%{version}
%{__sed} -i -e 's/^from ez_setup/#from ez_setup/' setup.py
%{__sed} -i -e 's/^use_setuptools()/#use_setuptools()/' setup.py

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--optimize=2 \
	--skip-build \
	--root $RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{py_sitescriptdir}/%{module}*.py[co]
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/%{module}-%{version}-*.egg-info
%endif
