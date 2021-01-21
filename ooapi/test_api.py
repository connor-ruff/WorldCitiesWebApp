import unittest
from cities_library import _city_database

class TestAPI(unittest.TestCase):

	def test_load_cities(self):
		cdb = _city_database()
		cdb.load_cities('worldcities.csv')
		self.assertTrue(cdb.city_details)
		self.assertTrue(cdb.city_coords)
		self.assertTrue(cdb.ID_List)
		self.assertTrue(cdb.maxID > 0)
		self.assertEqual(cdb.city_details[1840002127]['Name'], 'Belle Fourche')

	def test_reset_all_data(self):
		cdb = _city_database()
		cdb.load_cities('worldcities.csv')
		newCity = {}
		newCity['Name'] = 'Gotham'
		newCity['Country'] = 'Jupiter'
		newCity['Coordinates'] = [4.20, 69.0]
		newID = cdb.add_city(newCity)
		resp = cdb.reset_all_data()
		self.assertTrue(resp)
		resp = cdb.get_all_city_info(newID)
		self.assertFalse(resp)


	def get_all_IDs(self):
		cdb = _city_database()
		cdb.load_cities('worldcities.csv')
		ret = []
		ret = cdb.get_all_IDs()
		self.assertTrue(ret)
		self.assertEqual(ret[-2], 1840002540)

	def test_get_cities_in_country(self):
		cdb = _city_database()
		cdb.load_cities('worldcities.csv')
		listy = cdb.get_cities_in_country('China')
		self.assertTrue(listy)
		self.assertEqual('Yulin', listy[2])

	def test_get_distance(self):
		cdb = _city_database()
		cdb.load_cities('worldcities.csv')
		dist = cdb.get_distance(1840002540, 1840021263)
		self.assertEqual(dist, 2059)


	def test_time_of_flight(self):
		cdb = _city_database()
		cdb.load_cities('worldcities.csv')
		time = cdb.time_of_flight(1840002540, 1840021263)
		self.assertTrue(time)
		self.assertEqual(time[0], 2)
		self.assertEqual(time[1], 20)

	def test_get_all_city_info(self):
		cdb = _city_database()
		cdb.load_cities('worldcities.csv')
		ret = cdb.get_all_city_info(1840001590)
		self.assertEqual(ret['Name'], 'Lansing')
		self.assertEqual(ret['Country'], 'United States')
		self.assertEqual(ret['Coordinates'][1], '-94.8952')

	def test_set_city(self):
		cdb = _city_database()
		cdb.load_cities('worldcities.csv')
		new_city = {'Name': 'FakeCity', 'Country': 'FakeCountry', 'Coordinates' : [0,0]}
		test_id = 1840001590
		cdb.set_city(test_id, new_city)
		new_city = cdb.get_all_city_info(test_id)
		self.assertEqual(new_city['Name'], 'FakeCity')
		self.assertEqual(new_city['Country'], 'FakeCountry')
		self.assertEqual(new_city['Coordinates'][1], 0)

	def test_add_city(self):
		cdb = _city_database()
		cdb.load_cities('worldcities.csv')
		maxIDBefore = cdb.maxID
		newCity = {}
		newCity['Name'] = 'Gotham'
		newCity['Country'] = 'Jupiter'
		newCity['Coordinates'] = [4.20, 69.0]
		newID = cdb.add_city(newCity)
		resp = cdb.get_all_city_info(newID)
		self.assertEqual(resp['Name'], 'Gotham')
		self.assertEqual(resp['Country'], 'Jupiter')
		self.assertEqual(resp['Coordinates'][0], 4.20)
		self.assertEqual(cdb.city_coords[newID][1], 69.0)



if __name__ == "__main__":
	unittest.main()
