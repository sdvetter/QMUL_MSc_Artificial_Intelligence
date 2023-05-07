#!/usr/bin/env python
import rospy
from eye_hand_prediction.srv import prediction_accuracy, prediction_accuracyResponse
import numpy as np
import random
## Should handle calculation of expression probabilties 
## Did not implement bayesian network, simplified uniform probabilities
def callback(request):
    res = [1/3,1/3,1/3]
    r1 = random.uniform(0,1)
    r2 = random.uniform(0, (1-r1))
    r3 = 1 - (r1+r2)

    '''
    if res[0] == 0:
        if res[1] == 0 and res[2] == 0:
            print("o + ac + e")
        elif res[1] == 0:
            print("o + ac")
        elif res[2] == 0:
            print("o + e")
        else:
            res[0] = 0.8*0.5 + 1*0.5
            res[1] = 0.2*0.5
            res[2] = 0
    elif res[2] == 0:
        if (res[3] == 0):
            print("ac + e")
        else:
            print("ac")

    elif res[3] == 0:
        print("e")
    '''

    
    return prediction_accuracyResponse(r1, r2, r3)

## Creating the service 
def accuracy_computer():
    rospy.init_node("accuracy_computer")
    service = rospy.Service("accuracy_computer_service", prediction_accuracy, callback)
    
if __name__ == "__main__":
    try: 
        accuracy_computer()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass