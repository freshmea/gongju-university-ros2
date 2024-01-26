import random, time
import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile

from my_interface.msg import ArithmeticArgument
from my_interface.srv import ArithmeticOperator
from my_interface.action import ArithmeticChecker

from rclpy.callback_groups import ReentrantCallbackGroup
from rclpy.executors import MultiThreadedExecutor
from rclpy.action import ActionServer
from rclpy.action.server import ServerGoalHandle


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
        self.arithmetic_actino_server = ActionServer(
            self,
            ArithmeticChecker,
            "checker",
            self.checker_callback,
            callback_group=ReentrantCallbackGroup(),
        )
        self.argument_a = 0.0
        self.argument_b = 0.0
        self.argument_result = 0.0
        self.argument_fomula = ""
        self.operator_symbol = ["+", "-", "*", "/"]
        self.argument_operator = self.operator_symbol[1]

    def argument_callback(self, msg: ArithmeticArgument):
        self.argument_a = msg.argument_a
        self.argument_b = msg.argument_b
        self.get_logger().info(f"Argument A: {self.argument_a}")
        self.get_logger().info(f"Argument B: {self.argument_b}")
        self.arrument_formula = f"{self.argument_a} {self.argument_operator} {self.argument_b} = {self.argument_result}"
        self.argument_result = 0.0

    def operator_callback(self, request, response):
        self.get_logger().info("Incoming request")
        self.get_logger().info(
            f"Operator: {self.operator_symbol[request.arithmetic_operator-1]}"
        )
        self.argument_operator = self.operator_symbol[request.arithmetic_operator - 1]
        if request.arithmetic_operator == ArithmeticOperator.Request.PLUS:
            self.argument_result = self.argument_a + self.argument_b
        elif request.arithmetic_operator == ArithmeticOperator.Request.MINUS:
            self.argument_result = self.argument_a - self.argument_b
        elif request.arithmetic_operator == ArithmeticOperator.Request.MULTIPLY:
            self.argument_result = self.argument_a * self.argument_b
        elif request.arithmetic_operator == ArithmeticOperator.Request.DIVIDE:
            if self.argument_b != 0.0:
                self.argument_result = self.argument_a / self.argument_b
            else:
                self.argument_result = 0.0
        self.argument_fomula = f"{self.argument_a} {self.argument_operator} {self.argument_b} = {self.argument_result}"
        response.arithmetic_result = self.argument_result

        self.get_logger().info(f"Result: {self.argument_fomula}")
        return response

    def checker_callback(self, goal_handle: ServerGoalHandle):
        feedback_msg = ArithmeticChecker.Feedback()
        feedback_msg.formula = []
        total_sum = 0.0
        goal_sum = goal_handle.request.goal_sum
        while total_sum < goal_sum:
            total_sum += self.argument_result
            feedback_msg.formula.append(self.argument_fomula)
            goal_handle.publish_feedback(feedback_msg)
            time.sleep(1)
        goal_handle.succeed()
        result = ArithmeticChecker.Result()
        result.all_formula = feedback_msg.formula
        result.total_sum = total_sum
        return result


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
