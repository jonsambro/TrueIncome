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

function jobChanged() {
    function setColour(value, average) {

    }

    function getColor(value, average) {
        value = (value/average) -0.5
        var hue = ((value) * 120).toString(10);
        return ["hsl(", hue, ",100%,50%)"].join("");
    }

    var average_adjusted_income = 0;
    var e = document.getElementById('profession_selecter');
    e = e[e.selectedIndex].value;
    $.getJSON('markers', {'OCC_ID': e}, function (x) {
        $.each(x, function (index, value) {
            average_adjusted_income = average_adjusted_income + value.adjusted_median;
        })
        average_adjusted_income = average_adjusted_income / x.length;
        console.log(typeof x)
        console.log(average_adjusted_income);
        $.each(x, function (index, value) {
            console.log(value);

            myColour = getColor(value.adjusted_median, average_adjusted_income)
            var cityCircle = new google.maps.Circle({
                strokeColor: myColour,
                strokeOpacity: 0.8,
                strokeWeight: 2,
                fillColor: myColour,
                fillOpacity: 0.35,
                map: map,
                center: {lat: value.lat, lng: value.lng},
                radius: 50000
            });
            /*
             var marker = new google.maps.Marker({
             position: {lat: value.lat, lng: value.lng},
             map: map,
             title: value.name
             });
             marker.addListener('click', function () {
             console.log(marker.title)
             });*/
        })
    })
    console.log("Markers added");
}

function markerClicked() {

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