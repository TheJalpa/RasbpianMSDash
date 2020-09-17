#Work in progress, this is not ready for testing
#If anyone wants to test and contribute, feel free.
#The idea here is to have a script that will allow for a push button gpio swap the executes this script
#Which will essentially kill tuner studio, swap the dash files, and fire it back up.

from gpiozero import Button
import os

#dashbuttonstock = Button(3)
#dashbuttonrace = Button(2)

def swapdashstock():
    grabts = os.system("ps -ef | grep \"tty1\" | grep \"init ro\" | grep \"root\" | awk {\'print $2\'}")
    os.system("kill " + grabts)
    sleep(3)
    os.system("rm -rf /home/pi/dashfile && cp /home/pi/dash1 /home/pi/dashfile")
    #os.system("command to start tuner studio with specific tune")
def swapdashrace():
    grabts = os.system("ps -ef | grep \"tty1\" | grep \"init ro\" | grep \"root\" | awk {\'print $2\'}")
    os.system("kill " + grabts)
    sleep(3)
    os.system("rm -rf /home/pi/dashfile && cp /home/pi/dash2 /home/pi/dashfile")
#dashbuttonstock.when_pressed = swapdashstock()
#dashbuttonrace.when_pressed = swapdashrace()
swapdashstock()
#pause()