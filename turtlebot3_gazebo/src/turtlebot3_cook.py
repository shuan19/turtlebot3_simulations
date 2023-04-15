#!/usr/bin/env python
import rospy
import numpy
import math
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

def move(xdistance):
   rospy.init_node('turtlebot3')
   velocity_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
   speed=0.1
   vel_msg = Twist()
   vel_msg.linear.x = speed*numpy.sign(xdistance)

	#Setting the current time for distance calculus
   t0 = rospy.Time.now().to_sec()
   current_distance = 0

   #Loop to move the turtle in an specified distance
   while(current_distance < abs(xdistance) ):
      #Publish the velocity
      velocity_publisher.publish(vel_msg)
      #Takes actual time to velocity calculus
      t1=rospy.Time.now().to_sec()
      #Calculates distancePoseStamped
      current_distance= speed*(t1-t0)
      #After the loop, stops the robot
   vel_msg.linear.x = 0
   #Force the robot to stop
   velocity_publisher.publish(vel_msg)

def rotate(angle):
   rospy.init_node('turtlebot3')
   velocity_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
   rotation_speed=0.25
   vel_msg = Twist()
   vel_msg.angular.z = rotation_speed*numpy.sign(angle)

	#Setting the current time for distance calculus
   t0 = rospy.Time.now().to_sec()
   current_angle = 0

   #Loop to move the turtle in an specified distance
   while(current_angle < abs(angle) ):
      #Publish the velocity
      velocity_publisher.publish(vel_msg)
      #Takes actual time to velocity calculus
      t1=rospy.Time.now().to_sec()
      #Calculates distancePoseStamped
      current_angle= rotation_speed*(t1-t0)
      #After the loop, stops the robot
   vel_msg.angular.z = 0
   #Force the robot to stop
   velocity_publisher.publish(vel_msg)

def stop():
   rospy.init_node('turtlebot3')
   velocity_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
   vel_msg = Twist()
   vel_msg.angular.z = 0
   vel_msg.linear.x = 0
   velocity_publisher.publish(vel_msg)

def Plate_to_rice():
    # Starts a new node
    rotate(-1.07*math.pi*0.5)
    move(0.37)
    rotate(-1.07*math.pi*0.5)
    move(0.5)
    rotate(1.07*math.pi*0.5)
    rospy.sleep(2)

def Rice_to_stove():
   rotate(1.07*math.pi*0.5)
   move(0.48)
   rotate(0.92*math.pi*0.5)
   move(1.05)
   rotate(-1.07*math.pi*0.5)
   rospy.sleep(2)

def Stove_to_fish():
   rotate(1.16*math.pi*0.5)
   move(0.15)
   rotate(1.23*math.pi*0.5)
   move(0.49)
   rospy.sleep(2)

def Fish_to_cuttingboard():
   rotate(1.02*math.pi*0.5)
   move(0.65)
   rotate(-1.07*math.pi*0.5) 
   rospy.sleep(2)

def Cuttingboard_to_plate():
   rotate(1.08*math.pi*0.5)
   move(0.19)
   rotate(1.05*math.pi*0.5)
   move(0.5)  

def myhook():
  print ("shutdown time!")

rospy.on_shutdown(myhook)

if __name__ == '__main__':    
    try:
        stop()
        Plate_to_rice()
        Rice_to_stove()
        Stove_to_fish()
        Fish_to_cuttingboard()
        Cuttingboard_to_plate()
        

    except rospy.ROSInterruptException: pass
