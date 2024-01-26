import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient
from my_interface.action import ArithmeticChecker
from rclpy.task import Future
from rclpy.action.client import ClientGoalHandle
import sys
import argparse


class Checker(Node):
    def __init__(self):
        super().__init__("checker")  # type: ignore
        self.action_client = ActionClient(self, ArithmeticChecker, "checker")

    def send_goal(self, goal_sum):
        goal_msg = ArithmeticChecker.Goal()
        goal_msg.goal_sum = float(goal_sum)
        while not self.action_client.wait_for_server(timeout_sec=0.5):
            self.get_logger().info("Waiting for Server")

        self.send_goal_future = self.action_client.send_goal_async(
            goal_msg, feedback_callback=self.feedback_callback
        )
        self.send_goal_future.add_done_callback(self.goal_response_callback)

    def feedback_callback(self, feedback_msg):
        self.get_logger().info(f"Feedback: {feedback_msg.feedback.formula}")

    def goal_response_callback(self, future: Future):
        goal_handle: ClientGoalHandle = future.result()  # type: ignore
        if not goal_handle.accepted:
            self.get_logger().info("Goal Rejected")
            return
        self.get_logger().info("Goal Accepted")
        self.get_result_future: Future = goal_handle.get_result_async()
        self.get_result_future.add_done_callback(self.get_result_callback)
        self.get_logger().info("Goal Sent")

    def get_result_callback(self, future: Future):
        result = future.result().result  # type: ignore
        self.get_logger().info(f"Result: {result.all_formula} {result.total_sum}")


def main(argv=sys.argv[1:]):
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument(
        "-g", "--goal_total_sum", help="Goal Sum", default=100, type=float
    )
    parser.add_argument(
        "argv", nargs=argparse.REMAINDER, help="Remapping arguments for ROS"
    )
    args = parser.parse_args()
    rclpy.init(args=args.argv)
    node = Checker()  # type: ignore
    try:
        node.send_goal(args.goal_total_sum)
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.destroy_node()


if __name__ == "__main__":
    main()
