import os, sys
import serial, json

sys.path.append("../")
try:
    sys.path.append("../")
    from data_connection import data_connection
except IOError:
    print "can not find module"


class data_interpreter():
    def __init__(self):
        pass

    def GPS_Interpreter(self):
        gps_dict = {}

        # local_gps_file = open("../gps_module/gps_data",'r')
        local_gps_file = data_connection.connection_method("linux")
        local_gps_file = local_gps_file.LOCAL_DATA("gps_data", "gps")

        # local_gps_file = (local_gps_file.read()).split()

        for each_line in local_gps_file:
            if each_line[0:6] == "$GPGGA":
                each_line = each_line.split(",")
                gps_dict["message_id"] = each_line[0]
                gps_dict["UTC_time"] = each_line[1]
                gps_dict["latitude"] = each_line[2]
                gps_dict["NS_indicator"] = each_line[3]
                gps_dict["longitude"] = each_line[4]
                gps_dict["EW_indicator"] = each_line[5]
        # print self.gps_dict
        return gps_dict

    def Serial_RAW_DATA(self, port, baudrate):

        selected_port = data_connection.connection_method("linux")
        selected_port = selected_port.RS232()
        selected_port = str("/dev/" + selected_port[port])
        # print selected_port
        ser = serial.Serial(port=selected_port, baudrate=baudrate)

        try:
            get_serial_ouput = ser.readline()
        except IOError as e:
            return "serial port error"
        else:
            return get_serial_ouput

    def Modbus_Interpreter(self):
        pass

    def JSON_Interpreter(self):
        pass

    def Other(self):
        pass


if __name__ == '__main__':
    a = data_interpreter()
    print a.GPS_Interpreter()
    print a.Serial_RAW_DATA(0, 9600)
