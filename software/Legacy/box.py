import machine

class Box:
    def __init__(self):
        #machine definitions
        self.np1SensorPin = 1
        self.np2SensorPin = 2
        self.np3SensorPin = 3
        self.np4SensorPin = 4
        self.np5SensorPin = 5
        self.houseLightPin = 6
        self.np1LEDPin = 7
        self.np2LEDPin = 8
        self.np3LEDPin = 9
        self.np4LEDPin = 10
        self.np5LEDPin = 11
        self.foodDispenserTriggerPin = 12
        self.foodDispenserSensorPin = 14

        #all sensors
        self.np1Sensor = machine.Pin(self.np1SensorPin, machine.Pin.IN)
        self.np2Sensor = machine.Pin(self.np1SensorPin, machine.Pin.IN)
        self.np3Sensor = machine.Pin(self.np1SensorPin, machine.Pin.IN)
        self.np4Sensor = machine.Pin(self.np1SensorPin, machine.Pin.IN)
        self.np5Sensor = machine.Pin(self.np1SensorPin, machine.Pin.IN)
        self.foodDispenserSensor = machine.Pin(self.foodDispenserSensorPin, machine.Pin.IN)

        #all outputs
        self.np1LED = machine.Pin(self.np1LEDPin, machine.Pin.OUT)
        self.np2LED = machine.Pin(self.np2LEDPin, machine.Pin.OUT)
        self.np3LED = machine.Pin(self.np3LEDPin, machine.Pin.OUT)
        self.np4LED = machine.Pin(self.np4LEDPin, machine.Pin.OUT)
        self.np5LED = machine.Pin(self.np5LEDPin, machine.Pin.OUT)
        self.houseLight = machine.Pin(self.houseLightPin, machine.Pin.OUT)
        self.foodDispenserTrigger = (self.foodDispenserSensorPin,machine.Pin.OUT)