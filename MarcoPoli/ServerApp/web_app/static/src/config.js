/* disable right menu */
var snapper = new Snap({
	element: document.getElementById('myAppContent'),
	disable: 'right'
});

/* open/close notify's panel */
$( "#notificaBottom" ).click(function() {
  $( "#notificaBottom" ).hide( "slow", function() {
	//alert( "Animation complete." );
  });
});

function vediNotifica(testo){
	$( "#notificaBottom" ).show( "slow", function() {
		$( "#notificaBottom" ).text(testo);
	//alert( "Animation complete." );
  });
}