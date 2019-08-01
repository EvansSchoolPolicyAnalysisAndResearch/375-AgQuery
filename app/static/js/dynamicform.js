function SelectAll(name) {
	var boxes =  document.getElementsByClassName(name);
	for(i = 0; i < boxes.length; i++) {
		boxes[i].checked = true;
	}
}


function ClearAll(name) {
	var boxes = document.getElementsByClassName(name);
	for(i = 0; i < boxes.length; i++) {
		boxes[i].checked = false;
	}
}

function ToggleSelect(element) {
	if(element.checked == true){
		SelectAll(element.id);
	} else {
		ClearAll(element.id);
	}
}

function EnableButtons() {
	var indicators	= document.getElementsByName("indicator");
	var geoyears	= document.getElementsByName("geo_year");
	var hasind		= false;
	var hasgeo		= false;
	var submitters	= document.getElementsByClassName("submitter");
	for(i=0; i < indicators.length; i++) {
		if(indicators[i].checked == true){
			hasind = true;
			break;
		}
	}
	for(i=0; i < geoyears.length; i++) {
		if(geoyears[i].checked == true){
			hasgeo = true;
			break;
		}
	}
	if(hasind && hasgeo) {
		for(i=0; i < submitters.length; i++) {
			submitters[i].removeAttribute('disabled');
		}
	} else {
		for(i=0; i < submitters.length; i++){
			submitters[i].setAttribute('disabled', 'true');
		}
	}

}

