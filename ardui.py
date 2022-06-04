import serial
import time
from sq import insert_data

def test():
    serialArduino=serial.Serial('COM3',9600)
    time.sleep(5)
    while True:
        cad=serialArduino.readline().decode('ascii')
        insert_data("temp_ex", float(cad))
        print(cad)

def save():
    file=open('test.txt', 'w')
    serialArduino=serial.Serial('COM3',9600)
    time.sleep(1)

    cad=serialArduino.readline().decode('ascii')
    print(cad)
    file.write(cad)
    
if __name__ == '__main__':
    test()
