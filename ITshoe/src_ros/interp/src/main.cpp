
/* Include Files */
#include "header/rt_nonfinite.c"
#include "Untitled.c"
#include "header/main.h"
#include "header/Untitled_terminate.c"
#include "header/Untitled_initialize.c"

#include "header/rtGetInf.c"
#include "header/rtGetNaN.c"


#include "stdio.h"
#include <unistd.h>
#include <stdlib.h>

#include "ros/ros.h"
#include "std_msgs/String.h"
#include <sstream>
#include <vector>
#include <string>
#include <iostream>

std_msgs::String msg;

ros::Subscriber sub;
double gggg_data[100]; double UU[100];
int gggg_size[2];
std_msgs::String msg2;
ros::Publisher data_nn1;
std::ostringstream auu;
std::string aaaa;

/* Function Declarations */
static void argInit_1xd100_real_T(double result_data[], int result_size[2]);
static double argInit_real_T(void);
static void main_Untitled(void);

/* Function Definitions */

/*
 * Arguments    : double result_data[]
 *                int result_size[2]
 * Return Type  : void
 */
static void argInit_1xd100_real_T(double result_data[], int result_size[2])
{
  int idx1;

  /* Set the size of the array.
     Change this size to the value that the application requires. */
  result_size[0] = 1;
  result_size[1] = 2;

  /* Loop over the array to initialize each element. */
  for (idx1 = 0; idx1 < 2; idx1++) {
    /* Set the value of the array element.
       Change this value to the value that the application requires. */
    result_data[idx1] = argInit_real_T();
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


void chatterCallback2(const std_msgs::String::ConstPtr& msg) {

 
	//ROS_INFO("I heard: [%s]", msg->data.c_str());

std::string str = msg->data;

std::string delimiter =",";

size_t pos = 0;
std::string token;
int i=0;
while((pos = str.find(delimiter)) != std::string::npos){ 
    token = str.substr(0,pos);
    gggg_data[i] = atof(token.c_str());
    //std::cout << token << std::endl;
    str.erase(0,pos + delimiter.length());
    i++;
}
gggg_size[0] = 1;
gggg_size[1] = i;
//printf("%d\n",i);

msg2.data="";

Untitled(gggg_data, gggg_size, UU);




double HH[100];
double di=UU[0];
for(int h =1; h<100;h++)
     {
         HH[h-1]=UU[h]-di;
         di=UU[h];
     } 

 
for(int h =0; h<99;h++)
     {
         auu.str("");
         auu << HH[h];//-di;
         aaaa = auu.str();
         msg2.data+=aaaa;
         msg2.data+=",";
         //di=goal[h];
     }
     
   //  for(int j=0; j<99; j++){printf(" |%f| ", HH[j]);}
       data_nn1.publish(msg2);
     
}


/*
 * Arguments    : void
 * Return Type  : void
 */
static void main_Untitled(void)
{
  
}

/*
 * Arguments    : int argc
 *                const char * const argv[]
 * Return Type  : int
 */
int main(int argc, char *argv[])
{
  argInit_1xd100_real_T(gggg_data, gggg_size);
 ros::init(argc, argv, "my_node2");

  ros::NodeHandle n;

   data_nn1 = n.advertise<std_msgs::String>("/data_nn1", 1000);
  ros::Subscriber sub= n.subscribe("data_nn", 1000, chatterCallback2);

  ros::spin();
return 0;
}

/*
 * File trailer for main.c
 *
 * [EOF]
 */
