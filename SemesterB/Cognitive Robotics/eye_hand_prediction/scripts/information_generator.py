#!/usr/bin/env python
import rospy
from eye_hand_prediction.msg import gaze_info, preshape_info, time_interval
import random 

gaze_info_pub = rospy.Publisher("gaze_info_gen", gaze_info, queue_size = 10)
preshape_info_pub = rospy.Publisher("preshape_info_gen", preshape_info, queue_size = 10)
time_interval_pub = rospy.Publisher("time_interval", time_interval, queue_size = 10)


def information_generator():
    rospy.init_node('information_generator', anonymous=True)
    id_counter = 0
    rate = rospy.Rate(0.1) 
    time_intervals = [0, 200, 400, 600]
    while not rospy.is_shutdown():
        g_info = gaze_info()
        ps_info = preshape_info()
        time_int = time_interval()

        g_info.id = id_counter
        g_info.is_congruent = bool(random.getrandbits(1))

        ps_info.id = id_counter
        ps_info.is_congruent = bool(random.getrandbits(1))

        time_int.time_interval = random.choice(time_intervals)

        id_counter += 1
        gaze_info_pub.publish(g_info)
        preshape_info_pub.publish(ps_info)
        time_interval_pub.publish(time_int)

        rospy.loginfo(rospy.get_caller_id() + " Information generator \n Gaze is_congruent: \n %s ,  \n Preshape is_congruent: %s \n Time interval: %d " , g_info , ps_info, time_int)
        rate.sleep()

if __name__ == "__main__":
    try: 
        information_generator()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
