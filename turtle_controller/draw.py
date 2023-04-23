#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class Draw(Node):

    def __init__(self):
        super().__init__("draw")
        self.pub_vel_ = self.create_publisher(Twist, "/turtle1/cmd_vel", 10)
        self.timer_ = self.create_timer(2.0, self.send_pub_vel)
        self.part = 1
        self.msg = Twist()
        self.get_logger().info("Drawing...")

    def movement1(self):
        self.msg.linear.x = 2.0
        self.msg.angular.z = 2.0
        self.pub_vel_.publish(self.msg)

    def movement2(self):
        self.msg.linear.x = -3.0
        self.msg.angular.z = 3.0
        self.pub_vel_.publish(self.msg)

    def send_pub_vel(self):
        if self.part == 1:
            self.movement1()
            self.part += 1

        else:
            self.movement2()
            self.part -= 1

def main(args=None):
    rclpy.init(args=args)
    node = Draw()
    rclpy.spin(node)
    rclpy.shutdown()
