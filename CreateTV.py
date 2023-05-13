# OOP CREATE TV OBJECTS

from tv import TV
import pyfiglet as fig
print("\033[36m","="*150,"\033[m")
title = "TV OBJECTS"
print("\033[32m",fig.figlet_format(title),"\033[m")
print(fig.figlet_format("Made by: Leoj M Suaverdez",font="bubble"))

tv1 = TV()
tv2 = TV()

while True:
    while True:
        response = input("Do you want to turn on tv1? Y/N ").upper()
        if response not in {"Y", "N"}:
            print("\033[1;31mInvalid Answer\033[0m")
        else:
            break

    if response == "Y":
        tv1.turn_on()
        print("\033[1;32mTV1 is now turned on\033[0m")
        desired_channel = int(input("Enter your desired channel for TV1: "))
        tv1.setChannel(desired_channel)
        
        while True:
            response = input("Do you want to change the volume of TV1? Y/N ").upper()
            if response not in {"Y", "N"}:
                print("\033[1;31mInvalid Answer\033[0m")
            else:
                break

        if response == "Y":
            desired_volume = int(input("Enter your desired volume level for TV1: "))
            tv1.setVolume(desired_volume)
        print("\033[32m", "=" * 100, "\033[m", f"\033[1;36mtv1's channel is {tv1.channel} and volume level is {tv1.volume_level}\033[0m", "\033[32m", "=" * 100, "\033[m", sep="\n")
        break
    else:
        tv1.turn_off()
        print("\033[1;36mTV1 is still off\033[0m")
        break
while True:
    while True:
        response = input("Do you want to turn on tv2? Y/N ").upper()
        if response not in {"Y", "N"}:
            print("\033[1;31mInvalid Answer\033[0m")
        else:
            break

    if response == "Y":
        tv2.turn_on()
        print("\033[1;32mTV2 is now turned on\033[0m")
        desired_channel = int(input("Enter your desired channel for TV2: "))
        tv2.setChannel(desired_channel)
        
        while True:
            response = input("Do you want to change the volume of TV2? Y/N ").upper()
            if response not in {"Y", "N"}:
                print("\033[1;31mInvalid Answer\033[0m")
            else:
                break

        if response == "Y":
            desired_volume = int(input("Enter your desired volume level for TV2: "))
            tv2.setVolume(desired_volume)
        print("\033[32m", "=" * 100, "\033[m", f"\033[1;36mtv2's channel is {tv2.channel} and volume level is {tv2.volume_level}\033[0m", "\033[32m", "=" * 100, "\033[m", sep="\n")
        break
    else:
        tv2.turn_off()
        print("\033[1;36mTV2 is still off\033[0m")
        break
print("\033[36m","="*150,"\033[m")