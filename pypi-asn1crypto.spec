#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-asn1crypto
Version  : 1.5.1
Release  : 69
URL      : https://files.pythonhosted.org/packages/de/cf/d547feed25b5244fcb9392e288ff9fdc3280b10260362fc45d37a798a6ee/asn1crypto-1.5.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/de/cf/d547feed25b5244fcb9392e288ff9fdc3280b10260362fc45d37a798a6ee/asn1crypto-1.5.1.tar.gz
Summary  : Fast ASN.1 parser and serializer with definitions for private keys, public keys, certificates, CRL, OCSP, CMS, PKCS#3, PKCS#7, PKCS#8, PKCS#12, PKCS#5, X.509 and TSP
Group    : Development/Tools
License  : MIT
Requires: pypi-asn1crypto-license = %{version}-%{release}
Requires: pypi-asn1crypto-python = %{version}-%{release}
Requires: pypi-asn1crypto-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
A fast, pure Python library for parsing and serializing ASN.1 structures.
        
         - [Features](#features)
         - [Why Another Python ASN.1 Library?](#why-another-python-asn1-library)
         - [Related Crypto Libraries](#related-crypto-libraries)
         - [Current Release](#current-release)
         - [Dependencies](#dependencies)
         - [Installation](#installation)
         - [License](#license)
         - [Security Policy](#security-policy)
         - [Documentation](#documentation)
         - [Continuous Integration](#continuous-integration)
         - [Testing](#testing)
         - [Development](#development)
         - [CI Tasks](#ci-tasks)

%package license
Summary: license components for the pypi-asn1crypto package.
Group: Default

%description license
license components for the pypi-asn1crypto package.


%package python
Summary: python components for the pypi-asn1crypto package.
Group: Default
Requires: pypi-asn1crypto-python3 = %{version}-%{release}

%description python
python components for the pypi-asn1crypto package.


%package python3
Summary: python3 components for the pypi-asn1crypto package.
Group: Default
Requires: python3-core
Provides: pypi(asn1crypto)

%description python3
python3 components for the pypi-asn1crypto package.


%prep
%setup -q -n asn1crypto-1.5.1
cd %{_builddir}/asn1crypto-1.5.1
pushd ..
cp -a asn1crypto-1.5.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656356716
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-asn1crypto
cp %{_builddir}/asn1crypto-1.5.1/LICENSE %{buildroot}/usr/share/package-licenses/pypi-asn1crypto/11a01d5a56df1236ce6c2751489eef7029861b4c
cp %{_builddir}/asn1crypto-1.5.1/asn1crypto.egg-info/LICENSE %{buildroot}/usr/share/package-licenses/pypi-asn1crypto/11a01d5a56df1236ce6c2751489eef7029861b4c
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-asn1crypto/11a01d5a56df1236ce6c2751489eef7029861b4c

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
