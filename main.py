import tkinter as tk
import gpiozero as gz
from time import sleep

class Seg7():
    def showNumber(self, numberToShow):
        if numberToShow in self._numbers.keys():
            self._numberToShow = self._numbers[numberToShow]
        else:
            self._numberToShow = self._numbers["E"]
            
        for i in range(8):
            self._pins[i].value = self._numberToShow[i]

    def __init__(self):
        self._numbers = {
            # L F E D
            "L": [0, 0, 0, 1, 1, 1, 0, 0],
            1: [0, 1, 1, 0, 0, 0, 0, 0],
            2: [1, 1, 0, 1, 1, 0, 1, 0],
            "H": [0, 1, 1, 0, 1, 1, 1, 0],
            "E": [1, 1, 0, 0, 1, 1, 1, 0],
        }
        
        self._pins = [gz.LED(14), gz.LED(15), gz.LED(18), gz.LED(2), gz.LED(3), gz.LED(17), gz.LED(27), gz.LED(22)]

class Valve():
    def __init__(self):
        self._valve_green = gz.LED(5)
        self._valve_red = gz.LED(6)
    
    def remplissage(self):
        self._valve_green.on()
        self._valve_red.off()
    
    def purge(self):
        self._valve_green.off()
        self._valve_red.on()

class Cuve():
    def __init__(self):
        self._seg7 = Seg7()
        self._valve = Valve()
        self._cap00 = gz.Button(21)
        self._cap01 = gz.Button(20)
        self._cap02 = gz.Button(16)
        self._cap03 = gz.Button(26)

        # Configuration des fonctions de rappel pour les boutons
        self._cap00.when_pressed = self.cap00
        self._cap01.when_pressed = self.cap01
        self._cap02.when_pressed = self.cap02
        self._cap03.when_pressed = self.cap03

    def cap00(self):
        self._seg7.showNumber("L")
        self._valve.remplissage()
        print("cap00 pressed so remplissage")
    
    def cap01(self):
        self._seg7.showNumber(1)
        self._valve.remplissage()
        print("cap01 pressed so remplissage")

    def cap02(self):
        self._seg7.showNumber(2)
        self._valve.remplissage()
        print("cap02 pressed so remplissage")

    def cap03(self):
        self._seg7.showNumber("H")
        self._valve.purge()
        print("cap03 pressed so Purge")

def main():
    # Instanciation de la cuve et des capteurs
    cuve = Cuve()
    # CrÃ©ation de la fenÃªtre
    window = tk.Tk()
    window.title("Cuve")
    window.geometry("800x600")
    # Affichage de la fenÃªtre
    window.mainloop()

if __name__ == "__main__":
    main()