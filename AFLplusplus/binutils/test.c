#include <stdio.h>
#include <stdlib.h>
#include "./binutils/addr2line.h"


int main(int argc,char** argv){
    printf("TEST\n");
    char f_name[40] = {0,};
    addr2line(argv[1],argv[2],f_name);
    printf("test: %s\n",f_name);
    return 0;
}