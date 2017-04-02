#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-dichromat
Version  : 2.0.0
Release  : 29
URL      : http://cran.r-project.org/src/contrib/dichromat_2.0-0.tar.gz
Source0  : http://cran.r-project.org/src/contrib/dichromat_2.0-0.tar.gz
Summary  : Color Schemes for Dichromats
Group    : Development/Tools
License  : GPL-2.0
BuildRequires : clr-R-helpers

%description
No detailed description available

%prep
%setup -q -c -n dichromat

%build
export LANG=C
export SOURCE_DATE_EPOCH=1489127444

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1489127444
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library dichromat
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library dichromat


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/dichromat/DESCRIPTION
/usr/lib64/R/library/dichromat/INDEX
/usr/lib64/R/library/dichromat/Meta/Rd.rds
/usr/lib64/R/library/dichromat/Meta/data.rds
/usr/lib64/R/library/dichromat/Meta/hsearch.rds
/usr/lib64/R/library/dichromat/Meta/links.rds
/usr/lib64/R/library/dichromat/Meta/nsInfo.rds
/usr/lib64/R/library/dichromat/Meta/package.rds
/usr/lib64/R/library/dichromat/NAMESPACE
/usr/lib64/R/library/dichromat/R/dichromat
/usr/lib64/R/library/dichromat/R/dichromat.rdb
/usr/lib64/R/library/dichromat/R/dichromat.rdx
/usr/lib64/R/library/dichromat/R/sysdata.rdb
/usr/lib64/R/library/dichromat/R/sysdata.rdx
/usr/lib64/R/library/dichromat/data/dalton.rda
/usr/lib64/R/library/dichromat/help/AnIndex
/usr/lib64/R/library/dichromat/help/aliases.rds
/usr/lib64/R/library/dichromat/help/dichromat.rdb
/usr/lib64/R/library/dichromat/help/dichromat.rdx
/usr/lib64/R/library/dichromat/help/paths.rds
/usr/lib64/R/library/dichromat/html/00Index.html
/usr/lib64/R/library/dichromat/html/R.css
