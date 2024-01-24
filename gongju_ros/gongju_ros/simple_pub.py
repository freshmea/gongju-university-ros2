import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile
from rclpy.qos import QoSHistoryPolicy, QoSDurabilityPolicy, QoSReliabilityPolicy
from std_msgs.msg import String
from my_interface.msg import MyTopic


class Simple_pub(Node):
    def __init__(self):
        super().__init__("simple_pub")  # type: ignore
        self.create_timer(1, self.print_callback)
        self.qos_profile = QoSProfile(
            history=QoSHistoryPolicy.KEEP_LAST,
            reliability=QoSReliabilityPolicy.BEST_EFFORT,
            durability=QoSDurabilityPolicy.VOLATILE,
            depth=10,
        )

        self.pub = self.create_publisher(String, "str", self.qos_profile)
        self.pub2 = self.create_publisher(MyTopic, "my_topic", self.qos_profile)

    def print_callback(self):
        msg = String()
        msg.data = "test string"
        msg2 = MyTopic()
        msg2.stamp = self.get_clock().now().to_msg()
        msg2.my_float = 3.141592

        self.pub.publish(msg)
        self.pub2.publish(msg2)


def main():
    rclpy.init()
    node = Simple_pub()  # type: ignore
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.destroy_node()


if __name__ == "__main__":
    main()
