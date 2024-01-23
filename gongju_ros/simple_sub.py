import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class Simple_sub1(Node):
    def __init__(self):
        super().__init__('simple_sub1') #type: ignore
        self.create_subscription(String, 'str', self.str_callback, 10)
        
    def str_callback(self, msg: String):
        # print('simple_sub1', msg.data)
        self.get_logger().info(f'simple_sub1 :{msg.data}')
        

def main():
    rclpy.init()
    node = Simple_sub1() #type: ignore
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.destroy_node()

if __name__ == '__main__':
    main()
