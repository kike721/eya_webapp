var Search = function(){

	function sendSearch() {
		$(".btnSearch").click(function (e) {
			e.preventDefault();
			var btnSend = $(this);
			formCont = $(this).closest("form");
			var error = formCont.find('.searchError');
			var text = formCont.find('.searchText');
			error.html('')
			if(text.val().length < 3){
				error.html('<i class="icon-alert"></i> Asegúrate de ingresar al menos tres letras');
			}
			else{
				var loader = $("#loader").find(".loader").clone();
				loader.addClass('active');
				$('body').append(loader);
				$('body').css('overflow', 'hidden');
				var url = '/busqueda/' + '?search=' + encodeURI(text.val().toLowerCase());
				window.location.replace(url);
			}
		});
	}

	function clearForm(form){
		form.find('input[type="text"]').each(function(){
			$(this).val('');
		});
	}

	function start(){
		sendSearch();
	}

	return{
		start:start
	}
}();

$(function(){
	Search.start();
});