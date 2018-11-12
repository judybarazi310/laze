// This example displays a marker at the center of Australia.
// When the user clicks the marker, an info window opens.
// The maximum width of the info window is set to 200 pixels.

// maps api:
// https://developers.google.com/maps/documentation/javascript/examples/map-simple

function initMap() {
    var wlu = {lat: 43.4735, lng: -80.5273};
    var tims = {lat: 43.4732, lng: -80.5255};
    var subway = {lat: 43.4727, lng: -80.5265};

    var map = new google.maps.Map(document.getElementById('map'), {
        zoom: 17,
        center: wlu,
        streetViewControl: false,
        fullscreenControl: false
    });
    
    var timsString = '<h1>Tims</h1>';
    var subwayString = '<h1>Subway Bricker</h1>';

    var timswindow = new google.maps.InfoWindow({
    content: timsString,
    maxWidth: 200
    });
    var subwaywindow = new google.maps.InfoWindow({
    content: subwayString,
    maxWidth: 200
    });

    var timsmarker = new google.maps.Marker({
    position: tims,
    map: map,
    icon: pinIcon,
    title: 'Tim Hortons Science'
    });
    var subwaymarker = new google.maps.Marker({
    position: subway,
    map: map,
    icon: pinIcon,
    title: 'Subway Bricker'
    });

    timsmarker.addListener('click', function(){
    timswindow.open(map, timsmarker);
    })
    subwaymarker.addListener('click', function(){
    subwaywindow.open(map, subwaymarker);
    })

    clickListener(map);
    // setOverlay(map);
}

function clickListener(map) {
    map.addListener('click', function(event) {
        var userin = prompt("What is happening here?");
        if (userin != null && userin != ''){
            var newCoordinates = {lat: event.latLng.lat(), lng: event.latLng.lng()};
            var newMarkerString = '<h1>' + userin + '</h1>';
            var newMarker = new google.maps.Marker({
                position: newCoordinates,
                map: map,
                icon: pinIcon,
                title: 'New marker'
            });
            var newMarkerWindow = new google.maps.InfoWindow({
                content: newMarkerString,
                maxWidth: 200
            });
            newMarker.addListener('click', function(){
                newMarkerWindow.open(map, newMarker);
            })
        }

    })
}

function setOverlay(map){
    var imageBounds = {
        north: 43.4768,
        south: 43.4712,
        east: -80.5203,
        west: -80.5322
    };
    wluOverlay = new google.maps.GroundOverlay(
        overlayUrl,
        imageBounds);
    wluOverlay.setMap(map);
}