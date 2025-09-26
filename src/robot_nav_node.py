#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from geometry_msgs.msg import PoseStamped

class RobotNav(Node):
    def __init__(self):
        super().__init__('robot_nav')
        self.sub = self.create_subscription(String, '/fire_goal', self.goal_callback, 10)
        self.pub = self.create_publisher(PoseStamped, '/goal_pose', 10)

    def goal_callback(self, msg):
        self.get_logger().info(f"Received fire goal: {msg.data}")
        goal = PoseStamped()
        goal.header.frame_id = "map"
        goal.header.stamp = self.get_clock().now().to_msg()
        goal.pose.position.x = 2.0
        goal.pose.position.y = 0.0
        goal.pose.orientation.w = 1.0
        self.pub.publish(goal)
        self.get_logger().info("Sent goal to Nav2")

def main(args=None):
    rclpy.init(args=args)
    node = RobotNav()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()