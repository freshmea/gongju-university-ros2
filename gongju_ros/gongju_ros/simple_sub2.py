import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from my_interface.msg import MyTopic


class Simple_sub2(Node):
    def __init__(self):
        super().__init__("simple_sub2")  # type: ignore
        self.create_subscription(String, "str", self.str_callback, 10)
        self.create_subscription(MyTopic, "my_topic", self.topic_callback, 10)

    def str_callback(self, msg: String):
        self.get_logger().info(f"simple_sub2: {msg.data}")

    def topic_callback(self, msg: MyTopic):
        self.get_logger().info(f"simple_sub2: {msg.stamp.sec}.{msg.stamp.nanosec}")
        self.get_logger().info(f"{msg.my_float}")


def main():
    rclpy.init()
    node = Simple_sub2()  # type: ignore
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.destroy_node()


if __name__ == "__main__":
    main()
