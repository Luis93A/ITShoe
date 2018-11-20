
/* Include Files */
#include "rt_nonfinite.h"
#include "neural_function.h"
#include "neural_function_initialize.h"

/* Function Definitions */

/*
 * Arguments    : void
 * Return Type  : void
 */
void neural_function_initialize(void)
{
  rt_InitInfAndNaN(8U);
}


