import rospy
from yahboomcar_msgs.msg import TargetArray
import time
from Rosmaster_Lib import Rosmaster
import math

bot = Rosmaster()

bot.create_receive_threading()

last = None


class YoloDetectSubscriber:
   
    def __init__(self):
        rospy.init_node('yolo_detect_subscriber', anonymous=True)
        rospy.Subscriber('DetectMsg', TargetArray, self.callback)
        rospy.spin()

    def callback(self, data):
        # Implement your logic here to handle received messages
        # For example, you can print the received data
        print("Received targets:")
        for target in data.data:
            print("Frame ID:", target.frame_id)
            #print("Scores:", target.scores)
            print("Position (x, y):", "%.2f"% target.ptx, ",", "%.2f"% target.pty)
            print("Width, Height:", "%.2f"% target.distw, ",", "%.2f"% target.disth)
            print("Center (x, y):", "%.2f"% target.centerx, ",", "%.2f"% target.centery)
            #print("Stamp:", target.stamp)
            print("--------------------")

            nama_obj = target.frame_id
            kordinat_x = target.ptx + target.centerx
            kordinat_z = target.disth / 2
            print("Position (x, y, z):", "%.2f"% kordinat_x,  "%.2f"% kordinat_z)
            
            # Menggerakkan servo arm
            self.run_motor_pt(nama_obj, kordinat_x, kordinat_z)
        
        def run_motor(self, M1, M2, M3, M4):
            bot.set_motor(M1, M2, M3, M4)
            return M1, M2, M3, M4
            
            
        def motor_from_pt(self, nama_obj, kordinat_x, kordinat_z):
        
            # rumus untuk following object terhadap kordinat_x dan kordinat_z
               
            
         

if __name__ == '__main__':
    try:
       
        YoloDetectSubscriber()
    
        
    except rospy.ROSInterruptException:
        pass

