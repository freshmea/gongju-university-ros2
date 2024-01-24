import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class Simple_pub(Node):
    def __init__(self):
        super().__init__('simple_pub') #type: ignore
        self.create_timer(1, self.print_callback)
        self.pub = self.create_publisher(String, 'str', 10)
        
    def print_callback(self):
        msg = String()
        msg.data = 'test string'
        self.pub.publish(msg)

def main():
    rclpy.init()
    node = Simple_pub() #type: ignore
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.destroy_node()

if __name__ == '__main__':
    main()
