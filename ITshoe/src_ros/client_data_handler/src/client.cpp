 /*
    C socket server, handles multiple clients using threads
*/
 
//Includes
#include "ros/ros.h"
#include "std_msgs/String.h"
#include <sstream>
#include<stdio.h>
#include<string.h>    //strlen
#include<stdlib.h>    //strlen
#include<sys/socket.h>
#include<arpa/inet.h> //inet_addr
#include<unistd.h>    //write
#include<pthread.h> //for threading , link with lpthread
#include<iostream>
#include<fstream>
#include<sys/time.h>
#include<signal.h>

//Defines
#define BUFLEN 255
#define PORT 8888
#define NL 1//75



using namespace std;
struct timeval begin , now;
int sockfd;

//Files
ofstream myfile("shoe_Left", ios::app);
ofstream myfile1("shoe_Right", ios::app);

typedef struct{ uint16_t count; 
		uint16_t S1[NL]; 
		uint16_t S2[NL]; 
		uint16_t S3[NL];
		uint16_t S4[NL]; 
		uint16_t S5[NL]; 
		uint16_t S6[NL]; 
		uint16_t S7[NL]; 
		uint16_t S8[NL]; 
		uint16_t endline;} pacote;

pacote buf;


//Functions

//errors
void err(char *);
//the thread function
void *connection_handler(void *);
//save data function
void save_data(void);
void save_data1(void);
//end connection, sock etc.
void terminator(int );

//
std_msgs::String msg;
ros::Publisher chatter_pub;
	

//MAIN
int main(int argc , char *argv[])
{

    ros::init(argc,argv,"ndnode");

	ros::NodeHandle n;
	chatter_pub = n.advertise<std_msgs::String>("data", 1000);
	
    struct sockaddr_in server , client;
    int  i; //int *new_sock;
    socklen_t slen=sizeof(client);
    //char buf[BUFLEN];
    char *aux;
    signal(SIGINT, terminator);
    signal(SIGTSTP, terminator);
	
    if ((sockfd = socket(AF_INET, SOCK_DGRAM, IPPROTO_UDP)) == -1)
	err("socket");
    else
	puts("Server : socket() successful");
 
    bzero(&server, sizeof(server));
    server.sin_family = AF_INET;
    server.sin_port = htons(PORT);
    server.sin_addr.s_addr = htonl(INADDR_ANY);


    if (bind(sockfd, (struct sockaddr*)&server, sizeof(server)) == -1)
	err("bind");
    else
        puts("Server : bind() successful\n");
	gettimeofday(&begin, NULL);
    while(1){
	i=recvfrom(sockfd, &buf, sizeof(buf), 0, (struct sockaddr*)&client, &slen) ;
	if(i==-1)
	    err("recvfrom()");
	
printf(" %d--", buf.count);
//printf(" %d\n ", buf.endline);

	//printf("Received %d bytes from %s:%d ----", i,inet_ntoa(client.sin_addr), ntohs(client.sin_port));
	aux= inet_ntoa(client.sin_addr);
	//printf("Ip : %d%d%d\n",aux[10]-'0', aux[11]-'0', aux[12]-'0');	
	if((aux[12]-'0') == 8)
	save_data();
	if((aux[12]-'0') == 0)
	save_data1();
    }
    close(sockfd); 
    return 0;
}

void save_data(void ){

    char string1[1000], string2[1000], string3[1000], string4[1000] ,string5[1000],string6[1000],string7[1000],string8[1000];
    double timediff;

    if(buf.endline == 333) {

	//printf(" end-line detected --> spliting received message...\n");	
		
	snprintf(string1,4,"%d", buf.S1[0]); 
	snprintf(string2,4,"%d", buf.S2[0]);
	snprintf(string3,4,"%d", buf.S3[0]);
	snprintf(string4,4,"%d", buf.S4[0]);
	snprintf(string5,4,"%d", buf.S5[0]);
	snprintf(string6,4,"%d", buf.S6[0]);
	snprintf(string7,4,"%d", buf.S7[0]);
	snprintf(string8,4,"%d", buf.S8[0]);

	strcat(string1, ","); strcat(string2, ","); strcat(string3, ","); strcat(string4, ","); 
	strcat(string5, ","); strcat(string6, ","); strcat(string7, ","); strcat(string8, ","); 

	for (int h=1; h<NL; h++){
	snprintf(string1+strlen(string1),4,"%d", buf.S1[h]); 
	snprintf(string2+strlen(string2),4,"%d", buf.S2[h]);
	snprintf(string3+strlen(string3),4,"%d", buf.S3[h]);
	snprintf(string4+strlen(string4),4,"%d", buf.S4[h]);
	snprintf(string5+strlen(string5),4,"%d", buf.S5[h]);
	snprintf(string6+strlen(string6),4,"%d", buf.S6[h]);
	snprintf(string7+strlen(string7),4,"%d", buf.S7[h]);
	snprintf(string8+strlen(string8),4,"%d", buf.S8[h]);

	strcat(string1, ","); strcat(string2, ","); strcat(string3, ","); strcat(string4, ","); 
	strcat(string5, ","); strcat(string6, ","); strcat(string7, ","); strcat(string8, ","); 
	}

	 //printf("--> saving data to file.\n\n");	
     printf("%s-%s-%s-%s-%s-%s-%s-%s\n",string1, string2,string3,string4,string5,string6,string7,string8);	
     
	 gettimeofday(&now, NULL);
	 timediff = (now.tv_sec - begin.tv_sec) + 1e-6 * (now.tv_usec - begin.tv_usec);

////

msg.data= string1;
msg.data+= string2;
msg.data+= string3;
msg.data+= string4;
msg.data+= string5;
msg.data+= string6;
msg.data+= string7;
msg.data+= string8;

chatter_pub.publish(msg);

////

	 myfile << buf.count << "," << string1  << string2  << string3  << string4 << string5  << string6 << string7  << string8 <<  timediff << "\n" ;
    }
}

void save_data1(void ){

  
   char string1[1000], string2[1000], string3[1000], string4[1000] ,string5[1000],string6[1000],string7[1000],string8[1000];
    double timediff;

    if(buf.endline == 333) {

	//printf(" end-line detected --> spliting received message...");	
		
	snprintf(string1,4,"%d", buf.S1[0]); 
	snprintf(string2,4,"%d", buf.S2[0]);
	snprintf(string3,4,"%d", buf.S3[0]);
	snprintf(string4,4,"%d", buf.S4[0]);
	snprintf(string5,4,"%d", buf.S5[0]);
	snprintf(string6,4,"%d", buf.S6[0]);
	snprintf(string7,4,"%d", buf.S7[0]);
	snprintf(string8,4,"%d", buf.S8[0]);

	strcat(string1, ","); strcat(string2, ","); strcat(string3, ","); strcat(string4, ","); 
	strcat(string5, ","); strcat(string6, ","); strcat(string7, ","); strcat(string8, ","); 

	for (int h=1; h<NL; h++){
	snprintf(string1+strlen(string1),4,"%d", buf.S1[h]); 
	snprintf(string2+strlen(string2),4,"%d", buf.S2[h]);
	snprintf(string3+strlen(string3),4,"%d", buf.S3[h]);
	snprintf(string4+strlen(string4),4,"%d", buf.S4[h]);
	snprintf(string5+strlen(string5),4,"%d", buf.S5[h]);
	snprintf(string6+strlen(string6),4,"%d", buf.S6[h]);
	snprintf(string7+strlen(string7),4,"%d", buf.S7[h]);
	snprintf(string8+strlen(string8),4,"%d", buf.S8[h]);

	strcat(string1, ","); strcat(string2, ","); strcat(string3, ","); strcat(string4, ","); 
	strcat(string5, ","); strcat(string6, ","); strcat(string7, ","); strcat(string8, ","); 
	}

	// printf("--> saving data to file.\n\n");	

	 gettimeofday(&now, NULL);
	 timediff = (now.tv_sec - begin.tv_sec) + 1e-6 * (now.tv_usec - begin.tv_usec);

////////////////////

//
	 myfile1 << buf.count << "," << string1  << string2  << string3  << string4 << string5  << string6 << string7  << string8 <<  timediff << "\n" ;
    }
}

void terminator(int sig){
	puts("Time to go.");
	myfile.close();
	fflush(stdout);
	close(sockfd); 
	exit(sig);
}

void err(char *str){
    perror(str); exit(1);
}
