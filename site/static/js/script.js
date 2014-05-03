$(function(){
	var verificaMenu=false;
	$("#menuOptions").click(function() {
		$("#menuContext").css('display', 'block');
	});
	
});

function redimensionaPalpites(){
	var tamanhoAtual = $("#context").height()+$(".containerPalpites").height();
	$("#context").css("height",tamanhoAtual.toString());
	alert("teste:"+tamanhoAtual);
}