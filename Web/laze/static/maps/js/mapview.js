// This example displays a marker at the center of Australia.
// When the user clicks the marker, an info window opens.
// The maximum width of the info window is set to 200 pixels.

// maps api:
// https://developers.google.com/maps/documentation/javascript/examples/map-simple

var markers = [];
var infowindows = [];

function toggleMenuGroup(event) {
    $(event.target).parent().children(".menu-group-body").each((i, child) => {
        $(child).toggleClass("collapsed");
    });
    $(event.target).children().first().toggleClass("rotate");
}

function createMenuGroupListeners(){
    $(".menu-group-header").each((i, obj) => {
        $(obj).click(toggleMenuGroup);
    });
    //toggle menu visibility, toggle right arrow visibility
    $(".map-arrowbtn").click( ()=> {
        $(".menu-wrapper").toggle(100);
        $("#arrowbtn-right").toggleClass('right-arrow-display');
    })
}

function initMap() {
    var strictBounds = new google.maps.LatLngBounds(
        new google.maps.LatLng(43.461, -80.559),
        new google.maps.LatLng(43.4872, -80.509), 
        
    )
    var wlu = {lat: 43.4735, lng: -80.5273};
    var tims = {lat: 43.4732, lng: -80.5255};
    var subway = {lat: 43.4727, lng: -80.5265};
    

    var map = new google.maps.Map(document.getElementById('map'), {
        minZoom:16,
        maxZoom:20,
        zoom: 16,
        center: wlu,
        streetViewControl: false,
        fullscreenControl: false,
        mapTypeControl: false,
        zoomControl: true
    });

    // createPin("Tim Hortons", "text", "TESTING", tims, map);
    // createPin("Subway Bricker", "text", "TESTING", subway, map);

    let overlay = setOverlay(map);
    addOverlayClickListener(map, overlay);
    google.maps.event.addListener(map, 'dragend', function() {
        if (strictBounds.contains(map.getCenter())) return;
        var c = map.getCenter(),
         x = c.lng(),
         y = c.lat(),
         maxX = strictBounds.getNorthEast().lng(),
         maxY = strictBounds.getNorthEast().lat(),
         minX = strictBounds.getSouthWest().lng(),
         minY = strictBounds.getSouthWest().lat();

     if (x < minX) x = minX;
     if (x > maxX) x = maxX;
     if (y < minY) y = minY;
     if (y > maxY) y = maxY;

     map.setCenter(new google.maps.LatLng(y, x));
    });
    // TODO: define minZoomLevel
    // google.maps.event.addListener(map, 'zoom_changed', function() {
    //     if (map.getZoom() < minZoomLevel) map.setZoom(minZoomLevel);
    // });
    
    //create pins from server data
    var i;
    for (i = 0; i < pinsToCreate.length; i++){
        createPin(pinsToCreate[i].title, pinsToCreate[i].desc, pinsToCreate[i].cat, {lat: Number(pinsToCreate[i].lat), lng: Number(pinsToCreate[i].lng)}, map);
    }
    $('#id_title,#id_description').addClass('form-control');
}

function addOverlayClickListener(map, overlay) {
    overlay.addListener('click', (event) => {
        let newCoordinates = {lat: event.latLng.lat(), lng: event.latLng.lng()};
        $('.form-control').val('');
        $('#newPinDialog').modal('show');
        
        // Setting the value of latitude and longitude in the form
        $('#id_longitude').val(newCoordinates.lng);
        $('#id_latitude').val(newCoordinates.lat);
       
        $('#newPinDialog .btn-primary').off().click(function() {
            let location = $('#id_title').val();
            let message = $('#id_description').val();
            let category = $('#id_category').val();
            if (location !== '') {
                $('#newPinDialog').modal('hide');
                createPin(location, message, category, newCoordinates, map);
            }
        });
    });
}

function createPin(location, message, category, coordinates, map) {
    // change pin icon according to category
    var pinIcon;
    if (category == 'VEHP') { pinIcon = parkingPinIcon; category = 'Parking';}
    else if (category == 'STY') { pinIcon = studyPinIcon; category = 'Study';}
    else if (category == 'FOOD') { pinIcon  = foodPinIcon; category = 'Food';}
    else {pinIcon = defaultPinIcon; category = 'Info';}

    let newMarker = new google.maps.Marker({
        position: coordinates,
        map: map,
        icon: pinIcon,
        title: location
    });
    let newMarkerString = '<h1 style="font-family: Varela-Round; font-size:1.5rem">' + location + '</h1><br>' + '<p style="font-family: Varela-Round; font-size:1rem">' + message + '</p>' + category;
    let newMarkerWindow = new google.maps.InfoWindow({
        content: newMarkerString,
        maxWidth: 200
    });
    newMarker.addListener('click', () => {
        for (var i = 0; i < infowindows.length; i++ ) infowindows[i].close();
        newMarkerWindow.open(map, newMarker);
    });
    markers.push(newMarker);
    infowindows.push(newMarkerWindow);
}

function setOverlay(map){
    var imageBounds = {
        north: 43.4763,
        south: 43.4687,
        east: -80.5192,
        west: -80.5331
    };
    wluOverlay = new google.maps.GroundOverlay(
        overlayUrl,
        imageBounds);
    wluOverlay.setMap(map);
    
    return wluOverlay;
}

createMenuGroupListeners();

function saveLocation(position) {
    $.ajaxSetup({
        headers: { "X-CSRFToken": getCookie("csrftoken") }
    });

    let url = window.location.origin + '/save-location/';
    let data = {
        'latitude': position.coords.latitude,
        'longitude': position.coords.longitude
    }

    $.ajax({
        type: 'POST',
        url: url,
        data: data,
        dataType: 'json'
    });
}

if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(saveLocation);
}

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}