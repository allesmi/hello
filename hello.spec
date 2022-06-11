Name:           hello
Version:        2.10
Release:        1%{?dist}
Summary:        Produces a familiar, friendly greeting

License:        GPLv3+
URL:            http://ftp.gnu.org/gnu/%{name}
Source0:        http://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  make

%description
The GNU Hello program produces a familiar, friendly greeting. Yes, this is
another implementation of the classic program that prints “Hello, world!” when
you run it.

%prep
%autosetup
mv THANKS THANKS.old
iconv --from-code=ISO-8859-1 --to-code=UTF-8 --output=THANKS THANKS.old

%build
%configure
%make_build

%install
%make_install
rm %{buildroot}/%{_infodir}/dir
%find_lang %{name}

%check
make check

%files -f %{name}.lang
%{_mandir}/man1/hello.1.*
%{_infodir}/hello.info.*
%{_bindir}/hello
%doc AUTHORS ChangeLog NEWS README THANKS TODO
%license COPYING

%changelog
* Sat Jun 11 2022 Alexander Miller <alles.mil@gmail.com> 2.10-1
- Initial version of the package
