import rclpy
from rclpy.node import Node
from std_msgs.msg import Header


class T_sub(Node):
    def __init__(self):
        super().__init__('time_sub') #type: ignore
        self.pub = self.create_subscription(Header, 'time', self.sub_callback, 10)
        
    def sub_callback(self, msg: Header):
        print(msg.frame_id)
        print(f"Sec: {msg.stamp.sec}, Nanosec: {msg.stamp.nanosec}")

def main():
    rclpy.init()
    node = T_sub() #type: ignore
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.destroy_node()

if __name__ == '__main__':
    main()
