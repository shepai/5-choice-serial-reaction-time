import Serial_communication


b=SB.Board()
print(b.serial_ports())

b.connect('/dev/ttyUSB0')
b.runFile("food_magazine.py")
b.record(till=True)