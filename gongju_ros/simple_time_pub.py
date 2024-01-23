import rclpy
from rclpy.node import Node
from std_msgs.msg import Header


class T_pub(Node):
    def __init__(self):
        super().__init__('time_pub') #type: ignore
        self.create_timer(1, self.pub_callback)
        self.pub = self.create_publisher(Header, 'time', 10)
        self.clock = self.get_clock()
        
    def pub_callback(self):
        msg = Header()
        msg.frame_id = 'this is time'
        msg.stamp = self.clock.now().to_msg()
        self.pub.publish(msg)

def main():
    rclpy.init()
    node = T_pub() #type: ignore
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.destroy_node()

if __name__ == '__main__':
    main()
