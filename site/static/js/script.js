$(function(){
	var verificaMenu=false;
	$("#menuOptions").click(function(event) {

		if (verificaMenu) {
			$("#menuLeftBar").removeClass('transitionLeftToRight');
			$("#menuLeftBar").addClass('transitionRightToLeft');
			$("#contextCenter").css("width","100%");
			$("#contextCenter").css("margin-left","0%");
			
			$("#menuLeftBar").css("margin-left","-8%");
			verificaMenu=false;
		} else{
			$("#menuLeftBar").addClass('transitionLeftToRight');
			$("#menuLeftBar").css('margin-top',$(window).scrollTop())
			$("#contextCenter").css("width","92%");
			$("#contextCenter").css("margin-left","8%");
			
			$("#menuLeftBar").css("margin-left","0%");
			verificaMenu=true;
		};
		
	});

	$(".barraMenuLeft").hover(
	  function() {
	    $(this).css("width","100%");
	    
	  },
	  function() {
	    $(this).css("width","40%");
	    
	  }
	);

	$(window).scroll(function() {
	  if (verificaMenu) {

	  	$("#menuLeftBar").css('margin-top',$(window).scrollTop());
	  }
	});
});