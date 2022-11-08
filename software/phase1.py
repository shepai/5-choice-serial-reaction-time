#T1 PHASE ESP32 is used currently as a circuit board for the SENSOR of the box:
                #It replaces the bottons 

#THIS WORKS WITH REAL SENSORS AND LEDs.
import machine
import utime
import random
#T1 PHASE:
    #1. Use 3 lights and 3 buttons to mark the NP
    #2 When 1/3 button is pressed --> All lights turn off and food dispenser is on
    #Mouse collects food
    #Again but with the time interval
        
def run():
    led=machine.Pin(5, machine.Pin.OUT) #LED WORKS
    button_food=machine.Pin(15,machine.Pin.IN)


    timer_starts =utime.ticks_ms()
    now=button_food.value(1)

    button_1 = machine.Pin(15,machine.Pin.IN)
    button_2 = machine.Pin(2,machine.Pin.IN)
    NP_1=machine.Pin(26,machine.Pin.OUT)
    NP_2=machine.Pin(25,machine.Pin.OUT)
    NP_3=machine.Pin(22,machine.Pin.OUT)
    NP_4=machine.Pin(23,machine.Pin.OUT)
    NP_5=machine.Pin(18,machine.Pin.OUT)

    NP_1.value(0)
    NP_2.value(0)
    NP_3.value(0)
    NP_4.value(0)
    NP_5.value(0)

    #PHASE 1:

    count_of_clicks = 0
    timer_starts = utime.ticks_ms()

    #times=[4,8,16,32]
    #times_num = random.choice(times)
    #print(times_num)
     #utime.sleep(times_num)


    #for x in range (1, 50):
    for x in range (1,51):
        print ("This is trial", x)
        #button_pressed = False
       # print("nnf")
       # print(button_1.value())
        while button_pressed== False:
        
            if button_1.value() == 0 or button_2.value() == 0  or button_3.value() == 0  or button_4.value() == 0: #if any of the NPs are poked
                 #Lights are tunred off 
            
                NP_1.value(0) #THE Lights remain on
                NP_2.value(0)
                NP_3.value(0)
                NP_4.value(0)
               # NP_5.value(0)
                led.value(1) #LED is on leading to food falling
                button_food.value(0)
                print("Food out")
                while button_food.value() == 1:
                    led.value(1)
                    
              #  if button_food.value() == 0:
                timer_food = utime.ticks_ms()
                mouse_to_food = timer_food -timer_starts #it accumulates instead f timing it one by one
                print("mouse ate pallet at " + str(mouse_to_food) + "ms")
                led.value(0)
            
            
                #times=[4,8,16,32]
                times=[1]
                times_num = random.choice(times)
                print("The ITI will run for", times_num, "s") 
                utime.sleep(times_num)
                
                button_pressed = True
            #ITI timer starts again
                       
        
            elif button_1.value() == 1 or button_2.value() == 1 or button_3.value() == 1 or button_4.value() == 1:#0 meaning the NPs haven't been touched     
                    NP_1.value(1) #THE Lights remain on
                    NP_2.value(1)
                    NP_3.value(1)
                    NP_4.value(1)
                    NP_5.value(1)
                    led.value(0)
           
           #Need to figure out how to take it out of the while loop once hte 50th trial is done to go onto phase 2
                    
                    
run