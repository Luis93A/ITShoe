#!/usr/bin/python2

################## imports ########
##### tkinter ######
from Tkinter import *
import Tkinter as tk
import tkMessageBox
from PIL import Image, ImageTk

##### ROS ######
#include "ros/ros.h"
import rospy
from std_msgs.msg import String 

##### others ######
import math
import os
from math import *
from time import sleep
import sys
import time
import sched, time
import re 
import numpy as np
import threading
import socket
import struct
import csv
import qi
from threading import Timer
from collections import namedtuple
from pprint import pprint
global offset_fnright, offset_fnleft
offset_fnright = 0
offset_fnleft = 0
#### db ######
import MySQLdb as mdb
import _mysql as sql

#### naoqi ######
from naoqi import ALProxy

#### matlab #####
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

#include "std_msgs/String.h"

###### Structure to receive data from ITshoe ######
MyStruct = namedtuple("MyStruct", "count s1 s2 s3 s4 s5 s6 s7 s8 endline")
i=0

##### attempt to add scroll to the main window #####
class VerticalScrolledFrame(Frame):
    """A pure Tkinter scrollable frame that actually works!
    * Use the 'interior' attribute to place widgets inside the scrollable frame
    * Construct and pack/place/grid normally
    * This frame only allows vertical scrolling

    """
    def __init__(self, parent, *args, **kw):
        Frame.__init__(self, parent, *args, **kw)            

        # create a canvas object and a vertical scrollbar for scrolling it
        vscrollbar = Scrollbar(self, orient=VERTICAL)
        vscrollbar.pack(fill=Y, side=RIGHT, expand=FALSE)
        canvas = Canvas(self, bd=0, highlightthickness=0,
                        yscrollcommand=vscrollbar.set)
        canvas.pack(side=LEFT, fill=BOTH, expand=TRUE)
        vscrollbar.config(command=canvas.yview)

        # reset the view
        canvas.xview_moveto(0)
        canvas.yview_moveto(0)

        # create a frame inside the canvas which will be scrolled with it
        self.interior = interior = Frame(canvas)
        interior_id = canvas.create_window(0, 0, window=interior,
                                           anchor=NW)

        # track changes to the canvas and frame width and sync them,
        # also updating the scrollbar
        def _configure_interior(event):
            # update the scrollbars to match the size of the inner frame
            size = (interior.winfo_reqwidth(), interior.winfo_reqheight())
            canvas.config(scrollregion="0 0 %s %s" % size)
            if interior.winfo_reqwidth() != canvas.winfo_width():
                # update the canvas's width to fit the inner frame
                canvas.config(width=interior.winfo_reqwidth())
        interior.bind('<Configure>', _configure_interior)

        def _configure_canvas(event):
            if interior.winfo_reqwidth() != canvas.winfo_width():
                # update the inner frame's width to fill the canvas
                canvas.itemconfigure(interior_id, width=canvas.winfo_width())
        canvas.bind('<Configure>', _configure_canvas)


##### super class ####### manages connections, receiveis and forwards data throught ros topics.. , so on
class super1():

##### TK ROOT #####
	root = Tk()

	# GLOBAL VARIABLES
	#sys.setrecursionlimit(1000000)

	#trigger to start recording data
	global recording_data 
	recording_data= False

	#trigger to stop robot motion
	global dc_button 

	#connection variables with robot and itshoes 
	entry_IP = StringVar()
	entry_IP_itshoe_L = StringVar()
	entry_IP_itshoe_R =StringVar()
	entry_PORT = StringVar()
	display_textR= StringVar()
	UDP_IP_ADDRESS = StringVar()
	UDP_PORT_NO =8888
	global ip_sapato
	global LFsrFL,	LFsrFR,	LFsrBL,	LFsrBR,	RFsrFL,	RFsrFR,	RFsrBL,	RFsrBR,	COP_lx,	COP_ly,	COP_rx,	COP_ry
	global fn_left, fn_right
	global x_right, x_left
	x_right = 0
	x_left =0
	global fhmovX, fhmovY
	fhmovX = []
	fhmovY = []
	LFsrFL =float()
	LFsrFR= float()
	LFsrBL=float()
	LFsrBR=float()
	RFsrFL=float()
	RFsrFR=float()
	RFsrBL=float()
	RFsrBR=float()
	COP_lx=float()
	COP_ly=float()
	COP_rx=float()
	COP_ry=float()


	#global robot proxys and variables
	motionProxy = StringVar()
	batteryProxy = StringVar()
	Step_length= StringVar()
	ydistance = StringVar()
	rotation = StringVar()
	Step_frequency= StringVar()
	distance = StringVar()
	batt=StringVar()
	Step_torsowx = StringVar()
	Step_torsowy = StringVar()
	Step_height = StringVar()
	countShoe =np.zeros((100,1))
	global dcm
	global GyrX , GyrY,	GyrZ,	angX,	angY,	angZ,	accX,	accY,	accZ
	global GyrX_inp ,GyrY_inp ,GyrZ_inp ,angX_inp ,angY_inp ,angZ_inp, accX_inp, accY_inp, accZ_inp
	GyrX_inp = []
	GyrY_inp = []
	GyrZ_inp = []
	angX_inp = []
	angY_inp = []
	angZ_inp = []
	accX_inp = []
	accY_inp = []
	accZ_inp = []
	GyrX =float()
	GyrY=float()
	GyrZ=float()
	angX=float()
	angY=float()
	angZ=float()
	accX=float()
	accY=float()
	accZ=float()

	#database variables
	db_table = StringVar()
	var_additional_info=StringVar()
	db = StringVar()
	db1= StringVar()
	cur = StringVar()
	cur1 = StringVar()
	db_table_name1=StringVar()
	db_table_info=StringVar()

	#robot COP buffer
	Lcop_buffer_x =np.zeros((101,1))
	Lcop_buffer_y=np.zeros((101,1))

	#sensors
	global sensor1L5, sensor1L6 ,sensor1L7 ,sensor1L8 ,sensor25L1, sensor25L2 ,sensor25L3 ,sensor25L4 ,sensor1R5 ,sensor1R6 ,sensor1R7 , sensor1R8 
	global sensor25R1 ,sensor25R2 , sensor25R3 , sensor25R4 
	offsetR = StringVar()
	offsetL = StringVar()
	offsetR.set(0)
	offsetL.set(0)
	global printfn
	printfn = 1
	global printfn_l
	printfn_l = 1


	#others variables
	global var 
	countRobot = 1
	global button_move11
	global helpme
	helpme= 1
	global t0, t0_dcm
	t0 = 0
	t0_dcm = 0
	global aux_net_left
	aux_net_left =0
	global aux_net_right
	aux_net_right = 0
	global nn_ip
	global cs_button
	var= IntVar()
	AFT_L= 0
	AFT_R = 0
	global my_data
	entry_IP_itshoe_Lapato=0
	server_socket=StringVar()
	
# Make a regular expression 
# for validating an Ip-address 
	regex = '''^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
	            25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
	            25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
	            25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)'''
 
# validate an Ip addess 


#def click save to save all data to file, later to db, since it requires more time to record to db.
	def click_to_save(self):
		global LFsrFL,	LFsrFR,	LFsrBL,	LFsrBR,	RFsrFL,	RFsrFR,	RFsrBL,	RFsrBR,	COP_lx,	COP_ly,	COP_rx,	COP_ry
		global GyrX ,	GyrY,	GyrZ,	angX,	angY,	angZ,	accX,	accY,	accZ
		global sensor1L5, sensor1L6, sensor1L7, sensor1L8, sensor25L1 ,sensor25L2,sensor25L3,sensor25L4 
		global sensor1R5, sensor1R6, sensor1R7, sensor1R8, sensor25R1, sensor25R2, sensor25R3, sensor25R4
		global dcm
		global helpme
		global t0 , t0_dcm ,cs_button

		cs_button.configure(bg = "blue")
		if helpme ==1:
			print("Recording to file... ")
			t0= time.time()
			#print(t0)
			t0_dcm=dcm.getTime(0)

		while(True):
			t1= time.time()
			t1_dcm = dcm.getTime(0)
			
			
			STFile = [t1,sensor1L5, sensor1L6, sensor1L7, sensor1L8, sensor25L1 ,sensor25L2,sensor25L3,sensor25L4,sensor1R5, sensor1R6, sensor1R7, sensor1R8, sensor25R1, sensor25R2, sensor25R3, sensor25R4,t1_dcm,LFsrFL,LFsrFR,LFsrBL,LFsrBR,RFsrFL,RFsrFR,RFsrBL,RFsrBR,COP_lx,COP_ly,COP_rx,COP_ry,GyrX,GyrY,GyrZ,angX,angY,angZ,accX,accY,accZ]
			#print(STFile)
			with open('Aludata.csv', mode ='a') as teste_file:
				teste_writer =csv.writer(teste_file, delimiter=',')
				teste_writer.writerow(STFile)

			helpme = 0
			
			#make it save at 100 hz rate
			time.sleep(0.01- ((time.time()-t1) % 0.01))
			
		
#def to publish data as inputs for neural network node
	def publish_to_network(self):
		global fhmovX, fhmovY, GyrX_inp ,GyrY_inp ,GyrZ_inp ,angX_inp ,angY_inp ,angZ_inp, accX_inp, accY_inp, accZ_inp, nn_ip 
		#print("finalmente entrei aqui")
		#rospy.init_node('talker', anonymous = 'True', disable_signals = True)
		#self.thread_save_from_topic()
		if nn_ip == 6:
			pub= rospy.Publisher("/data_nn", String, queue_size =1)
			print("writting left shoedata for nn..") 
			
		if nn_ip == 4:
			pub= rospy.Publisher("/data_nn1", String, queue_size=1)
			print("writting right shoedata for nn..")
			
		send_msg = [fhmovX , fhmovY ,GyrX_inp , GyrY_inp  ,GyrZ_inp,  angX_inp ,angY_inp,angZ_inp,  accX_inp,  accY_inp, accZ_inp]
		pub.publish(str(send_msg))

		#record_msg = [nn_ip, fhmovX , fhmovY ,GyrX_inp , GyrY_inp  ,GyrZ_inp,  angX_inp ,angY_inp,angZ_inp,  accX_inp,  accY_inp, accZ_inp]
		#with open('Steps111.csv', mode ='a') as teste_file:
		#		teste_writer =csv.writer(teste_file, delimiter=',')
		#		teste_writer.writerow(record_msg)

		fhmovX = []
		fhmovY = []
		GyrZ_inp = []
		GyrY_inp= []
		GyrX_inp= []
		angX_inp= []
		angY_inp= []
		angZ_inp= []
		accX_inp= []
		accY_inp= []
		accZ_inp= []
		
		#debug
		print("publiquei algo")


#gather the first 50points of each step to send to def save that will forward to the network node
	def save_from_topic_callback(self,msg):
		global AFT_L, AFT_R, ip_sapato
		global sensor1L5, sensor1L6, sensor1L7, sensor1L8, sensor25L1 ,sensor25L2,sensor25L3,sensor25L4 
		global sensor1R5, sensor1R6, sensor1R7, sensor1R8, sensor25R1, sensor25R2, sensor25R3, sensor25R4
		global LFsrFL,	LFsrFR,	LFsrBL,	LFsrBR,	RFsrFL,	RFsrFR,	RFsrBL,	RFsrBR,	COP_lx,	COP_ly,	COP_rx,	COP_ry,	GyrX ,	GyrY,	GyrZ,	angX,	angY,	angZ,	accX,	accY,	accZ
		global t0 , t0_dcm 
		global fn_left, fn_right
		global x_right, x_left
		global aux_net_left
		global aux_net_right, nn_ip 
		global fhmovX, fhmovY, GyrX_inp ,GyrY_inp ,GyrZ_inp ,angX_inp ,angY_inp ,angZ_inp, accX_inp, accY_inp, accZ_inp
		global offset_fnright, offset_fnleft
		global printfn, printfn_l
		a= msg.data

		#default 
		
		AFT_L=0
		AFT_R=0
		#print(dir(a))
		#print(a)#			rospy.loginfo(rospy.get_caller_id() + "I heard %s", str(String.data))
		
		#offsetR.set("")
		#offsetL.set("")
		aa= a.split(",")
		#print(aa)
		#print(aa[0])
		#add client que publica o ip do sapato
		#if sapato tal values R if tal values L make globals to be used all around
		ip_sapato = int(aa[0])
		#print(ip_sapato)
		#print(ip_sapato)

		#right itshoe calibration curves
		if ip_sapato == 4:# right itshoe
			
			sensor25R1 = math.exp(((float(aa[4]) + 124.13)/162.04))
			sensor25R2 = math.exp(((float(aa[2]) + 99.792)/149.78))
			sensor25R3 = math.exp(((float(aa[7]) + 108.92)/144.13))
			sensor25R4 = math.exp(((float(aa[5]) + 187.42)/151.69))

			sensor1R5 = math.exp(((float(aa[3]) + 33.103)/156.63))
			sensor1R6 = math.exp(((float(aa[1]) + 62.183)/157.88))
			sensor1R7 = math.exp(((float(aa[8]) + 46.256)/160.14))
			sensor1R8 = math.exp(((float(aa[6]) + 49.447)/154.53))

			fn_right = sensor25R1 + sensor25R2 + sensor25R3 + sensor25R4 - offset_fnright;
			printfn = printfn +1
			if printfn == 300:

				label_fnR = tk.Label(self.root, text=" Fn right: " + str(round(fn_right,2)))
				label_fnR.grid(row = 17,column = 2, pady=1, padx =1)
			
				fnRoffset_label=tk.Label(self.root, text="Fn offset right:").grid(row = 18,column = 2, pady=1, padx =1)
				fnRoffset_entry = tk.Entry(self.root,textvariable=self.offsetR).grid(row = 19,column = 2, pady=1, padx =1)

				offset_fnright =  float(self.offsetR.get())
				printfn =0

			if fn_right < 10 and fn_right > -50 and aux_net_right == 0:
				aux_net_right= 1
				x_right = 0
				#print("menor de 10N")

			if fn_right > 10 and aux_net_right == 1 and x_right < 50:
				
				fhmovX.append(-sensor1R5*0.7071 + sensor1R6*0.7071 -sensor1R7*0.7071 + sensor1R8*0.7071);
				fhmovY.append(sensor1R5*0.7071 + sensor1R6*0.7071 -sensor1R7*0.7071 - sensor1R8*0.7071); 
				GyrX_inp.append(GyrX)
				GyrY_inp.append(GyrY)
				GyrZ_inp.append(GyrZ)
				angX_inp.append(angX)
				angY_inp.append(angY)
				angZ_inp.append(angZ)
				accX_inp.append(accX)
				accY_inp.append(accY)
				accZ_inp.append(accZ)
				x_right=x_right+1

				record_msg = [x_right, -sensor1R5*0.7071 + sensor1R6*0.7071 -sensor1R7*0.7071 + sensor1R8*0.7071, sensor1R5*0.7071 + sensor1R6*0.7071 -sensor1R7*0.7071 - sensor1R8*0.7071, GyrX, GyrY, GyrZ, angX , angY, angZ, accX, accY, accZ]
				with open('Steps3.csv', mode ='a') as teste_file:
					teste_writer =csv.writer(teste_file, delimiter=',')
					teste_writer.writerow(record_msg)
				#debug
				


			if x_right== 49: 
				aux_net_right= 0
				x_right = 0
				nn_ip = ip_sapato
				self.publish_to_network()
				

			#sensor25R1 = float(aa[1]) 
			#sensor25R2 = float(aa[3]) 
			#sensor25R3 = float(aa[6]) 
			#sensor25R4 = float(aa[8]) 

			#sensor1R5 = float(aa[2]) 
			#sensor1R6 = float(aa[4]) 
			#sensor1R7 = float(aa[5]) 
			#sensor1R8 = float(aa[7]) 

			#AFT_R= sensor25R1+sensor25R2+sensor25R3+sensor25R4

		if ip_sapato == 6:#left itshoe
			
			#left itshoe calibration curves
			sensor25L1 = math.exp(((float(aa[2]) + 215.61)/169.22))
			sensor25L2 = math.exp(((float(aa[4]) + 107.18)/152.1))
			sensor25L3 = math.exp(((float(aa[7]) + 129.29)/152.58))
			sensor25L4 = math.exp(((float(aa[5]) + 162.06)/145.27))


			sensor1L5 = math.exp(((float(aa[1]) + 23.526)/145.98))  
			sensor1L6 = math.exp(((float(aa[3]) + 69.2)/161.15))
			sensor1L7 = math.exp(((float(aa[8]) - 5.7915)/143.01))
			sensor1L8 = math.exp(((float(aa[6]) + 32.989)/154.65))

			

			#fn_left = sensor25L1 + sensor25L2 + sensor25L3 + sensor25L4 -35;
			#label_fnL = tk.Label(self.root, text="Fn right" + fn_left)
			#label_fnL.grid(row = 3,column = 30, columnspan =2, pady= 1, padx =2)

			fn_left = sensor25L1 + sensor25L2 + sensor25L3 + sensor25L4 - offset_fnleft;

			printfn_l = printfn_l +1
			if printfn_l ==  300:

				label_fnL = tk.Label(self.root, text=" Fn left:   " + str(round(fn_left,2)))
				label_fnL.grid(row = 20,column = 2, pady=1, padx =1)
			
				fnLoffset_label=tk.Label(self.root, text="Fn offset left:").grid(row = 21,column = 2, pady=1, padx =1)
				fnLoffset_entry = tk.Entry(self.root,textvariable=self.offsetL).grid(row = 22,column = 2,pady=1, padx =1)

				offset_fnleft =  float(self.offsetL.get())
				printfn_l = 0



			#print(fn_right)

			if fn_left < 10 and fn_left > -50 and aux_net_left== 0:
				aux_net_left= 1
				x_left =0 
				#print("aux_net_left:   ")
				#print(aux_net_left)

			if fn_left > 10 and aux_net_left == 1 and x_left < 50:
				
				fhmovX.append(-sensor1L5*0.7071 + sensor1L6*0.7071 -sensor1L7*0.7071 + sensor1L8*0.7071);
				fhmovY.append(sensor1L5*0.7071 + sensor1L6*0.7071 -sensor1L7*0.7071 - sensor1L8*0.7071); 
				GyrX_inp.append(GyrX)
				GyrY_inp.append(GyrY)
				GyrZ_inp.append(GyrZ)
				angX_inp.append(angX)
				angY_inp.append(angY)
				angZ_inp.append(angZ)
				accX_inp.append(accX)
				accY_inp.append(accY)
				accZ_inp.append(accZ)
				x_left=x_left+1
				#print(fhmovX)
				#print(x_left)


			if x_left== 49: 
				aux_net_left= 0
				x_left=0

				nn_ip = ip_sapato
				#print("right 50 points 1 step")
				#print(fhmovX)
				self.publish_to_network()

			#sensor1L5 =float(aa[2])  
			#sensor1L6 = float(aa[4]) 
			#sensor1L7 = float(aa[5]) 
			#sensor1L8 = float(aa[7]) 

			#sensor25L1 = float(aa[1]) 
			#sensor25L2 = float(aa[3]) 
			#sensor25L3 = float(aa[6]) 
			#sensor25L4 = float(aa[8]) 

			#AFT_L= sensor25L1+sensor25L2+sensor25L3+sensor25L4

			#print(sensor1L5, sensor1L6, sensor1L7, sensor1L8, sensor25L1 ,sensor25L2,sensor25L3,sensor25L4 )
			
	
#def subscribe from ros topic that receives the itshoe data
	def save_from_topic(self):
		rospy.init_node('listener', anonymous = 'True', disable_signals = True)
		#self.thread_save_from_topic()
		rospy.Subscriber("/data", String, self.save_from_topic_callback)
		print("listening..")
		rospy.spin()
		
#def connect to db where all the data will be stored for later analysis
	def Connect_DB(self):
		try:
			global db
			#global db1
			global cur
			#global cur1
			db=mdb.connect(host = 'localhost', user = 'root', passwd = 'shinobi39', db = 'itshoedata', port =3306 )	
			#db1=mdb.connect(host = 'localhost', user = 'root', passwd = 'shinobi39', db = 'itshoedata', port =3306 )	
			cur = db.cursor()
			#print(db)
			label_confirmDB_connect = tk.Label(self.root, text="connected to db")
			label_confirmDB_connect.grid(row = 0,column = 20, columnspan =2, pady= 1, padx =2)
			#print(String.data.x)
		except:
			print("db Failed to connect ")
			label_confirmDB_connect = tk.Label(self.root, text="failed to connect to db")
			label_confirmDB_connect.grid(row = 0,column = 20, columnspan =2, pady= 1, padx =2)

#disconnect db
	def Disconnect_DB(self):
		try:
		#cur.close()
			db.close()
		except:
			print("Error closing DB COM")
	


#def example to plot data in case we want to see it live on the app 
#replace x y and z  e.g cop, zmp, sensors Fn, fh

	def plot(self):
		#COP_lx, COP_ly, COP_rx, COP_ry
		x=np.array([1, 2, 3, 4, 5])
		y=np.array([5, 4, 3, 2, 1])
		z=np.array([-5, -4, -3, -2, -1])

		fig=Figure(figsize=(4,4))
		a= fig.add_subplot(121)
		a.scatter(x,y,color="red")
	

		a.set_title("ZMP")
		a.set_ylabel("Y",fontsize=14)
		a.set_xlabel("X", fontsize=14)


		b= fig.add_subplot(122)
		b.scatter(z,x,color="red")
		b.set_title("ZMP")
		b.set_ylabel("Y",fontsize=14)
		b.set_xlabel("X", fontsize=14)

		canvas = FigureCanvasTkAgg(fig, self.root)
		canvas.get_tk_widget().grid(row = 17, rowspan = 8, column = 17, columnspan = 8 )
		canvas.draw()


#def to read robot sensors and calculate zmp values, can also be used to print live on an itshoe image representation to observe the zmp behavior
#calculates robot nao COP and step phase
	def zmp_coordinates(self):
		#canvas = tk.Canvas(self.root,width=405, height=294, bg ='white smoke')
		#self.gif1 = ImageTk.PhotoImage(file='/home/la/Desktop/shoes.png')
			# put gif image on canvas
			# pic's upper left corner (NW) on the canvas is at x=50 y=10
		#canvas.create_image(0, 0,  image=self.gif1, anchor=NW)
		global sensor1L5, sensor1L6, sensor1L7, sensor1L8, sensor25L1 ,sensor25L2,sensor25L3,sensor25L4
		memoryProxy = ALProxy("ALMemory", str(self.entry_IP.get()), int(self.entry_PORT.get()))

		while memoryProxy:
			LFsrFL = memoryProxy.getData("Device/SubDeviceList/LFoot/FSR/FrontLeft/Sensor/Value")
			LFsrFR = memoryProxy.getData("Device/SubDeviceList/LFoot/FSR/FrontRight/Sensor/Value")
			LFsrBL = memoryProxy.getData("Device/SubDeviceList/LFoot/FSR/RearLeft/Sensor/Value")
			LFsrBR = memoryProxy.getData("Device/SubDeviceList/LFoot/FSR/RearRight/Sensor/Value")

			  # Get The Right Foot Force Sensor Values kg
			RFsrFL = memoryProxy.getData("Device/SubDeviceList/RFoot/FSR/FrontLeft/Sensor/Value")
			RFsrFR = memoryProxy.getData("Device/SubDeviceList/RFoot/FSR/FrontRight/Sensor/Value")
			RFsrBL = memoryProxy.getData("Device/SubDeviceList/RFoot/FSR/RearLeft/Sensor/Value")
			RFsrBR = memoryProxy.getData("Device/SubDeviceList/RFoot/FSR/RearRight/Sensor/Value")

			##############################################################################################################################################
			dx_R =np.array([0.07025, 0.07025, -0.03025,-0.02965])
			dy_R =np.array([0.0231, -0.0299, 0.0191, -0.0299])
			dx_L =np.array([0.07025, 0.07025, -0.03025, - 0.02965])
			dy_L =np.array([0.0299, -0.0231,0.0299, -0.0191])

			dx_R_ITshoe =np.array([0.0672, 0.0672, -0.02725,-0.02725])
			dy_R_ITshoe =np.array([-0.0219, 0.016103, -0.0219, -0.016103])
			dx_L_ITshoe =np.array([0.0672, 0.0672, -0.02725, - 0.02725])
			dy_L_ITshoe =np.array([0.0219, -0.016103,0.0219, -0.016103])


			Force = np.array([ LFsrFL, LFsrFR, LFsrBL, LFsrBR, RFsrFL, RFsrFR, RFsrBL, RFsrBR])


			if any(Force[0:3]) & any(Force[4:7]):   #If there is at least one sensor reading on both feet at the same time...
				auxx = (dx_L)*[Force[4],Force[5],Force[6],Force[7]] + (dx_R)*[Force[0],Force[1],Force[2],Force[3]] # dx_L * posicao x centro pe esquerdo para direito 
				auxy = (dy_L+0.01)*[Force[4],Force[5],Force[6],Force[7]] + (dy_R)*[Force[0],Force[1],Force[2],Force[3]] # same dx_R* POS[1]
				#print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
				#print(auxx)
				#print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
				if sum(Force[:])==0:
					CoPx = 0
					CoPy = 0
				else:
					CoPx = sum(auxx)/sum(Force[:])
					CoPy = sum(auxy)/sum(Force[:])
				phase = 3
			elif ~any(Force[0:3]) & any(Force[4:7]): #   %If ONLY the Right Foot is contacting the ground
				auxx = (dx_L)*[Force[4],Force[5],Force[6],Force[7]]
				auxy = (dy_L)*[Force[4],Force[5],Force[6],Force[7]]
				if sum(Force[4:7])==0:
					CoPx = 0
					CoPy = 0
				else:
					CoPx = sum(auxx)/sum(Force[4:7])
					CoPy = sum(auxy)/sum(Force[4:7])
				phase = 1
			elif any(Force[0:3]) & ~any(Force[4:7]):#   %If ONLY the Left Foot is contacting the ground
				auxx = (dx_R)*[Force[0],Force[1],Force[2],Force[3]]
				auxy = (dy_R)*[Force[0],Force[1],Force[2],Force[3]]
				if sum(Force[0:3])==0:
					CoPx = 0
					CoPy = 0
				else:
					CoPx = sum(auxx)/sum(Force[0:3])
					CoPy = sum(auxy)/sum(Force[0:3])
				phase = 2
			else:
				CoPx = np.nan
				CoPy = np.nan
				phase = 4 
			print(phase)


			Force_IT = np.array([ sensor25L1, sensor25L2, sensor25L3, sensor25L4, sensor1L5 ,sensor1L6,sensor1L7,sensor1L8])


			if any(Force_IT[0:3]) & any(Force_IT[4:7]):   #If there is at least one sensor reading on both feet at the same time...
				auxx_IT = (dx_L_ITshoe)*[Force_IT[4],Force_IT[5],Force_IT[6],Force_IT[7]] + (dx_R_ITshoe)*[Force_IT[0],Force_IT[1],Force_IT[2],Force_IT[3]] # dx_L * posicao x centro pe esquerdo para direito 
				auxy_IT = (dy_L_ITshoe+0.01)*[Force_IT[4],Force_IT[5],Force_IT[6],Force_IT[7]] + (dy_R_ITshoe)*[Force_IT[0],Force_IT[1],Force_IT[2],Force_IT[3]] # same dx_R* POS[1]
				#print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
				#print(auxx)
				#print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
				if sum(Force_IT[:])==0:
					CoPx_IT = 0
					CoPy_IT = 0
				else:
					CoPx_IT = sum(auxx_IT)/sum(Force_IT[:])
					CoPy_IT= sum(auxy_IT)/sum(Force_IT[:])
				phase_IT = 3
			elif ~any(Force_IT[0:3]) & any(Force_IT[4:7]): #   %If ONLY the Right Foot is contacting the ground
				auxx_IT = (dx_L_ITshoe)*[Force_IT[4],Force_IT[5],Force_IT[6],Force_IT[7]]
				auxy_IT = (dy_L_ITshoe)*[Force_IT[4],Force_IT[5],Force_IT[6],Force_IT[7]]
				if sum(Force_IT[4:7])==0:
					CoPx_IT = 0
					CoPy_IT = 0
				else:
					CoPx_IT = sum(auxx_IT)/sum(Force_IT[4:7])
					CoPy_IT = sum(auxy_IT)/sum(Force_IT[4:7])
				phase_IT = 1
			elif any(Force_IT[0:3]) & ~any(Force_IT[4:7]):#   %If ONLY the Left Foot is contacting the ground
				auxx_IT = (dx_R_ITshoe)*[Force_IT[0],Force_IT[1],Force_IT[2],Force_IT[3]]
				auxy_IT = (dy_R_ITshoe)*[Force_IT[0],Force_IT[1],Force_IT[2],Force_IT[3]]
				if sum(Force_IT[0:3])==0:
					CoPx_IT = 0
					CoPy_IT = 0
				else:
					CoPx_IT = sum(auxx_IT)/sum(Force_IT[0:3])
					CoPy_IT = sum(auxy_IT)/sum(Force_IT[0:3])
				phase_IT = 2
			else:
				CoPx_IT = np.nan
				CoPy_IT = np.nan
				phase_IT = 4 
			#Center_y = 406
			#Center_x = 385
			#Metertopixel= 3779.528
			#1 metro = 3779.528 pixels

			copx_label = tk.Label(self.root, text="robot CoPx:" + str(round(CoPx,4)))
			copx_label.grid(row = 20,column = 20, columnspan =2, pady= 1, padx =2)

			copy_label = tk.Label(self.root, text="robot CoPy:" +str(round(CoPy,4)))
			copy_label.grid(row = 21,column = 20, columnspan =2, pady= 1, padx =2)

			copx_label_IT = tk.Label(self.root, text="itshoe CoPx:" +str(round(CoPx_IT,4)))
			copx_label_IT.grid(row = 22,column = 20, columnspan =2, pady= 1, padx =2)

			copy_label_IT= tk.Label(self.root, text="itshoe CoPy:" +str(round(CoPy_IT,4)))
			copy_label_IT.grid(row = 23,column = 20, columnspan =2, pady= 1, padx =2)

			phase_R= tk.Label(self.root, text="PHASE_R:" +str(phase))
			phase_R.grid(row = 24,column = 20, columnspan =2, pady= 1, padx =2)

			phase_I= tk.Label(self.root, text="PHASE_IT:" +str(phase_IT))
			phase_I.grid(row = 25,column = 20, columnspan =2, pady= 1, padx =2)
			#CoPx = 0
			#CoPy = 0.01
			#draw_CoPy = (-CoPx * Metertopixel) + Center_x
			#aux=1
			#marker= canvas.create_oval(draw_CoPx/2, draw_CoPy/2, (draw_CoPx/2)+2, (draw_CoPy/2)+2, width = 5, fill = 'black')
			#canvas.grid(column =2, columnspan = 2, row = 10)
			#aux = aux +1
			#if aux == 100:
			#	aux=1
			#	canvas.delete(marker)
		#line.pack()
		#canvas = Canvas()
		#canvas.create_oval(x, y, xf, yf, outline="#f11",fill="#1f1", width=10)
		#canvas.pack(fill=BOTH, expand=1)

#donothing
	def donothing(self):
	   filewin = Toplevel(self.root)
	   button = Button(filewin, text="Do nothing button")
	   button.pack()

#create window to connect with the itshoes
	def create_window_to_setup_ITshoe_IP(self):
		window_itshoe = Toplevel()
		window_itshoe.geometry("200x200")
		label_confirmIP_itshoe_left = tk.Label(window_itshoe, text="Insert ITshoe L IP:").pack()
		Insert_IP_text_widget_itshoe_L=tk.Entry(window_itshoe,textvariable=self.entry_IP_itshoe_L).pack()
		label_confirmIP_itshoe_right = tk.Label(window_itshoe, text="Insert ITshoe R IP:").pack()
		Insert_IP_text_widget_itshoe_R=tk.Entry(window_itshoe,textvariable=self.entry_IP_itshoe_R).pack()

		#str(self.entry_IP_itshoe_L.get()) Ip left shoe
		
		button_confirmIP_itshoe = tk.Button(window_itshoe, text="Confirm", command=lambda: self.doit_in_thread1()).pack()

	
# connect IThsoe () both shoes.
	def connect_ITshoes(self):
		#dividir em 2 funcoes
		global db_table_name1
		global server_socket
		global db_table_info
		#global sensor1L5, sensor1L6, sensor1L7, sensor1L8, sensor25L1 ,sensor25L2,sensor25L3,sensor25L4
		server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		server_address =('192.168.8.1',8888)
		server_socket.bind(server_address)

		db_table_name_label=Label(self.root, text="Enter a name for the db_table").grid(row = 1,column = 16, pady= 1, padx =1)
		db_table_name= Entry(self.root, textvariable=self.db_table).grid(row = 1,column = 20, pady= 1, padx = 1)
		
		var11= tk.IntVar()
		
		db_info_label=Label(self.root, text="Experience info..").grid(row = 2,column = 16, pady= 1, padx =1)
		db_info= Entry(self.root, textvariable=self.var_additional_info)
		db_info.grid(row = 2,column = 20, pady= 1, padx = 1)
		db_table_info =  self.var_additional_info.get()

		#myframe =self.root.tkraise()
		
		db_table_name1 =  self.db_table.get()
		button_setdbname= Button(self.root, text="set DB name", command=lambda: var11.set(1))
		button_setdbname.grid(row = 3,column = 16, pady= 1, padx = 1)
		
		#button_setdbname.bind("<ButtonRelease-1>",var.get())
		while len(db_table_name1) < 5:
			print("waiting...")
			button_setdbname.wait_variable(var11)
			print("done waiting.")
			db_table_recording=Label(self.root, text="ready to start recording... connect with the Robot").grid(row = 3,column = 20, pady= 1, padx =1)
			db_table_name1 =  self.db_table.get()
			db_table_info =  self.var_additional_info.get()
		

		self.thread_readitshoevalues()
		
#another previous attempt

		#if((sys.getsizeof(db_table_name1) < 5) or (sys.getsizeof(db_table_name1 > 15) )):
		#	print 'Please enter a valid name between 5 and 15 characters'
		#	tkMessageBox.showwarning("DB_table_NAME", "Please enter a valid name between 5 and 15 characters")
		#	return

		#global i
		#global db
		#global cur
		#j=0
		#trygloballlll 
		#print("cheguei aqui..")

		#while True:
			#print("waiting for itshoe..")
		#try:
		#	data, address= server_socket.recvfrom(1024)
		#except:
		#	print("failed to connect with itshoes")
		#print(data)
		#m = struct.unpack('HHHHHHHHHH',data)
		#ITDATA = MyStruct(m[0],m[1],m[2],m[3],m[4],m[5],m[6],m[7],m[8],m[9])
				
		#print(db_table_info)
			#j=j+1

			#if j > 100:
		#i=i+1
		#sensor1L5 = math.exp(((m[1] + 23.526)/145.98))  
		#sensor1L6 = math.exp(((m[3] + 69.2)/161.15))
		#sensor1L7 = math.exp(((m[6] - 5.7915)/143.01))
		#sensor1L8 = math.exp(((m[8] + 32.989)/154.65))

		#sensor25L1 = math.exp(((m[2] + 215.61)/169.22))
		#sensor25L2 = math.exp(((m[4] + 107.18)/152.1))
		#sensor25L3 = math.exp(((m[5] + 129.29)/152.58))
		#sensor25L4 = math.exp(((m[7] + 162.06)/145.27))
		#count = 1
		#aux = "CREATE TABLE IF NOT EXISTS "  + db_table_name1 + " (ITshoe_id varchar(15) DEFAULT NULL,data_date varchar(15) DEFAULT NULL,read_number varchar(30) DEFAULT NULL,s1 int(4) DEFAULT NULL,s2 int(4) DEFAULT NULL,s3 int(4) DEFAULT NULL,s4 int(4) DEFAULT NULL,s5 int(4) DEFAULT NULL,s6 int(4) DEFAULT NULL,s7 int(4) DEFAULT NULL,s8 int(4) DEFAULT NULL)"
		#db.query(aux)		
		#sql1 = "INSERT INTO " +db_table_name1+ " (ITshoe_id, data_date, read_number, s1,s2,s3,s4,s5,s6,s7,s8 ) VALUES (%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s)"
		#val = ("192.168.8.65","date",db_table_info,sensor1L5,sensor1L6,sensor1L7,sensor1L8,sensor25L1,sensor25L2,sensor25L3,sensor25L4)
		#cur.execute(sql1, val)
		#db.commit() 
		#Fn = sensor25L1 + sensor25L2+ sensor25L3 + sensor25L4
		#try linear calibration instead of logaritmic
				
		#print(Fn) # all variables inside the struct

		#fig=Figure(figsize=(4,4))
		#a=fig.add_subplot(111)
		
		#print(i)
		#self.Lcop_buffer_x[i]=i
		#self.Lcop_buffer_y[i]=Fn-11.5
					
		#a.scatter(self.Lcop_buffer_x,self.Lcop_buffer_y,color="red")
		#a.set_title("Normal Force")
		#a.set_ylabel("Fn",fontsize=14)
		#a.set_xlabel("X", fontsize=14)		
	
		#if i > 99:
		#	canvas = FigureCanvasTkAgg(fig, self.root)
		#	canvas.get_tk_widget().grid(row = 10, rowspan = 7, column = 0, columnspan = 2 )
		#	canvas.draw()
		#	i=0
		#	self.Lcop_buffer_x =np.zeros((101,1))
		#	self.Lcop_buffer_y=np.zeros((101,1))	

		#self.root.after(10,self.connect_ITshoes)
	#	after(10000, self.connect_ITshoes)
			#	j= 0
			
    		#	file.write("%d" % (len(data)))
# One difference is that we will have to bind our declared IP address
# and port number to our newly declared serverSock


#read itshoe data  #alternative to ros topic, [sends to db and plots data on a window #commented]
	def read_itshoe_values(self):
		global server_socket, countShoe
		global sensor1L5, sensor1L6, sensor1L7, sensor1L8, sensor25L1 ,sensor25L2,sensor25L3,sensor25L4 
		global sensor1R5, sensor1R6, sensor1R7, sensor1R8, sensor25R1, sensor25R2, sensor25R3, sensor25R4

		aux = "CREATE TABLE IF NOT EXISTS "  + db_table_name1 + " (ITshoe_id varchar(15) DEFAULT NULL,data_date varchar(4) DEFAULT NULL,read_number varchar(20) DEFAULT NULL, countshoe varchar(6) DEFAULT NULL,s1 FLOAT(7,4) DEFAULT NULL,s2 FLOAT(7,4) DEFAULT NULL,s3 FLOAT(7,4) DEFAULT NULL,s4 FLOAT(7,4) DEFAULT NULL,s5 FLOAT(7,4) DEFAULT NULL,s6 FLOAT(7,4) DEFAULT NULL,s7 FLOAT(7,4) DEFAULT NULL,s8 FLOAT(7,4) DEFAULT NULL)"
		db.query(aux)	
	
		i=1
		while(1):
			try:
				data, address= server_socket.recvfrom(1024)
			#print("ad")
			except:
				print("failed to connect with itshoes")
			auxxx=address[0]
		#print(auxxx[11])

		#if auxxx[11] == 6:
			
			m = struct.unpack('HHHHHHHHHH',data)
			ITDATA = MyStruct(m[0],m[1],m[2],m[3],m[4],m[5],m[6],m[7],m[8],m[9])
				
		#print(db_table_info)
			#j=j+1

			#if j > 100:
		
			sensor1L5 = math.exp(((m[1] + 23.526)/145.98))  
			sensor1L6 = math.exp(((m[3] + 69.2)/161.15))
			sensor1L7 = math.exp(((m[6] - 5.7915)/143.01))
			sensor1L8 = math.exp(((m[8] + 32.989)/154.65))

			sensor25L1 = math.exp(((m[2] + 215.61)/169.22))
			sensor25L2 = math.exp(((m[4] + 107.18)/152.1))
			sensor25L3 = math.exp(((m[5] + 129.29)/152.58))
			sensor25L4 = math.exp(((m[7] + 162.06)/145.27))
		
			countShoe = m[0]
			#i=i+1
			#if i==100:
			#	self.thread_save_to_db()
			#	i=1
			
			#sleep(0.01)
			#self.thread_save_to_db()
			with open('testeaa.csv', mode ='a') as teste_file:
				teste_writer =csv.writer(teste_file, delimiter=',')
				teste_writer.writerow(ITDATA)
				
		#if auxxx[11]== 4:

		#	n = struct.unpack('HHHHHHHHHH',data)
		#	ITDATA = MyStruct(n[0],n[1],n[2],n[3],n[4],n[5],n[6],n[7],n[8],n[9])

		#	sensor25R1 = math.exp(((n[1] + 124.13)/162.04))
		#	sensor25R2 = math.exp(((n[2] + 99.792)/149.78))
		#	sensor25R3 = math.exp(((n[3] + 108.92)/144.13))
		#	sensor25R4 = math.exp(((n[4] + 187.42)/151.69))

		#	sensor1R5 = math.exp(((n[5] + 33.103)/156.63))
		#	sensor1R6 = math.exp(((n[6] + 62.183)/157.88))
		#	sensor1R7 = math.exp(((n[7] + 46.256)/160.14))
		#	sensor1R8 = math.exp(((n[8] + 49.447)/154.53))

		#	countShoe = n[0]
		#countShoe=1
		#aux = "CREATE TABLE IF NOT EXISTS "  + db_table_name1 + " (ITshoe_id varchar(15) DEFAULT NULL,data_date varchar(15) DEFAULT NULL,read_number varchar(30) DEFAULT NULL,s1 int(4) DEFAULT NULL,s2 int(4) DEFAULT NULL,s3 int(4) DEFAULT NULL,s4 int(4) DEFAULT NULL,s5 int(4) DEFAULT NULL,s6 int(4) DEFAULT NULL,s7 int(4) DEFAULT NULL,s8 int(4) DEFAULT NULL)"
		#db.query(aux)		
		#sql1 = "INSERT INTO " +db_table_name1+ " (ITshoe_id, data_date, read_number, s1,s2,s3,s4,s5,s6,s7,s8 ) VALUES (%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s)"
		#val = ("192.168.8.65","date",db_table_info,sensor1L5,sensor1L6,sensor1L7,sensor1L8,sensor25L1,sensor25L2,sensor25L3,sensor25L4)
		#cur.execute(sql1, val)
		#db.commit() 
		#Fnl = sensor25L1 + sensor25L2+ sensor25L3 + sensor25L4
		#Fnr= sensor25R1+sensor25R2+sensor24R3+sensor25R4
		#try linear calibration instead of logaritmic
				
		#print(Fn) # all variables inside the struct

		#fig=Figure(figsize=(4,4))
		#a=fig.add_subplot(111)
		
		
		#self.Lcop_buffer_x[i]=i
		#self.Lcop_buffer_y[i]=Fn-11.5
				
		#a.scatter(self.Lcop_buffer_x,self.Lcop_buffer_y,color="red")
		#a.set_title("Normal Force")
		#a.set_ylabel("Fn",fontsize=14)
		#a.set_xlabel("X", fontsize=14)		
	
		#if i > 99:
		#	canvas = FigureCanvasTkAgg(fig, self.root)
		#	canvas.get_tk_widget().grid(row = 10, rowspan = 7, column = 0, columnspan = 2 )
		#	canvas.draw()
		#	i=0
		#	self.Lcop_buffer_x =np.zeros((101,1))
		#	self.Lcop_buffer_y=np.zeros((101,1))	

		#self.root.after(10,self.read_itshoe_values)

#creat window to connect with robot nao
	def create_window_to_setup_robot_IP_and_PORT(self):


		window = Toplevel()
		window.geometry("200x200")
		label_confirmIP = tk.Label(window, text="Insert Robot IP:")
		label_confirmPORT = tk.Label(window, text="Insert Robot Port:")
		
		self.entry_IP.set("192.168.8.65")
		self.entry_PORT.set(9559)
		Insert_IP_text_widget=tk.Entry(window,textvariable=self.entry_IP)
		Insert_PORT_text_widget=tk.Entry(window,textvariable=self.entry_PORT)
		#Insert_IP_text_widget.grid(row=5, column=5)
		#Insert_PORT_text_widget.grid(row=6, column=5)
		self.display_textR.set("Disconnected!")
		label_confirm_tryagain = Label(window, textvariable=self.display_textR)
		
		#label_confirm_tryagain.grid(row=9, column=1)
		label_confirm_tryagain.pack()

		label_ip_port = Label(window, textvariable="Default!! IP: 192.168.8.65; Port: 9559").pack()

		label_confirmIP.pack()
		Insert_IP_text_widget.pack()
		label_confirmPORT.pack()
		Insert_PORT_text_widget.pack()


		button_confirmIPandPORT = tk.Button(window, text="Confirm", command=lambda: self.check_and_get_entry())
		
		button_exit_current_window = tk.Button(window, text="Close", command=window.destroy)

		button_confirmIPandPORT.pack()
		button_exit_current_window.pack()
		
		#print(self.entry_IP)
		#print(self.entry_PORT)
		#print("here")
		 # return true or false, if true next if false clear entry and try again
		return self.entry_IP, self.entry_PORT

	#T.insert(tk.END, "Just a text Widget\nin two lines\n")

#check if ip and port are valid
	def check_and_get_entry(self):
		
		
		if(re.search(self.regex, self.entry_IP.get())):  
			#print("Valid Ip address")  
			
			#print(str(self.entry_IP.get()))
			#print(str(self.entry_PORT.get()))
			self.connectRobot_callback()
			self.thread_readFSRvalues()
			#self.thread_zmp_coordinates()
		else:  
			self.display_textR.set("try again")
			#print("Invalid Ip address")  


#read robot sensors 
	def readFSRvalues_callback(self):
		global ip_sapato
		global sensor1L5, sensor1L6, sensor1L7, sensor1L8, sensor25L1 ,sensor25L2,sensor25L3,sensor25L4 
		global sensor1R5, sensor1R6, sensor1R7, sensor1R8, sensor25R1, sensor25R2, sensor25R3, sensor25R4
		global LFsrFL,	LFsrFR,	LFsrBL,	LFsrBR,	RFsrFL,	RFsrFR,	RFsrBL,	RFsrBR,	COP_lx,	COP_ly,	COP_rx,	COP_ry,	GyrX ,	GyrY,	GyrZ,	angX,	angY,	angZ,	accX,	accY,	accZ
		global countRobot
		global dcm 

		try:
			memoryProxy = ALProxy("ALMemory", str(self.entry_IP.get()), int(self.entry_PORT.get()))
			dcm = ALProxy("DCM", str(self.entry_IP.get()), int(self.entry_PORT.get()))
		#	start_recording_button = tk.Button(self.root, text="start db recording", command=lambda: self.thread_save_to_db())
		#	start_recording_button.grid(row = 17,column = 18, columnspan =2, pady= 1, padx =2)
		except:
			print("failed to connect with robot")
		#t0= time.time()
		#t0_dcm = dcm.getTime(0)
	
		Lcop_buffer_x =np.zeros((1000,1))

		Lcop_buffer_y=np.zeros((1000,1))

		Rcop_buffer_x =np.zeros((1000,1))

		Rcop_buffer_y=np.zeros((1000,1))
		
			
		while memoryProxy:

			
			LFsrFL = memoryProxy.getData("Device/SubDeviceList/LFoot/FSR/FrontLeft/Sensor/Value")
			LFsrFR = memoryProxy.getData("Device/SubDeviceList/LFoot/FSR/FrontRight/Sensor/Value")
			LFsrBL = memoryProxy.getData("Device/SubDeviceList/LFoot/FSR/RearLeft/Sensor/Value")
			LFsrBR = memoryProxy.getData("Device/SubDeviceList/LFoot/FSR/RearRight/Sensor/Value")

				  # Get The Right Foot Force Sensor Values kg
			RFsrFL = memoryProxy.getData("Device/SubDeviceList/RFoot/FSR/FrontLeft/Sensor/Value")
			RFsrFR = memoryProxy.getData("Device/SubDeviceList/RFoot/FSR/FrontRight/Sensor/Value")
			RFsrBL = memoryProxy.getData("Device/SubDeviceList/RFoot/FSR/RearLeft/Sensor/Value")
			RFsrBR = memoryProxy.getData("Device/SubDeviceList/RFoot/FSR/RearRight/Sensor/Value")
				
				#COP
			COP_lx= memoryProxy.getData("Device/SubDeviceList/LFoot/FSR/CenterOfPressure/X/Sensor/Value")
			COP_ly= memoryProxy.getData("Device/SubDeviceList/LFoot/FSR/CenterOfPressure/Y/Sensor/Value")
			COP_rx= memoryProxy.getData("Device/SubDeviceList/RFoot/FSR/CenterOfPressure/X/Sensor/Value")
			COP_ry= memoryProxy.getData("Device/SubDeviceList/RFoot/FSR/CenterOfPressure/X/Sensor/Value")
				#Gyroscope
			GyrX= memoryProxy.getData("Device/SubDeviceList/InertialSensor/GyroscopeX/Sensor/Value")
			GyrY= memoryProxy.getData("Device/SubDeviceList/InertialSensor/GyroscopeY/Sensor/Value")	
			GyrZ= memoryProxy.getData("Device/SubDeviceList/InertialSensor/GyroscopeZ/Sensor/Value")
				#ANGLE
			angX= memoryProxy.getData("Device/SubDeviceList/InertialSensor/AngleX/Sensor/Value")
			angY= memoryProxy.getData("Device/SubDeviceList/InertialSensor/AngleY/Sensor/Value")
			angZ= memoryProxy.getData("Device/SubDeviceList/InertialSensor/AngleZ/Sensor/Value")
				#ACCELEROMETER
			accX= memoryProxy.getData("Device/SubDeviceList/InertialSensor/AccelerometerX/Sensor/Value")
			accY= memoryProxy.getData("Device/SubDeviceList/InertialSensor/AccelerometerY/Sensor/Value")
			accZ= memoryProxy.getData("Device/SubDeviceList/InertialSensor/AccelerometerZ/Sensor/Value")

			countRobot = 1
			#t1_dcm = dcm.getTime(0)
			#t1= time.time()
			
		#	STFile = [t1-t0,sensor1L5, sensor1L6, sensor1L7, sensor1L8, sensor25L1 ,sensor25L2,sensor25L3,sensor25L4,sensor1R5, sensor1R6, sensor1R7, sensor1R8, sensor25R1, sensor25R2, sensor25R3, sensor25R4,t0_dcm-t1_dcm,LFsrFL,LFsrFR,LFsrBL,LFsrBR,RFsrFL,RFsrFR,RFsrBL,RFsrBR,COP_lx,COP_ly,COP_rx,COP_ry,GyrX,GyrY,GyrZ,angX,angY,angZ,accX,accY,accZ]
			#print(STFile)
		#	with open('teste06FEV.csv', mode ='a') as teste_file:
		#		teste_writer =csv.writer(teste_file, delimiter=',')
		#		teste_writer.writerow(STFile)
		#print(LFsrFL)	
			#aux1 = "CREATE TABLE IF NOT EXISTS "  + db_table_name2 + " ( DATE1 varchar(25) DEFAULT NULL,LFsrFL varchar(25) DEFAULT NULL,LFsrFR varchar(25) DEFAULT NULL, LFsrBL varchar(25) DEFAULT NULL,LFsrBR varchar(25) DEFAULT NULL,RFsrFL varchar(25) DEFAULT NULL, RFsrFR varchar(25) DEFAULT NULL, RFsrBL varchar(25) DEFAULT NULL, RFsrBR varchar(25) DEFAULT NULL,COP_lx varchar(25) DEFAULT NULL,COP_ly varchar(25) DEFAULT NULL,COP_rx varchar(25) DEFAULT NULL,COP_ry varchar(25) DEFAULT NULL, GyrX varchar(25) DEFAULT NULL, GyrY varchar(25) DEFAULT NULL, GyrZ varchar(25) DEFAULT NULL,angX varchar(25) DEFAULT NULL,angY varchar(25) DEFAULT NULL,angZ varchar(25) DEFAULT NULL, accX varchar(25) DEFAULT NULL,accY varchar(25) DEFAULT NULL,accZ varchar(25) DEFAULT NULL)"
			#db.query(aux1)	
			#sql1 = "INSERT INTO " +db_table_name2+ " (DATE1 ,LFsrFL ,LFsrFR , LFsrBL ,LFsrBR ,RFsrFL , RFsrFR , RFsrBL , RFsrBR ,COP_lx ,COP_ly ,COP_rx ,COP_ry , GyrX , GyrY , GyrZ ,angX ,angY ,angZ , accX ,accY ,accZ ) VALUES (%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"		 
			#val = ("date",LFsrFL ,LFsrFR , LFsrBL ,LFsrBR ,RFsrFL , RFsrFR , RFsrBL , RFsrBR ,COP_lx ,COP_ly ,COP_rx ,COP_ry , GyrX , GyrY , GyrZ ,angX ,angY ,angZ , accX ,accY ,accZ )
			#cur.execute(sql1, val)
			#db.commit() 
		#fig=Figure(figsize=(4,4))
		#a= fig.add_subplot(121)
		#if (i > 999):
	#		i =0
#		self.Lcop_buffer_x[i]=COP_lx
#		self.Lcop_buffer_y[i]=COP_ly
			
#		a.scatter(Lcop_buffer_x,Lcop_buffer_y,color="red")
	

#		a.set_title("ZMP")
#		a.set_ylabel("Y",fontsize=14)
#		a.set_xlabel("X", fontsize=14)


#		b= fig.add_subplot(122)
#		Rcop_buffer_x[i]=COP_rx
#		Rcop_buffer_y[i]=COP_ry
#		i=i+1
#		b.scatter(Rcop_buffer_x,Rcop_buffer_y,color="red")
#		b.set_title("ZMP")
#		b.set_ylabel("Y",fontsize=14)
#		b.set_xlabel("X", fontsize=14)

#		canvas = FigureCanvasTkAgg(fig, self.root)
#		canvas.get_tk_widget().grid(row = 10, rowspan = 7, column = 0, columnspan = 2 )
			
#		canvas.draw()
			#self.thread_save_to_db()
			
			#self.root.after(10,self.readFSRvalues_callback)
			
			#print(COP_lx, COP_ly, COP_rx, COP_ry)


#connect with robot nao and create proxys for ocmmunication and control
	def connectRobot_callback(self):
		global button_move11
		#b = tk.Button(root, text="Confirm", command=create_window)
		#b.pack()

		#robotIP = "127.0.0.1"
		#port= 39077
		#print(self.entry_IP, self.entry_PORT)
			#ALProxy setups
		try:
		   postureProxy = ALProxy("ALRobotPosture", str(self.entry_IP.get()), int(self.entry_PORT.get()))
		   self.motionProxy = ALProxy("ALMotion", str(self.entry_IP.get()), int(self.entry_PORT.get()))
		   memoryProxy = ALProxy("ALMemory", str(self.entry_IP.get()), int(self.entry_PORT.get()))
		   speechProxy = ALProxy("ALTextToSpeech", str(self.entry_IP.get()), int(self.entry_PORT.get()))
		   self.batteryProxy = ALProxy("ALBattery", str(self.entry_IP.get()), int(self.entry_PORT.get()))
		   batterylabel=tk.Label(self.root, text="Robot battery (%):").grid(row = 26,column = 0, pady= 2, padx =2)
		   self.batt.set(self.batteryProxy.getBatteryCharge())
		   batterylabellevel= tk.Label(self.root, textvariable=self.batt).grid(row = 26,column = 1, pady= 2, padx = 2)
		   print("Connecting..")
		   self.display_textR.set("Connected!")
		   

		   #descomentar isto importante !!!"!!!!!!!!"!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1!!!!!!!!!!!!!!!!!!!!!!!!!!1
		   #descomentar isto importante !!!"!!!!!!!!"!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1!!!!!!!!!!!!!!!!!!!!!!!!!!1	
		   #descomentar isto importante !!!"!!!!!!!!"!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1!!!!!!!!!!!!!!!!!!!!!!!!!!1
		   #descomentar isto importante !!!"!!!!!!!!"!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1!!!!!!!!!!!!!!!!!!!!!!!!!!1
		   #descomentar isto importante !!!"!!!!!!!!"!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1!!!!!!!!!!!!!!!!!!!!!!!!!!1
		   #descomentar isto importante !!!"!!!!!!!!"!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1!!!!!!!!!!!!!!!!!!!!!!!!!!1
		   #descomentar isto importante !!!"!!!!!!!!"!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1!!!!!!!!!!!!!!!!!!!!!!!!!!1
		   #descomentar isto importante !!!"!!!!!!!!"!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1!!!!!!!!!!!!!!!!!!!!!!!!!!1
		   #descomentar linhas abaixo importante !!!"!!!!!!!!"!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1!!!!!!!!!!!!!!!!!!!!!!!!!!1


		   #pnames = 'Body'
 		   #pstif= 1.0

  		   #ptime= 1.0
 		   #self.motionProxy.setStiffnesses(pnames,pstif)
		   postureProxy.goToPosture("StandInit",1)

		   #names = [ "HeadYaw", "Headpitch", "RSshoulderRoll"]
		   self.motionProxy.setStiffnesses("Head", 0)
		   self.motionProxy.setStiffnesses("RShoulderPitch", 0)

		   #default
		   self.distance.set(1)
		   self.Step_length.set(0.02)
		   self.Step_frequency.set(0.5)
		   self.Step_height.set(0.02)
		   self.Step_torsowx.set(0.0)
		   self.Step_torsowy.set(0.1)
		   self.ydistance.set(0.0)
		   self.rotation.set(0.0)


		   moveitconfig_lable=tk.Label(self.root, text="Gait config:").grid(row = 16,column = 1, pady= 1, padx =1)

		   distance_label=tk.Label(self.root, text="X:distance [m]").grid(row = 17,column = 0, pady= 1, padx =1)
		   distance1= tk.Entry(self.root, textvariable=self.distance).grid(row = 17,column = 1, pady= 1, padx = 1)
		   
		   Sl_label=tk.Label(self.root, text="Step length [m]").grid(row = 18,column = 0, pady= 1, padx =1)
		   Step_length1 = tk.Entry(self.root,textvariable=self.Step_length).grid(row = 18,column = 1, pady= 1, padx =1)

		   Sf_label=tk.Label(self.root, text="Step Frequency [0-1]").grid(row = 19,column = 0, pady= 1, padx =1)
		   Step_frequency1 = tk.Entry(self.root,textvariable=self.Step_frequency).grid(row = 19,column = 1, pady= 1, padx =1)


		   Sh_label=tk.Label(self.root, text="Step Height [m]").grid(row = 20,column = 0, pady= 1, padx =1)
		   Step_height1 = tk.Entry(self.root,textvariable=self.Step_height).grid(row = 20,column = 1, pady= 1, padx =1)


		   Sf_label=tk.Label(self.root, text="Torso Wx [0-1]").grid(row = 21,column = 0, pady= 1, padx =1)
		   Step_torsowx1 = tk.Entry(self.root,textvariable=self.Step_torsowx).grid(row = 21,column = 1, pady= 1, padx =1)


		   Sf_label=tk.Label(self.root, text="Torso Wy [0-1]").grid(row = 22,column = 0, pady= 1, padx =1)
		   Step_torsowy1 = tk.Entry(self.root,textvariable=self.Step_torsowy).grid(row = 22,column = 1, pady= 1, padx =1)

		   Ydist_label=tk.Label(self.root, text="Y distance [m]").grid(row = 23,column = 0, pady= 1, padx =1)
		   Ydist_entry = tk.Entry(self.root,textvariable=self.ydistance).grid(row = 23,column = 1, pady= 1, padx =1)


		   rotation_label=tk.Label(self.root, text="Robot orientation [rad]").grid(row = 24,column = 0, pady= 1, padx =1)
		   rotation_entry = tk.Entry(self.root,textvariable=self.rotation).grid(row = 24,column = 1, pady= 1, padx =1)


		   button_move11 = tk.Button(self.root, text="Move", command=lambda: self.doit_in_thread())
		   button_move11.grid(row = 25,column = 0,columnspan= 2, pady= 1, padx =1)
		   a=1;

#to show sensors data on the app
		   #N1=tk.Label(self.root, text="N1[N]").grid(row = 4,column = 2, pady= 2, padx =2)
		   #N1_val=tk.Label(self.root, textvariable=a).grid(row = 4,column = 3, pady= 2, padx =2)

		   #N2=tk.Label(self.root, text="N2[N]").grid(row = 4,column = 4, pady= 2, padx =2)
		   #N2_val=tk.Label(self.root, textvariable=a).grid(row = 4,column = 5, pady= 2, padx =2)

		   #N3=tk.Label(self.root, text="N3[N]").grid(row = 5,column = 2, pady= 2, padx =2)
		   #N1_val=tk.Label(self.root, textvariable=a).grid(row = 4,column = 3, pady= 2, padx =2)

		   #N4=tk.Label(self.root, text="N4[N]").grid(row = 5,column = 4, pady= 2, padx =2)
		   #N1_val=tk.Label(self.root, textvariable=a).grid(row = 4,column = 5, pady= 2, padx =2)

		   #H1=tk.Label(self.root, text="H1[N]").grid(row = 6,column = 2, pady= 2, padx =2)
		   #N1_val=tk.Label(self.root, textvariable=a).grid(row = 4,column = 3, pady= 2, padx =2)

		   #H2=tk.Label(self.root, text="H2[N]").grid(row = 6,column = 4, pady= 2, padx =2)
		   #N1_val=tk.Label(self.root, textvariable=a).grid(row = 4,column = 5, pady= 2, padx =2)

		   #H3=tk.Label(self.root, text="H3[N]").grid(row = 7,column = 2, pady= 2, padx =2)
		   #N1_val=tk.Label(self.root, textvariable=a).grid(row = 4,column = 3, pady= 2, padx =2)

		   #H4=tk.Label(self.root, text="H4[N]").grid(row = 7,column = 4, pady= 2, padx =2)
		   #N1_val=tk.Label(self.root, textvariable=a).grid(row = 4,column = 5, pady= 2, padx =2)


		 #  plot_button = tk.Button(self.root, text="plot", command=lambda: self.plot())
		 #  plot_button.grid(row = 24,column = 0,columnspan= 2, pady= 1, padx =1)

		except error:
		   print("Connection error: ", error)
		   #label_confirm_tryagain = tk.Label(self.window, text="try again!").pack()
		   self.display_textR.set('wrong IP or PORT, check again!')

		# Get The Left Foot Force Sensor Valuess kg 912092343
		
			#read for example torsoangle and fill with label.config
			#TorsoAngleX = memProxy.getData("Device/SubDeviceList/LElbowRoll/Position/Sensor/Value")
			#print(TorsoAngleX)
			#value_example.config(text= "TorsoAngleX : " + str(TorsoAngleX))
			#para fazer com que esta callback seja chamada de 20 em 20 segundos
			#motProxy.post.walkTo(0.05, 0, 0)
			#button_connectwithrobot.after(20, connectRobot_callback)
		return self.entry_IP, self.entry_PORT

#control robot nao gait, make it move
	def makerobotmove(self):

		global button_move11
		entrydistance =  float(self.distance.get())
		#print '########################################################################################################################'
		 
		if((entrydistance > float(2)) or (entrydistance < float(-2))):
			print('Please enter a value between -2 and 2 [m]')
			tkMessageBox.showwarning("Distance", "Please enter a value between -2 and 2")
			return

		
		entryString_Sl = float(self.Step_length.get())
		if((entryString_Sl > float(0.08)) or (entryString_Sl < float(0.01))):
			print('Please enter a value between 0.001 and 0.08 [m]')
			tkMessageBox.showwarning("Step_lenght", "Please enter a value between 0.01 and 0.08")
			return

		entryString_Sf = float(self.Step_frequency.get())
		if((entryString_Sf > float(1)) or (entryString_Sf < float(0))):
			print('Please enter a value between 0 and 1')
			tkMessageBox.showwarning("Step_frequency", "Please enter a value between 0 and 1")
			return


		entryString_Sh= float(self.Step_height.get())
		if((entryString_Sh > float(0.04)) or (entryString_Sh < float(0.005))):
			print('Please enter a value between 0.005 and 0.04 [m]')
			tkMessageBox.showwarning("Step_height", "Please enter a value between 0.005 and 0.04")
			return


		entryString_Wx= float(self.Step_torsowx.get())
		if((entryString_Wx < float(-0.122)) or (entryString_Wx > float(0.122))):
			print('Please enter a value between -0.122 and 0.122 rad')
			tkMessageBox.showwarning("Torso_Wx", "Please enter a value between -0.122 and 0.122")
			return

		entryString_Wy= float(self.Step_torsowy.get())
		if((entryString_Wy < float(-0.122)) or (entryString_Wy > float(0.122))):
			print('Please enter a value between -0.122 and 0.122 rad')
			tkMessageBox.showwarning("Torso_Wy", "Please enter a value between -0.122 and 0.122")
			return

		entryydist =  float(self.ydistance.get())
		#print '########################################################################################################################'
		 
		if((entryydist > float(2)) or (entryydist < float(-2))):
			print('Please enter a value between -pi and pi [m]')
			tkMessageBox.showwarning("Y Distance", "Please enter a value between -2 and 2")
			return

		entryrotation =  float(self.rotation.get())
		#print '########################################################################################################################'
		 
		if((entryrotation > float(3.15)) or (entryrotation < float(-3.15))):
			print('Please enter a value between -pi and pi [m]')
			tkMessageBox.showwarning("Rotation", "Please enter a value between -pi and pi")
			return


		#default entryString_Sh = 0.02; entryString_Wx = 0.0; entryString_Wy = 0.1
		#batterylabel=tk.Label(self.root, text="Robot battery charge (%):").grid(row = 24,column = 0, pady= 2, padx =2)
		self.batt.set(self.batteryProxy.getBatteryCharge())
		batterylabellevel= tk.Label(self.root, textvariable=self.batt).grid(row = 26,column = 1, pady= 2, padx = 2)

		self.motionProxy.moveTo(entrydistance, entryydist, entryrotation,
            [ ["MaxStepX", entryString_Sl],         # step of 2 cm in front
              ["MaxStepY", 0.16],         # default value
              ["MaxStepTheta", 0.349],      # default value
              ["MaxStepFrequency", entryString_Sf],  # low frequency
              ["StepHeight", entryString_Sh],       # step height of 1 cm
              ["TorsoWx", entryString_Wx],           # default value
              ["TorsoWy", entryString_Wy] ]) 

	  	if self.motionProxy.walkIsActive():
	  		button_move11.configure(bg="blue")
	  	else:
	  		button_move11.configure(bg="red")


#default config to gather data or to reapeat an experience
	def default_config(self):

		global recording_data, dc_button

		while recording_data:
			dc_button.configure(bg="blue")

			self.motionProxy.moveTo(0.5, 0, 0,
            [ ["MaxStepX", 0.02],         # step of 2 cm in front
              ["MaxStepY", 0.16],         # default value
              ["MaxStepTheta", 0.349],      # default value
              ["MaxStepFrequency", 0.5],  # low frequency
              ["StepHeight", 0.02],       # step height of 1 cm
              ["TorsoWx", 0.0],           # default value
              ["TorsoWy", 0.1] ]) 

			self.motionProxy.moveTo(0, 0, 3.1418,
            [ ["MaxStepX", 0.02],         # step of 2 cm in front
              ["MaxStepY", 0.16],         # default value
              ["MaxStepTheta", 0.349],      # default value
              ["MaxStepFrequency", 0.5],  # low frequency
              ["StepHeight", 0.02],       # step height of 1 cm
              ["TorsoWx", 0.0],           # default value
              ["TorsoWy", 0.1] ]) 


#stop robot motion
	def stop_default(self):
		global recording_data, dc_button
		recording_data = False
		dc_button.configure(bg="red") 
		if self.motionProxy.walkIsActive():
			self.motionProxy.stopMove()
			self.motionProxy.stopMove()
			self.motionProxy.stopMove()
			self.motionProxy.stopMove()
			self.motionProxy.stopMove()
			self.motionProxy.stopMove()
			self.motionProxy.stopMove()
			self.motionProxy.stopMove()
			self.motionProxy.stopMove()
			self.motionProxy.stopMove()
			self.motionProxy.stopMove()
			self.motionProxy.stopMove()
			self.motionProxy.stopMove()
			self.motionProxy.stopMove()
			self.motionProxy.stopMove()
			self.motionProxy.stopMove()


#start robot default motion gait
	def start_default(self):
		global recording_data, dc_button
		recording_data = True
		dc_button.configure(bg="green")

	# remove stiffness from body
#	def kill():
 #   	motProxy.setStiffnesses('Body', 0)

	# stop walking if active    
#	def killWalk():
  #  	if self.motionProxy.walkIsActive():
 #       	walkTo(0.00001, 0, 0)


####### threads #######
	def default_thread(self):
		self.thread = threading.Thread(target=self.default_config)
		self.thread.start()

	def doit_in_thread(self):
		self.thread = threading.Thread(target=self.makerobotmove)
		self.thread.start()
	
	def doit_in_thread1(self):
		self.thread1 = threading.Thread(target=self.connect_ITshoes)
		self.thread1.start()

	def thread_zmp_coordinates(self):
		self.thread_zmp = threading.Thread(target=self.zmp_coordinates)
		self.thread_zmp.start()

	def thread_readFSRvalues(self):
		self.thread_FSR = threading.Thread(target=self.readFSRvalues_callback)
		self.thread_FSR.start()
	
	def thread_save_to_db(self):
		self.thread_savetodb = threading.Thread(target=self.save_to_db)
		self.thread_savetodb.start()

	def thread_readitshoevalues(self):
		self.thread_readitshoevalue = threading.Thread(target=self.read_itshoe_values)
		self.thread_readitshoevalue.start()

	def thread_save_from_topic(self):
		self.thread_saveftopic = threading.Thread(target=self.save_from_topic)
		self.thread_saveftopic.start()

	def thread_click_to_save(self):
		self.thread_clicksave = threading.Thread(target=self.click_to_save)
		self.thread_clicksave.start()


	
	#def save_to_db(self):
	#	global db_table_name1
	#	global db, cur
	#	global db_table_info
	#	global countShoe, countRobot
	#	global sensor1L5, sensor1L6, sensor1L7, sensor1L8, sensor25L1 ,sensor25L2,sensor25L3,sensor25L4,LFsrFL,	LFsrFR,	LFsrBL,	LFsrBR,	RFsrFL,	RFsrFR,	RFsrBL,	RFsrBR,	COP_lx,	COP_ly,	COP_rx,	COP_ry,	GyrX ,	GyrY,	GyrZ,	angX,	angY,	angZ,	accX,	accY,	accZ
		#print(sensor25L1)
	#	aux = "CREATE TABLE IF NOT EXISTS "  + db_table_name1 + " (ITshoe_id varchar(15) DEFAULT NULL,data_date varchar(15) DEFAULT NULL,read_number varchar(30) DEFAULT NULL, countshoe varchar(10) DEFAULT NULL,s1 varchar(50) DEFAULT NULL,s2 varchar(50) DEFAULT NULL,s3 varchar(50) DEFAULT NULL,s4 varchar(50) DEFAULT NULL,s5 varchar(50) DEFAULT NULL,s6 varchar(50) DEFAULT NULL,s7 varchar(50) DEFAULT NULL,s8 varchar(50) DEFAULT NULL, countrobot varchar(10) DEFAULT NULL,LFsrFL varchar(25) DEFAULT NULL,LFsrFR varchar(25) DEFAULT NULL, LFsrBL varchar(25) DEFAULT NULL,LFsrBR varchar(25) DEFAULT NULL,RFsrFL varchar(25) DEFAULT NULL, RFsrFR varchar(25) DEFAULT NULL, RFsrBL varchar(25) DEFAULT NULL, RFsrBR varchar(25) DEFAULT NULL,COP_lx varchar(25) DEFAULT NULL,COP_ly varchar(25) DEFAULT NULL,COP_rx varchar(25) DEFAULT NULL,COP_ry varchar(25) DEFAULT NULL, GyrX varchar(25) DEFAULT NULL, GyrY varchar(25) DEFAULT NULL, GyrZ varchar(25) DEFAULT NULL,angX varchar(25) DEFAULT NULL,angY varchar(25) DEFAULT NULL,angZ varchar(25) DEFAULT NULL, accX varchar(25) DEFAULT NULL,accY varchar(25) DEFAULT NULL,accZ varchar(25) DEFAULT NULL)"
	#	db.query(aux)		
	#	sql1 = "INSERT INTO " +db_table_name1+ " (ITshoe_id, data_date, read_number, countShoe, s1,s2,s3,s4,s5,s6,s7,s8,countRobot ,LFsrFL ,LFsrFR , LFsrBL ,LFsrBR ,RFsrFL , RFsrFR , RFsrBL , RFsrBR ,COP_lx ,COP_ly ,COP_rx ,COP_ry , GyrX , GyrY , GyrZ ,angX ,angY ,angZ , accX ,accY ,accZ ) VALUES (%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s )"
	#	val = ("192.168.8.65","date",db_table_info,countShoe,sensor1L5,sensor1L6,sensor1L7,sensor1L8,sensor25L1,sensor25L2,sensor25L3,sensor25L4,countRobot,LFsrFL ,LFsrFR , LFsrBL ,LFsrBR ,RFsrFL , RFsrFR , RFsrBL , RFsrBR ,COP_lx ,COP_ly ,COP_rx ,COP_ry , GyrX , GyrY , GyrZ ,angX ,angY ,angZ , accX ,accY ,accZ )
	#	cur.execute(sql1, val)
	#	db.commit() 

#def save data to db 
	def save_to_db(self):
		global db_table_name1
		global db, cur
		global db_table_info
		global countShoe, countRobot
		global sensor1L5, sensor1L6, sensor1L7, sensor1L8, sensor25L1 ,sensor25L2,sensor25L3,sensor25L4
		#print(sensor25L1)
		
		sql1 = "INSERT INTO " +db_table_name1+ " (ITshoe_id, data_date, read_number, countShoe, s1,s2,s3,s4,s5,s6,s7,s8 ) VALUES (%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s,%s )"
		val = ("192.168.8.65","date",db_table_info,countShoe,sensor1L5,sensor1L6,sensor1L7,sensor1L8,sensor25L1,sensor25L2,sensor25L3,sensor25L4)
		cur.execute(sql1, val)
		db.commit() 


#def main, launch app
def main():
	
	global helpme, dc_button, cs_button
	helpme = 1

	supera= super1()
	#sb=Scrollbar(supera.root).grid(sticky ='ns')

	#frame = VerticalScrolledFrame(supera.root).grid(row =0 , column=0, sticky="ns")
	
	
	menubar = Menu(supera.root)
	filemenu = Menu(menubar, tearoff = 0)
	filemenu.add_command(label="Connect_wR", command = supera.create_window_to_setup_robot_IP_and_PORT)
	filemenu.add_command(label = "Connect_wITshoe", command = supera.create_window_to_setup_ITshoe_IP)
	filemenu.add_command(label = "Connect_wDB", command = supera.Connect_DB)
	filemenu.add_command(label = "Save as...", command = supera.donothing)
	filemenu.add_command(label = "Close", command = supera.donothing)

	filemenu.add_separator()

	filemenu.add_command(label = "Exit", command = supera.root.quit)
	menubar.add_cascade(label = "File", menu = filemenu)
	editmenu = Menu(menubar, tearoff=0)
	editmenu.add_command(label = "Undo", command = supera.donothing)

	editmenu.add_separator()

	editmenu.add_command(label = "Cut", command = supera.donothing)
	editmenu.add_command(label = "Copy", command = supera.donothing)
	editmenu.add_command(label = "Paste", command = supera.donothing)
	editmenu.add_command(label = "Delete", command = supera.donothing)
	editmenu.add_command(label = "Select All", command = supera.donothing)

	menubar.add_cascade(label = "Edit", menu = editmenu)
	helpmenu = Menu(menubar, tearoff=0)
	helpmenu.add_command(label = "Help Index", command = supera.donothing)
	helpmenu.add_command(label = "About...", command = supera.donothing)
	menubar.add_cascade(label = "Help", menu = helpmenu)
	
	
	cs_button = tk.Button(supera.root, text="save_data", command=lambda: supera.thread_click_to_save())
	cs_button.grid(row = 1,column = 30, columnspan =2, pady= 1, padx =2)
	
	dc_button = tk.Button(supera.root, text="default_config", command=lambda: supera.default_thread())
	dc_button.grid(row = 27,column = 1, pady= 1, padx =2)

	dc_lable=tk.Label(supera.root, text="data gathering:").grid(row = 27,column = 0, pady= 1, padx =1)

	dcstart_button = tk.Button(supera.root, text="start", command=lambda: supera.start_default())
	dcstart_button.grid(row = 27,column = 2, pady= 1, padx =2)

	dcstop_button = tk.Button(supera.root, text="stop", command=lambda: supera.stop_default())
	dcstop_button.grid(row = 27,column = 3, pady= 1, padx =2)
	#FAZER POP UP DE 1 JANELA COM 2 OPcOES SAPATO OU ROBO , OU AMBAS, E COM BASE NA OPcAO IR PARA FUNcAO 1 OU 2 SAPATO OU ROBO . 
	#zmp_button = tk.Button(supera.root, text="zmp tracking", command=lambda: supera.thread_zmp_coordinates())
	#zmp_button.grid(row = 16,column = 16, columnspan =2, pady= 1, padx =2)

	

	#frame= supera.root.geometry("1024x720")

	#frame1=tk.Frame(supera.root).grid(row =0, column=0,sticky=tk.NW)

	#canvas=tk.Canvas(frame1,bg="Yellow",yscrollcommand=vscrollbar.set).grid(row=0,column=0)

#	vsbar = tk.Scrollbar(frame1,orient =VERTICAL,command = canvas.yview).grid(row=0,column= 30, sticky ='ns')

#	canvas.config(yscrollcommand=vsbar.set)
	
	#scrollbar= tk.scrollbar(frame,orient="vertical",command=canvas.yview)
	termf_lable=tk.Label(supera.root, text="Terminal").grid(row = 0,column = 7, pady= 1, padx =1)

	termf=Frame(supera.root, height=360, width=512)
	termf.grid(row = 1, rowspan= 15, column=0, columnspan= 15)
	wid = termf.winfo_id()
	os.system('xterm -into %d -geometry 512x360 -sb &' % wid)
	supera.root.config(menu = menubar)
	
	#place crussor on the textbox while updating different frames. how to fix? maybe the following instruction
	 #para dar update aos graficos e zmp sem ter de update na window toda. 
	
	#supera.root.after(1000,supera.connect_ITshoes)
	supera.thread_save_from_topic()
	supera.root.mainloop()

if __name__ == "__main__":
	main()