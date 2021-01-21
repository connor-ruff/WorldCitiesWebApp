const mainURL = "http://student05.cse.nd.edu:51031/";

function loadAllCities(){
    var tbody = document.getElementById("fullTableBody");
    tbody.innerHTML = ''

    var xhr = new XMLHttpRequest();
    var targetURL = mainURL + 'cities/';

    xhr.open("GET", targetURL);

    xhr.onload = function(e) {
        var resp = JSON.parse(xhr.responseText);
        addEntries(resp['Cities']);
    }

    xhr.onerror = function (e) {
        console.log("error");
    }

    xhr.send(null);
}

function testFunc(){
    console.log("in test!");
}

function addEntries(resp){

	// resp should be a list where each entry is [ID, city, country, lat, long]
    var tableBody = document.getElementById("fullTableBody");

    for (entry in resp){

        var newRow = document.createElement("tr");

        var ID = resp[entry][0];
        var country = resp[entry][2];
        var city = resp[entry][1];
        var lat = resp[entry][3];
        var longy = resp[entry][4];

        var td = document.createElement("td");
        var node = document.createTextNode(city);
        td.appendChild(node);
        newRow.appendChild(td);

        td = document.createElement("td");
        node = document.createTextNode(country);
        td.appendChild(node);
        newRow.appendChild(td);

        td = document.createElement("td");
        node = document.createTextNode(lat);
        td.appendChild(node);
        newRow.appendChild(td);

        td = document.createElement("td");
        node = document.createTextNode(longy);
        td.appendChild(node);
        newRow.appendChild(td);

        td = document.createElement("td");
        node = document.createTextNode(ID);
        td.appendChild(node);
        newRow.appendChild(td);

        tableBody.appendChild(newRow);
    }


}

function searchByName(){

    var tableBody = document.getElementById("fullTableBody");
    tableBody.innerHTML = "";

    var xhr = new XMLHttpRequest();

    var cityToSearch = document.getElementById("citySearchEntry").value;
    console.log('Searching: '+ cityToSearch);
    var targetURL = mainURL + "cities/" + cityToSearch;
    xhr.open("GET", targetURL);

    xhr.onload = function(e) {
        var toBeAdded = [];
        var resp = JSON.parse(xhr.responseText);
        console.log(resp);
        for (ID in resp['Cities']){
            var newCity = [];
            newCity.push(ID);
            newCity.push(resp['Cities'][ID][0]);
            newCity.push(resp['Cities'][ID][1]);
            newCity.push(resp['Cities'][ID][2]);
            newCity.push(resp['Cities'][ID][3]);

			console.log(newCity)
            toBeAdded.push(newCity);
        }

        addEntries(toBeAdded);

    }

    xhr.onerror = function (e) {
        console.log("error");
    }


    xhr.send();

}

function searchByCountry(){

	var tableBody = document.getElementById("fullTableBody");
	tableBody.innerHTML = "";

	var xhr = new XMLHttpRequest();

	var countryToSearch = document.getElementById("countrySearchEntry").value;
	var targetURL = mainURL + "country/" + countryToSearch;
	xhr.open("GET", targetURL);

	xhr.onload = function(e) {
		var toBeAdded = [];
		var resp = JSON.parse(xhr.responseText);
		for (ID in resp['Cities']){;
			var newCity = [];
			newCity.push(resp['Cities'][ID][0]);
			newCity.push(resp['Cities'][ID][1]);
			newCity.push(resp['Cities'][ID][2]);
			newCity.push(resp['Cities'][ID][3][0]);
			newCity.push(resp['Cities'][ID][3][1]);

			toBeAdded.push(newCity);
		}


		addEntries(toBeAdded);

	}

	xhr.onerror = function (e) {
		console.log("error");
	}

	xhr.send(null);
}

function resetTable(){

  document.getElementById("citySearchEntry").value= "";
  document.getElementById("countrySearchEntry").value= "";
  document.getElementById("addCityCity").value= "";
  document.getElementById("addCityLat").value= "";
  document.getElementById("addCityLon").value= "";
  document.getElementById("addCityCountry").value= "";
  document.getElementById("removeCityInput").value= "";
  document.getElementById("cityID1Entry").value= "";
  document.getElementById("cityID2Entry").value= "";
    var tableBody = document.getElementById("fullTableBody");


    var xhr = new XMLHttpRequest();
    var targetURL = mainURL + "reset/";

    xhr.open("PUT", targetURL);

    xhr.onload = function(e){
        //console.log(xhr.responseText)
        loadAllCities();
    }

    xhr.onerror = function (e){
        console.log("error");
    }

    xhr.send("");
}

function addCity(){



    var cityName = document.getElementById("addCityCity").value;
    var countryName = document.getElementById("addCityCountry").value;
    var lat = document.getElementById("addCityLat").value;
    var lonny = document.getElementById("addCityLon").value;

    var newCity = {};
    newCity['name'] = cityName;
    newCity['country'] = countryName;
    newCity['latitude'] = lat;
    newCity['longitude'] = lonny;

    console.log(newCity)

    var xhr = new XMLHttpRequest();
    var targetURL = mainURL + "cities/";

    xhr.open("POST", targetURL);

    xhr.onload = function(e){
        //console.log('hello')
        var resp = xhr.responseText;
        console.log(resp);

        // Add To Top of Table
        var tableBody = document.getElementById("fullTableBody");
        var newRow = document.createElement("tr");

        var td = document.createElement("td");
        var node = document.createTextNode(cityName);
        td.appendChild(node);
        newRow.appendChild(td);

        td = document.createElement("td");
        node = document.createTextNode(countryName);
        td.appendChild(node);
        newRow.appendChild(td);

        td = document.createElement("td");
        node = document.createTextNode(lat);
        td.appendChild(node);
        newRow.appendChild(td);

        td = document.createElement("td")
        node = document.createTextNode(lonny);
        td.appendChild(node);
        newRow.appendChild(td);

        td = document.createElement("td");
        node = document.createTextNode(JSON.parse(resp)['id']);
        td.appendChild(node);
        newRow.appendChild(td);

        tableBody.prepend(newRow);

        document.getElementById("addConf").innerHTML = 'NewID: ' + JSON.parse(resp)['id'];

    }

    xhr.onerror = function (e) {
        console.log("error")
    }

    xhr.send(JSON.stringify(newCity))
}

function removeCity(){
    var cityToDel = document.getElementById("removeCityInput").value ;
    var targetURL = mainURL + 'city/' + cityToDel;

    var xhr = new XMLHttpRequest();

    xhr.open("DELETE", targetURL);

    xhr.onload = function(e){
        var resp = JSON.parse(xhr.responseText)
        if (resp['result'] === 'success'){
            document.getElementById("removeConf").innerHTML = 'Successfully Removed';
            loadAllCities();
        }
        else {
            document.getElementById("removeConf").innerHTML = 'City Not Found';
        }
    }

    xhr.onerror = function(e){
        console.log(error);
    }

    xhr.send("");
}

function getDistances() {
    var city1 = document.getElementById("cityID1Entry").value;
    var city2 = document.getElementById("cityID2Entry").value;
    document.getElementById("from").innerHTML="";

    var targetURL = mainURL + 'distance/'
    var inputObj = {};
    inputObj['c1'] = city1;
    inputObj['c2'] = city2;
    console.log(inputObj);

    var xhr = new XMLHttpRequest();

    xhr.open("PUT", targetURL);

    xhr.onload = function(e){
        var resp = JSON.parse(xhr.responseText);

        console.log(resp);
        makeRequestCountries(resp["city1"], "from", parseInt(resp['distance']));
        makeRequestCountries(resp["city2"], "to", parseInt(resp['distance']));


    }

    xhr.onerror = function(e){
        console.log("error");
    }

    xhr.send(JSON.stringify(inputObj));



}


function makeRequestCountries(id, key, distance){
  console.log("entered updateMessages");
  //making requests to find countries
  var xhr = new XMLHttpRequest();
  console.log(id);
  var targetURL = mainURL + "city/" + id;
  xhr.open("GET", targetURL);
  xhr.onload = function(e){
      var resp_1 = JSON.parse(xhr.responseText);
      console.log(resp_1);
      if(key == "from"){
        document.getElementById("from").innerHTML = "Distance"
      }
      document.getElementById("from").innerHTML +=" "+ key +" "+ resp_1["Data"]["Name"]+ ", " + resp_1["Data"]["Country"];
      makeRequestFlag(resp_1["Data"]["Country"], key);
      if(key == "to"){
        document.getElementById("from").innerHTML += " is "+  distance + " kilometers.";
      }
  }

  xhr.onerror = function(e){
      console.log("error");
  }

  xhr.send(null);

}



function makeRequestFlag(country, key){
  console.log("entered makeRequestFlag");
  var xhr = new XMLHttpRequest();
  console.log(country);
  var targetURL = "https://restcountries.eu/rest/v2/name/" + country;
  xhr.open("GET", targetURL);
  xhr.onload = function(e){
      var resp = JSON.parse(xhr.responseText);
      console.log(resp[0]["flag"]);
      try{
        var previous_flag = document. getElementById("flag" + key);
        previous_flag. parentNode. removeChild(previous_flag);
      }
      catch(err){
        console.log(err);
      }
      var img = document.createElement('img');

      img.setAttribute("id", "flag" + key);
      img.setAttribute("height", "100");
      img.setAttribute("width", "150");
      img.src = resp[0]["flag"];

      document.getElementById(key+'_flag').appendChild(img);

  }

  xhr.onerror = function(e){
      console.log("error");
  }

  xhr.send(null);

}


// Get Rid of Response Labels To Add And Remove Buttons Whenever There's another click
document.body.addEventListener('click', e => {
    document.getElementById("removeConf").innerHTML = '';
    document.getElementById("addConf").innerHTML = '';
});
