/* prand.c - generates Poissondistributed random numbers
   
   Usage
     void sprand(int m)  - set the  Poissondistribution mean (5 default) 
     int prand()         - returns a Poissondistribted random number 
                           in the interval [0,3m] 
*/

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>

static int m = 5;    // Poisson mean

void sprand(int mp) {
  m = mp;
}

double poisson(int x, int m) {
  double f = 1.;
  int i;
  for (i=1; i<=x; i++)
    f = f*i;
  return exp(-m)*pow(m,x)/f; 
}

int prand() {
  static int     firstCall=1;
  static int     size;
  static double *distribution;
  int            i;
  time_t         ttime;
  if (firstCall) { 
    double sum = 0.;
    firstCall  = 0;
    size = 3*m;
    distribution = (double *)malloc(size*sizeof(double));
    for (i=0; i<size; i++) {
      sum = sum + poisson(i, m);
      distribution[i] = sum;
    }  
    srand48(time(&ttime));
  }
  double s = drand48();
  for (i=0; i<size; i++)
    if ( s<distribution[i] )
      return i;
  return size;
}

