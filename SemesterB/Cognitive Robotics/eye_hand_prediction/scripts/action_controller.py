#!/usr/bin/env python
import rospy
from eye_hand_prediction.msg import gaze_info, preshape_info, time_interval
import random 

class PerceivedInfoNode(object):
    def __init__(self):
        self.gaze_info = gaze_info()
        self.preshape_info = preshape_info()
        self.time_interval = time_interval() 

        # self.perceived_info_pub = rospy.Publisher("perceived_info", perceived_info, queue_size = 10)
        rospy.Subscriber("gaze_info_gen", gaze_info, self.gaze_info_handler)
        rospy.Subscriber("time_interval", time_interval, self.time_interval_handler)
        rospy.Subscriber("preshape_info_gen", preshape_info, self.preshape_info_handler)

    def time_interval_handler(self, time_interval):
        self.time_interval = time_interval
        return
        
    def gaze_info_handler(self, gaze_data):
        self.gaze_info = gaze_data
        return

    def preshape_info_handler(self, preshape_data):
        rate = rospy.Rate(0.1)

        rand_int = random.randint(1,8)
        self.preshape_info = preshape_data
        
        rospy.loginfo( "\n  human handler: self object \n %s self human %s", self.gaze_info, preshape_data )
        '''
        p_info = perceived_info()
        p_info.id = self.preshape_info.id
        p_info.human_expression = self.preshape_info.human_expression
        p_info.human_action = self.preshape_info.human_action
        p_info.object_size = self.gaze_info.object_size

        p_info = self.switch(rand_int, p_info)

        self.perceived_info_pub.publish(p_info)
        rospy.loginfo(rospy.get_caller_id() + "\n  Filter node with int: %d \n publishing:\n %s", rand_int, p_info )
        '''
        rate.sleep()

    def switch(self,rand_int, p_info):
        
        if rand_int == 1:
            p_info.object_size = 0
        elif rand_int == 2: 
            p_info.human_action = 0
        elif rand_int == 3: 
            p_info.human_expression = 0
        elif rand_int == 4: 
            p_info.object_size = 0
            p_info.human_action = 0
        elif rand_int == 5: 
            p_info.object_size = 0
            p_info.human_expression = 0
        elif rand_int == 6: 
            p_info.human_action = 0
            p_info.human_expression = 0
        elif rand_int == 7: 
            p_info.object_size = 0
            p_info.human_action = 0
            p_info.human_expression = 0
        return p_info
    


    def loop(self):
        rospy.spin()
    

if __name__ == "__main__":
    rospy.init_node('perception_filter', anonymous=True)
    node = PerceivedInfoNode()
    node.loop()

'''
        def switch(rand_int):
            p_info = perceived_info()
            match rand_int:
                case 1:
                    perceived_info.object_size = 0
                case 2:
                    perceived_info.human_action = 0
                case 3: 
                    perceived_info.human_expression = 0
                case 4:
                    perceived_info.object_size = 0
                    perceived_info.human_action = 0
                case 5:
                    perceived_info.object_size = 0
                    perceived_info.human_expression = 0
                case 6: 
                    perceived_info.human_action = 0
                    perceived_info.human_expression = 0
                case 7:
                    perceived_info.object_size = 0
                    perceived_info.human_action = 0
                    perceived_info.human_expression = 0
'''

    