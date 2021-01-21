import cherrypy
import sys
sys.path.insert(1, '../ooapi/')
from cities_library import _city_database
from citiesController import CitiesController
from resetController import ResetController
from distanceController import DistanceController
from deleteController import DeleteController

class optionsController:
	def OPTIONS(self, *args, **kwargs):
		return ""

def CORS():
	cherrypy.response.headers["Access-Control-Allow-Origin"] = "*"
	cherrypy.response.headers["Access-Control-Allow-Methods"] = "GET, PUT, POST, DELETE, OPTIONS"
	cherrypy.response.headers["Access-Control-Allow-Credentials"] = "true"

def start_service():

	dispatcher = cherrypy.dispatch.RoutesDispatcher()

	cdb = _city_database()

	citiesController = CitiesController(cdb=cdb)
	resetController = ResetController(cdb=cdb)
	distanceController = DistanceController(cdb=cdb)
	deleteController = DeleteController(cdb=cdb)

	dispatcher.connect('city_get_by_name', '/cities/:name', controller=citiesController, action='GET_CITIES_BY_NAME', conditions=dict(method=['GET']))
	dispatcher.connect('get_cities', '/cities/', controller=citiesController, action = 'GET_CITIES', conditions=dict(method=['GET']))
	dispatcher.connect('get_city', '/city/:idNum', controller=citiesController, action='GET_CITY_INFO', conditions=dict(method=['GET']))
	dispatcher.connect('cities_of_country_get', '/country/:country', controller=citiesController, action='GET_COUNTRY_CITIES', conditions=dict(method=['GET']))
	dispatcher.connect('reset_all_put', '/reset/', controller=resetController, action = 'PUT_ALL', conditions=dict(method=['PUT']))
	dispatcher.connect('reset_city_put', '/reset/:idNum', controller=resetController, action = 'PUT_CITY', conditions=dict(method=['PUT']))
	dispatcher.connect('distance_get', '/distance/', controller=distanceController, action = 'GET_DISTANCE', conditions=dict(method=['PUT']))
	dispatcher.connect('add_city', '/cities/', controller=citiesController, action='POST_CITY', conditions=dict(method=['POST']))
	dispatcher.connect('get_ids_all', '/ids/', controller=citiesController, action = 'GET_ALL_IDS', conditions=dict(method=['GET']))
	dispatcher.connect('get_flight_time', '/time/', controller=distanceController, action = 'GET_TIME_FLIGHT', conditions=dict(method=['PUT']))

	dispatcher.connect('city_delete', '/city/:idNum', controller=deleteController, action = 'DELETE_CITY', conditions=dict(method=['DELETE']))
	dispatcher.connect('all_delete', '/cities/', controller=deleteController, action = 'DELETE_ALL', conditions=dict(method=['DELETE']))


	# CORS Stuff
	dispatcher.connect('get_cities_options', '/cities/', controller=optionsController, action = 'OPTIONS', conditions=dict(method=['OPTIONS']))
	dispatcher.connect('get_reset_options', '/reset/', controller=optionsController, action = 'OPTIONS', conditions=dict(method=['OPTIONS']))
	dispatcher.connect('get_delete_options', '/city/:city', controller=optionsController, action = 'OPTIONS', conditions=dict(method=['OPTIONS']))
	dispatcher.connect('get_distance_options', '/distance/', controller=optionsController, action = 'OPTIONS', conditions=dict(method=['OPTIONS']))

	conf = {
	'global' : {
		'server.thread_pool' : 5,
		'server.socket_host' : 'student05.cse.nd.edu',
		'server.socket_port' : 51031
		},
	'/': {
		'request.dispatch' : dispatcher,
		'tools.CORS.on' : True,
		}
	}

	cherrypy.config.update(conf)
	app = cherrypy.tree.mount(None, config=conf)
	cherrypy.quickstart(app)

if __name__ == '__main__':
	cherrypy.tools.CORS = cherrypy.Tool('before_finalize', CORS)
	start_service()
