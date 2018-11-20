
/* Include Files */
#include "header/rt_nonfinite.c"
#include "neural_function.c"
#include "main.h"
#include "header/neural_function_terminate.c"
#include "header/neural_function_initialize.c"
#include "header/bsxfun.c"
#include "header/rtGetInf.c"
#include "header/rtGetNaN.c"
#include "header/neural_function_types.h"

#include "stdio.h"
#include <unistd.h>
#include <stdlib.h>

#include "ros/ros.h"
#include "std_msgs/String.h"
#include <sstream>
#include <vector>
#include <string>
#include <iostream>

/* Function Declarations */
static void argInit_99x1_real_T(double result[99]);
static double argInit_real_T(void);
static void main_neural_function(void);
static int roundNo(double);

std_msgs::String msg;
double x[99]; double y[4];
ros::Subscriber sub;

/*
 * Arguments    : double result[99]
 * Return Type  : void
 */
static void argInit_99x1_real_T(double result[99])
{
  int idx0;

  /* Loop over the array to initialize each element. */
  for (idx0 = 0; idx0 < 99; idx0++) {
    /* Set the value of the array element.
       Change this value to the value that the application requires. */
    result[idx0] = argInit_real_T();
  }
}

/*
 * Arguments    : void
 * Return Type  : double
 */
static double argInit_real_T(void)
{
  return 0.0;
}

/*
 * Arguments    : void
 * Return Type  : void
 */
static void main_neural_function(void)
{
  double dv3[99];
  double Y[4];

  /* Initialize function 'neural_function' input arguments. */
  /* Initialize function input argument 'X'. */
  /* Call the entry-point 'neural_function'. */
  argInit_99x1_real_T(dv3);
  neural_function(dv3, Y);
}

static int roundNo(double num)
{
  return num < 0 ? num - 0.5 : num + 0.5;
}
/*
 * Arguments    : int argc
 *                const char * const argv[]
 * Return Type  : int
 */
void chatterCallback1(const std_msgs::String::ConstPtr& msg) {



	ROS_INFO("I heard: [%s]", msg->data.c_str());

std::string str = msg->data;

std::string delimiter =",";

size_t pos = 0;
std::string token;
int i=0;
while((pos = str.find(delimiter)) != std::string::npos){ 
    token = str.substr(0,pos);
    x[i] = atof(token.c_str());
    //std::cout << token << std::endl;
    str.erase(0,pos + delimiter.length());
    i++;
}

//printf("\n \n \n %d \n \n \n", i );
 neural_function(x,y);
 
printf("\nB4 round:       ");
for(int i=0; i<4; i++){
printf("%f ",y[i]);
}
printf("\n");
for(int i=0; i<4; i++){
y[i]=roundNo(y[i]);
}
printf("After round:    ");
for(int i=0; i<4; i++){
    printf("%f ",y[i]);
}
printf("\n");

int check[4];
check[0]=(int) y[0];
check[1]=(int) y[1];
check[2]=(int) y[2];
check[3]=(int) y[3];

if(check[0] == 1){ printf("ground detected: Teflon\n\n");}
if(check[1] == 1){ printf("ground detected: Acrylic\n\n");}
if(check[2] == 1){ printf("ground detected Aluminium\n\n");}
if(check[3] == 1){ printf("ground detected Green carpet\n\n");}
}


 
 
int main(int argc, char *argv[])
{

    ros::init(argc, argv, "listener");

  ros::NodeHandle n;
  sub= n.subscribe("/data_nn1", 1000, chatterCallback1);
  
  ros::spin();
  return 0;
}

/*
 * File trailer for main.c
 *
 * [EOF]
 */
