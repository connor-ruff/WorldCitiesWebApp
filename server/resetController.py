import cherrypy
import re, json
import sys
sys.path.insert(1, '../ooapi/')
from cities_library import _city_database

class ResetController(object):
	def __init__(self, cdb=None):
		if cdb is None:
			self.cdb = _city_database()
		else:
			self.cdb = cdb

	def PUT_ALL(self):
	#when PUT request comes in to /reset/ endpoint, then the city database is reloaded'''
		output = {'result':'success'}
		try:
			self.cdb.reset_all_data()
		except Exception as ex:
			output['result'] = 'error'
			output['message'] = str(ex)

		return json.dumps(output)

	def PUT_CITY(self, idNum):
		#resets one city given its name
		output = {'result':'success'}
		try:
			tempData = _city_database()
			tempData.load_cities('worldcities.csv')
			tempCity = tempData.get_all_city_info(idNum)
			output['CityUpdated'] = tempCity
			self.cdb.set_city(int(idNum), tempCity)

		except Exception as ex:
			output['result'] = 'error'
			output['message'] = str(ex)

		return json.dumps(output)
