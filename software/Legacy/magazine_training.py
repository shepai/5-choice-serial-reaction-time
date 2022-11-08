# Magazine Training
# created by AMChagas 20220309

# magazine training is described here: https://github.com/BeeHive-org/5-choice-serial-reaction-time/issues/8

import machine
import box
import utime

class MagazineTraining:
    def __init__(self):
        self.trials = 50
        self.itis = [4000,8000,16000,32000]
        self.box = box()
    
    def start_training(self):
        time1 = utime.ticks_ms()
        time2 = utime.ticks_ms()
        #iti
        while time2-time1< 100:#ITI select
            time2 = utime.tick_ms()
            
    

    def time_intervals(self, interval_ms=100):
        time1 = utime.ticks_ms()
        time2 = utime.ticks_ms()
        while time2 - time1 < interval_ms:
            time2 = utime.ticks_ms()


        

# Magazine training in steps:
# Total number of trials = 50 > will make a for loop
# Reward pellets were dropped at a random fixed inter-trial interval (ITI; 4, 8, 16 and 32 sec),
# which coincided with switching on the magazine stimulus light. 
# An ITI was only initiated when the previous pellet had been collected,
# as registered by a magazine response, after which the magazine stimulus light was switched off.
