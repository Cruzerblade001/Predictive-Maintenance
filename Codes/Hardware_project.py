#!/usr/bin/env python3

import joblib
import numpy as np
import serial
import time

def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

if __name__ == '__main__':
    
    # ls/dev/tty*
    
    ser = serial.Serial('/dev/ttyACM1', 9600, timeout=1)
    ser.reset_input_buffer()
    random_forest_model = joblib.load(r'trained_model.pkl')

    # function to read process temperature from Arduino
    def read_process_temp():
        while True:
            data = ser.readline().decode('utf-8').rstrip()
            if is_float(data):
                return float(data)

    air_temp = float(input("Enter air temperature in Kelvin "))
    process_temp = read_process_temp() # to take input from Arduino
    print("Process Temperature in Kelvin:", process_temp) 
    #process_temp = float(input("Enter process temperature in Kelvin ")) #for custom input
    
    rot_speed = float(input("Enter rotational speed in rpm "))
    torque = float(input("Enter torque in Nm "))
    time_used = float(input("Enter tool use time in minutes "))

    test_features = np.array([air_temp, process_temp, rot_speed, torque, time_used]).reshape(1, -1)
    predicted_label = random_forest_model.predict(test_features)

    if predicted_label[0] == 1:
        ser.write(b"Maintenance !!\n")
        #print('Maintenance Required')
    elif predicted_label[0] == 0:
        ser.write(b"Continue :)\n")
        #print('Maintenance Not Required')

