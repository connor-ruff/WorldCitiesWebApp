import cherrypy
import re, json
import sys
sys.path.insert(1, '../ooapi/')
from cities_library import _city_database

class DeleteController(object):
    def __init__(self, cdb=None):
        if cdb is None:
            self.cdb = _city_database()
        else:
            self.cdb = cdb

    def DELETE_ALL(self):
        output = {'result':'success'}
        self.cdb.city_details.clear()
        if self.cdb.city_details:
            output['result'] = 'error'
            output['message'] = 'unable to clear city details dict'
        self.cdb.city_coords.clear()
        if self.cdb.city_coords:
            output['result'] = 'error'
            output['message'] = 'unable to clear coordinates dict'
        self.cdb.ID_List.clear()
        if self.cdb.ID_List:
            output['result'] = 'error'
            output['message'] = 'unable to clear ID list'

        self.maxID = 0
        return json.dumps(output)

    def DELETE_CITY(self, idNum):
        output = {'result':'success'}
        idNum = int(idNum)
        try:
            city = self.cdb.remove_city(idNum)
            if self.cdb.get_all_city_info(idNum) is not None:
                output['result'] = 'error'
                output['message'] = 'lib error'
        except Exception as ex:
            output['result'] = 'error'
            output['message'] = str(ex)
        return json.dumps(output)
