'''LEOJ M. SUAVERDEZ OBJECT ORIENTED TV ASSIGNMENT'''
# Create class named TV
class TV:
# Self Attributes for TV class which is channel, volume level, power
    def __init__(self, channel=1, volume_level=1, power=False):
        if not 1 <= channel <= 120:
            raise ValueError("Channel must be between 1 and 120.")
        if not 0 <= volume_level <= 7:
            raise ValueError("Volume level must be between 0 and 7.")
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
        if self.power:
            print (f"Your Current Channel is {self.channel}")
        else:
            print("The TV is currently turned off.")
# Set Channel
    def setChannel(self,newchannel):
        if self.power:
            if 1<newchannel<=120:
                self.channel = newchannel
            else:
                print(f"The new set channel ({newchannel}) is out of range\nYou are back to Channel({self.channel})")
        else:
            print("The TV is currently turned off.")
# Get Volume
    def getVolume(self):
        if self.power:
            print (f"The Volume level is {self.volume_level}")
        else:
            print("The TV is currently turned off.")
# Set Volume
    def setVolume(self,newvolume):
        if self.power:
            if 0<=newvolume<=7:
                self.volume_level = newvolume
            else:
                print(f"The new set volume ({newvolume}) is out of range\nYou are back to Volume({self.volume_level})")
        else:
            print("The TV is currently turned off.")
# Channel Up
    def channelUp(self):
        if self.power:
            if self.channel == 120:
                print(f"You are currently at the end of the channel list which is ({self.channel})")
            else:
                self.channel = int(self.channel) + 1 
        else:
            print("The TV is currently turned off.")
# Channel Down
    def channelDown(self):
        if self.power:
            if self.channel == 1:
                print(f"You are currently at channel ({self.channel}) and there is no channel 0")
            else:
                self.channel = int(self.channel) - 1
        else:
            print("The TV is currently turned off.")
# Volume Up
    def volumeUp(self):
        if self.power:
            if self.volume_level == 7:
                print("You are currently at the highest volume level")
            else:
                self.volume_level = int(self.volume_level) + 1
        else:
            print("The TV is currently turned off.")
# Volume Down
    def volumeDown(self):
        if self.power:
            if self.volume_level == 0:
                print("You are currently at the lowest volume level")
            else:
                self.volume_level = int(self.volume_level) - 1
        else:
            print("The TV is currently turned off.")