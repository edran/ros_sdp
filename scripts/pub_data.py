#!/usr/bin/python

import rospy
from ros_sdp.sdp_publisher import SDPPublisher

def main():
    rospy.init_node("ros_sdp_pub")
    pub = SDPPublisher()
    while not rospy.is_shutdown():
        pub.step()

if __name__ == "__main__":
    main()
