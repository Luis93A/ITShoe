#include <TimerOne.h> //IT IS NECESSARY TO DOWNLOAD THE LIBRARY TIMERONE
#include <SoftwareSerial.h>

typedef struct{ uint16_t count;
                uint16_t S1;
                uint16_t S2;
                uint16_t S3;
                uint16_t S4;
                uint16_t S5;
                uint16_t S6;
                uint16_t S7;
                uint16_t S8;
                uint16_t endline;} pacote;

pacote T1;
#define DEBUG false
#define TIMER_US 1000000

SoftwareSerial esp8266(10,11); // make RX Arduino line is pin 10, make TX Arduino line is pin 11.


int  flexiForcePin0 = A0; //analog pin 0
int  flexiForcePin1 = A1; //analog pin 1
int  flexiForcePin2 = A2; //analog pin 2
int  flexiForcePin3 = A3; //analog pin 4
int  flexiForcePin4 = A4; //analog pin 5
int  flexiForcePin5 = A5; //analog pin 6
int  flexiForcePin6 = A6; //analog pin 7
int  flexiForcePin7 = A7; //analog pin 8

  
void setup() {

  Serial.begin(115200);

  //WIFI ESP- CONFIG,RUN WIFI - BEGIN
  esp8266.begin(115200); //  esp's baud rate 

  sendData("AT+RST\r\n",2000,DEBUG); // reset module
  sendData("AT+CWMODE=1\r\n",2000,DEBUG); // configure as access point
  sendData("AT+CWJAP=\"test\",\"\"\r\n", 8000, DEBUG); //ifconfig pa ver o ip do pc pa por cipstart
  sendData("AT+CIPMUX=0\r\n",1000,DEBUG);
  sendData("AT+CIPSTART=\"UDP\",\"192.168.8.1\",8888,8889,0\r\n", 8000, DEBUG);
  //WIFI ESP- CONFIG,RUN WIFI - END


 Timer1.initialize(1000000);                  // Initialise timer 1
 Timer1.attachInterrupt( timerIsr, 10000);
  
}

void loop() {

}


void timerIsr(void)
{ 
  

 T1.count = T1.count + 1;


  T1.S1= safeAnalogRead(flexiForcePin0);
  T1.S2= safeAnalogRead(flexiForcePin1);
  T1.S3= safeAnalogRead(flexiForcePin2);
  T1.S4= safeAnalogRead(flexiForcePin3);
  T1.S5= safeAnalogRead(flexiForcePin4);
  T1.S6= safeAnalogRead(flexiForcePin5);
  T1.S7= safeAnalogRead(flexiForcePin6);
  T1.S8= safeAnalogRead(flexiForcePin7);
  
 

 T1.endline = 333;
 
 String cipSend = "AT+CIPSEND=";
 cipSend += sizeof(T1) ;
 cipSend +="\r\n";
 
 esp8266.print(cipSend);
 delayMicroseconds(1000);

 //String Force_data = cc + "," + a0 + ","+ a1 + ","+a2  + ","+ a3  + ","+ a4  + ","+ a5  +","+  a6 +","+  a7 +","+ "A";

 esp8266.write((uint8_t*)&T1 ,sizeof(T1));
}



//FUNCTIONS

//SERVER SEND DATA function

String sendData(String command, const int timeout, boolean debug)
{
    String response = "";
    
    esp8266.print(command); // send the read character to the esp8266
    
    long int time1 = millis();
    
    while( (time1+timeout) > millis())
    {
      while(esp8266.available())
      {
        
        // The esp has data so display its output to the serial window 
        char c = esp8266.read(); // read the next character.
        response+=c;
      }  
    }
    
    if(debug)
    {
      Serial.print(response);
    }
    
    return response;
}


//Safe analog read function
int safeAnalogRead(int pin)
{
  int x = analogRead(pin);  // make an initial reading to set up the ADC
  delayMicroseconds(250) ;           // let the ADC stabilize
  x = analogRead(pin);      // toss the first reading and take one we will keep
  delayMicroseconds(100) ;            // delay again to be friendly to future readings
  return x;
  
}




