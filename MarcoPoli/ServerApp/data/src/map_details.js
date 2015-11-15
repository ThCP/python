	
	var position = [45.0628540000000000, 7.6612320000000000];
	
	var savedMap;
	
	var locations = [];
	var stations = [];
	
	function showGoogleMaps() {

		
		var latLng = new google.maps.LatLng(position[0], position[1]);
	 
		var mapOptions = {
			zoom: 17, // initialize zoom level - the max value is 21
			streetViewControl: false, // hide the yellow Street View pegman
			scaleControl: false, // allow users to zoom the Google Map
			zoomControl: false,
			mapTypeControl: false,
			mapTypeId: google.maps.MapTypeId.ROADMAP,
			center: latLng
		};
	 
		map = new google.maps.Map(document.getElementById('googlemaps'),
			mapOptions);
			
	 
		// Show the default red marker at the location
		/*marker = new google.maps.Marker({
			position: latLng,
			map: map,
			draggable: false,
			animation: google.maps.Animation.DROP
		});*/

		savedMap = map;
		getStationData();
	}


	
	
	
	/////////////////////////////////////////////
	function addStationToMap(x, y, str, sensors) {
		var image = 'img/icons/event_64.png';
		
		var marker = new google.maps.Marker({
			position: new google.maps.LatLng(x, y),
			map: savedMap,
			icon: image
		});
		
		
		//luce, umidità, temperatura, rumore, persone.
		
		var contentString;
		contentString="<b>Station#"+str+"</b><br>";
		contentString+= "<br><i class='fa fa-fire' style='color: #0066FF;'></i> Temperature: "+ sensors[2] +"&deg;C";
		contentString+= "<br><br><i class='fa fa-group' style='color: #FF0000;'></i> Crowding: "+ sensors[4] +"%";
		contentString+= "<br><br><i class='fa fa-lightbulb-o' style='color: gold;'></i> Light: "+ sensors[0] +"%";
		contentString+= "<br><br><i class='fa fa-volume-up' style='color: #009933;'></i> Noise: "+ sensors[3] +"%";
		
		var infowindow = new google.maps.InfoWindow({
			content: contentString
		});
		
		google.maps.event.addListener(marker, 'click', function() {
			infowindow.open(savedMap,marker);
		});
		
		stations.push(marker);
		
	}
	
	
	/////////////////////////////////////////////
	function addDestinationToMap(x, y, str, tipo) {
		var image = 'img/circle_orange.png';
		
		//alert(tipo);
		
		var marker = new google.maps.Marker({
			position: new google.maps.LatLng(x, y),
			map: savedMap,
			icon: image
		});
		
		
		//luce, umidità, temperatura, rumore, persone.
		
		var contentString = str;
		
		var infowindow = new google.maps.InfoWindow({
			content: contentString
		});
		
		google.maps.event.addListener(marker, 'click', function() {
			infowindow.open(savedMap,marker);
		});
		
		locations.push(marker);
		
	}


	//////////////////////////////////////////////////
	function deleteAllStations() {
		for (var i = 0; i < stations.length; i++) {
			stations[i].setMap(null);
		}
		stations = [];
	}
	
	// Sets the map on all markers in the array.
	function setAllMap(map) {
	  for (var i = 0; i < stations.length; i++) {
		stations[i].setMap(map);
	  }
	  for (var i = 0; i < locations.length; i++) {
		locations[i].setMap(map);
	  }
	}

	// Removes the markers from the map, but keeps them in the array.
	function hideMarkers() {
	  setAllMap(null);
	}

	// Shows any markers currently in the array.
	function showMarkers() {
	  setAllMap(savedMap);
	}

	// Deletes all markers
	function deleteMarkers() {
	  clearMarkers();
	  stations = [];
	}
	
	
	///////////////////////////////////////////////////
	function deleteAllDestinations() {
		for (var i = 0; i < locations.length; i++) {
			locations[i].setMap(null);
		}
		locations = [];
	}
	
	 
	google.maps.event.addDomListener(window, 'load', showGoogleMaps);