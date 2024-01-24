import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import time
MAX_LIN = 0.21
MAX_ANG = 2.00


class Move_turtle(Node):
    def __init__(self):
        super().__init__('move_turtle') #type: ignore
        self.create_timer(0.1, self.pub_callback)
        self.create_timer(1/30, self.update_callback)
        self.pub = self.create_publisher(Twist, 'cmd_vel', 10)
        self.msg = Twist()
        self.ptime = time.time()
        
    def pub_callback(self):
        if self.msg.linear.x > MAX_LIN:
            self.msg.linear.x = MAX_LIN
        if self.msg.angular.z > MAX_ANG:
            self.msg.angular.z = MAX_ANG
        if self.msg.linear.x < -MAX_LIN:
            self.msg.linear.x = -MAX_LIN
        if self.msg.angular.z < -MAX_ANG:
            self.msg.angular.z = -MAX_ANG
        self.pub.publish(self.msg)

    def update_callback(self):
        # create your idea
        # self.msg.angular.z = 2.0
        # self.msg.linear.x += 0.01
        # if self.msg.linear.x > 10:
        #     self.msg.linear.x = 0.0
        if time.time() - self.ptime < 1:
            self.msg.linear.x = 0.1
            self.msg.angular.z = 0.0
        elif time.time() - self.ptime < 1.5:
            self.msg.linear.x = 0.0
            self.msg.angular.z = 1.0
        else:
            self.ptime = time.time()
        

def main():
    rclpy.init()
    node = Move_turtle() #type: ignore
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        # stop turtlebot3
        msg = Twist()
        msg.linear.x= 0.0
        msg.angular.z= 0.0
        for _ in range(10):
            node.pub.publish(msg)
        node.destroy_node()

if __name__ == '__main__':
    main()
