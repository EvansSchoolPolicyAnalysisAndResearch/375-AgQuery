
/**
 * Creates an object which contains the functions for manipulating the web
 *
 * @author     s. kiel
 * @copyright  Evans School Policy Analysis and Research Group 2019
 *
 * @type       {Object} Custom object to prevent global namespace pollution
 */
var AgQuery = new Object({


	/**
	 * { function_description }
	 *
	 * @param      String  classname  The classname of the 
	 */
	SelectAll: function(classname)  {
		// Finds all of the check boxes with the given name.
		var boxes =  document.getElementsByClassName(classname);

		for (let box of boxes) {
			if (box.offsetWidth != 0 && box.offsetHeight !=0){
				box.checked = true;
			}
		}
	},

	ClearAll: function(classname) {

		var boxes = document.getElementsByClassName(classname);
		for (let box of boxes) {
			if (box.offsetWidth != 0 && box.offsetHeight !=0){
				box.checked = false;
			}
		}
	},

	ToggleSelect: function(element) {
		if(element.checked == true){
			this.SelectAll(element.id);
		} else {
			this.ClearAll(element.id);
		}
	},

	EnableButtons: function() {
		var indicators, geoyears, submitters, hasind, hasgeo;

		indicators	= document.getElementsByName("indicator");
		geoyears	= document.getElementsByName("geo_year");
		submitters	= document.getElementsByClassName("submitter");
		hasind		= false;
		hasgeo		= false;

		for (let ind of indicators) {
			if(ind.checked == true){
				hasind = true;
				break;
			}
		}
		for (let geo of geoyears) {
			if(geo.checked == true){
				hasgeo = true;
				break;
			}
		}
		if(hasind && hasgeo) {
			for (let sub of submitters) {
				sub.removeAttribute('disabled');
			}
		} else {
			for (let sub of submitters) {
				sub.setAttribute('disabled', 'true');
			}
		}

	},

	FilterList: function(element) {
		var filt_list, item_text, filt_text;
		filt_list = document.getElementsByClassName(element.dataset.filterclass);
		filt_text = element.value.toUpperCase();
		// Filter the lists to remove elements which don't match the filter. 
		for (let item of filt_list) {
			item_text = item.textContent || item.innerText;
			if(item_text.toUpperCase().indexOf(filt_text) > -1 || filt_text == "") {
				item.style.display = "block";
			} else {
				item.style.display = "none";
			}

		}
		// Add/remove class for dealing with populated search boxes which do not
		// have focus.
		if(filt_text.length > 0){
			element.classList.add('haschars');
		} else if (filt_text.length == 0) {
			element.classList.remove('haschars');
		}
	}

});
