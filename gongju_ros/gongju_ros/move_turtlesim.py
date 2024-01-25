import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import time
from rcl_interfaces.msg import SetParametersResult


class Move_turtle(Node):
    def __init__(self):
        super().__init__("move_turtle")  # type: ignore
        self.create_timer(0.1, self.pub_callback)
        self.create_timer(1 / 30, self.update_callback)
        self.create_timer(1, self.param_callback)
        self.pub = self.create_publisher(Twist, "turtle1/cmd_vel", 10)
        self.pub2 = self.create_publisher(Twist, "turtle2/cmd_vel", 10)
        self.msg = Twist()
        self.msg2 = Twist()
        self.ptime = time.time()
        self.declare_parameter("myparam", "My node default parameter")
        self.myparam = self.get_parameter("myparam").value
        # self.add_on_set_parameters_callback(self.setparam)
        self.add_on_set_parameters_callback(self.setparam)

    def setparam(self, param):
        self.myparam = param[0].value
        return SetParametersResult(successful=True)

    def pub_callback(self):
        self.pub.publish(self.msg)
        self.pub2.publish(self.msg2)

    def update_callback(self):
        # create your idea
        # self.msg.angular.z = 2.0
        # self.msg.linear.x += 0.01
        # if self.msg.linear.x > 10:
        #     self.msg.linear.x = 0.0
        if time.time() - self.ptime < 1:
            self.msg.linear.x = 3.0
            self.msg.angular.z = 0.0
        elif time.time() - self.ptime < 1.5:
            self.msg.linear.x = 0.0
            self.msg.angular.z = 2.0
        else:
            self.ptime = time.time()
        # update self.msg2
        self.msg2.linear.x = 2.0
        self.msg2.angular.z = 2.0

    def param_callback(self):
        self.get_logger().info(self.myparam)


def main():
    rclpy.init()
    node = Move_turtle()  # type: ignore
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.destroy_node()


if __name__ == "__main__":
    main()
