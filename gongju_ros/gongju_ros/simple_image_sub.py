import rclpy
from rclpy.node import Node
from sensor_msgs.msg import CompressedImage
import cv2
from cv_bridge import CvBridge, CvBridgeError


class Simple_sub_image(Node):
    def __init__(self):
        super().__init__("simple_sub_image")  # type: ignore
        self.create_subscription(
            CompressedImage, "/camera/image/compressed", self.img_callback, 10
        )
        self.cb = CvBridge()

    def img_callback(self, msg: CompressedImage):
        self.frame = self.cb.compressed_imgmsg_to_cv2(msg)
        cv2.imshow("img", self.frame)
        cv2.waitKey(1)


def main():
    rclpy.init()
    node = Simple_sub_image()  # type: ignore
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.destroy_node()


if __name__ == "__main__":
    main()
