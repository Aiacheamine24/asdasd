from system import System
from gpiozero import Button
import time

def main():
    # Create an instance of the System class
    # CN0 = 21
    # CN1 = 20
    # CN2 = 16
    # CN3 = 26
    # Valve Remplissage = 5
    # Valve Purge = 6
    # A = 14
    # B = 15
    # C = 18
    # D = 2
    # E = 3
    # F = 17
    # G = 27
    # P = 22
    sys = System(21, 20, 16, 26, 5, 6, 14, 15, 18, 2, 3, 17, 27, 22)
    # Launch the system
    sys.launch()
    
    # Check the sensors system.checkCn0()
    sys.cn0_button.wait_for_press()
    sys.checkCn0()
    sys.cn1_button.wait_for_press() 
    sys.checkCn1()
    sys.cn2_button.wait_for_press()
    sys.checkCn2()
    sys.cn3_button.wait_for_press() 
    sys.checkCn3()
    time.sleep(1)
    pass







if __name__ == '__main__':
    main()
    pass
