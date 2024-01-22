import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist


class Move_turtle(Node):
    def __init__(self):
        super().__init__('move_turtle') #type: ignore
        self.create_timer(0.1, self.pub_callback)
        self.create_timer(1/30, self.update_callback)
        self.pub = self.create_publisher(Twist, 'turtle1/cmd_vel', 10)
        self.msg = Twist()
        
    def pub_callback(self):
        self.pub.publish(self.msg)

    def update_callback(self):
        # create your idea
        self.msg.angular.z = 2.0
        self.msg.linear.x += 0.01
        if self.msg.linear.x > 10:
            self.msg.linear.x = 0.0

def main():
    rclpy.init()
    node = Move_turtle() #type: ignore
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.destroy_node()

if __name__ == '__main__':
    main()
