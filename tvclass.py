'''LEOJ M. SUAVERDEZ OBJECT ORIENTED TV ASSIGNMENT'''
# Create class named TV
class TV:
# Self Attributes for TV class which is channel, volume level, power
    def __init__(self, channel, volume_level, power):
        self.channel = channel
        self.volume_level = volume_level
        self.power = power
# Turn on tv
    def turn_on(self):
        self.power = True
# Turn off tv
    def turn_off(self):
        self.power = False
# Get channel
    def getChannel(self):
        print (f"Your current channel is {self.channel}")
# Set Channel
# Get Volume
# Set Volume
# Channel Up
# Channel Down
# Volume Up
# Volume Down
# Create two objects TV1 and TV2
# TV1 = channel 30 and volume level 3
# TV2 = channel 3 and volume level 2

####################################TESTER ONLY######################################

tv1 = TV(0,0,False)

print(tv1.power)

tv1.turn_on()

print(tv1.power)

tv1.getChannel()