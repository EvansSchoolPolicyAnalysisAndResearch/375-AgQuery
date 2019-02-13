function SelectAll(name) {
	var boxes =  document.getElementsByName(name);
	for(i = 0; i < boxes.length; i++) {
		boxes[i].checked = true;
	}
}


function ClearAll(name) {
	var boxes = document.getElementsByName(name);
	for(i = 0; i < boxes.length; i++) {
		boxes[i].checked = false;
	}
}

