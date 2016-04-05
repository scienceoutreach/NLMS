"""
*
* Project Name: 	House Probing Robot for The Elderly

* Author List: 		Ridhwan Luthra

* Filename: 		ultrasonic.py

* Functions: 		ultra, callibration_ultra
* Global Variables:	NONE
*
"""

import RPi.GPIO as gpio
import time

print "Distance Measurement In Progress"
"""
        *
        * Function Name:    get_coords
        
        * Input:        digit
        
        * Output:       Returns coordinate of the obstacle with given digit from database.
        
        * Logic:        It opens the file containing the database and compares the digit values and then gives the coordinates
        
        * Example Call:     getcoords(8)
        """
        
def ultra():
        try:
                gpio.setmode(gpio.BCM)

                trig = 20
                echo = 21

                gpio.setup(trig,gpio.OUT)
                gpio.setup(echo,gpio.IN)
                gpio.output(trig, False)

                time.sleep(1)

                gpio.output(trig, True)
                time.sleep(0.00001)
                gpio.output(trig, False)

                while gpio.input(echo)==0:
                  pulse_start = time.time()

                while gpio.input(echo)==1:
                  pulse_end = time.time()      

                pulse_duration = pulse_end - pulse_start
                distance = pulse_duration*17150
                distance = round(distance, 2)
                return distance
        except:
                print "reading was interrupted"
        finally:
                gpio.cleanup(trig)
                gpio.cleanup(echo)

def callibration_ultra():
        try:
                gpio.setmode(gpio.BCM)

                trig_forward = 20
                echo_forward = 21
                
                trig_back = 22
                echo_back = 23
                
                trig_left = 19
                echo_left = 26

                gpio.setup(trig_forward,gpio.OUT)
                gpio.setup(trig_left,gpio.OUT)
                gpio.setup(trig_back,gpio.OUT)
                
                gpio.setup(echo_forward,gpio.IN)
                gpio.setup(echo_left,gpio.IN)
                gpio.setup(echo_back,gpio.IN)
                
                gpio.output(trig_forward, False)
                gpio.output(trig_left, False)
                gpio.output(trig_back, False)

                time.sleep(1)

                #taking forward distance
                gpio.output(trig_forward, True)
                time.sleep(0.00001)
                gpio.output(trig_forward, False)

                while gpio.input(echo_forward) == 0:
                  pulse_start = time.time()

                while gpio.input(echo_forward) == 1:
                  pulse_end = time.time()      

                pulse_duration = pulse_end - pulse_start
                d_forward = pulse_duration*17150
                d_forward = round(d_forward, 2)
		print d_forward
                print "forward done"
                """
		time.sleep(2)
                #taking left distance
                gpio.output(trig_left, False)
                time.sleep(1)
                gpio.output(trig_left, True)
                time.sleep(0.00001)
                gpio.output(trig_left, False)

                while gpio.input(echo_left) == 0:
                  pulse_start = time.time()

                while gpio.input(echo_left) == 1:
                  pulse_end = time.time()      

                pulse_duration = pulse_end - pulse_start
                d_left = pulse_duration*17150
                d_left = round(d_left, 2)
		print d_left
                print "left done"
		time.sleep(2)
                #taking back distance
                gpio.output(trig_back, False)
                time.sleep(1)
                gpio.output(trig_back, True)
                time.sleep(0.00001)
                gpio.output(trig_back, False)

                while gpio.input(echo_back) == 0:
                  pulse_start = time.time()

                while gpio.input(echo_back) == 1:
                  pulse_end = time.time()      

                pulse_duration = pulse_end - pulse_start
                d_back = pulse_duration*17150
                d_back = round(d_back, 2) - 1
		print d_back
                print "back taken"
                """
                return [d_forward, 0, 0]
        except KeyboardInterrupt:
                print "reading was interrupted"
        finally:
                gpio.cleanup(trig_forward)
                gpio.cleanup(echo_forward)
                gpio.cleanup(trig_left)
                gpio.cleanup(echo_left)
                gpio.cleanup(trig_back)
                gpio.cleanup(echo_back)
