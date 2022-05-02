import time
import uuid

import paho.mqtt.client as mqtt
import serial


def receive_data_from_sensor():
    ser = serial.Serial(port='/dev/cu.usbmodem101', baudrate=9600)
    b = ser.readline()
    string_n = b.decode()
    res = int(string_n.rstrip())
    print(res)
    return res - 130


def publish():
    client = mqtt.Client(str(uuid.uuid1()))
    client.tls_set()
    client.username_pw_set('idd', 'device@theFarm')
    client.connect('farlab.infosci.cornell.edu', port=8883)

    while True:
        cmd = input('>> topic: IDD/')
        if ' ' in cmd:
            print('sorry white space is a no go for topics')
        else:
            topic = f"IDD/{cmd}"
            print(f"now writing to topic {topic}")
            print("type new-topic to swich topics")
            while True:
                val = receive_data_from_sensor()
                if val == 'new-topic':
                    break
                else:
                    client.publish(topic, val)


if __name__ == '__main__':
    publish()
