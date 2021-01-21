# ParadigmsProject
- eromero4
- cruff

# IMPORTANT - USAGE
	To run the application, first start the server:

	cd server
	python server.py

	Currently, the server is hard coded to run on student05.cse.nd.edu:51031
	If needed, this can be changed in server.py

	Then open up ui/index.html in a web browser, and you're on your way!
	NOTE: the JS front end is currently hard coded to connect to student05.cse.nd.edu:51031.
	If needed, this can be changed in index.js, where a global variable is hard coded at the top of the file!

	Finally, the data can not be accessed from the gitlab public repo page, because https does not allow unsecure XML requests. So the manually starting the ui/index.html page in the browswer is neccessary to see the functionality

# Tests For Web Client
	To test the web client, we did the above steps to start the application. Then, we tested the functionality of the site by adding cities, removing cities and checking that they were gone, and by calculating the distances between the cities, and checking that they were accurate. We also entered faulty data to the input units to ensure that the application did not crash upon doing so

# OO API
 The OO API is used to return useful data structures that the controllers will use. Our server uses multiple structures to store different types of data. For instance, one dictionary contains coordinates of certain cities, and another dictionary contains info about each city. Both of these structures use the unique city ID to identify a city. Because the data is organized this way, our API library accesses both of these structures, and returns something useful.  This API should be used by creating an object of the API class. Then, you can call the methods of that object to load the data structures, and to do different types of accessing, such as returning all of the city IDs, adding a city to the database, etc.

	There is a test file, test_api.py that tests the functionality of the OO API library. To use this test, you simply need to go to the directory of the OO API and run the file. For instance:
	
	cd ooapi
	python3 ./test_api.py
	
# Server
The server runs on port 51037. To run this server, go to the server directory and run the python file:

	cd server
	python3 ./server.py

Until the UI and JS front end is finished, the server should be accessed using the requests library's functions, such as request.get, request.put, etc. With the specified end point. For instance,

	http://student05.cse.nd.edu:51037/cities/

Multiple test files have been provided to do make such requests and verify that they worked. You can run these tests via:
	
	cd server
	python3 ./server.py

	(in another terminal)
	cd server
	python3 ./test_ws.py (will run tests in tests directory)
# JSON Specification

Request Type - Resource Endpoint - Body - Expected Response - Inner Handler
GET - /cities/ - no body - string formatted json of all data - GET_CITIES
GET - /cities/:name - no body - string formatted json of city entries that match the specified name - GET_ALL_CITIES_BY_NAME
GET - /city/:id - no body - string formatted json of all info on the city of the specified ID
GET - /country/:country - no body - string formatted json of all cities in a certain country - GET_COUNTRY_CITIES
PUT - /reset/ - no body - {'result':'success'} if successful - PUT_ALL
PUT - /reset/:id - no body - {'result':'success'} if operation worked - PUT_CITY
PUT - /distance/ - {'city1':<ID>, 'city2' <ID>} - string formatted json of the two cities and the distance between them - GET_DIST
POST - /cities/ - {'name':<name>, 'country':<country>, 'latitude':<lat>, 'longitude':<long>} - {result : success, ID: id} - POST_CITY
DELETE - cities/:city - no body - {'result':'success'} if successful - DELETE_CITY
DELETE - /cities/ - no body - {'result':'success'} if successful - DELETE_ALL
GET - /ids/ - no body - string formatted json of all cities and their IDs - GET_ALL_IDS


# Complexity - Milestone 3

	The project is very large scale, as it encompassess all significant cities in the world. Because of this, loading the initial data does take some time, and this adds to the overall complexity of the project. Furthermore, the project is further scalable, as it allows for the entry of new cities to be entered into it, and still perform the same operations with those cities.
	As for complexity, this mainly arose from the sheer amount of cities. Complexity arose because many cities across the globe actually have the same name, requiring the querying to return an indefinite number of results (for instance, if the user searches for "Paris," 5 entries will actually show up! The use of city ID was critical to addressing this complexity, as we could show the user all the IDs that pertained to a certian city name, and they could then use that ID for the main distance calculation.
