#!/usr/bin/python
import rospy
from std_msgs.msg import String
import MySQLdb as mdb

import _mysql as sql

global n

n=0

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


def callback(data):	
    global n    
    n+=1
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
    d = data.data.split(",")
    print(d[0]);
    #db.query("INSERT INTO ITshoeData3 (ITshoe_id, data_date, read_number, s1,s2,s3,s4,s5,s6,s7,s8 ) VALUES (data.data,'DATA',123,1,2,3,4,5,6,7,8)");
    #cur.execute("INSERT INTO ITshoeData3 ('%s' ,'%s' ,%d ,%d ,%d ,%d ,%d ,%d ,%d ,%d ,%d)" % (writers[0], writers[1] ,1 ,2 ,3 ,4 ,5 ,6 ,7 ,8 ,9))
    sql1 = "INSERT INTO ITshoeData4 (ITshoe_id, data_date, read_number, s1,s2,s3,s4,s5,s6,s7,s8 ) VALUES (%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s)"
    val = ("192.168.8.85","12-02-2019",n,d[0],d[1],d[2],d[3],d[4],d[5],d[6],d[7],"experience N")
    cur.execute(sql1, val)
    db.commit()
    


def create_table(db):
	db.query("CREATE TABLE IF NOT EXISTS ITshoeData (IP varchar(15) DEFAULT NULL,DATE varchar(15) DEFAULT NULL,N int(11) DEFAULT NULL,s1 int(4) DEFAULT NULL,s2 int(4) DEFAULT NULL,s3 int(4) DEFAULT NULL,s4 int(4) DEFAULT NULL,s5 int(4) DEFAULT NULL,s6 int(4) DEFAULT NULL,s7 int(4) DEFAULT NULL,s8 int(4) DEFAULT NULL, other varchar(100) DEFAULT NULL)")		

create_table(db)

def create_table2(db):
	db.query("CREATE TABLE IF NOT EXISTS gaitpar (DATE varchar(15) DEFAULT NULL,distance float(15) DEFAULT NULL,MaxStepX float(4) DEFAULT NULL,MaxStepY float(5) DEFAULT NULL,MaxStepTheta float(5) DEFAULT NULL,MaxStepFrequency float(5) DEFAULT NULL,StepHeight float(5) DEFAULT NULL,other varchar(100) DEFAULT NULL)")		

create_table2(db)

sql2 = "INSERT INTO gaitpar (DATE, distance, MaxStepX , MaxStepY,MaxStepTheta,MaxStepFrequency,StepHeight,other ) VALUES (%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s)"
val2=  ("12-02-2019", "0.5", "0.02", "0.16", "0.349", "0.2", "0.02", "experience N")
cur.execute(sql2,val2)





def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    

    rospy.init_node('listener', anonymous=True)
  
    rospy.Subscriber("data", String, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
   