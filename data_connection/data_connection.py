import os,sys
import serial
import json
import subprocess
sys.path.append("../")


class connection_method:
    def __init__(self, os_type):
        self.platform = os_type
        if self.platform == 'linux':
            self.SERIAL_SCAN = "dmesg | grep 'tty' | awk '{ print $4 }' | grep '^tty'"
        elif self.platform == 'windows':
            pass

    def LOCAL_DATA(self, file_path, file_type):

        try:
            local_file = open(file_path, 'r')
        except IOError:
            print "Error:can not find local file"

        if file_type == 'gps':
            local_file1 = (local_file.read()).split()
        elif file_type == 'other':
            pass
        else:
            pass
        return local_file1

    def RS232(self):
        port_list = list(subprocess.check_output([self.SERIAL_SCAN], shell=True).split())
        port_list = set(port_list)
        new_list = []
        for each_port in port_list:
            list_one = list(each_port)
            list_one = [x for x in list_one if x != ":"]
            list_one = ''.join(list_one)
            new_list.append(list_one)
        port_list = new_list
        return port_list

    def RS485(self):
        pass

    def Ethernet(self, ip_address):
        pass

    def WIFI(self, ip_address, SSID):
        pass

    def GPRS(self):
        pass


if __name__ == '__main__':
    aa = connection_method("linux")
    print aa.LOCAL_DATA("../gps_module/gps_data", "gps")

    print aa.RS232()
