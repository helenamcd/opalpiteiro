$(function(){
	var verificaMenu=false;
	$("#menuOptions").hover(function() {
		$("#menuContext").css('display', 'block');
	}, function() {
		$("#menuContext").css('display', 'none');
	});
	$("#menuContext").hover(function() {
		$("#menuContext").css('display', 'block');
	}, function() {
		$("#menuContext").css('display', 'none');
	});
});