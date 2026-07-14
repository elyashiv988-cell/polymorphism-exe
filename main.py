# 1 
class Device:
    def __init__(self,name):
        self.name=name
    def activate(self):
        print(f"Device {self.name} is now on. ")
class SmartTV(Device):
    def __init__(self, name):
        super().__init__(name)
    def activate(self):
        print(f"TV {self.name} is playing the home screen")
class SmartSeaker(Device):
    def __init__(self, name):
        super().__init__(name)
    def activate(self):
        print(f"Speaker {self.name} is ready to play music. ")
tv=SmartTV("Samsung")
tv.activate()

speaker=SmartSeaker("Echo")
speaker.activate()

# 2

class Device:
    def __init__(self,name):
        self.name=name
    def deactivate(self):
        print(f"Device {self.name} is now off. ")
class SmartLamp(Device):
    def __init__(self, name):
        super().__init__(name)
    def deactivate(self):
        print(f"Lamp {self.name} is dimming and turning off")
class SmartAC(Device):
    def __init__(self, name):
        super().__init__(name)
    def deactivate(self):
        print(f"AC {self.name} is cooling down and switching off. ")
bedroom=SmartLamp("Bedroom Lamp")
bedroom.deactivate()        
ac=SmartAC("Living Room AC")
ac.deactivate()
