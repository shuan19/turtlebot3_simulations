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
   rospy.sleep(2)

def  Plate_to_stove():
    # Starts a new node
    rotate(1.01*math.pi*0.5)
    move(0.7)
    rotate(-1.01*math.pi*0.5)
    rospy.sleep(2)

def Stove_to_cuttingboard():
   rotate(-0.95*math.pi*0.5)
   move(0.5)
   rotate(-1.06*math.pi*0.5)
   move(0.4)
   rospy.sleep(2)

def Cuttingboard_to_nori():
   rotate(1.01*math.pi*0.5)
   move(0.52)
   rotate(-1.05*math.pi*0.5)
   move(0.55)
   rotate(1.04*math.pi*0.5)
   rospy.sleep(2)

def Nori_to_customer():
   rotate(-1.02*math.pi*0.5)
   move(0.42)
   rotate(0.95*math.pi*0.5) 
   move(1.38)
   rotate(1.05*math.pi*0.5) 
   move(0.45)
   rospy.sleep(5)

def myhook():
  print ("shutdown time!")

rospy.on_shutdown(myhook)

if __name__ == '__main__':    
    try:
        stop()
        Plate_to_stove()
        Stove_to_cuttingboard()
        Cuttingboard_to_nori()
        Nori_to_customer()
        

    except rospy.ROSInterruptException: pass
