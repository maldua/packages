Summary:            a libzmq 3.x wrapper for Perl
Name:               zimbra-perl-zmq-libzmq3
Version:            VERSION
Release:            ITERATIONZAPPEND
License:            Artistic 2.0
Source:             %{name}-%{version}.tar.gz
Packager:           Zimbra Packaging Services <packaging-devel@zimbra.com>
Group:              Development/Languages
BuildRequires:      zimbra-perl-base, zimbra-zeromq-devel, zimbra-perl-zmq-constants
Requires:           zimbra-perl-base, zimbra-zeromq-libs, zimbra-perl-zmq-constants
AutoReqProv:        no
URL:                https://metacpan.org/release/ZMQ-LibZMQ3

%define perl_archname %(eval "`perl -V:archname`"; echo $archname)

%description
The ZMQ::LibZMQ3 module is a wrapper of the 0MQ message passing
library for Perl.  This module is merely a thin wrapper around the C
API: You need to understand how the C API works in order to properly
use this module.

%define debug_package %{nil}

%prep
%setup -n ZMQ-LibZMQ3-%{version}

%build
# Notes/Workarounds:
# * LIBS not working as expected due to a MakeMaker bug:
#     https://github.com/Perl-Toolchain-Gang/ExtUtils-MakeMaker/pull/240
#   - (RHEL) use -LOZCL in LDLOADLIBS since -L is not preserved
rm -f t/104_ipc.t # HACK: avoid tests requiring Test::SharedFork
%if 0%{?rhel} < 7
# HACK: avoid tests requiring Test::Fatal or Test::Require or Test::More::subtest
rm -f t/001_context.t t/002_socket.t t/003_message.t t/005_poll.t t/006_anyevent.t
rm -f t/100_basic.t t/101_threads.t t/200_fork.t t/201_thread.t t/202_proxy.t
rm -f t/rt64944.t t/rt74653.t
%endif
%if 0%{?rhel} == 9
#https://metacpan.org/release/XSAWYERX/perl-5.26.0/view/pod/perldelta.pod#Removal_of_the_current_directory_(%22.%22)_from_@INC
export PERL_USE_UNSAFE_INC=1;
%endif
ZMQ_INCLUDES=OZCI ZMQ_LIBS=OZCL ZMQ_H=OZCI \
 perl -I OZCL/perl5 Makefile.PL INSTALL_BASE=OZC \
 INSTALLSITEMAN1DIR=OZCS/man/man1 INSTALLSITEMAN3DIR=OZCS/man/man3
LD_RUN_PATH=OZCL PERL5LIB=OZCL/perl5 make test LDLOADLIBS="-LOZCL -lzmq"

%install
make install DESTDIR=${RPM_BUILD_ROOT}
rm -f %{buildroot}OZCL/perl5/%{perl_archname}/perllocal.pod
rm -f %{buildroot}OZCL/perl5/%{perl_archname}/auto/*/*/.packlist

%files
%defattr(-,root,root)
OZCL
OZCS/man
