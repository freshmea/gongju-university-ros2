import random
import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile
from my_interface.msg import ArithmeticArgument
from my_interface.srv import ArithmeticOperator
from rclpy.callback_groups import ReentrantCallbackGroup
from rclpy.executors import MultiThreadedExecutor


class Calculator(Node):
    def __init__(self):
        super().__init__("calculator")  # type: ignore
        qos_profile = QoSProfile(depth=10)
        self.create_subscription(
            ArithmeticArgument, "argument", self.argument_callback, qos_profile
        )
        self.arithmetic_service_server = self.create_service(
            ArithmeticOperator,
            "operator",
            self.operator_callback,
            qos_profile=qos_profile,
            callback_group=ReentrantCallbackGroup(),
        )
        self.argument_a = 0.0
        self.argument_b = 0.0
        self.operator_symbol = ["+", "-", "*", "/"]

    def argument_callback(self, msg: ArithmeticArgument):
        self.argument_a = msg.argument_a
        self.argument_b = msg.argument_b
        self.get_logger().info(f"Argument A: {self.argument_a}")
        self.get_logger().info(f"Argument B: {self.argument_b}")

    def operator_callback(self, request, response):
        self.get_logger().info("Incoming request")
        self.get_logger().info(
            f"Operator: {self.operator_symbol[request.arithmetic_operator-1]}"
        )
        if request.arithmetic_operator == ArithmeticOperator.Request.PLUS:
            response.arithmetic_result = self.argument_a + self.argument_b
        elif request.arithmetic_operator == ArithmeticOperator.Request.MINUS:
            response.arithmetic_result = self.argument_a - self.argument_b
        elif request.arithmetic_operator == ArithmeticOperator.Request.MULTIPLY:
            response.arithmetic_result = self.argument_a * self.argument_b
        elif request.arithmetic_operator == ArithmeticOperator.Request.DIVIDE:
            if self.argument_b != 0.0:
                response.arithmetic_result = self.argument_a / self.argument_b
            else:
                response.arithmetic_result = 0.0
        self.get_logger().info(f"Result: {response.arithmetic_result}")
        return response


def main():
    rclpy.init()
    node = Calculator()  # type: ignore
    executor = MultiThreadedExecutor(num_threads=4)
    executor.add_node(node)
    try:
        executor.spin()
    except KeyboardInterrupt:
        node.destroy_node()


if __name__ == "__main__":
    main()
