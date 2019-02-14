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



#def main(robotIP):
 #   try:
   #     motionProxy = ALProxy("ALMotion", robotIP, 41739)#9559)
 #	motionProxy1 = ALProxy("ALMotion", robotIP, 41739)#9559)
  #  except Exception, e:
   #     print "Could not create proxy to ALMotion"
    #    print "Error was: ", e

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
    

def talker(robotIP):

    try:
        motionProxy = ALProxy("ALMotion", robotIP, 41739)#9559)
 	motionProxy1 = ALProxy("ALMotion", robotIP, 41739)#9559)
    except Exception, e:
        print "Could not create proxy to ALMotion"
        print "Error was: ", e

    # Set NAO in stiffness On
  #  StiffnessOn(motionProxy)

    motionProxy.setStiffnesses("Head", 1.0)

    # Example showing how to set angles, using a fraction of max speed
 
	
    # This example show customization for the both foot
    # with all the possible gait parameters
    motionProxy.post.moveTo(0.2, 0, 0,
            [ ["MaxStepX", 0.02],         # step of 5 cm in front[0.055, 0.02]
              ["MaxStepY", 0.16],         # default value
              ["MaxStepTheta", 0.349],      # default value
              ["MaxStepFrequency", 0.2],  # low frequency
              ["StepHeight", 0.02],   # step height of 1 cm [0.033, 0.6]
              ["TorsoWx", 0.0],           # default value
              ["TorsoWy", 0.0] ])        
	
    pub = rospy.Publisher('state', String, queue_size=1000)
    rospy.init_node('talker', anonymous=True)
    t_sec= time.time()
    i=0;
     
    while motionProxy.moveIsActive():
	    names         = "Body"
	    useSensors    = False
	    commandAngles = motionProxy1.getAngles(names, useSensors)
	    #print "Command angles:"
	    #print str(commandAngles)
            pub.publish(str(commandAngles))
	    print i
            print ""
    	    i=i+1
            t_sic = time.time()    
	    print t_sic-t_sec 
            


if __name__ == "__main__":
    robotIP = "127.0.0.1"#"192.168.8.65"

   # if len(sys.argv) <= 1:
    #    print "Usage python motion_moveToCustomization.py robotIP (optional default: 127.0.0.1)"
    #else:
     #   robotIp = sys.argv[1]
    
    try:
    	talker(robotIP)
    except rospy.ROSInterruptException:
        pass

    #main(robotIp)

    






