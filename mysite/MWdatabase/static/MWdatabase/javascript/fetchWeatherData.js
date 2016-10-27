/**
 * Created by amdudda on 10/27/16.
 */

// alert("loaded fetchWeatherData");
// mars weather api at http://marsweather.ingenology.com/#get_started
	function httpGetAsync(theUrl, callback){
	    var xmlHttp = new XMLHttpRequest();
		xmlHttp.onreadystatechange = function() {
		    if (xmlHttp.readyState == 4 && xmlHttp.status == 200) {
				callback(xmlHttp.responseText);
			}
			else {
			    // alert("current state is: " + xmlHttp.response);
			}
    }

    xmlHttp.open("GET", theUrl, true); // true for asynchronous
    xmlHttp.send(null);
	}

	function writeCurrentWeather(jsondata){
		mydata = JSON.parse(jsondata);
		weatherdata = mydata.report;
		// alert(weatherdata["terrestrial_date"]);
		info2print = "";
		Object.keys(weatherdata).forEach(function(key) {
			info2print += (key + ": " + weatherdata[key] + "\n");
		});
		document.getElementById("current").innerText = info2print;
	}

	// TODO: this only fetches the first page of results, we'll need to figure out how
	// to page through results.  Maybe use a recursive function to simulate threading?
	function writeMultiDayWeather(jsondata) {
		// alert(jsondata);
		mydata = JSON.parse(jsondata);
		weatherdata = mydata.results;
		// alert(weatherdata[0].sol);
		info2print = "";
		for (i=0; i<weatherdata.length; i++){
			Object.keys(weatherdata[i]).forEach(function(key) {
				info2print += (key + ": " + weatherdata[i][key] + "\n");
			});
			// extra line break between records
			info2print += "\n";
		}
		document.getElementById("recent_past").innerText = info2print;
	}

	latestweather = "http://marsweather.ingenology.com/v1/latest/?format=json";
	oct2012 = "http://marsweather.ingenology.com/v1/archive/?terrestrial_date_start=2012-10-01&terrestrial_date_end=2012-10-31&format=json";

	httpGetAsync(latestweather,writeCurrentWeather);
	httpGetAsync(oct2012,writeMultiDayWeather);