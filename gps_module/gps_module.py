import os
import serial
class GPS_Interpreter:
	def __init__(self):
		pass
	def open_local_data(self):
		self.gps_dict={}
		self.local_gps_file = open("gps_data",'r')
		self.local_gps_file = (self.local_gps_file.read()).split()

		for each_line in self.local_gps_file:
			if each_line[0:6] == "$GPGGA":
				each_line = each_line.split(",")
				self.gps_dict["message_id"]		=	each_line[0]
				self.gps_dict["UTC_time"]		=	each_line[1]
				self.gps_dict["latitude"]		=	each_line[2]
				self.gps_dict["NS_indicator"]	=	each_line[3]
				self.gps_dict["longitude"]		=	each_line[4]
				self.gps_dict["EW_indicator"]	=	each_line[5]
		#print self.gps_dict
		return self.gps_dict
	def open_serial_data(self):
		pass

	def open_third_parties_data(self):
		pass
			



if __name__ == '__main__':
	a = GPS_Interpreter()
	print a.open_local_data()