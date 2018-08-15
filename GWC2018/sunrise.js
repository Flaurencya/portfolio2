var lat;
var lng; //variables declared at top

function sunriseTime () {
  lat = document.getElementById ("lat").value; //gets user latitude value
  lng = document.getElementById("lng").value; //gets user longitude value
  var query = "https://api.sunrise-sunset.org/json?lat=" + lat + "&lng=" + lng;
  //gets us to doc that has info about user latitude/longitude value
  var request = new XMLHttpRequest();
  request.open('GET', query, false);
  request.send();
  var requestInformation = JSON.parse(request.responseText);
  //we don't know what these lines mean yet but it's ok!!!!!!
  var sunriseTime = requestInformation.results.sunrise;
  alert("The sunrise time is " + sunriseTime);
}
function sunsetTime () {
  lat = document.getElementById ("lat").value; //gets user latitude value
  lng = document.getElementById("lng").value; //gets user longitude value
  var query = "https://api.sunrise-sunset.org/json?lat=" + lat + "&lng=" + lng;
  //gets us to doc that has info about user latitude/longitude value
  var request = new XMLHttpRequest();
  request.open('GET', query, false);
  request.send();
  var requestInformation = JSON.parse(request.responseText);
  //we don't know what these lines mean yet but it's ok!!!!!!
  var sunsetTime = requestInformation.results.sunset;
  alert("The sunset time is " + sunsetTime);
}
