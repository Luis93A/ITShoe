//Includes
#include "ros/ros.h"
#include "std_msgs/String.h"
#include <sstream>
#include <vector>
#include <string>
#include <iostream>

 
//Var
int k=0;int i; int n =1; int start =0; double AF0[8];
double a1=0.0005, a2= 0.0003731 , a3= 0.0005, a4 = 0.0005, a5= 1.0963, a6= 1.0958, a7= 1.0845, a8 = 1.0809, b1= -0.00004, b2= 0.000049,b3= 0.0001,b4= 0.00001,b5= 65.881,b6= 69.702,b7= 66.179,b8=63.568,v1[1],v2[1],v3[1],v4[1],r1[1],r2[1],r3[1],r4[1],f1[1],f2[1],f3[1],f4[1],f5[1],f6[1],f7[1],f8[1],fhmov[1],fn[1]; 
int axx= 0; int aux = 0; double goal[100]; 

std_msgs::String msg1;
ros::Publisher data_nn;
std::ostringstream auu;
std::string aaaa;


//Callback
void chatterCallback(const std_msgs::String::ConstPtr& msg)
{

std::string str = msg->data;
std::string delimiter =",";

size_t pos = 0;
std::string token;
i=0;
while((pos = str.find(delimiter)) != std::string::npos){ 
    token = str.substr(0,pos);
    AF0[i] = atof(token.c_str());
    str.erase(0,pos + delimiter.length());
    i++;
}


v1[0]=((AF0[1]+100.0)*(5.0/1023.0));
v2[0]=(AF0[3])*(5.0/1023.0);
v3[0]=(AF0[5])*(5.0/1023.0);
v4[0]=(AF0[6])*(5.0/1023.0);


r1[0] = (6000.0/v1[0]) - 1200.0;
r2[0] = (6000.0/v2[0]) - 1200.0;
r3[0] = (6000.0/v3[0]) - 1200.0;
r4[0] = (6000.0/v4[0]) - 1200.0;

f1[0] = ((1/r1[0])- b1)* (4.448221/a1);
f2[0] = ((1/r2[0])- b2)* (4.448221/a2);
f3[0] = ((1/r3[0])- b3)* (4.448221/a3);
f4[0] = ((1/r4[0])- b4)* (4.448221/a4);

f5[0]= ((AF0[2]-b5)/a5)/100.0;
f6[0]= ((AF0[0]-b6)/a6)/100.0;
f7[0]= ((AF0[4]-b7)/a7)/100.0;
f8[0]= ((AF0[7]-b8)/a8)/100.0;

fn[0]=f1[0]+f2[0]+f3[0]+f4[0];

fhmov[0]= (-f5[0]*0.7071 + f6[0]*0.7071 -f7[0]*0.7071 + f8[0]*0.7071);

//Step ..
if(fn[0] < 1.5 && fn[0] > -5 && start==0 ){

  aux=1;
   k=0;
}

if(fn[0] >1.5 && aux==1 && k<100){

    goal[k]=fhmov[0];
    start =1;
    if(k == 0 && axx==0) {
        k=k-1; axx=1;
    }
    k++;
}

if(fn[0]>1.5 && k>99) { aux = 0; start = 0; axx = 0;}
if(fn[0] < 1.5 && k< 70){start = 0; axx= 0; memset(goal,0,sizeof(goal));}

   if(fn[0] < 1.5 && start==1 && k> 70 && k <100){
   printf("step %d\n",k);
   goal[k]=fhmov[0];
   axx=0;
     aux = 0; 
     msg1.data="";
     start= 0;
     //publish goal to topic!!
     for(int h =0; h<k+1;h++)
     {
         auu.str("");
         auu << goal[h];
         aaaa = auu.str();
         msg1.data+=aaaa;
         msg1.data+=",";
         
     }
     
     //for(int j=0; j<k+1; j++){printf(" |%f| ", goal[j]);}

     data_nn.publish(msg1);
     memset(goal,0,sizeof(goal));
     k=0;
   }

}
 

int main(int argc, char *argv[])
{
  ros::init(argc, argv, "my_node");

  ros::NodeHandle n;

  data_nn = n.advertise<std_msgs::String>("/data_nn", 1000);
  ros::Subscriber sub= n.subscribe("data", 1000, chatterCallback);

  ros::spin();
  return 0;

}
