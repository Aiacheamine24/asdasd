from gpiozero import LEDCharDisplay, LEDCharFont



class Seg:
    ### 7-segment display
    ### led1 = gpioinput for segment a and the other leds consequently

    def __init__(self, led1, led2, led3, led4, led5, led6, led7, led8):
 
        self.display = LEDCharDisplay(led1, led2, led3, led4, led5, led6, led7,active_high=False )
        pass
    
    def show_a_char(self, char):
        self.display.value = char
        pass
