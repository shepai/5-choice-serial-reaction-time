
 #CHANGE SO THAT TIMER STARTS WHEN LIGHT IS ON ONLY IF LED.VALUE(1)


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

#
timer_food =utime.ticks_ms()
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


#5csrtt PHASE1:

#TRIAL 1:
#same start as the other one
#5 second ITI
#NP turns on for a period of time (2)
#only if mouse reacts to the NP correctly within the illumination or 4 seconds after it does it get smth

#LED is on

#Food collected --> 20 seconds interval

#TRIAL 2:
#Time outs:
# same thing but incorrect responce or np during ITI or omission  = 5 second time out
#after time out led and food dispenser on

start_time=utime.ticks_ms

count_of_clicks = 0
SD = 9000

nose_pokes = [NP_1,NP_2, NP_3, NP_4]
np_buttons = [button_1,button_2,button_3,button_4]


choice = random.randint(0,1)# need to sort this out

#list of wrong buttons that can be pressed during the game
np_buttons_wrong = [] 
for i in range(len(np_buttons)):
    if i != choice:
        np_buttons_wrong.append(np_buttons[i])
        
        
#print(np_buttons_wrong[2].value())

#random choice between 0 to length of nose_pokes


for i in range(100):
    print('Trial:',str(i+1)+('/100'))
    
    start_timer = utime.ticks_ms()

    led.value(1) 
    NP_1.value(0) 
    NP_2.value(0)
    
    
    while button_food.value() == 1: #this loop waits for the button to be pressed
        timer_food = utime.ticks_ms()
        next
        
    led.value(0)
    time_food = (timer_food - start_timer) #This might be wrong need to check when everything works
    print("Mouse ate food at ", time_food, "ms")
   
    break_time = True
    button_pressed = False #when true, loop stops and button is pressed. If false no button pressed
    correct_button_pressed = False # if true correct button pressed if false wrong button press
    
    print('NP number chosen',choice)
    #premature responce:
    
    
    
    print("ITI - 5 SECONDS")
    while break_time == True:
        
        premature_responce_timer = utime.ticks_ms()
        premature_timer= premature_responce_timer - start_timer
        
        if premature_timer < 5000:
      #      print(premature_timer) #work when the time is printed
       #     utime.sleep(0.2)
            
            if np_buttons_wrong[0].value() == 1 or np_buttons_wrong[1].value() == 1 or np_buttons_wrong[2].value() == 1 or np_buttons[choice].value() == 1:
                
                led.value(0)
                print("premature responce at ", premature_timer, "ms")
                nose_pokes[choice].value(0)
                #utime.sleep(5)
                button_pressed = True
                break
               
        # 
        elif premature_timer > 5000:
           
           #print('elif is played')
            if np_buttons_wrong[0].value() == 0 or np_buttons_wrong[1].value() == 0 or np_buttons_wrong[2].value() == 0 or np_buttons[choice].value() == 0:
                button_pressed = False
                break_time = False
                
                
                
                
                
        

    print("Task starts")
    while button_pressed == False:
        
        nose_pokes[choice].value(1)
        task_time= utime.ticks_ms()
        task_duration = task_time - start_timer
        
        if task_duration < SD + 4000:   #this makes it so that the buttons are still active for 4 seconds after the led value is turned off
           
           #this is for LED off but keep everything active for 4 more seconds
            if task_duration > SD:
                  nose_pokes[choice].value(0)
                


            if np_buttons[choice].value() == 1:		#wHEN correct button is pressed then the button pressed is true and corect button is true 
                #print(task_duration, "3")

                print('Mouse chose the right button at', timess, "ms")
                button_pressed = True 
                correct_button_pressed = True
                led.value(1) #food agazine eld turns on
                NP_1.value(0)
                NP_2.value(0)
                button_food.value() == 1 #task stops until the mouse goes towards the food

                #food sensor turns on and wait for mouse to get pellet
                while button_food.value() == 1:
                    next 
            
                led.value(0) 
                time_food =utime.ticks_ms()
                mouse_to_food = time_food - task_time 
                print("mouse ate pallet at " + str(mouse_to_food) + "ms")
         
                print('eating for 20 seconds')        
                utime.sleep(20) #should be 20
                
                
            elif np_buttons_wrong[0].value() == 1 or np_buttons_wrong[1].value() == 1 or np_buttons_wrong[2].value() == 1: #if the wrong button is pressed then time out utime sleep 5
                print('Mouse chose the wrong button at', task_duration, "ms")
                led.value(0)
                nose_pokes[choice].value(0)
                print("5 second time out")

                utime.sleep(5)
                    
                button_pressed = True
                chosen_button_pressed = False
                
            
        if task_duration > SD + 4000: #trying to sort out time but doesn't work over a condition?
            print("omission")
           
            led.value(0)
            nose_pokes[choice].value(0)
            print("5 second time out")
            utime.sleep(5)
            
            button_pressed = True
            chosen_button_pressed = False
            
            
