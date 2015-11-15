	
	var position = [45.0628540000000000, 7.6612320000000000];
	
	var savedMap;
	
	var locations = [];
	var stations = [];
	var events = [];
	var minZoomLevel=16;
	
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
		
		// Limit the zoom level
		   google.maps.event.addListener(map, 'zoom_changed', function() {
			 if (map.getZoom() < minZoomLevel) map.setZoom(minZoomLevel);
		   });

		savedMap = map;
		getStationData();
		getEvents();
	}

	
	
	
	
	/////////////////////////////////////////////
	function addStationToMap(x, y, str, sensors) {
		//  (array) sensors = {luce, umidità, temperatura, rumore, persone}
		crowd=sensors[4];
		temp=sensors[2];
		light=sensors[0];
		noise=sensors[3];
		
		var image = 'img/icons/verde.png';
		
		if(crowd>=70 || noise>=15){
			image = 'img/icons/rosso.png';
		}
		else if(crowd>=30 || noise>=8){
			image = 'img/icons/giallo.png';
		}
		

		var marker = new google.maps.Marker({
			position: new google.maps.LatLng(x, y),
			map: savedMap,
			icon: image
		});

		
		var contentString;
		
		contentString="<b>Station#"+str+"</b><br>";
		
		if(temp>=25)
			contentString+= "<br><i class='fa fa-fire' style='color: #FF0000;'></i> Temperature: "+ temp +"&deg;C"; //caldo
		else if(temp<=15)
			contentString+= "<br><i class='fa fa fa-asterisk' style='color: #0066FF;'></i> Temperature: "+ temp +"&deg;C"; //freddo
		else
			contentString+= "<br><i class='fa fa-sun-o' style='color: gold;'></i> Temperature: "+ temp +"&deg;C"; //normale
			
		
		if(crowd>=70)
			contentString+= "<br><br><i class='fa fa-group' style='color: #FF0000;'></i> Crowd: "+ crowd +"%"; //affollato
		else if(crowd<=30)
			contentString+= "<br><br><i class='fa fa-group' style='color: #009933;'></i> Crowd: "+ crowd +"%"; //poca gente
		else
			contentString+= "<br><br><i class='fa fa-group' style='color: gold;'></i> Crowd: "+ crowd +"%";  //normale
			
		
		contentString+= "<br><br><i class='fa fa-lightbulb-o' style='color: gold;'></i> Light: "+ light +"%";
		
		if(noise>=15)
			contentString+= "<br><br><i class='fa fa-volume-up' style='color: #FF0000;'></i> Noise: "+ noise +"%"; //rumore alto
		else if(noise<=8)
			contentString+= "<br><br><i class='fa fa-volume-up' style='color: #009933;'></i> Noise: "+ noise +"%"; //rumore basso
		else
			contentString+= "<br><br><i class='fa fa-volume-up' style='color: gold;'></i> Noise: "+ noise +"%"; //rumore medio
			
		
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
		
		if(tipo=="AULA")
			image="img/room.png";
			
		if(tipo=="BAR")
			image="img/bar.png";
			
		if(tipo=="LAB_DIDAT")
			image="img/lab.png";
						
		if(tipo=="BIBLIO")
			image="img/library.png";
		
		logInfo = x+" "+y+" " + str + " " + tipo;
		console.log(logInfo);
		
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
	
	/////////////////////////////////////////////
	function addEventToMap(x,y,name,from_date,from_hour,to_date,to_hour,where,i) {
	
		var image = 'img/star.png';
			
		var marker = new google.maps.Marker({
			position: new google.maps.LatLng(x, y),
			map: savedMap,
			icon: image
		});
		
		var contentString = '<b>'+name+'</b>';
		
		if(where!=-1)
			contentString+='<br><i class="fa fa-map-marker"></i> '+where;
		
		if(from_date!=-1){
			contentString+='<br><i class="fa fa-calendar"></i> From: '+from_date;
			if(from_hour!=-1){
				contentString+=' - <i class="fa fa-clock-o"></i> '+from_hour;
			}	
		}else if(from_hour!=-1){
			contentString+='<br><i class="fa fa-clock-o"></i> From: '+from_hour;
		}
		

		if(to_date!=-1){
			contentString+='<br><i class="fa fa-calendar"></i> To: '+to_date;
			if(to_hour!=-1){
				contentString+=' - <i class="fa fa-clock-o"></i> '+to_hour;
			}	
		}else if(to_hour!=-1){
			contentString+='<br><i class="fa fa-clock-o"></i> To: '+to_hour;
		}
		
		
		var infowindow = new google.maps.InfoWindow({
			content: contentString
		});
		
		google.maps.event.addListener(marker, 'click', function() {
			infowindow.open(savedMap,marker);
		});
		
		events.push(marker);
		
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
	
	///////////////////////////////////////////////////
	function deleteAllEvents() {
		for (var i = 0; i < events.length; i++) {
			events[i].setMap(null);
		}
		events = [];
	}
	
	 
	google.maps.event.addDomListener(window, 'load', showGoogleMaps);