
/* Include Files */
#include "header/rt_nonfinite.h"
#include "header/Untitled.h"

/* Function Definitions */

/*
 * Arguments    : const double gggg_data[]
 *                const int gggg_size[2]
 *                double UU[100]
 * Return Type  : void
 */
void Untitled( double gggg_data[], const int gggg_size[2], double UU[100])
{
  int ndbl;
  int apnd;
  int cdiff;
  double xol_data[100];
  int low_ip1;
  int k;
  double xil[100];
  double delta1;
  double y_data[100];
  int mid_i;
  if (gggg_size[1] < 1) {
    ndbl = 0;
    apnd = 0;
  } else {
    ndbl = (int)floor(((double)gggg_size[1] - 1.0) + 0.5);
    apnd = ndbl + 1;
    cdiff = (ndbl - gggg_size[1]) + 1;
    if (fabs(cdiff) < 4.4408920985006262E-16 * (double)gggg_size[1]) {
      ndbl++;
      apnd = gggg_size[1];
    } else if (cdiff > 0) {
      apnd = ndbl;
    } else {
      ndbl++;
    }
  }

  if (ndbl > 0) {
    xol_data[0] = 1.0;
    if (ndbl > 1) {
      xol_data[ndbl - 1] = apnd;
      low_ip1 = ndbl - 1;
      cdiff = low_ip1 / 2;
      for (k = 1; k < cdiff; k++) {
        xol_data[k] = 1.0 + (double)k;
        xol_data[(ndbl - k) - 1] = apnd - k;
      }

      if (cdiff << 1 == ndbl - 1) {
        xol_data[cdiff] = (1.0 + (double)apnd) / 2.0;
      } else {
        xol_data[cdiff] = 1.0 + (double)cdiff;
        xol_data[cdiff + 1] = apnd - cdiff;
      }
    }
  }

  xil[99] = gggg_size[1];
  xil[0] = 1.0;
  delta1 = ((double)gggg_size[1] - 1.0) / 99.0;
  for (k = 0; k < 98; k++) {
    xil[1 + k] = 1.0 + (1.0 + (double)k) * delta1;
  }

  cdiff = gggg_size[0] * gggg_size[1];
  for (low_ip1 = 0; low_ip1 < cdiff; low_ip1++) {
    y_data[low_ip1] = gggg_data[low_ip1];
  }

  for (low_ip1 = 0; low_ip1 < 100; low_ip1++) {
    UU[low_ip1] = rtNaN;
  }

  if (xol_data[1] < xol_data[0]) {
    low_ip1 = ndbl >> 1;
    for (apnd = 1; apnd <= low_ip1; apnd++) {
      delta1 = xol_data[apnd - 1];
      xol_data[apnd - 1] = xol_data[ndbl - apnd];
      xol_data[ndbl - apnd] = delta1;
    }

    cdiff = gggg_size[1] >> 1;
    for (apnd = 1; apnd <= cdiff; apnd++) {
      low_ip1 = gggg_size[1] - apnd;
      delta1 = y_data[apnd - 1];
      y_data[apnd - 1] = y_data[low_ip1];
      y_data[low_ip1] = delta1;
    }
  }

  for (k = 0; k < 100; k++) {
    if ((xil[k] > xol_data[ndbl - 1]) || (xil[k] < xol_data[0])) {
    } else {
      cdiff = 1;
      low_ip1 = 2;
      apnd = ndbl;
      while (apnd > low_ip1) {
        mid_i = (cdiff >> 1) + (apnd >> 1);
        if (((cdiff & 1) == 1) && ((apnd & 1) == 1)) {
          mid_i++;
        }

        if (xil[k] >= xol_data[mid_i - 1]) {
          cdiff = mid_i;
          low_ip1 = mid_i + 1;
        } else {
          apnd = mid_i;
        }
      }

      delta1 = (xil[k] - xol_data[cdiff - 1]) / (xol_data[cdiff] -
        xol_data[cdiff - 1]);
      if (delta1 == 0.0) {
        UU[k] = y_data[cdiff - 1];
      } else if (delta1 == 1.0) {
        UU[k] = y_data[cdiff];
      } else if (y_data[cdiff - 1] == y_data[cdiff]) {
        UU[k] = y_data[cdiff - 1];
      } else {
        UU[k] = (1.0 - delta1) * y_data[cdiff - 1] + delta1 * y_data[cdiff];
      }
    }
  }

  /* %UU= interp1(gggg,1:size(gggg,2)/101:size(gggg,2)) */
  /* y1=resample(x,10,6)%UU1= resample(fhmov(III(1):FFF(1)),100,89) */
}

