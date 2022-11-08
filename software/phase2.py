    
#Phase 2:

#PHASE 1 ESP37

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
        

led=machine.Pin(5, machine.Pin.OUT) #LED WORKS
button_food=machine.Pin(15,machine.Pin.IN)


timer_starts =utime.ticks_ms()
#now=button_food.value(1)


NP_1=machine.Pin(26,machine.Pin.OUT)
NP_2=machine.Pin(25,machine.Pin.OUT)
NP_3=machine.Pin(22,machine.Pin.OUT)
NP_4=machine.Pin(23,machine.Pin.OUT)
NP_5=machine.Pin(18,machine.Pin.OUT)

button_1 = machine.Pin(2,machine.Pin.IN)
button_2 = machine.Pin(16,machine.Pin.IN) #pin 4
button_3 = machine.Pin(17,machine.Pin.IN)
button_4 = machine.Pin(4,machine.Pin.IN)



NP_1.value(0)
NP_2.value(0)
NP_3.value(0)
NP_4.value(0)
NP_5.value(0)


button_pressed = False


for i in range(100):
    print('Trial:',str(i+1)+('/100'))
    T2_timer= utime.ticks_ms()
    
    #if button_food.value()==0: #when the dispense-food button is not pressed
    led.value(1) #food indicator LED is turned on as food is dispensed
    #for now, the 2 NP buttons' leds are turned off
    NP_1.value(0) 
    NP_2.value(0)
    
    while button_food.value() == 1: 
        next
    
    #while button_food.value()==0: #when the dispense-food button is pressed, which means the IR-Beam has been broken
    print("mouse break IR Beam")# ADD TIME
    led.value(0) 
    utime.sleep(5)     

    nose_pokes = [NP_1,NP_2,NP_3,NP_4]
    
    np_buttons = [button_1,button_2,button_3,button_4]
    
    #random choice between 0 to length of nose_pokes
    choice = random.randint(0,3)
    
    print('NP number chosen',choice)
    
    nose_pokes[choice].value(1) #NP turns on but button hasn't yet been activated
    np_buttons[choice].value(0)
    led.value(0) # Foood is off
    
    while np_buttons[choice].value() == 1: #while there is no np button detected, nothing happens
        
        next
    #button has been pressed
    #print("this phase")
    nose_pokes[choice].value(0) #NP LED is turned off
    led.value(1) #Food LED is turned on
    
    #initial food button now needs to be pressed, representing the IR-beam being broken
    while button_food.value() == 1: #waits for IR beam to broken which means food is eaten
        #print("CC")
        next
        
        
    led.value(0) #Food LED is turned off as food has been eaten (IR-beam broken)
    time_food =utime.ticks_ms()
    mouse_to_food = time_food - T2_timer#time still feels wrong 
    print("mouse ate pallet at " + str(mouse_to_food) + "ms")
     
    print('eating for 20 seconds')        
    utime.sleep(20)
    
    
    
#Again, need to look at time for mouse to food and need to add time for the whole task
        