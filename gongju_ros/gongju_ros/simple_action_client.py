import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient
from my_interface.action import Fibonacci
import sys


class Fibonacci_action_client(Node):
    def __init__(self):
        super().__init__("fibonacci_client")  # type: ignore
        self.action_client = ActionClient(self, Fibonacci, "fibonacci")

    def send_goal(self, step):
        goal_msg = Fibonacci.Goal()
        goal_msg.step = int(step)
        self.action_client.wait_for_server()
        self.send_goal_future = self.action_client.send_goal_async(
            goal_msg, feedback_callback=self.feedback_callback
        )
        self.send_goal_future.add_done_callback(self.goal_response_callback)

    def feedback_callback(self, feedback_msg):
        self.get_logger().info(f"Feedback: {feedback_msg.feedback.temp_seq}")

    def goal_response_callback(self, future):
        goal_handle = future.result()
        if not goal_handle.accepted:
            self.get_logger().info("Goal Rejected")
            return
        self.get_logger().info("Goal Accepted")
        self.get_result_future = goal_handle.get_result_async()
        self.get_result_future.add_done_callback(self.get_result_callback)
        self.get_logger().info("Goal Sent")

    def get_result_callback(self, future):
        result = future.result().result
        self.get_logger().info(f"Result: {result.seq}")


def main(args=None):
    rclpy.init(args=args)
    node = Fibonacci_action_client()  # type: ignore
    try:
        node.send_goal(sys.argv[1])
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.destroy_node()


if __name__ == "__main__":
    main()
