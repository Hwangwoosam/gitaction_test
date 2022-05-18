all: bucomm.o version.o filemode.o addr2line.o addr2line

.PHONY: bucomm.o
bucomm.o: 
	gcc -DHAVE_CONFIG_H -I. -I../bfd -I./../bfd -I./../include -DLOCALEDIR="\"/usr/local/share/locale\"" -Dbin_dummy_emulation=bin_vanilla_emulation  -W -Wall -Wstrict-prototypes -Wmissing-prototypes -Wshadow -Wstack-usage=262144 -Werror -I./../zlib -g -O2 -MT bucomm.o -MD -MP -MF .Tpo -c -o bucomm.o bucomm.c

.PHONY: version.o
version.o:
	gcc -DHAVE_CONFIG_H -I. -I../bfd -I./../bfd -I./../include -DLOCALEDIR="\"/usr/local/share/locale\"" -Dbin_dummy_emulation=bin_vanilla_emulation  -W -Wall -Wstrict-prototypes -Wmissing-prototypes -Wshadow -Wstack-usage=262144 -Werror -I./../zlib -g -O2 -MT version.o -MD -MP -MF .Tpo -c -o version.o version.c

.PHONY: filemode.o
filemode.o:
	gcc -DHAVE_CONFIG_H -I. -I../bfd -I./../bfd -I./../include -DLOCALEDIR="\"/usr/local/share/locale\"" -Dbin_dummy_emulation=bin_vanilla_emulation  -W -Wall -Wstrict-prototypes -Wmissing-prototypes -Wshadow -Wstack-usage=262144 -Werror -I./../zlib -g -O2 -MT filemode.o -MD -MP -MF .Tpo -c -o filemode.o filemode.c

.PHONY: addr2line.o
addr2line.o:
	gcc -DHAVE_CONFIG_H -I. -I../bfd -I./../bfd -I./../include -DLOCALEDIR="\"/usr/local/share/locale\"" -Dbin_dummy_emulation=bin_vanilla_emulation  -W -Wall  -Wshadow -Wstack-usage=262144 -Werror -I./../zlib -g -O2 -MT addr2line.o -MD -MP -MF .Tpo -c -o addr2line.o addr2line.c
#-Wstrict-prototypes -Wmissing-prototypes
#.PHONY: addr2line
addr2line:
	ar crv libaddr2line.a ../../src/funcov.o addr2line.o bucomm.o version.o filemode.o ../bfd/libbfd.a ../libiberty/libiberty.a  ../zlib/libz.a
#	gcc -W -Wall -Wstrict-prototypes -Wmissing-prototypes -Wshadow -Wstack-usage=262144 -Werror -I./../zlib -g -O2 -o addr2line addr2line.o bucomm.o version.o filemode.o ../bfd/libbfd.a ../libiberty/libiberty.a  ../zlib/libz.a -ldl

clean:
	rm bucomm.o version.o filemode.o addr2line.o libaddr2line.a