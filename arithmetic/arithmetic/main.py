import random
import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile
from my_interface.msg import ArithmeticArgument
from rcl_interfaces.msg import SetParametersResult
from rclpy.parameter import Parameter


class Calculator(Node):
    def __init__(self):
        super().__init__("calculator")  # type: ignore
        qos_profile = QoSProfile(depth=10)
        self.create_subscription(
            ArithmeticArgument, "argument", self.argument_callback, qos_profile
        )
        self.argument_a = 0.0
        self.argument_b = 0.0

    def argument_callback(self, msg: ArithmeticArgument):
        self.argument_a = msg.argument_a
        self.argument_b = msg.argument_b
        self.get_logger().info(f"Argument A: {self.argument_a}")
        self.get_logger().info(f"Argument B: {self.argument_b}")


def main():
    rclpy.init()
    node = Calculator()  # type: ignore
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.destroy_node()


if __name__ == "__main__":
    main()
