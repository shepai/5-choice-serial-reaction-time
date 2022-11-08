# Magazine Training
# 28/07/21

# Magazine training in steps:
# Total number of trials = 50 > will make a for loop
# Reward pellets were dropped at a random fixed inter-trial interval (ITI; 4, 8, 16 and 32 sec),
# which coincided with switching on the magazine stimulus light. 
# An ITI was only initiated when the previous pellet had been collected,
# as registered by a magazine response, after which the magazine stimulus light was switched off.


import machine
import utime
import urandom
import _thread

# OUTPUTS:
# stimulus lights

led_1 = machine.Pin(15, machine.Pin.OUT)
led_2 = machine.Pin(14, machine.Pin.OUT)
led_3 = machine.Pin(13, machine.Pin.OUT)
led_mag = machine.Pin(12, machine.Pin.OUT) # magazine light

# create header for file to record data

# Feeder is another output so should be added here
# feeder = machine.Pin(11, machine.Pin.OUT)

# IR emitters and sensors for each light
# IR emitters:

IR_led_1 = machine.Pin(16, machine.Pin.OUT)
IR_led_2 = machine.Pin(17, machine.Pin.OUT)
IR_led_3 = machine.Pin(18, machine.Pin.OUT)
IR_led_mag = machine.Pin(19, machine.Pin.OUT)

# INPUTS:
# IR sensors:

IR_sensor_led1 = machine.ADC(28)
IR_sensor_led2 = machine.ADC(27)
IR_sensor_led3 = machine.ADC(26)
# Pico has only 3 ADC pins
# IR_sensor_mag = machine.Pin(8, machine.Pin.IN)
# IR_sensor_feeder = machine.Pin(input no, machine.Pin.IN, machine.Pin.PULL_DOWN)

# Test if the components are working
#Test the LEDs

while True:
    led_1.value(1)
    utime.sleep(3)
    led_1.value(0)
    led_2.value(1)
    utime.sleep(3)
    led_2.value(0)
    led_3.value(1)
    utime.sleep(3)
    led_3.value(0)
    led_mag.value(1)
    utime.sleep(3)
    led_mag.value(0)
    
# Test if the IR LEDs are working

while True:
    IR_led_1.value(1)
    utime.sleep(3)
    IR_led_1.value(0)
    IR_led_2.value(1)
    utime.sleep(3)
    IR_led_2.value(0)
    IR_led_3.value(1)
    utime.sleep(3)
    IR_led_3.value(0)
    IR_led_mag.value(1)
    utime.sleep(3)
    IR_led_mag.value(0)

# Check if the phototransistors are working
# Change the names for each light sensor to check

conversion_factor = 3.3/(65535)

while True:
    IR_led_3.value(1)
    current = IR_sensor_led3.read_u16() * conversion_factor
    print(current)
    utime.sleep(2)

# Global Variables:
# Stage number
# ITI duration: create a list of variables which will be randomized (urandom)
# (ITI; 4, 8, 16 and 32 sec)
# ITI = urandom.choice(4, 8, 16, 32)*1000 #convert to ms
# urandom.seed(0): makes sure different boxes run with the same sequence of random numbers
# Number of trials = 50
# magazine latency (chapter 6: reaction game)


# Main program:
# Program checks the computer time to start
# a for loop to repeat 50 times
# 1. mag led = 1 on
# and feeder = 1 on > release 1 pellet
# then feeder = 0 off
# 2.wait until respond
# 3.Mag Response (RT- IRQ) - detected by mag IR
#    - mag led 0 off
#    - ITI picked urandom
# 4. back to step 1 in the loop

#when mag light is on and IR_mag_sensor is 0;
# count the no of seconds to get the magazine latency

For i in range(50):
    
    led_mag.value(1)
    feeder.value(1)
    utime.sleep(1)
    feeder.value(0)
    mag_timer_start = utime.ticks_ms()
    
    while IR_sensor_mag.value() == 0:
        mag_latency = utime.ticks_diff(utime.ticks_ms(), mag_timer_start)

    led_mag.value(0)
    ITI_time1 = utime.ticks_ms()
    ITI_time2 = utime.ticks_ms()
    magazine_count = 0
    ITI = urandom.choice(4, 8, 16, 32)*1000
    while ITI_time2-ITI_time1<ITI:
        ITI_time2 = utime.ticks_ms()
        if IR_sensor_mag.value() == 1:
            magazine_count = magazine_count+1
            utime.sleep(10)    
    
    i,mag_timer_start,"magazine",ITI,mag_latency,magazine_count
    "Number of trial, Starttime, Stage, ITI, Magazine Latency, Number of premature magazine responses, Number of np1 responses, Number of np2 responses, Number of np3 responses"



# ITI urandom
# mag led=0
# while mag IR = o
# wait
# switch on mag led = 1 + feeder= 1
# while mag IR = 0
# wait
# feeder = 1
# wait 100ms


# check if they do a nosepoke into other stimulus holes
# read np to led_1
# read np to led_2
# read np to led_3


# Array format for the data:
# array format magazine training (c = 1)  
# x(0) = start time of trial 
# x(1) = 
# x(2) = Stage (1 = magazine, 2 = training_1, 3 = training_2, 4 = SD_16, 5 = SD_8, 6 = SD_4, 7 = SD_2, 8 = SD_1.5, 9 = SD_1, 10 = vITI, 11 = SD_1, 12 = vSD, 13 = SD_1) 
# x(3) = ITI during this trial 
# x(4) = variable b; in this case number of trials (to be checked with criterion) 
# x(5) = Magazine latency (s) after a pellet drop; time between free drop and magazine response 
# x(6) = Number of anticipatory magazine responses 
# x(7) = Number of np1 responses 
# x(8) = Number of np2 responses 
# x(9) = Number of np3 responses 

# add this above
file = open("mid_mag_training.csv", "w")
file.write("Number of trial, Starttime, Stage, ITI, Magazine Latency, Number of premature magazine responses, Number of np1 responses, Number of np2 responses, Number of np3 responses")
file.close() #at the end
