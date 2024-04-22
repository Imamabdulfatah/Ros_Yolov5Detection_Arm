import time

class YoloDetectSubscriber:
    def __init__(self):
        """Initializer for the YoloDetectSubscriber."""
        pass

    def update_coordinates_null(self):
       ptx, pty = 45, 45  # Initialize starting points
       while pty <= 335:
            # Check if ptx is between 100 and 200
            if 100 <= ptx <= 200:
                yield (0, 0)
            else:
                yield (ptx, pty)

            # Increment ptx
            ptx += 40
            # Reset ptx to 45 if it exceeds 535 and increment pty
            if ptx > 535:
                ptx = 45
                pty += 40

            time.sleep(1)  # Pause for 1 second
            print(f"Current ptx: {ptx}, Current pty: {pty}")
    
    def update_coordinates(self):
        """Generator method to update and yield coordinates in a controlled environment."""
        ptx, pty = 45, 45  # Initialize starting points
        while pty <= 335:
            yield (ptx, pty)
            ptx += 20
            if ptx > 535:
                ptx = 0
                pty += 20
            time.sleep(1)  # Simulate delay for obtaining new coordinates
            print(pty, ptx)
    def arm_servo(self, s1, s2, s3, s4, s5, s6):
        return s1, s2, s3, s4, s5, s6

    def arm_servo_from_pt(self):
        """
        Coordinate transformation and servo control based on detected points.
        """
        for x, y in self.update_coordinates_null():
            s1, s2 = x, y   
            s3, s4, s5, s6 = 90, 90, 90, 90  

            s1_main = s1 / 6
            s2_main = s2 / 3.76

            servo_positions = self.arm_servo(s1_main, s2_main, s3, s4, s5, s6)
            print(f"Updated servo positions to {servo_positions}")
            print("==============================================")
# Example usage
if __name__ == "__main__":
    try:
        subscriber = YoloDetectSubscriber()
        subscriber.arm_servo_from_pt()
    except:
        pass 


# untuk sudut x servo 1   dengan kordinat 45 - 135
# untuk sudut y servo 2, 3 dan 4 dengan kordinat servo 2 (45 - 90) servo 3(90 - 45) servo 4 (135 - 180)
# untuk sudut z servo 2, 3 dan 4 dengan kordinat servo 2 (90 - 135)  servo 3 
