# 1 
'''
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
        
# 4 

class Device:
    def __init__(self,name):
        self.name=name
    def activate(self):
        print(f"{self.name} is working")
class SmartTV(Device):
    def __init__(self, name):
        super().__init__(name)
    def activate(self):
        print(f"TV {self.name} is working now")
class SmartLamp(Device):
    def __init__(self, name):
        super().__init__(name)
    def activate(self):
        print(f"Lamp {self.name} is working")
class SmartSpeaker(Device):
    def __init__(self, name):
        super().__init__(name)
        self.name=name
    def activate(self):
        print(f"Speaker {self.name} is working")

tv=SmartTV("LG")
lamp=SmartLamp("Desk Lamp")
speaker=SmartSpeaker("Echo")
Devices=[tv,lamp,speaker]
for device in Devices:
    device.activate()

# 5 

class Device:
    def __init__(self,name):
        self.name=name
    def volume(self,level):
        self.level=level
        print(f"Device {self.name} volume set to {self.level}")
class SmartSpeaker(Device):
    def __init__(self, name):
        super().__init__(name)
    def volume(self,level):
        self.level=level
        print(f"Speaker {self.name} is now at volume {self.level}/10.")
        print("Loud!" if self.level>7 else " ")
class SmartTV(Device):
    def __init__(self, name):
        super().__init__(name)
        self.name=name
    def volume(self, level):
        self.level=level
        print(f"{self.name} volume: {level}")
        print("Muted!" if self.level==0 else "")

speaker=SmartSpeaker("Bose")
speaker.volume(8)
speaker.volume(3)
tv=SmartTV("LG")
tv.volume(0)

# 6

class Device:
    def __init__(self,name):
        self.name=name
    def run_command(self,cmd):
        self.cmd=cmd
        print(f"Device {self.name} receiveed command: {self.cmd}")

class Oven(Device):
    def __init__(self, name):
        super().__init__(name)
    def run_command(self, cmd):
        print(f"Oven {self.name} receiveed command to {cmd}")
class AC(Device):
    def __init__(self, name):
        super().__init__(name)
    def run_command(self, cmd):
        print(f"AC {self.name} receiveed command to {cmd}")
class Speaker(Device):
    def __init__(self, name):
        super().__init__(name)
    def run_command(self, cmd):
        print(f"Speaker {self.name} receiveed command to {cmd}")
class Lights(Device):
    def __init__(self, name):
        super().__init__(name)
    def run_command(self, cmd):
        print(f"Lights {self.name} receiveed command to {cmd}")

oven=Oven("Suzuky")
ac=AC("Tadiran")
speaker=Speaker("Bose")
lights=Lights("main")
Devices=[oven,ac,speaker,lights]

def send(device,cmd):
    device.run_command(cmd)
send(ac,"start")
send(oven,"start")
send(speaker,"start")
send(lights,"start")

# 7

class Device:
    def __init__(self,name):
        self.name=name
    def run_schedule(self,hour):
        self.hour=hour
        print(f"{self.name} is idle. ")
class SmartLamp(Device):
    def __init__(self, name):
        super().__init__(name)
    def run_schedule(self, hour):
        print(f"turning on" if 18<=hour<=23 else "turning off")
class SmartAC(Device):
    def __init__(self, name):
        super().__init__(name)
    def run_schedule(self, hour):
        print(f"turning on" if 12<=hour<=20 else "turning off")
class SmartTV(Device):
    def __init__(self, name):
        super().__init__(name)
    def run_schedule(self, hour):
        print(f"turning on" if 20<=hour<=23 else "turning off")
lamp=SmartLamp("Bedroom")
ac=SmartAC("Living Room")
tv=SmartTV("Samsung")
lamp.run_schedule(21)
ac.run_schedule(21)
tv.run_schedule(21)

# 8 

class Device:
    def __init__(self,name):
        self.name=name
    def energy_usage(self):
        return 10
class SmartTV(Device):
    def __init__(self, name):
        super().__init__(name)
    def energy_usage(self):
        return 150
class SmartAC(Device):
    def __init__(self, name):
        super().__init__(name)
    def energy_usage(self):
        return 900
class SmartLamp(Device):
    def __init__(self, name):
        super().__init__(name)
    def energy_usage(self):
        return 8
class SmartSpeaker(Device):
    def __init__(self, name):
        super().__init__(name)
    def energy_usage(self):
        return 30
Devices=[
    SmartTV("SmartTV"),
    SmartAC("SmartAC"),
    SmartLamp("SmartLamp"),
    SmartSpeaker("SmartSpeaker")]
total=0

for device in Devices:
    print(device.name,":",device.energy_usage(),"w")
    total+=device.energy_usage()
print("Total:",total,"W")

# 9

class Device:
    def __init__(self,name):
        self.name=name
        self.curecct_status=None
    def activate(self):
        print(f"{self.name} is now on" )
    def deacticate(self):
        print(f"{self.name} is now off")
    def status(self):
        print(f"{self.name} unknown")
class SmartAC(Device):
    def __init__(self, name):
        super().__init__(name)
    def activate(self):
        print(f"AC {self.name} is now on")
        self.correct_status=True
    def deacticate(self):
        print(f"AC {self.name} is now off")
        self.correct_status=False
    def status(self):
        if self.correct_status==True:
            print(f"AC {self.name} temperature is set to 22 C")
        else:
            print(f"AC {self.name} is off")
class SmartGate(Device):
    def __init__(self, name):
        super().__init__(name)
    def activate(self):
        print(f"Gate {self.name} is open now")
        self.curecct_status=True
    def deacticate(self):
        print(f"Gate {self.name} is close now")
        self.curecct_status=False
    def status(self):
        if self.curecct_status==True:
            print(f"Gate {self.name} is currently closed")
        else:
            print(f"Gate {self.name} is off")
class SmartLighte(Device):
    def __init__(self, name):
        super().__init__(name)
    def activate(self):
        print(f"Light {self.name} is turn on")
    def deacticate(self):
        print(f"Light {self.name} is turn off")
    def status(self):
        print(f"Light {self.name}brightness is at 80%")
class SmartTV(Device):
    def __init__(self, name):
        super().__init__(name)
    def activate(self):
        print(f"Tv {self.name} is on")
        self.curecct_status=True
    def deacticate(self):
        print(f"TV {self.name} is off")
        self.curecct_status=False
    def status(self):
        if self.curecct_status==True:
            print(f"TV {self.name} is on")
        else:
            print(f"TV {self.name} is off")
class SmartSpeaker(Device):
    def __init__(self, name):
        super().__init__(name)
    def activate(self): 
        print(f"Speaker {self.name} is turn on")
        self.curecct_status=True
    def deacticate(self):
        print(f"Speaker {self.name} is turn off")
        self.curecct_status=False
    def status(self):
        if self.curecct_status==True:
            print(f"Speaker {self.name} is playing songs")
        else:
            print(f"Speaker {self.name} is off")

class HomeSystem:
    def __init__(self,devices):
        self.devices=devices if devices is not None else []
    def activate_all(self):
        for device in self.devices:
            device.activate()
    def deactivate_all(self):
        for device in self.devices:
            device.deacticate()
    def system_report(self):
        for device in self.devices:
            device.status()
    
devices_list = [
    SmartAC("Tornado"),
    SmartTV("LG"),
    SmartGate("Main Gate"),
    SmartSpeaker("Bose"),
    SmartLighte("Living Room")]

smarthome=HomeSystem(devices_list)

smarthome.activate_all()
smarthome.deactivate_all()
smarthome.system_report()
'''

# 10 

class Device:
    def __init__(self,name):
        self.name=name
    def trigger_alarm(self,alert_type):
        print(f"{self.name} received alert: {alert_type}")
class  SmartLamp(Device):
    def trigger_alarm(self, alert_type):
        print(f"{self.name} received alert {alert_type}, flash on!")
class SmartSpeaker(Device):
    def trigger_alarm(self, alert_type):
        print(f"{self.name} received alret {alert_type}, sound on!")
class SmartTV(Device):
    def trigger_alarm(self, alert_type):
        print(f"{self.name} received alret {alert_type},  emergency broadvast on")
class SmartDoorLock(Device):
    def trigger_alarm(self, alert_type):
        print(f"{self.name} received alret {alert_type}, the doors are locks")

class AlarmSystem:
    def __init__(self):
        self.devices=[
        SmartTV("LG"),
        SmartDoorLock("All doors"),
        SmartSpeaker("Bose"),
        SmartLamp("Living Room")]

    def send_alert(self,alert_type):
        for device in self.devices:
            device.trigger_alarm(alert_type)


emergency1=AlarmSystem()
emergency1.send_alert("fire")
emergency1.send_alert("break-in")

        

