import cherrypy
import re, json
import sys
sys.path.insert(1, '../ooapi/')
from cities_library import _city_database

class DistanceController(object):
    def __init__(self, cdb=None):
        if cdb is None:
            self.cdb = _city_database()
        else:
            self.cdb = cdb

    def GET_DISTANCE(self):
        output = {'result' : 'success'}
        data = json.loads(cherrypy.request.body.read().decode('utf-8'))
        print(data)

        try:
            distance = self.cdb.get_distance(data['c1'], data['c2'])
            output['city1'] = data['c1']
            output['city2'] = data['c2']
            output['distance'] = distance
        except Exception as e:
            output['result'] = 'error'
            output['message'] = str(e)

        return json.dumps(output)

    def GET_TIME_FLIGHT(self):
        output = {'result': 'success'}
        data = json.loads(cherrypy.request.body.read().decode('utf-8'))
        output['time'] = list()
        try:
            time = self.cdb.time_of_flight(data['c1'],data['c2'])
            output['city1'] = data['c1']
            output['city2'] = data['c2']
            output['time'] = time
        except Exception as e:
            output['result'] = 'error'
            output['message'] = str(e)

        return json.dumps(output)
