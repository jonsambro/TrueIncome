var map;
var cities;

function locationChanged() {
    var t = document.getElementById('selecter');
    var cityName = t[t.selectedIndex].value;
    document.getElementById("words").innerHTML = cityName;
    var city = cities[cityName];
    map.panTo(new google.maps.LatLng(city.lat, city.lon));
    //map.setZoom(10);
}

$(function () {
    console.log(window.location.pathname)
    //jQuery goes here

    var e = document.getElementById('selecter');
    if (e.length == 0) {
        $.getJSON('cities', function (x) {
            cities = x.cities;
            $.each(cities, function (index, value) {
                var option = document.createElement("option");
                option.text = value.Name;
                e.add(option);
            })
        })
    }
    console.log("Hello!");

});

function initMap() {
    var northEast = new google.maps.LatLng(49.579647, -65.225113);
    var southWest = new google.maps.LatLng(24.941723, -125.499005);
    var bounds = new google.maps.LatLngBounds(southWest, northEast);

    map = new google.maps.Map(document.getElementById('map'), {
        center: {lat: -34.397, lng: 150.644},
        zoom: 12,
        maxZoom: 12,
        minZoom: 1
    });

    map.setCenter(bounds.getCenter());
    map.fitBounds(bounds);
}

$(window).resize(function () {
    var northEast = new google.maps.LatLng(49.579647, -65.225113);
    var southWest = new google.maps.LatLng(24.941723, -125.499005);
    var bounds = new google.maps.LatLngBounds(southWest, northEast);

    map.setCenter(bounds.getCenter());
    map.fitBounds(bounds);
})