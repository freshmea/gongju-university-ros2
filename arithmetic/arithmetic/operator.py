import rclpy
from rclpy.node import Node
from my_interface.srv import ArithmeticOperator
import random


class Operator(Node):
    def __init__(self):
        super().__init__("operator")  # type: ignore
        self.cli = self.create_client(ArithmeticOperator, "argument")
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info("service not available, waiting again...")
        self.req = ArithmeticOperator.Request()

    def send_request(self):
        self.req.arithmetic_operator = random.randint(1, 4)
        self.future = self.cli.call_async(self.req)
        return self.future


def main():
    rclpy.init()
    node = Operator()  # type: ignore
    future = node.send_request()
    user_trigger = True
    while rclpy.ok():
        if user_trigger:
            rclpy.spin_once(node)
            if future.done():
                try:
                    response = future.result()
                except Exception as e:
                    node.get_logger().info("Service call failed %r" % (e,))
                else:
                    node.get_logger().info(
                        f"Result of calculation: {response.arithmetic_result}"  # type: ignore
                    )
                    user_trigger = False
        else:
            user_input = input("Press Enter to continue: ")
            if user_input == "":
                future = node.send_request()
                user_trigger = True
    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
