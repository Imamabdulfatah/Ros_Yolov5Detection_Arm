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
            print("Width, Height:", "%.2f"% target.distw, ",", "%.2f"% target.disth)
            print("--------------------")

            nama_obj = target.frame_id
            kordinat_x = target.ptx + target.centerx
            kordinat_y = 480 - (target.pty + target.centery)
            kordinat_z = (target.ptx + target.disth)/2
            print("Position (x, y, z):", "%.2f"% kordinat_x, ",", "%.2f"% kordinat_y, ",", "%.2f"% kordinat_z)
            
            # Menggerakkan servo arm
            self.arm_servo_from_pt(nama_obj, kordinat_x, kordinat_y, kordinat_z)

    def arm_servo(self, s1, s2, s3, s4, s5, s6):
        bot.set_uart_servo_angle_array([s1, s2, s3, s4, s5, s6])
        return s1, s2, s3, s4, s5, s6

    def arm_servo_from_pt(self, nama_obj, kordinat_x, kordinat_y, kordinat_z):
        # Lakukan pemetaan linier dari koordinat ptx dan pty ke sudut servo
        # Contoh implementasi sederhana
        read_array = bot.get_uart_servo_angle_array()
        print (read_array)
        s1 = read_array[0]
        s2 = read_array[2]
        if s1 and s2 == -1:
            pass
        else:    
            if kordinat_x<320 and kordinat_y<240:
                pos_x = 20 - (math.ceil(kordinat_x/16))
                pos_y = 11 + (math.ceil(kordinat_y/22))
                pos_z = (math.ceil(kordinat_z/2.389))
                #s2 = pos_z
                #s4 = pos_z
                print(pos_x)
                print(pos_y)
                print(pos_z)
                #print (s1-pos_x)
                #self.arm_servo(s1-pos_x, 130, s2-pos_y, 0, 90, 90)
                print("read array:", read_array)
            else:
                pos_x = math.ceil((kordinat_x-320)/16)
                pos_y = math.ceil((kordinat_y-240)/22)
                pos_z = (math.ceil(kordinat_z/2.389))
                #s4 = pos_z
                print(pos_x)
                print(pos_y)
                print(pos_z)
                self.arm_servo(s1+pos_x, 130, s2+pos_y, 0, 90, 90)
                print("read array:", read_array) 
    	
        nama = nama_obj
           
        #Set sudut servo menggunakan metode arm_servo yang ada
        #if nama == "cabe_merah":
        # if s2 > 90 :
        #     s2 = 90
        # else :
        #     s2 = s2
        # global last
        # if last == s1:
        # 	pass
        # else:
        # 	self.arm_servo(s1, 180, 0, 0, 90, 90)
        # 	#time.sleep(0.1)
        # 	last = s1
        # 	read_array = bot.get_uart_servo_angle_array()
        # 	print("read array:", read_array)

if __name__ == '__main__':
    try:
       
        YoloDetectSubscriber()
    
        
    except rospy.ROSInterruptException:
        pass

