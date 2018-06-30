#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : asn1crypto
Version  : 0.24.0
Release  : 17
URL      : http://pypi.debian.net/asn1crypto/asn1crypto-0.24.0.tar.gz
Source0  : http://pypi.debian.net/asn1crypto/asn1crypto-0.24.0.tar.gz
Summary  : Fast ASN.1 parser and serializer with definitions for private keys, public keys, certificates, CRL, OCSP, CMS, PKCS#3, PKCS#7, PKCS#8, PKCS#12, PKCS#5, X.509 and TSP
Group    : Development/Tools
License  : MIT
Requires: asn1crypto-python3
Requires: asn1crypto-python
BuildRequires : pbr
BuildRequires : pip

BuildRequires : python3-dev
BuildRequires : setuptools

%description
# asn1crypto
A fast, pure Python library for parsing and serializing ASN.1 structures.

%package legacypython
Summary: legacypython components for the asn1crypto package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the asn1crypto package.


%package python
Summary: python components for the asn1crypto package.
Group: Default
Requires: asn1crypto-python3

%description python
python components for the asn1crypto package.


%package python3
Summary: python3 components for the asn1crypto package.
Group: Default
Requires: python3-core

%description python3
python3 components for the asn1crypto package.


%prep
%setup -q -n asn1crypto-0.24.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1519345437
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1519345437
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
