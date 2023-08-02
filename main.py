import sensor, image, time

from pid import PID
from pyb import Servo

pan_servo=Servo(1)
tilt_servo=Servo(2)
pan_servo.pulse_width(1800)
tilt_servo.pulse_width(1800)

pan_servo.calibration(1200,2500,1800) #-90 ~ 90
tilt_servo.calibration(1450,2050,1800) #-32 ~ 23

#red_threshold  = (68, 100, 7, 127, 5, 21)
red_threshold  =(82, 100, -56, 127, 8, 65)

#pan_pid = PID(p=0.08, i=0, imax=90) #脱机运行或者禁用图像传输，使用这个PID
#tilt_pid = PID(p=0.08, i=0, imax=90) #脱机运行或者禁用图像传输，使用这个PID
pan_pid = PID(p=0.1, i=0, imax=90)#在线调试使用这个PID
#tilt_pid = PID(p=0.1, i=0, imax=90)#在线调试使用这个PID


sensor.reset() # Initialize the camera sensor.
sensor.set_pixformat(sensor.RGB565) # use RGB565.
sensor.set_framesize(sensor.QQVGA) # use QQVGA for speed.
sensor.skip_frames(10) # Let new settings take affect.
sensor.set_auto_whitebal(False) # turn this off.
clock = time.clock() # Tracks FPS.

def find_max(blobs):
    max_size=0
    for blob in blobs:
        if blob[2]*blob[3] > max_size:
            max_blob=blob
            max_size = blob[2]*blob[3]
    return max_blob


while(True):
    clock.tick() # Track elapsed milliseconds between snapshots().
    img = sensor.snapshot() # Take a picture and return the image.

    blobs = img.find_blobs([red_threshold])
    #pan_servo.angle(180)
    #tilt_servo.angle(0)

        #tilt_output=tilt_pid.get_pid(tilt_error,1)
        #print("pan_output",Servo.pulse_width())
        #pan_servo.angle(pan_servo.angle()+pan_output)
        #tilt_servo.angle(tilt_servo.angle()-tilt_output)
    #pan_servo.angle(-90)
    #pan_servo.pulse_width(1200)

    #tilt_servo.angle(23)
