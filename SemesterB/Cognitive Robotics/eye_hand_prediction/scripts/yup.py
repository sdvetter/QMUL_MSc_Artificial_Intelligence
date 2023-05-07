#!/usr/bin/env python
import rospy
from cr_week6_test.msg import perceived_info, robot_info
from cr_week6_test.srv import predict_robot_expression

class RobotController(object):
    def __init__(self):
     
        self.robot_info_pub = rospy.Publisher("robot_info_likelihoods", robot_info, queue_size = 10)
        rospy.Subscriber("perceived_info", perceived_info, self.handler)

    def handler(self, perceived_data):
        rospy.loginfo(rospy.get_caller_id() + "\n  perceived info: %s",perceived_data )

        rospy.wait_for_service("expression_prediction_service")
        ## Calling service to compute probabilites
        try:
            expression_likelihood_cli = rospy.ServiceProxy("expression_prediction_service", predict_robot_expression)
            expression_likelihoods = expression_likelihood_cli(perceived_data.object_size, perceived_data.human_action, perceived_data.human_expression)
            
        except rospy.ServiceException as e:
            print("Error: %s", e)

        rospy.loginfo("From service: \n %s",expression_likelihoods)

        ## Call on method to publish the expression probabilities
        self.publish_likelihoods(perceived_data.id, expression_likelihoods)
        
    ## Method creating a robot_info msg and publishing it
    def publish_likelihoods(self,id, expression_likelihoods):
        rob_info = robot_info()
        rob_info.id = id
        rob_info.p_happy = expression_likelihoods.p_happy
        rob_info.p_sad = expression_likelihoods.p_sad
        rob_info.p_neutral = expression_likelihoods.p_neutral

        self.robot_info_pub.publish(rob_info)

    def loop(self):
        rospy.spin()
    
if __name__ == "__main__":
    rospy.init_node('robot_controller', anonymous=True)
    node = RobotController()
    node.loop()
 
