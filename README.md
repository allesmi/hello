# hello

To start, get the tarball of `hello` with `wget http://ftp.gnu.org/gnu/hello/hello-2.10.tar.gz`.

## Fedora RPM

See the [spec file](hello.spec).

I followed the tutorial at [Packaging Tutorial: GNU Hello](https://docs.fedoraproject.org/en-US/package-maintainers/Packaging_Tutorial_GNU_Hello/) to create rpm packages for usage in Fedora 36.

It consisted mostly of editing the file in `hello.spec` (initially created with `rpmdev-newspec hello`) and running `fedpkg --release f36 mockbuild`.

Firstly I had to add `BuildRequires:` lines for `gcc`, `make`, and `gettext`. After building `fedpkg` complains about installed but unpackaged files which where then added under the `%files` section in `hello.spec`.

When `fedpkg` completes successfully  I can check for correctness with `rpmlint hello.spec results_hello/2.10/1.fc36/hello-2.10*.{x86_64,src}.rpm`.

## Flatpak

See the [flatpak manifest](eu.sunbeng.hello.yml).

Following the tutorial at [Building your first Flatpak](https://docs.flatpak.org/en/latest/first-build.html).
The manifest contains the URL of the GNU hello tarball, along with its sha256 sum.
Just setting `buildsystem: autotools` is enough to build and package the program.
