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

# 3 

class Device:
    def __init__(self,name,is_on):
        self.name=name
        self.is_on=is_on
    def status(self):
        print(f"{self.name}: on") if self.is_on else print(f"{self.name}: off")
class SmartTV(Device):
    def __init__(self, name, is_on,channel):
        super().__init__(name, is_on)
        self.channel=channel
    def status(self):
        print(f"{self.name}: on, watching chnnel {self.channel}") if self.is_on else print(f"{self.name}: off")
class SmartSpeaker(Device):
    def __init__(self, name, is_on,song):
        super().__init__(name, is_on)
        self.song=song
    def status(self):
        print(f"{self.name}: on, current song: {self.song}") if self.is_on else print(f"{self.name}: off")
tv=SmartTV("LG",True,8)
tv.status()
speaker=SmartSpeaker("Alexa",True,"Bohemian Rhapsody")
speaker.status()
        