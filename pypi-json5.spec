#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-json5
Version  : 0.9.9
Release  : 37
URL      : https://files.pythonhosted.org/packages/2a/f5/1522bab99b4691eb2933540bc6fe53ca15601ad3d5dffb591d3b4b9ae745/json5-0.9.9.tar.gz
Source0  : https://files.pythonhosted.org/packages/2a/f5/1522bab99b4691eb2933540bc6fe53ca15601ad3d5dffb591d3b4b9ae745/json5-0.9.9.tar.gz
Summary  : A Python implementation of the JSON5 data format.
Group    : Development/Tools
License  : Apache-2.0
Requires: pypi-json5-bin = %{version}-%{release}
Requires: pypi-json5-license = %{version}-%{release}
Requires: pypi-json5-python = %{version}-%{release}
Requires: pypi-json5-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
# pyjson5
A Python implementation of the JSON5 data format.
[JSON5](https://json5.org) extends the
[JSON](http://www.json.org) data interchange format to make it
slightly more usable as a configuration language:

%package bin
Summary: bin components for the pypi-json5 package.
Group: Binaries
Requires: pypi-json5-license = %{version}-%{release}

%description bin
bin components for the pypi-json5 package.


%package license
Summary: license components for the pypi-json5 package.
Group: Default

%description license
license components for the pypi-json5 package.


%package python
Summary: python components for the pypi-json5 package.
Group: Default
Requires: pypi-json5-python3 = %{version}-%{release}

%description python
python components for the pypi-json5 package.


%package python3
Summary: python3 components for the pypi-json5 package.
Group: Default
Requires: python3-core
Provides: pypi(json5)

%description python3
python3 components for the pypi-json5 package.


%prep
%setup -q -n json5-0.9.9
cd %{_builddir}/json5-0.9.9
pushd ..
cp -a json5-0.9.9 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1659452423
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
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
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-json5
cp %{_builddir}/json5-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-json5/c700a8b9312d24bdc57570f7d6a131cf63d89016
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
## Remove excluded files
rm -f %{buildroot}*/usr/lib/python3*/site-packages/README.md
rm -f %{buildroot}*/usr/lib/python3*/site-packages/tests/__init__.py
rm -f %{buildroot}*/usr/lib/python3*/site-packages/tests/__pycache__/__init__.cpython-3*.pyc
rm -f %{buildroot}*/usr/lib/python3*/site-packages/tests/__pycache__/host_fake.cpython-3*.pyc
rm -f %{buildroot}*/usr/lib/python3*/site-packages/tests/__pycache__/host_test.cpython-3*.pyc
rm -f %{buildroot}*/usr/lib/python3*/site-packages/tests/__pycache__/lib_test.cpython-3*.pyc
rm -f %{buildroot}*/usr/lib/python3*/site-packages/tests/__pycache__/tool_test.cpython-3*.pyc
rm -f %{buildroot}*/usr/lib/python3*/site-packages/tests/host_fake.py
rm -f %{buildroot}*/usr/lib/python3*/site-packages/tests/host_test.py
rm -f %{buildroot}*/usr/lib/python3*/site-packages/tests/lib_test.py
rm -f %{buildroot}*/usr/lib/python3*/site-packages/tests/tool_test.py
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/pyjson5

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-json5/c700a8b9312d24bdc57570f7d6a131cf63d89016

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
