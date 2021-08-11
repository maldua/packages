Summary:        Zimbra Perl
Name:           zimbra-perl
Version:        1.0.9
Release:        1zimbra8.7b1ZAPPEND
License:        GPL-2
Packager:       Zimbra Packaging Services <packaging-devel@zimbra.com>
Group:          Development/Languages
Requires:       zimbra-perl-base, zimbra-perl-archive-zip >= 1.53-1zimbra8.7b2ZAPPEND, zimbra-perl-berkeleydb
Requires:       zimbra-perl-bit-vector >= 7.4-1zimbra8.7b2ZAPPEND, zimbra-perl-cache-fastmmap, zimbra-perl-canary-stability
Requires:       zimbra-perl-carp-clan >= 6.08-1zimbra8.7b1ZAPPEND, zimbra-perl-class-inspector
Requires:       zimbra-perl-compress-raw-bzip2 >= 2.093-1zimbra8.7b1ZAPPEND
Requires:       zimbra-perl-compress-raw-zlib >= 2.103-1zimbra8.7b1ZAPPEND, zimbra-perl-config-inifiles >= 2.86-1zimbra8.7b2ZAPPEND
Requires:       zimbra-perl-convert-asn1
Requires:       zimbra-perl-convert-binhex, zimbra-perl-convert-tnef, zimbra-perl-convert-uulib
Requires:       zimbra-perl-crypt-openssl-random >= 0.11-1zimbra8.7b4ZAPPEND, zimbra-perl-crypt-openssl-rsa >= 0.33-1zimbra8.8b1ZAPPEND
Requires:       zimbra-perl-crypt-saltedhash
Requires:       zimbra-perl-data-uuid, zimbra-perl-date-calc >= 6.4-1zimbra8.7b2ZAPPEND, zimbra-perl-date-manip >= 6.90-1zimbra8.7b1ZAPPEND
Requires:       zimbra-perl-dbd-mysql >= 4.050-1zimbra8.7b5ZAPPEND
Requires:       zimbra-perl-dbd-sqlite, zimbra-perl-db-file, zimbra-perl-dbi, zimbra-perl-digest-hmac
Requires:       zimbra-perl-digest-sha1, zimbra-perl-email-date-format, zimbra-perl-encode-detect
Requires:       zimbra-perl-encode-locale, zimbra-perl-error, zimbra-perl-exporter-tiny, zimbra-perl-zmq-libzmq3
Requires:       zimbra-perl-file-grep, zimbra-perl-file-libmagic, zimbra-perl-file-listing, zimbra-perl-filesys-df
Requires:       zimbra-perl-file-tail, zimbra-perl-geography-countries, zimbra-perl-html-parser, zimbra-perl-http-cookies >= 6.01-1zimbra8.7b2ZAPPEND
Requires:       zimbra-perl-http-daemon >= 6.01-1zimbra8.7b2ZAPPEND, zimbra-perl-http-date, zimbra-perl-http-message >= 6.11-1zimbra8.7b2ZAPPEND
Requires:       zimbra-perl-http-negotiate >= 6.01-1zimbra8.7b2ZAPPEND
Requires:       zimbra-perl-innotop >= 1.9.1-1zimbra8.7b5ZAPPEND
Requires:       zimbra-perl-io-compress >= 2.093-1zimbra8.7b1ZAPPEND, zimbra-perl-io-html, zimbra-perl-io-sessiondata, zimbra-perl-io-socket-inet6
Requires:       zimbra-perl-io-socket-ip, zimbra-perl-io-socket-ssl >= 2.083-1zimbra8.7b4ZAPPEND, zimbra-perl-io-stringy, zimbra-perl-ip-country
Requires:       zimbra-perl-json-pp
Requires:       zimbra-perl-libwww >= 6.13-1zimbra8.7b5ZAPPEND, zimbra-perl-list-moreutils >= 0.428-1zimbra8.7b1ZAPPEND, zimbra-perl-lwp-mediatypes
Requires:       zimbra-perl-lwp-protocol-https >= 6.10-1zimbra8.7b4ZAPPEND
Requires:       zimbra-perl-mail-dkim >= 0.43-1zimbra8.8b1ZAPPEND, zimbra-perl-mail-spf, zimbra-perl-mailtools, zimbra-perl-math-bigint
Requires:       zimbra-perl-mime-lite
Requires:       zimbra-perl-mime-tools, zimbra-perl-mime-types, zimbra-perl-mozilla-ca, zimbra-perl-netaddr-ip
Requires:       zimbra-perl-net-cidr, zimbra-perl-net-cidr-lite, zimbra-perl-net-dns, zimbra-perl-net-dns-resolver-programmable
Requires:       zimbra-perl-net-http >= 6.09-1zimbra8.7b5ZAPPEND, zimbra-perl-net-ldap, zimbra-perl-net-ldapapi >= 3.0.3-1zimbra8.7b2ZAPPEND
Requires:       zimbra-perl-net-libidn
Requires:       zimbra-perl-net-server >= 2.009-1zimbra8.7b1ZAPPEND
Requires:       zimbra-perl-net-ssleay >= 1.92-1zimbra8.8b1ZAPPEND, zimbra-perl-parent, zimbra-perl-proc-processtable
Requires:       zimbra-perl-soap-lite >= 1.19-1zimbra8.7b5ZAPPEND, zimbra-perl-socket
Requires:       zimbra-perl-socket-linux, zimbra-perl-swatchdog >= 3.2.4-1zimbra8.7b2ZAPPEND, zimbra-perl-task-weaken, zimbra-perl-term-readkey, zimbra-perl-timedate
Requires:       zimbra-perl-unix-getrusage, zimbra-perl-unix-syslog, zimbra-perl-uri, zimbra-perl-www-robotrules
Requires:       zimbra-perl-xml-namespacesupport, zimbra-perl-xml-parser >= 2.44-1zimbra8.7b5ZAPPEND, zimbra-perl-xml-parser-lite, zimbra-perl-xml-sax
Requires:       zimbra-perl-xml-sax-base, zimbra-perl-xml-sax-expat >= 0.51-1zimbra8.7b5ZAPPEND, zimbra-perl-xml-simple >= 2.25-1zimbra8.7b4ZAPPEND
Requires:       zimbra-perl-zmq-constants
AutoReqProv:        no

%define debug_package %{nil}

%description
Zimbra Perl is a meta package that can be used to install most all
of the Zimbra required perl modules.  The current sole exception is
the Mail::SpamAssassin module, as that is for MTA nodes only

%changelog
* Tue Jun 13 2023 Zimbra Packaging Services <packaging-devel@zimbra.com> - 1.0.9
- Updated perl-net-ssleay, perl-dbd-mysql, perl-crypt-openssl-random, perl-crypt-openssl-rsa, perl-io-socket-ssl
- Updated perl-net-http, perl-libwww, perl-lwp-protocol-https, perl-xml-parser, perl-soap-lite, perl-xml-sax-expat
- Updated perl-xml-simple, perl-mail-dkim, perl-innotop
* Tue Feb 07 2023 Zimbra Packaging Services <packaging-devel@zimbra.com> - 1.0.8
- Upgraded Date-Manip to 6.90
* Thu Jan 19 2023 Zimbra Packaging Services <packaging-devel@zimbra.com> - 1.0.7
- Upgraded Compress::Raw::Zlib to 2.103
* Tue Aug 10 2021 Zimbra Packaging Services <packaging-devel@zimbra.com> - 1.0.6
- Updated archive-zip,bit-vector,carp-clan,compress-raw-bzip2,compress-raw-zlib,config-inifiles,date-calc
- Updated dbd-mysql,http-cookies,http-daemon,http-message,http-negotiate,innotop
- Updated io-compress,io-socket-ssl,libwww,list-moreutils,lwp-protocol-https
- Updated net-http,net-server,soap-lite,swatchdog,xml-parser,xml-sax-expat,xml-simple
* Sat Dec 05 2020 Zimbra Packaging Services <packaging-devel@zimbra.com> - 1.0.5
- Updated perl-net-ssleay, perl-dbd-mysql, perl-crypt-openssl-random, perl-crypt-openssl-rsa, perl-io-socket-ssl
- Updated perl-net-http, perl-libwww, perl-lwp-protocol-https, perl-xml-parser, perl-soap-lite, perl-xml-sax-expat
- Updated perl-xml-simple, perl-mail-dkim, perl-innotop
* Thu Sep 10 2020 Zimbra Packaging Services <packaging-devel@zimbra.com> - 1.0.4
- Updated perl-net-ssleay, perl-dbd-mysql, perl-crypt-openssl-random, perl-crypt-openssl-rsa, perl-io-socket-ssl
- Updated perl-net-http, perl-libwww, perl-lwp-protocol-https, perl-xml-parser, perl-soap-lite, perl-xml-sax-expat
- Updated perl-xml-simple, perl-mail-dkim, perl-innotop
* Thu Sep 7 2017 Zimbra Packaging Services <packaging-devel@zimbra.com> - 1.0.3
- Updated perl-dbd-mysql
* Fri Sep 22 2016 Zimbra Packaging Services <packaging-devel@zimbra.com> - 1.0.2
- Really add zimbra-perl-file-libmagic
* Thu Jan 21 2016  Zimbra Packaging Services <packaging-devel@zimbra.com> - 1.0.1
- Add zimbra-perl-file-libmagic

%files
