#!/usr/bin/python
import rospy
from std_msgs.msg import String
import MySQLdb as mdb

import _mysql as sql


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


def callback(state):	
    # rospy.loginfo(rospy.get_caller_id() + "I heard %s", state.data)
    d = state.data.split(",")
    #db.query("INSERT INTO ITshoeData3 (ITshoe_id, data_date, read_number, s1,s2,s3,s4,s5,s6,s7,s8 )

    # VALUES (data.data,'DATA',123,1,2,3,4,5,6,7,8)");
    #cur.execute("INSERT INTO ITshoeData3 ('%s' ,'%s' ,%d ,%d ,%d ,%d ,%d ,%d ,%d ,%d ,%d)" % (writers[0], writers[1] ,1 ,2 ,3 ,4 ,5 ,6 ,7 ,8 ,9))
    sql3 = "INSERT INTO rj4 (DATE1,RHipRoll ,RHipPitch, RKneePitch ,RAnklePitch ,RAnkleRoll, LHipYawPitch, LHipRoll ,LHipPitch, LKneePitch,LAnklePitch,LAnkleRoll, RShoulderPitch,RShoulderRoll ,RElbowYaw ,RElbowRoll , RWristYaw, LShoulderPitch ,LShoulderRoll ,LElbowYaw ,LElbowRoll, LWristYaw, HeadYaw , HeadPitch ) VALUES (%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s,%s ,%s,%s ,%s,%s ,%s,%s ,%s,%s ,%s,%s ,%s, %s ,%s,%s ,%s)"
    val3 =  (d[0],d[1],d[2],d[3],d[4],d[5],d[6],d[7],d[8],d[9],d[10],d[11],d[12],d[13],d[14],d[15],d[16],d[17],d[18],d[19],d[20],d[21],d[22],d[23])
    cur.execute(sql3, val3)
    db.commit()
    
   
def create_table3(db):
	db.query("CREATE TABLE IF NOT EXISTS rj4 ( DATE1 varchar(25) DEFAULT NULL,RHipRoll varchar(25) DEFAULT NULL,RHipPitch varchar(25) DEFAULT NULL, RKneePitch varchar(25) DEFAULT NULL,RAnklePitch varchar(25) DEFAULT NULL,RAnkleRoll varchar(25) DEFAULT NULL, LHipYawPitch varchar(25) DEFAULT NULL, LHipRoll varchar(25) DEFAULT NULL, LHipPitch varchar(25) DEFAULT NULL,LKneePitch varchar(25) DEFAULT NULL,LAnklePitch varchar(25) DEFAULT NULL,LAnkleRoll varchar(25) DEFAULT NULL,RShoulderPitch varchar(25) DEFAULT NULL, RShoulderRoll varchar(25) DEFAULT NULL, RElbowYaw varchar(25) DEFAULT NULL, RElbowRoll varchar(25) DEFAULT NULL,RWristYaw varchar(25) DEFAULT NULL,LShoulderPitch varchar(25) DEFAULT NULL,LShoulderRoll varchar(25) DEFAULT NULL, LElbowYaw varchar(25) DEFAULT NULL,LElbowRoll varchar(25) DEFAULT NULL,LWristYaw varchar(25) DEFAULT NULL, HeadYaw varchar(25) DEFAULT NULL,HeadPitch varchar(25) DEFAULT NULL)")		


create_table3(db)



def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    

    rospy.init_node('listener', anonymous=True)
  
    rospy.Subscriber("state", String, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
   