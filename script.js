var form = document.getElementById('file-form');
var fileSelect = document.getElementById('file-select');
var uploadButton = document.getElementById('upload-button');

var btn = document.getElementById("download");
$(document).ready(function() {
	$("#download").click(function adownload() {
		var url = /* enter your ngrok url here */"http://8a30a869.ngrok.io/retrieve/" + document.getElementById("filename").value;
    		location.assign(url);
	});

});

function _(el){
	return document.getElementById(el);
}

}
function progressHandler(event){
	_("loaded_n_total").innerHTML = "Uploaded" + event.loaded + " bytes of " + event.total;
	var percent = (event.loaded) / (event.total) * 100;
	_("progressBar").value = Math.round(percent);
	_("status").innerHTML = Math.round(percent) + "% uploaded... please wait";
}
function completeHandler(event){
	_("status").innerHTML = event.target.responseText;
	_("progressBar").value = 0;
}
function errorHandler(event){
	_("status").innerHTML = "Upload Failed"
}
function abortHandler(event){
	_("status").innerHTML = "Upload Aborted";
}
