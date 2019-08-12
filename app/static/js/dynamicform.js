
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
	 * { Set all checkboxes with a given name to checked }
	 *
	 * @param      {String}  classname  The classname of of the checkboxes to
	 * 								  select
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


	/**
	 * { Set all checkboxes with a given name to unchecked }
	 *
	 * @param      {<type>}  classname  The classname
	 */
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

		// Check to see if any indicators have been selected
		for (let ind of indicators) {
			if(ind.checked == true){
				// At least one indicator has been selected, set hasind to true
				// and end the loop early
				hasind = true;
				break;
			}
		}

		// Check to see if any geography/year combos have been selected
		for (let geo of geoyears) {
			if(geo.checked == true){
				// At least one geograpy/year combo has been selected, set 
				// hasgeo to true and end the loop early
				hasgeo = true;
				break;
			}
		}
		// Add or remove required as necessary for indicator checkboxes
		if (hasind) {
			for (let ind of indicators) {
				ind.removeAttribute('required')
			}
		} else {
			for (let ind of indicators) {
				ind.setAttribute('required', 'true')
			}
		}

		//  Same for geoyears. NOTE the required attribute helps with
		// accessibility for individuals with using screen readers.
		if (hasgeo) {
			for (let geo of geoyears) {
				geo.removeAttribute('required')
			}
		} else {
			for (let geo of geoyears) {
				geo.setAttribute('required', 'true')
			}
		}
		// If I can find a way to get override the error messages for required
		// text without using jquery than I will get rid of this. Until then
		// this last chunk stays
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
