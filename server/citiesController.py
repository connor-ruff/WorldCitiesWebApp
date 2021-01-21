import cherrypy
import re, json
import sys
sys.path.insert(1, '../ooapi/')
from cities_library import _city_database

class CitiesController(object):

	def __init__(self, cdb=None):
		if cdb is None:
			self.cdb = _city_database()
		else:
			self.cdb = cdb

		self.cdb.load_cities('worldcities.csv')


	# Returns Structure With All Cities of Specified Name (Plus their ID's and Country)
	def GET_CITIES_BY_NAME(self, name):
		output = {'result' : 'success'}
		try:
			output['Cities'] = dict()
			for entry in self.cdb.ID_List:
				if name.lower() == entry[1].lower():
					coords = self.cdb.city_coords[entry[0]]
					output['Cities'][int(entry[0])] = [ entry[1], entry[2], coords[0], coords[1] ]
		except Exception as e:
			output['result'] = 'failure'
			output['message'] = str(e)

		return json.dumps(output)


	# output['Cities'] is a list of all entries ( [ [id, city, country, lat, long] , [id, city, country, lat, long].... )
	def GET_CITIES(self):
		output = {'result' : 'success'}
		try:
			output['Cities'] = list()
			for ID in self.cdb.get_all_IDs():
				tempList = []
				tempList.append(ID)
				tempList.append(self.cdb.city_details[ID]['Name'])
				tempList.append(self.cdb.city_details[ID]['Country'])
				tempList.append(self.cdb.city_coords[ID][0])
				tempList.append(self.cdb.city_coords[ID][1])
				output['Cities'].append(tempList)

		except Exception as e:
			output['result'] = 'error'
			output['message'] = str(e)

		return json.dumps(output)

	# Get All Info For a city (specified by ID)
	def GET_CITY_INFO(self, idNum):
		output = {'result' : 'success'}
		try:
			result = self.cdb.get_all_city_info(idNum)
			if result is None:
				output['result'] = 'failure'
				output['message'] = 'internal library failure'
			else:
				output['Data'] = result

		except Exception as e:
			output['result'] = 'error'
			output['message'] = str(e)

		return json.dumps(output)


	# Return object that has complete information on each city in a country
	def GET_COUNTRY_CITIES(self, country):

		output = {'result' : 'success'}
		output['Cities'] = list()

		try:
			for entry in self.cdb.ID_List:
				if str(entry[2]).lower() == str(country).lower():
					output['Cities'].append([entry[0], entry[1], entry[2], entry[3]])

		except Exception as ex:
			output['result'] = 'error'
			output['message'] = str(ex)

		return json.dumps(output)

	def POST_CITY(self):
		output = {'result' : 'success'}

		data = json.loads(cherrypy.request.body.read().decode('utf-8'))
		print(data.items())
		new_city = {}
		try:
			new_city['Name'] = data['name']
			new_city['Country'] = data['country']
			new_city['Coordinates'] = [data['latitude'], data['longitude']]
			id = str(self.cdb.add_city(new_city))
			output['id'] = id
		except Exception as e:
			output['result'] = 'error'
			output['message'] = str(e)

		return json.dumps(output)

	def GET_ALL_IDS(self):
		output = {'result' : 'success'}
		output['Cities'] = dict()
		try:
			for ID in self.cdb.get_all_IDs():
				output['Cities'][ID] = [self.cdb.city_details[ID]['Name'], self.cdb.city_details[ID]['Country']]

		except Exception as e:
			output['result'] = 'error'
			output['message'] = str(e)

		return json.dumps(output)
