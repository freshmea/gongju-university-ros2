from launch import Action
import rclpy
from rclpy.node import Node
from rclpy.action import ActionServer
from my_interface.action import Fibonacci
import time


class Fibonacci_action_server(Node):
    def __init__(self):
        super().__init__("fibonacci_server")  # type: ignore
        self.action_server = ActionServer(
            self, Fibonacci, "fibonacci", self.execute_callback
        )

    def execute_callback(self, goal_handle):
        feedback_msg = Fibonacci.Feedback()
        feedback_msg.temp_seq = [0, 1]
        result = Fibonacci.Result()

        self.get_logger().info(f"Goal: {goal_handle.request.step} Accepted")

        for i in range(1, goal_handle.request.step):
            feedback_msg.temp_seq.append(
                feedback_msg.temp_seq[i - 1] + feedback_msg.temp_seq[i]
            )
            goal_handle.publish_feedback(feedback_msg)
            time.sleep(0.5)
        goal_handle.succeed()
        self.get_logger().info(f"Goal: {goal_handle.step} Succeeded")
        result.seq = feedback_msg.temp_seq
        return result


def main():
    rclpy.init()
    node = Fibonacci_action_server()  # type: ignore
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.destroy_node()


if __name__ == "__main__":
    main()
