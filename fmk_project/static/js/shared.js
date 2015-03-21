
////////////////////////////////////////
////////////////////////////////////////
function setCookie(c_name,value,exdays) {
	var exdate = new Date();
	exdate.setDate(exdate.getDate() + exdays);
	var c_value=escape(value) + ((exdays==null) ? "" : "; expires="+exdate.toUTCString());
	document.cookie = c_name + "=" + c_value;
}

function getCookie(c_name) {
	var i,x,y,ARRcookies=document.cookie.split(";");
	for (i=0; i<ARRcookies.length; i++) {
		x = ARRcookies[i].substr(0,ARRcookies[i].indexOf("="));
		y = ARRcookies[i].substr(ARRcookies[i].indexOf("=")+1);
		x = x.replace(/^\s+|\s+$/g,"");
		if (x==c_name) {
			return unescape(y);
		}
	}
}

////////////////////////////////////////
////////////////////////////////////////
function addCommas(nStr) {
    nStr += '';
    x = nStr.split('.');
    x1 = x[0];
    x2 = x.length > 1 ? '.' + x[1] : '';
    var rgx = /(\d+)(\d{3})/;
    while (rgx.test(x1)) {
        x1 = x1.replace(rgx, '$1' + ',' + '$2');
    }
    return x1 + x2;
}

////////////////////////////////////////
////////////////////////////////////////
function has3d() {
    var el = document.createElement('p'), 
        has3d,
        transforms = {
            'webkitTransform':'-webkit-transform',
            'OTransform':'-o-transform',
            'msTransform':'-ms-transform',
            'MozTransform':'-moz-transform',
            'transform':'transform'
        };

    // Add it to the body to get the computed style.
    document.body.insertBefore(el, null);

    for (var t in transforms) {
        if (el.style[t] !== undefined) {
            el.style[t] = "translate3d(1px,1px,1px)";
            has3d = window.getComputedStyle(el).getPropertyValue(transforms[t]);
        }
    }

    document.body.removeChild(el);

    return (has3d !== undefined && has3d.length > 0 && has3d !== "none");
}


////////////////////////////////////////
////////////////////////////////////////
//  Document Setup
$(window).load(function () {
	$('#container').delay(100).fadeIn();
	$('#containerAuth').delay(100).fadeIn();
});
$(document).ready(function() {

	Shadowbox.init({
		skipSetup: true, 
		overlayColor:'#999999'
	});


	var iPersonSize = 300;
	
	////////////////////////////////////////
	////////////////////////////////////////
	//  Browser detection
	bBrowserIsIE = false;
	if (/MSIE (\d+\.\d+);/.test(navigator.userAgent)) {
		bBrowserIsIE = true;
	}
	
	//  Fade or flip?
	var sInfoStyle = 'fade'; 
	if (has3d()) { 
		sInfoStyle = 'flip'; 
	}
	
	//  Don't scroll
	//document.addEventListener('touchmove', function(e) { 
	// e.preventDefault(); 
	//}, false);


	//  Home page game interactions
	if (sPage == 'home') { 
		

	
		//  Copy the peoples photos to the back here, saves filesize
		$('#person1 .photoMini').html($('#person1 .photoFrontImage').html());
		$('#person2 .photoMini').html($('#person2 .photoFrontImage').html());
		$('#person3 .photoMini').html($('#person3 .photoFrontImage').html());
		
		//  Tap or click?
		var pointerDown = 'mousedown';
		var pointerMove = 'mousemove';
		var pointerUp = 'mouseup';
		var pointerClick = 'click';
		if ('ontouchstart' in window) { 
			pointerDown = 'touchstart';
			pointerMove = 'touchmove';
			pointerUp = 'touchend';
			pointerClick = 'touchstart';
		} 

		//  Click anywhere, face the people forwards
		$(document).bind(pointerClick, function() {
			if (sInfoStyle == 'flip') { 
				$('#person1 .photoCard').removeClass('flipped');
				$('#person2 .photoCard').removeClass('flipped');
				$('#person3 .photoCard').removeClass('flipped');
			} else { 
				$('#person1 .photoBack').fadeOut();
				$('#person2 .photoBack').fadeOut();
				$('#person3 .photoBack').fadeOut();
			}
		});
		
		if (sInfoStyle == 'flip') { 
			$('#person1 .photoBack').addClass('threedee');
			$('#person2 .photoBack').addClass('threedee');
			$('#person3 .photoBack').addClass('threedee');
		} else { 
			$('#person1 .photoBack').hide();
			$('#person2 .photoBack').hide();
			$('#person3 .photoBack').hide();
		}
		/*
		//  Landing page start button
		$('#btnPlayGame').bind(pointerClick, function () { 
			$('#landingPage').fadeOut(); 
			$('#btnChangePeople').fadeIn();
			setCookie('seenLandingPage', 'true', 28);
			return false;
		});
		/*
		if (getCookie('seenLandingPage') == 'true') { 
			$('#landingPage').hide(); 
			$('#btnChangePeople').show();
		}
		*/
		
		//  Landing page start button
		$('#btnWhereVideo').bind(pointerClick, function () { 
			// open a welcome message as soon as the window loads
		    
		    Shadowbox.open({
		        content:    'http://player.vimeo.com/video/68350401',
		        player:     "iframe",
		        title:      ""
		    });
		    
			return false;
		});
		
		
		
		//  Auth button
		$('#btnAuthOpen').bind(pointerClick, function () { 
			$('#authNotSignedInClosed').hide();
			$('#authNotSignedInOpen').show();
			return false;
		});
	

		var personShag  = 0;
		var personMarry = 0;
		var personKill  = 0;

		//  Icon clicks
		function updateIcons() {

			$('#person1 #icon1 .word').hide();
			$('#person1 #icon2 .word').hide();
			$('#person1 #icon3 .word').hide();
			$('#person2 #icon1 .word').hide();
			$('#person2 #icon2 .word').hide();
			$('#person2 #icon3 .word').hide();
			$('#person3 #icon1 .word').hide();
			$('#person3 #icon2 .word').hide();
			$('#person3 #icon3 .word').hide();

			$('#person'+personShag+' #icon1 .word').show();
			$('#person'+personMarry+' #icon2 .word').show();
			$('#person'+personKill+' #icon3 .word').show();

			if (personShag == 0) {
				iconOn(1, 1);
				iconOn(2, 1);
				iconOn(3, 1);
			} else {
				iconOff(1, 1);
				iconOff(2, 1);
				iconOff(3, 1);
			}
			if (personMarry == 0) {
				iconOn(1, 2);
				iconOn(2, 2);
				iconOn(3, 2);
			} else {
				iconOff(1, 2);
				iconOff(2, 2);
				iconOff(3, 2);
			}
			if (personKill == 0) {
				iconOn(1, 3);
				iconOn(2, 3);
				iconOn(3, 3);
			} else {
				iconOff(1, 3);
				iconOff(2, 3);
				iconOff(3, 3);
			}

			//  Hide these
			overlaysAllOff();
			//borderAllOff();

			//  Show correct overlays
			if (personShag != 0) {
				overlayOn(personShag,1);
				borderOn(personShag,1);
			}
			if (personMarry != 0) {
				overlayOn(personMarry,2);
				borderOn(personMarry,2);
			}
			if (personKill != 0) {
				overlayOn(personKill,3);
				borderOn(personKill,3);
			}

			//  If we are done...
			if (personShag != 0 && personMarry != 0 && personKill != 0) {
				$('#btnChangePeople').hide();
				$('#btnNextRound').fadeIn();

				//  Overlays off
				overlaysAllOff();
                //


				//  Hide the info buttons
				$('.info').hide();

				//  Unbind icon buttons
				$('#person1 #icon1').unbind();
				$('#person1 #icon2').unbind();
				$('#person1 #icon3').unbind();
				$('#person2 #icon1').unbind();
				$('#person2 #icon2').unbind();
				$('#person2 #icon3').unbind();
				$('#person3 #icon1').unbind();
				$('#person3 #icon2').unbind();
				$('#person3 #icon3').unbind();

				//  Remove the pointer cursor from the icons
				$('.home .icon').css('cursor', 'auto');

				$.ajax({
				    url: "smk-result.json",
				    type: "GET",
				    dataType: "html",
				    data: "&sSMKUID="+sSMKUID+"&iPersonShag="+personShag+"&iPersonMarry="+personMarry+"&iPersonKill="+personKill+"&",
				    success: function(sData) {
				    	var aData = $.parseJSON(sData);

				    	$('.sums').fadeIn();
				    	$('#person1 #sumValue1').html(addCommas(aData['iPerson1CountShag']));
				    	$('#person1 #sumValue2').html(addCommas(aData['iPerson1CountMarry']));
				    	$('#person1 #sumValue3').html(addCommas(aData['iPerson1CountKill']));
				    	$('#person2 #sumValue1').html(addCommas(aData['iPerson2CountShag']));
				    	$('#person2 #sumValue2').html(addCommas(aData['iPerson2CountMarry']));
				    	$('#person2 #sumValue3').html(addCommas(aData['iPerson2CountKill']));
				    	$('#person3 #sumValue1').html(addCommas(aData['iPerson3CountShag']));
				    	$('#person3 #sumValue2').html(addCommas(aData['iPerson3CountMarry']));
				    	$('#person3 #sumValue3').html(addCommas(aData['iPerson3CountKill']));
				    }
				});



			}
		}

		function iconOn(p, i) {
			$('#person'+p+' #icon'+i+' img').fadeTo(250, 1.0);
		}
		function iconOff(p, i) {
			$('#person'+p+' #icon'+i+' img').fadeTo(250, 0.25);
		}



		function overlayOn(p, i) {
			$('#person'+p+' #overlay'+i).show();
		}
		function overlayOff(p, i) {
			$('#person'+p+' #overlay'+i).hide();
		}
		function overlaysAllOff() {
			overlayOff(1,1);
			overlayOff(1,2);
			overlayOff(1,3);
			overlayOff(2,1);
			overlayOff(2,2);
			overlayOff(2,3);
			overlayOff(3,1);
			overlayOff(3,2);
			overlayOff(3,3);
		}



		function borderOn(p, i) {
			if (i == 1) {
				$('#person'+p).addClass('shag');
			}
			if (i == 2) {
				$('#person'+p).addClass('marry');
			}
			if (i == 3) {
				$('#person'+p).addClass('kill');
			}
		}
		function borderOff(p, i) {
			$('#person'+p).removeClass('shag');
			$('#person'+p).removeClass('marry');
			$('#person'+p).removeClass('kill');
		}
		function borderAllOff() {
			borderOff(1,1);
			borderOff(1,2);
			borderOff(1,3);
			borderOff(2,1);
			borderOff(2,2);
			borderOff(2,3);
			borderOff(3,1);
			borderOff(3,2);
			borderOff(3,3);
		}

		$('#person1 #icon1').bind(pointerClick, function(e) {
			if (personShag  == 1) { personShag = 0; };
			if (personMarry == 1) { personMarry = 0; };
			if (personKill  == 1) { personKill  = 0; };
			personShag = 1;
			updateIcons();
		});
		$('#person1 #icon2').bind(pointerClick, function(e) {
			if (personShag  == 1) { personShag = 0; };
			if (personMarry == 1) { personMarry = 0; };
			if (personKill  == 1) { personKill  = 0; };
			personMarry = 1;
			updateIcons();
		});
		$('#person1 #icon3').bind(pointerClick, function(e) {
			if (personShag  == 1) { personShag = 0; };
			if (personMarry == 1) { personMarry = 0; };
			if (personKill  == 1) { personKill  = 0; };
			personKill = 1;
			updateIcons();
		});

		$('#person2 #icon1').bind(pointerClick, function(e) {
			if (personShag  == 2) { personShag = 0; };
			if (personMarry == 2) { personMarry = 0; };
			if (personKill  == 2) { personKill  = 0; };
			personShag = 2;
			updateIcons();
		});
		$('#person2 #icon2').bind(pointerClick, function(e) {
			if (personShag  == 2) { personShag = 0; };
			if (personMarry == 2) { personMarry = 0; };
			if (personKill  == 2) { personKill  = 0; };
			personMarry = 2;
			updateIcons();
		});
		$('#person2 #icon3').bind(pointerClick, function(e) {
			if (personShag  == 2) { personShag = 0; };
			if (personMarry == 2) { personMarry = 0; };
			if (personKill  == 2) { personKill  = 0; };
			personKill = 2;
			updateIcons();
		});

		$('#person3 #icon1').bind(pointerClick, function(e) {
			if (personShag  == 3) { personShag = 0; };
			if (personMarry == 3) { personMarry = 0; };
			if (personKill  == 3) { personKill  = 0; };
			personShag = 3;
			updateIcons();
		});
		$('#person3 #icon2').bind(pointerClick, function(e) {
			if (personShag  == 3) { personShag = 0; };
			if (personMarry == 3) { personMarry = 0; };
			if (personKill  == 3) { personKill  = 0; };
			personMarry = 3;
			updateIcons();
		});
		$('#person3 #icon3').bind(pointerClick, function(e) {
			if (personShag  == 3) { personShag = 0; };
			if (personMarry == 3) { personMarry = 0; };
			if (personKill  == 3) { personKill  = 0; };
			personKill = 3;
			updateIcons();
		});
		
			
		
	}		
	

	
});









































