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
        print (f"Your Current Channel is {self.channel}")
# Set Channel
    def setChannel(self,newchannel):
        if 1<newchannel<=120:
            self.channel = newchannel
        else:
            print(f"The new set channel ({newchannel}) is out of range\nYou are back to Channel({self.channel})")
# Get Volume
    def getVolume(self):
        print (f"The Volume level is {self.volume_level}")
# Set Volume
    def setVolume(self,newvolume):
        if 0<=newvolume<=7:
            self.volume_level = newvolume
        else:
            print(f"The new set volume ({newvolume}) is out of range\nYou are back to Volume({self.volume_level})")
# Channel Up
    def channelUp(self):
        if self.channel == 120:
            print(f"You are currently at the end of the channel list which is ({self.channel})")
        else:
            self.channel = int(self.channel) + 1 
# Channel Down
    def channelDown(self):
        if self.channel == 1:
            print(f"You are currently at channel ({self.channel}) and there is no channel 0")
        else:
            self.channel = int(self.channel) - 1
# Volume Up
    def volumeUp(self):
        if self.volume_level == 7:
            print("You are currently at the highest volume level")
        else:
            self.volume_level = int(self.volume_level) + 1
# Volume Down
    def volumeDown(self):
        if self.volume_level == 0:
            print("You are currently at the lowest volume level")
        else:
            self.volume_level = int(self.volume_level) - 1
# Create two objects TV1 and TV2
# TV1 = channel 30 and volume level 3
# TV2 = channel 3 and volume level 2