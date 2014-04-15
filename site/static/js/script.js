$(function(){
	var verificaMenu=false;
	$("#menuOptions").click(function(event) {

		if (verificaMenu) {
			$("#menuLeftBar").removeClass('transitionLeftToRight');
			$("#menuLeftBar").addClass('transitionRightToLeft');
			
			$("#contextCenter").css("width","100%");
			$("#contextCenter").css("margin-left","0%");
			$("#containerPalpiteRodada>button").css("width","8.3%");
			$("#menuLeftBar").css("margin-left","-5%");
			verificaMenu=false;
		} else{
			$("#menuLeftBar").addClass('transitionLeftToRight');
			$("#menuLeftBar").css('margin-top',$(window).scrollTop())
			$("#contextCenter").css("width","95%");
			$("#contextCenter").css("margin-left","5%");
			$("#containerPalpiteRodada>button").css("width","7%");
			$("#menuLeftBar").css("margin-left","0%");
			verificaMenu=true;
		};
		
	});

	$(window).scroll(function() {
	  if (verificaMenu) {

	  	$("#menuLeftBar").css('margin-top',$(window).scrollTop());
	  }
	});
});