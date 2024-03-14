from seg7 import Seg
from time import sleep
from gpiozero import Button
from gpiozero import LED

class System:
    # Example:
    # let's supose that the cn inputs are in the form of buttons.
    # cn0_pin = 17 # GPIO pin for the first Sensor
    # cn1_pin = 28 # GPIO pin for the second Sensor
    # cn2_pin = 20 # GPIO pin for the third Sensor
    # cn3_pin = 23 # GPIO pin for the fourth Sensor
    # valve_remp = 14 # GPIO pin for the remote valve
    # valve_purge = 7 # GPIO pin for the purge valve
    
    def __init__(self, cn0, cn1, cn2, cn3, valve_remp, valve_purge, a, b, c, d, e, f, g, p):
        self.seg = Seg(a, b, c, d, e, f, g, p)
        self.cn0_pin = cn0
        self.cn1_pin = cn1
        self.cn2_pin = cn2
        self.cn3_pin = cn3
        self.valve_remp = valve_remp
        self.valve_purge = valve_purge
        self.cn0_button = Button(self.cn0_pin)
        self.cn1_button = Button(self.cn1_pin)
        self.cn2_button = Button(self.cn2_pin)
        self.cn3_button = Button(self.cn3_pin)
        self.valve_purge_led = LED(self.valve_purge)
        self.valve_remp_led = LED(self.valve_remp)
        pass
    
    def setup(self):

        pass
    
    def launch(self):
        self.valve_remp_led.on()
        self.valve_purge_led.off()
        self.cn0, self.cn1, self.cn2, self.cn3 = 0, 0, 0, 0
        self.seg.show_a_char('L')
        pass
    
    def checkCn0(self):
        self.cn0, self.cn1, self.cn2, self.cn3 = 1, 0, 0, 0
        self.seg.show_a_char('0')
        pass
    
    def checkCn1(self):
        self.cn0, self.cn1, self.cn2, self.cn3 = 1, 1, 0, 0
        self.seg.show_a_char('1')
        pass
    
    def checkCn2(self):
        self.cn0, self.cn1, self.cn2, self.cn3 = 1, 1, 1, 0
        self.seg.show_a_char('2')
        pass
    
    def checkCn3(self):
        self.valve_remp_led.off()
        self.valve_purge_led.on()
        self.cn0, self.cn1, self.cn2, self.cn3 = 1, 1, 1, 1
        self.seg.show_a_char('H')
        pass
    
