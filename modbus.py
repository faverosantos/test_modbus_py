# A code by Favero Santos
# 2018/03/28

import minimalmodbus
import serial

MAJOR = 00
MINOR = 00

if __name__ == '__main__':
    print("Aloha from ModBus Reader!!")
    print("SW Version is V", str(MAJOR), "R", str(MINOR))

    instrument = minimalmodbus.Instrument('/dev/ttyUSB0', 247)
    instrument.serial.baudrate = 1200
    instrument.serial.bytesize = 8
    instrument.serial.parity = serial.PARITY_EVEN
    instrument.serial.stopbits = 1
    instrument.serial.timeout = 1

    local_counter = 0
    while(local_counter < 10):
        local_counter = local_counter + 1
        temperature = instrument.read_register(14, 1)  # Registernumber, number of decimals
        print(temperature)

    print("C-ya from ModBus Reader!!")

