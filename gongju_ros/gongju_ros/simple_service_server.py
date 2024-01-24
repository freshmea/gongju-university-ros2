import rclpy
from rclpy.node import Node
from my_interface.srv import Mysrv


class Simple_service_server(Node):
    def __init__(self):
        super().__init__("simple_serive_server")  # type: ignore
        self.create_service(Mysrv, "mysrv", self.mysrv_callback)  # type: ignore

    def mysrv_callback(self, request: Mysrv.Request, response: Mysrv.Response):
        self.get_logger().info(f"{request.first}, {request.second}")
        response.sum = request.first + request.second
        response.multiply = request.first * request.second
        try:
            response.division = request.first / request.second
        except ZeroDivisionError:
            response.division = 0
        return response


def main():
    rclpy.init()
    node = Simple_service_server()  # type: ignore
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.destroy_node()


if __name__ == "__main__":
    main()
