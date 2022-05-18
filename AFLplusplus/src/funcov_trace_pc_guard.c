#include <stdint.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include <execinfo.h>

#include "../include/funcov_shm_coverage.h"  

#define BT_BUF_SIZE 5
#define STR_BUFF 512

static cov_stat_t * curr_stat ; // shm
static int curr_stat_shmid ;

/**
 * README
 * 
 * You need to use "this file" for sanitizer coverage.
 * ...
*/

extern void 
__sanitizer_cov_trace_pc_guard_init(uint32_t *start, uint32_t *stop) 
{
	static uint64_t N;  
	if (start == stop || *start) return;  

	for (uint32_t *x = start; x < stop; x++)
		*x = ++N;  

	// curr_stat_shmid = get_shm(CURR_KEY, sizeof(cov_stat_t)) ;
	curr_stat_shmid = get_shm(USE, sizeof(cov_stat_t)) ;
}

/**
 * strings format
 * /home/kimseoye/git/FunCov/test/simple_example/example(negative+0x17) [0x512437]
 * /home/kimseoye/git/FunCov/test/simple_example/example(main+0x1a5) [0x512685]
*/


void
get_coverage (char * cov_string)
{
	curr_stat = attatch_shm(curr_stat_shmid) ;

	// char cov_string[BUF_SIZE] ;
	// sprintf(cov_string, "%s,%s", callee, caller) ;

	unsigned int id = hash16(cov_string) ;

	int found = 0 ;
	for (int i = 0; i < FUNCOV_MAP_SIZE; i++) {
		if (id >= FUNCOV_MAP_SIZE) {
			id = 0 ;
			continue ;
		}

		if (curr_stat->map[id].hit_count == 0) {
			strcpy(curr_stat->map[id].cov_string, cov_string) ;
			curr_stat->map[id].hit_count++ ;
			found = 1 ;
			break ;
		}
		else if (strcmp(curr_stat->map[id].cov_string, cov_string) == 0) {
			curr_stat->map[id].hit_count++ ;
			found = 1 ;
			break ;
		}
		else id++ ;
	}

	if (!found) {
		perror("get_coverage: map limit") ;
		exit(1) ; 
	}

	detatch_shm(curr_stat) ;
}

extern void 
__sanitizer_cov_trace_pc_guard(uint32_t *guard) 
{
	if (!*guard) return;  

	void *callee = __builtin_return_address(0);
  	void *caller = __builtin_return_address(1);
  	
	char cov_string[STR_BUFF];
	sprintf(cov_string,"%p",callee);

	get_coverage(cov_string) ;


}
