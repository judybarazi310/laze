// This example displays a marker at the center of Australia.
// When the user clicks the marker, an info window opens.
// The maximum width of the info window is set to 200 pixels.

function initMap() {
    var uluru = {lat: -25.363, lng: 131.044};
    var tims = {lat: 43.4732, lng: -80.5255};
    var subway = {lat: 43.4727, lng: -80.5265};
    var map = new google.maps.Map(document.getElementById('map'), {
    zoom: 17,
    center: tims
    });

    var contentString = '<div id="content">'+
        '<div id="siteNotice">'+
        '</div>'+
        '<h1 id="firstHeading" class="firstHeading">Uluru</h1>'+
        '<div id="bodyContent">'+
        '<p><b>Uluru</b>, also referred to as <b>Ayers Rock</b>, is a large ' +
        'sandstone rock formation in the southern part of the '+
        'Northern Territory, central Australia. It lies 335&#160;km (208&#160;mi) '+
        'south west of the nearest large town, Alice Springs; 450&#160;km '+
        '(280&#160;mi) by road. Kata Tjuta and Uluru are the two major '+
        'features of the Uluru - Kata Tjuta National Park. Uluru is '+
        'sacred to the Pitjantjatjara and Yankunytjatjara, the '+
        'Aboriginal people of the area. It has many springs, waterholes, '+
        'rock caves and ancient paintings. Uluru is listed as a World '+
        'Heritage Site.</p>'+
        '<p>Attribution: Uluru, <a href="https://en.wikipedia.org/w/index.php?title=Uluru&oldid=297882194">'+
        'https://en.wikipedia.org/w/index.php?title=Uluru</a> '+
        '(last visited June 22, 2009).</p>'+
        '</div>'+
        '</div>';
    
    var timsString = '<h1>Tims</h1>';
    var subwayString = '<h1>Subway Bricker</h1>';


    var infowindow = new google.maps.InfoWindow({
    content: contentString,
    maxWidth: 200
    });

    var timswindow = new google.maps.InfoWindow({
    content: timsString,
    maxWidth: 200
    });

    var subwaywindow = new google.maps.InfoWindow({
    content: subwayString,
    maxWidth: 200
    });

    var marker = new google.maps.Marker({
    position: uluru,
    map: map,
    title: 'Uluru (Ayers Rock)'
    });
    var timsmarker = new google.maps.Marker({
    position: tims,
    map: map,
    title: 'Tim Hortons Science'
    });
    var subwaymarker = new google.maps.Marker({
    position: subway,
    map: map,
    title: 'Subway Bricker'
    });
    marker.addListener('click', function() {
    infowindow.open(map, marker);
    });
    timsmarker.addListener('click', function(){
    timswindow.open(map, timsmarker);
    })
    subwaymarker.addListener('click', function(){
    subwaywindow.open(map, subwaymarker);
    })
}