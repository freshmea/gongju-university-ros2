import rclpy
from rclpy.node import Node
from std_msgs.msg import Header
from std_msgs.msg import String


class T_sub(Node):
    def __init__(self):
        super().__init__('time_sub') #type: ignore
        self.create_subscription(Header, 'time', self.sub_callback, 10)
        self.create_subscription(String, 'str', self.sub_m_callback, 10)

    def sub_callback(self, msg: Header):
        self.get_logger().info(msg.frame_id)
        self.get_logger().info(f"Sec: {msg.stamp.sec}, Nanosec: {msg.stamp.nanosec}")

    def sub_m_callback(self, msg: String):
        self.get_logger().info(f'Incomming Data: {msg.data}')

def main():
    rclpy.init()
    node = T_sub() #type: ignore
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.destroy_node()

if __name__ == '__main__':
    main()
