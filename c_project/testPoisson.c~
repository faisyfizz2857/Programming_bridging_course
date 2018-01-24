/* testPoisson.c */

#include <stdio.h>
#include "prand.h"
#include "prand.c"
#include <math.h>
int main() {
  int i;
  int v;
  int stat[20]={0};
  sprand(3);
  for (i=0; i<100; i++) {
    v=prand();
    stat[v]++;
    printf("%3d", v);
    
    if ( (i+1)%15==0 )
      printf("\n");      
  }
  printf("\n\n");
  for (i=0; i<20; i++) {
    printf("%3d", stat[i]);
  }
  printf("\n");
    
}
