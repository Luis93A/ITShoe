#!/usr/bin/python
import rospy
from std_msgs.msg import String
import MySQLdb as mdb
from naoqi import ALProxy
import _mysql as sql
import time
from time import sleep
import sys
from naoqi import ALProxy
import qi
import sched, time
import rospy
from std_msgs.msg import String
import csv
import operator 
import numpy
from numpy import inf,nan

def check(list1,val):
  count = 0;
  for x in list1:
    #print "joint: " +str(count)+ " " +str(x)
    count += 1;
    if x >= val:
        if count <= 12:
            # "_______________________"
            #print "Joint: "+str(count)+ "\n"+"Error(0-1): "+ str(x)
            return True
  return False

def Connect_DB():
        try:
            db=mdb.connect(host = 'localhost', user = 'root', passwd = 'shinobi39', db = 'itshoedata', port =3306 )
            print("Connected W DB")
            return db 

        except:
            print("Deu erro")
			
db = Connect_DB()			
def Disconnect_DB():
        try:
            #cur.close()
            db.close()
            
        except:
            print("Error closing DB COM")
			

cur = db.cursor()

def main(robotIP):

  try:  
        motionProxy = ALProxy("ALMotion", robotIP,9559)#9559
        motionProxy1 = ALProxy("ALMotion", robotIP, 9559)
        pProxy = ALProxy("ALRobotPosture", robotIP, 9559)
        #37149)#9559)
  except Exception, e:
        print "Could not create proxy to ALMotion"
        print "Error was: ", e


  names = ["RHipRoll" ,"RHipPitch" , "RKneePitch" ,"RAnklePitch" ,"RAnkleRoll", "LHipYawPitch"  , "LHipRoll" ,"LHipPitch" , "LKneePitch" ,"LAnklePitch","LAnkleRoll"]#, "RShoulderPitch" ,"RShoulderRoll" ,"RElbowYaw" ,"RElbowRoll" , "RWristYaw", "LShoulderPitch" ,"LShoulderRoll" ,"LElbowYaw" ,"LElbowRoll", "LWristYaw" ]
 
  #pnames = 'Body'
  #pstif= 1.0
  #ptime= 1.0
  #motionProxy.setStiffnesses(pnames,pstif)
  
  #print "here1"
  a= "select * from rj4"
  cur.execute(a)
  records= cur.fetchall()
  row = []
  for rows in records:
    row.append(rows)

  angles= [row[117][k] for k in range(1,12)]
  angles[0] = ''.join(h for h in angles[0] if not h== "[")
  #angles[22] = ''.join(h for h in angles[20] if not h== "]")
  for j in range(0,11):
    angles[j] = float(angles[j])
  motionProxy.angleInterpolation( names, angles,2, True) 
  
  #print "here2"  
  for i in range(117,8400,16):
      angles= [row[i][k] for k in range(1,12)]
      angles[0] = ''.join(h for h in angles[0] if not h== "[")
     # angles[22] = ''.join(h for h in angles[22] if not h== "]")
      for j in range(0,11):
        angles[j] = float(angles[j])
        #print angles[j]
      
      useSensor = False
      
      angles1= motionProxy1.getAngles( names, useSensor)
      
      wht = map(operator.sub, angles1, angles)
       #start_time_get = time.time()
      wht1= map(operator.truediv, numpy.abs(wht), numpy.abs(angles) )
      #print angles
      #print angles1
      
      while check(wht1,0.01):
         id=motionProxy.post.setAngles( names, angles,0.1) 
         motionProxy.wait(id,0)
         angles1= motionProxy1.getAngles( names, useSensor)  
         #print angles
         #print angles1
         #motionProxy.post.setAngles( names, angles,0.4) 
         
         wht = map(operator.sub, angles1, angles)
         wht1= map(operator.truediv, numpy.abs(wht), numpy.abs(angles) )
         #c1+=1
        # print wht1
         for j in range(0,10):
            if wht1[j] == inf or wht1[j] == nan:
                wht1[j] = 0
         #print i
      #print "here3"
  angles= [row[117][k] for k in range(1,12)]
  angles[0] = ''.join(h for h in angles[0] if not h== "[")
  #angles[22] = ''.join(h for h in angles[20] if not h== "]")
  for j in range(0,11):
    angles[j] = float(angles[j])
  motionProxy.angleInterpolation( names, angles,2, True)     
  print "finished"
if __name__ == "__main__":
    robotIP = "192.168.8.65"#"127.0.0.1"#"192.168.8.65"
    main(robotIP)
