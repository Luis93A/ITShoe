/*
 * File: bsxfun.c
 *
 * MATLAB Coder version            : 3.0
 * C/C++ source code generated on  : 19-Nov-2018 13:13:11
 */

/* Include Files */
#include "rt_nonfinite.h"
#include "neural_function.h"
#include "bsxfun.h"

/* Function Definitions */

/*
 * Arguments    : const double a[99]
 *                const double b[99]
 *                double c[99]
 * Return Type  : void
 */
void bsxfun(const double a[99], const double b[99], double c[99])
{
  int k;
  for (k = 0; k < 99; k++) {
    c[k] = a[k] - b[k];
  }
}

/*
 * File trailer for bsxfun.c
 *
 * [EOF]
 */
