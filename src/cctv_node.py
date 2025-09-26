#!/usr/bin/env python3

#Import Ros
import rclpy

from rclpy.node import Node
from sensor_msgs.msg import Image
from example_interfaces.msg import String

#OpenCv
import cv2
from cv_bridge import CvBridge


class CCTVNode(Node):
    def __init__(self):
        super().__init__('cctv_node')
        self.sub = self.create_subscription(Image, '/cctv/image', self.image_callback, 10)
        self.pub = self.create_publisher(String, '/fire_goal', 10)
        self.bridge = CvBridge()

    def image_callback(self, msg):
        frame = self.bridge.imgmsg_to_cv2(msg, "bgr8")
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        lower_fire = (0, 120, 150)
        upper_fire = (50, 255, 255)
        mask = cv2.inRange(hsv, lower_fire, upper_fire)
        if cv2.countNonZero(mask) > 500 :
            self.get_logger().info("Fire detected")
            self.pub.publish(String(data = "fire_at_(2,0)"))


def main(args=None):
    rclpy.init(args= args)
    node = CCTVNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()



if __name__ == "__main__":
    main()

