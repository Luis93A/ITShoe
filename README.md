# **ITShoe (Instrumented shoe)**:
Goal: Floors detection based on the measurement of the reaction forces robot-ground. 

To measure the reaction forces an instrumented shoe was developed and installed on a robot foot. 

ITshoe Hardware: PCB (Arduino mini, ESP8266, logic level shifter) and 8x pressure sensors.

# **(git code)**: 
Code to measure the sensors information and foward it through wifi to the ROS client. (arduino C) 

Code to receive the ITshoe data. (matlab and C/C++)

Code to analyze and treat the data (raw data -> forces, detach steps, interpolate steps). (matlab and C/C++)

Code to train and create a neural network. (matlab and C/C++)


# **FILES information**:
"arduino" : ITshoe script. 

"data" : Recorded data using the ITshoe for different grounds and robot gait parameters.

"matlab_scripts" : Matlab scripts. (offline)

"src_ros" : ROS package. (real-time)



# **"How to run" information** (ROS): 

(*Launch file MISSING*)

To connect the client computer with the ITshoes : *rosrun flex client*

To handle the sensor information : *rosrun flex data_handler*

To interpolate the data: *rosrun interp interp*

To launch the neural network and test individual steps: *rosrun nn1 ai*
