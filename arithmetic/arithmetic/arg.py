import random
import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile
from my_interface.msg import ArithmeticArgument
from rcl_interfaces.msg import SetParametersResult
from rclpy.parameter import Parameter


class Argument(Node):
    def __init__(self):
        super().__init__("argument")  # type: ignore
        qos_profile = QoSProfile(depth=10)
        self.publisher_ = self.create_publisher(
            ArithmeticArgument, "argument", qos_profile
        )
        self.declare_parameter("min_random_num", 0)
        self.declare_parameter("max_random_num", 10)
        self.min_random_num = self.get_parameter("min_random_num").value
        self.max_random_num = self.get_parameter("max_random_num").value
        self.add_on_set_parameters_callback(self.parameter_callback)

        self.timer_ = self.create_timer(1.0, self.publish_argument)
        self.get_logger().info("Argument node has been started")

    def parameter_callback(self, parameters: list[Parameter]):
        for parameter in parameters:
            if parameter.name == "min_random_num":
                self.min_random_num = parameter.value
            elif parameter.name == "max_random_num":
                self.max_random_num = parameter.value
        return SetParametersResult(successful=True)

    def publish_argument(self):
        msg = ArithmeticArgument()
        msg.stamp = self.get_clock().now().to_msg()
        msg.argument_a = float(random.randint(self.min_random_num, self.max_random_num))  # type: ignore
        msg.argument_b = float(random.randint(self.min_random_num, self.max_random_num))  # type: ignore
        self.publisher_.publish(msg)


def main():
    rclpy.init()
    node = Argument()  # type: ignore
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.destroy_node()


if __name__ == "__main__":
    main()
