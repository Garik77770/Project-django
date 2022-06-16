
window.onload = function() {
	    let linkWithAlert = document.getElementById("alertLink");
	    linkWithAlert.onclick = function() {
	        return confirm('Вы уверены?');
	    };
	};
