#!/usr/bin/env python
# -*- encoding: UTF-8 -*- 

'''Move To: Small example to make Nao Move To an Objective '''
'''         With customization '''

import sys
from naoqi import ALProxy
import time
from time import sleep
import qi
import sched, time
import rospy
from std_msgs.msg import String
import csv
import operator 
import numpy
from numpy import inf,nan

with open('awe.txt') as csv_file:
    csv_reader =csv.reader(csv_file,delimiter=',')
    line = []
    line_count = 0

    for lines in csv_reader:
      line.append(lines)
      
      

#ef main(robotIP):
 #  try:
  #     motionProxy = ALProxy("ALMotion", robotIP, 41739)#9559)
   #  	motionProxy1 = ALProxy("ALMotion", robotIP, 41739)#9559)
   #except Exception, e:
    #   print "Could not create proxy to ALMotion"
     #  print "Error was: ", e

    # Set NAO in stiffness On
  #  StiffnessOn(motionProxy)

    #motionProxy.setStiffnesses("Head", 1.0)

    # Example showing how to set angles, using a fraction of max speed
 
	
    # This example show customization for the both foot
    # with all the possible gait parameters
    #motionProxy.post.moveTo(0.2, 0, 0,
     #       [ ["MaxStepX", 0.02],         # step of 5 cm in front[0.055, 0.02]
      #        ["MaxStepY", 0.16],         # default value
       #       ["MaxStepTheta", 0.349],      # default value
        #      ["MaxStepFrequency", 0.2],  # low frequency
         #     ["StepHeight", 0.02],   # step height of 1 cm [0.033, 0.6]
          #    ["TorsoWx", 0.0],           # default value
           #   ["TorsoWy", 0.0] ])         # torso bend 0.1 rad in front



def check(list1,val):
  count = 0;
  for x in list1:
 #   print x
    count += 1;
    if x >= val :
      #print "_______________________"
     # print "Joint: "+str(count)+ "\n"+"Error(0-1): "+ str(x)
      return True
  return False

#def divide (n,d):
 # h= []
  #i=0;
  #for x,y in zip(n,d):
  #  if x == 0: 
  #    x =0.00001;
  #  h[i]=numpy.abs(x)/numpy.abs(y)
  #  print h[i]
  #  i+=1
  #return h

def talker(robotIP):

    try:  
        motionProxy = ALProxy("ALMotion", robotIP, 36421)#9559
        motionProxy1 = ALProxy("ALMotion", robotIP, 36421)
        pProxy = ALProxy("ALRobotPosture", robotIP, 36421)
        #37149)#9559)
    except Exception, e:
        print "Could not create proxy to ALMotion"
        print "Error was: ", e

    # Set NAO in stiffness On
  #  StiffnessOn(motionProxy)

    motionProxy.setSmartStiffnessEnabled(True)
   #"RHipYawPitch",
    names = ["RHipRoll" ,"RHipPitch" , "RKneePitch" ,"RAnklePitch" ,"RAnkleRoll", "LHipYawPitch"  , "LHipRoll" ,"LHipPitch" , "LKneePitch" ,"LAnklePitch","LAnkleRoll", "RShoulderPitch" ,"RShoulderRoll" ,"RElbowYaw" ,"RElbowRoll" , "RWristYaw", "LShoulderPitch" ,"LShoulderRoll" ,"LElbowYaw" ,"LElbowRoll", "LWristYaw", "HeadYaw" , "HeadPitch" ]
   # Example showing how to set angles, using a fraction of max speed
    #names = "HeadYaw"
    pnames = 'Body'
    pstif= 1.0
    ptime= 1.0
    motionProxy.setStiffnesses(pnames,pstif)


    sleep(1)

    fractionMaxspeed = 0.2
        #home = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.03489999845624,0,0,0,0,-0.034899950027466,0,0,0]
    #motionProxy.setAngles( names, home, fractionMaxspeed)
    #a=cb.enablePowerMonitoring(True)
   # pProxy.goToPosture("StandZero",1)
  
    angles= [float(line[0][k]) for k in range(1,24)]
    motionProxy.angleInterpolation( names, angles,1, True)
    start_time_sent = time.time()
    #
    interval =1.0
           
    #
    c1=0
    for i in range(1,814,1): #1022
       
       #angles = [ float(line[i][0]),float(line[i][1]),float(line[i][2]),float(line[i][3]),float(line[i][4]),float(line[i][5]),float(line[i][6]),float(line[i][7]),float(line[i][8]),float(line[i][9]),float(line[i][10]),float(line[i][11]),float(line[i][12]),float(line[i][13]),float(line[i][14]),float(line[i][15]),float(line[i][16]),float(line[i][17]),float(line[i][18]),float(line[i][19]),float(line[i][20]),float(line[i][21]),float(line[i][22]), float(line[i][23]) ]
       angles= [float(line[i][k]) for k in range(1,24)]
       
       motionProxy.angleInterpolation( names, angles,0.04, True)
       #motionProxy.wait(id,0)
       
      # sss= motionProxy.getSummary()
       #print sss
       useSensor = True
       
       angles1= motionProxy1.getAngles( names, useSensor)

       #print angles1
       wht = map(operator.sub, angles1, angles)
       #start_time_get = time.time()
       wht1= map(operator.truediv, numpy.abs(wht), numpy.abs(angles) )
       print wht1
       
       while check(wht1,0.01):#wht[0] > 0.01: 
       #  print "wht > error limit " + str(i) 
         #next_get = (time.time() - start_time_get)
       #  if next_get > 0.1: 
        #    break
        # print c1
         angles1= motionProxy1.getAngles( names, useSensor)  
         #print angles1
         wht = map(operator.sub, angles1, angles)
         wht1= map(operator.truediv, numpy.abs(wht), numpy.abs(angles) )
         #c1+=1
         for j in range(0,23):
            if wht1[j] == inf or wht1[j] == nan:
                wht1[j] = 0
       
       next_get = (time.time() - start_time_sent)
       print next_get

       #next_in = (time.time() - start_time_sent)   
       #if next_in < 0.1 : 
        #    sleep(0.1 - next_in)     
       
         #print wht1
         #print "________________"
         #print angles
         #print angles1
         #print angles1
         #if c1 >= 1000:
          #  print "____________________________________________________________________________________________________"
          #  break
         #print "   " + str(c1)
    #names ="LHipYawPitch"
    #angles = -1.12
    #motionProxy.setAngles( names, angles, fractionMaxspeed)
    #useSensor = True

   # angles1= motionProxy1.getAngles( names, useSensor)
   # print angles1[0]
         #print wht

    print "cycle finished"  

      #wht=map(operator.sub, 0.2010, angles1)
     # while float(angles1[0])-0.4 < 0.01:
      #  print float(angles1[0])
       # sleep(0.02)
        #angles1= motionProxy1.getAngles( names, useSensor)
     # while angles1 - angles > 0.001
         
   # while   
    #  motionProxy1.getAngles( names, angles, fractionMaxspeed)
	   # if getangles - setangles ( ) / setangles < 1% 
    
    # This example show customization for the both foot
    # with all the possible gait parameters
  
     


if __name__ == "__main__":
    robotIP = "127.0.0.1"#"192.168.8.65"#

    if len(sys.argv) <= 1:
        print "Usage python motion_moveToCustomization.py robotIP (optional default: 127.0.0.1)"
    else:
        robotIp = sys.argv[1]
    
    try:
    	  talker(robotIP)
    except rospy.ROSInterruptException:
        pass

    #
    #ain(robotIp)

    






