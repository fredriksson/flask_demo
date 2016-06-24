import os, sys
from  arduino_module import app
import arduino_class
import serial
import json

try:
    #sys.path.append("../")
    from data_interpreter import data_interpreter
    from data_connection import data_connection
except IOError:
    print "can not find module"


@app.route('/')
@app.route('/index')
def index():
    return "hello"


@app.route('/serial')
def get_serial_info():
    SERIAL_CONF_FILE = "serial.json"
    try:

        open_file = open(SERIAL_CONF_FILE, 'r')
    except IOError:
        return "can not find file or directory"

    else:
        json_date = json.load(open_file)
        json_date = str(json_date)
        return json_date


@app.route('/serial_data')
def show_serial_data():
    ser = serial.Serial(port='/dev/ttyACM0', baudrate=9600)

    try:
        a = ser.readline()
    except IOError as e:
        return "port error"
        exit()
    else:
        return a


@app.route('/port_list')
def show_serial_port_list():
    get_serial_info = arduino_class.ard_get_data()
    return str(get_serial_info.port_scan())


@app.route('/data')
def show_json():
    json_merge = {}
    data_source = data_interpreter.data_interpreter()
    data_rs232 = json.loads(data_source.Serial_RAW_DATA(0, 9600)) # 0 means the first port in the port list
    data_gps = data_source.GPS_Interpreter()
    json_merge["sensor_info"] = data_rs232
    json_merge["location"]  = data_gps
    json_merge = json.dumps(json_merge)


    return json_merge
