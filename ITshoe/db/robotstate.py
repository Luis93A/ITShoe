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
    #db.query("INSERT INTO ITshoeData3 (ITshoe_id, data_date, read_number, s1,s2,s3,s4,s5,s6,s7,s8 ) VALUES (data.data,'DATA',123,1,2,3,4,5,6,7,8)");
    #cur.execute("INSERT INTO ITshoeData3 ('%s' ,'%s' ,%d ,%d ,%d ,%d ,%d ,%d ,%d ,%d ,%d)" % (writers[0], writers[1] ,1 ,2 ,3 ,4 ,5 ,6 ,7 ,8 ,9))
    sql3 = "INSERT INTO robotjoint (DATE1,headyaw , headpitch , lshoulderpitch ,lshoulderroll ,lelbowyaw ,lelbowroll, lwristyaw , lhand , rshoulderpitch ,rshoulderroll ,relbowyaw ,relbowroll , rwristyaw , rhand , lhipyawpitch , rhipyawpitch , lhiproll ,lhippitch , lkneepitch ,lanklepitch ,lankleroll , rhiproll ,rhippitch , rkneepitch ,ranklepitch ,rankleroll , other ) VALUES (%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s,%s ,%s,%s ,%s,%s ,%s,%s ,%s,%s ,%s,%s ,%s,%s ,%s,%s ,%s,%s ,%s,%s ,%s)"
    val3 =  ("12-02-2019", d[0],d[1],d[2],d[3],d[4],d[5],d[6],d[7],d[8],d[9],d[10],d[11],d[12],d[13],d[14],d[15],d[16],d[17],d[18],d[19],d[20],d[21],d[22],d[23],d[24],d[25], "experience N")
    cur.execute(sql3, val3)
    db.commit()
    


def create_table3(db):
	db.query("CREATE TABLE IF NOT EXISTS robotjoint (DATE1 varchar(100) DEFAULT NULL,headyaw varchar(100) DEFAULT NULL, headpitch varchar(100) DEFAULT NULL, lshoulderpitch varchar(100) DEFAULT NULL,lshoulderroll varchar(100) DEFAULT NULL,lelbowyaw varchar(100) DEFAULT NULL,lelbowroll varchar(100) DEFAULT NULL, lwristyaw varchar(100) DEFAULT NULL, lhand varchar(100) DEFAULT NULL, rshoulderpitch varchar(100) DEFAULT NULL,rshoulderroll varchar(100) DEFAULT NULL,relbowyaw varchar(100) DEFAULT NULL,relbowroll varchar(100) DEFAULT NULL, rwristyaw varchar(100) DEFAULT NULL, rhand varchar(100) DEFAULT NULL, lhipyawpitch varchar(100) DEFAULT NULL, rhipyawpitch varchar(100) DEFAULT NULL, lhiproll varchar(100) DEFAULT NULL,lhippitch varchar(100) DEFAULT NULL, lkneepitch varchar(100) DEFAULT NULL,lanklepitch varchar(100) DEFAULT NULL,lankleroll varchar(100) DEFAULT NULL, rhiproll varchar(100) DEFAULT NULL,rhippitch varchar(100) DEFAULT NULL, rkneepitch varchar(100) DEFAULT NULL,ranklepitch varchar(100) DEFAULT NULL,rankleroll varchar(100) DEFAULT NULL, other varchar(100) DEFAULT NULL)")		


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
   