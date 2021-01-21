# Connor Ruff - cruff
# Estefania romero Valdez = eromero4

import sys
import json
from math import sin, cos, sqrt, atan2, radians

class _city_database:

	def __init__(self):
		self.city_details = dict()
		self.city_coords = dict()
		self.maxID = 0

		self.ID_List = list()

	def load_cities(self, csv_file=None):

		if csv_file is None:
			csv_file = '../ooapi/worldcities.csv'

		f = open(csv_file, "r")
		i=0
		for line in f:

			if i == 0:
				i = i + 1
				continue

			line = line.rstrip()
			tokens = line.split('"')

			cityID = int(tokens[-2])
			if (cityID > self.maxID):
				self.maxID = cityID

			cityName = tokens[3]
			coords = []
			coords.append(tokens[5])
			coords.append(tokens[7])
			country = tokens[9]

			# Add to ID list
			self.ID_List.append([cityID, cityName, country, coords])

			# Save Coordinates
			self.city_coords[cityID] = coords

			# Save City Details
			deets = {}
			deets['Name'] = cityName
			deets['Country'] = tokens[9]
			self.city_details[cityID] = deets
			i = i + 1
		f.close()


	def reset_all_data(self):
		try:
			self.city_details = dict()
			self.city_coords = dict()
			self.maxID = 0
			self.ID_List = list()
			self.load_cities()

		except Exception as e:
			return False

		return True


	def get_all_IDs(self):
		all_IDs = []
		for ID in self.city_details:
			all_IDs.append(ID)
		return all_IDs

	def get_cities_in_country(self, country):

		cities_in_country = []
		found = False
		for ID in self.city_details:
			if self.city_details[ID]['Country'] == country:
				cities_in_country.append(self.city_details[ID]['Name'])
				found = True
		if found is False:
			cities_in_country.append('No matches found')
		return cities_in_country



	def get_distance(self, cityID1, cityID2):
		earth_radius = 6371.0
		# getting coordinates
		try:
			coords1 = self.city_coords[int(cityID1)]
			lat_1 = radians(float(coords1[0]))
			lon_1 =  radians(float(coords1[1]))
			coords2 = self.city_coords[int(cityID2)]
			lat_2 = radians(float(coords2[0]))
			lon_2 =  radians(float(coords2[1]))


			#finding distance
			delta_lat = lat_2 - lat_1
			delta_lon = lon_2 - lon_1
			a = pow(sin(delta_lat / 2),2) + cos(lat_1) * cos(lat_2) * pow(sin(delta_lon / 2),2)
			c = 2 * atan2(sqrt(a), sqrt(1 - a))
			distance = earth_radius*c

		except Exception as ex:
			return (str(ex))
		return float(distance)

	def time_of_flight(self, cityID1, cityID2):
		try:
			distance = self.get_distance(cityID1, cityID2)
			hours = distance/880.0
			temp_string = str(hours).split('.')
			minutes = temp_string[1]
			minutes = int(float(minutes[:3])*0.06)
			time = list((int(hours), minutes))
		except Exception as ex:
			time = None
		return time

	def get_all_city_info(self, cityID):
		cityID = int(cityID)
		city_info = dict()

		try:
			city_info['Name'] = self.city_details[cityID]['Name']
			city_info['ID'] = cityID
			city_info['Country'] = self.city_details[cityID]['Country']
			coords = self.city_coords[cityID]
			city_info['Coordinates'] = coords

		except Exception as ex:
			return None

		return city_info

	# Called with name, country, coords, ID is set interally and returned
	def add_city(self, city_dict,idNum=0):
		if idNum == 0 or idNum>self.maxID:
			idNum = self.maxID + 1
			self.maxID = self.maxID + 1
		temp_dict = {}
		temp_dict['Name'] = city_dict['Name']
		temp_dict['Country'] = city_dict['Country']
		self.city_details[idNum] = temp_dict
		self.city_coords[idNum] = city_dict['Coordinates']
		self.ID_List.append([idNum, city_dict['Name'], city_dict['Country'], city_dict['Coordinates']])

		return idNum


	def remove_city(self, cityID):
		del(self.city_details[cityID])
		del(self.city_coords[cityID])
		i = 0
		for entry in self.ID_List:
			if int(entry[0])== int(cityID):
				self.ID_List.pop(i)
			i = i + 1

	def set_city(self, idNum, city):
		if idNum not in self.city_details.keys():
			self.add_city(city,idNum)
		self.city_details[idNum]['Name'] = city['Name']
		self.city_details[idNum]['Country'] = city['Country']
		self.city_coords[idNum] = city['Coordinates']


if __name__ == "__main__":

	db = _city_database()
	db.load_cities('worldcities.csv')
	db.reset_all_data()
	db.remove_city(1840002127)
	print(db.get_distance(1840002540, 1604728603))
	print(db.time_of_flight(1840002540, 1604728603))
	#print(db.city_details)
	#print(db.get_all_city_info(1604728603))
	#lima_dict = {'Name':'Lima', 'ID': 1604728603, 'Country':'LALA', 'Coordinates': [0,0]}
	#db.set_city(1604728603, lima_dict)
	#print(db.get_all_city_info(1604728603))
	#print(db.maxID)

