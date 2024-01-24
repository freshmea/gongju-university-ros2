import rclpy
from rclpy.node import Node
from my_interface.srv import Mysrv


class Simple_service_client(Node):
    def __init__(self):
        super().__init__("simple_serive_client")  # type: ignore
        self.cli = self.create_client(Mysrv, "mysrv")
        while not self.cli.wait_for_service(2.0):
            self.get_logger().info("waiting for server...")
        self.req = Mysrv.Request()

    def send_request(self, first: int, second: int):
        self.req.first = first
        self.req.second = second
        self.future = self.cli.call_async(self.req)
        rclpy.spin_until_future_complete(self, self.future)
        return self.future.result()


def main():
    rclpy.init()
    node = Simple_service_client()  # type: ignore
    response: Mysrv.Response = node.send_request(14, 16)  # type: ignore
    node.get_logger().info(
        f"Sum: {response.sum}, Multiply: {response.multiply}, Division: {response.division}"
    )
    node.destroy_node()


if __name__ == "__main__":
    main()
