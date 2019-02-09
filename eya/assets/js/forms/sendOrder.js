var senOrder = function(){

	function send() {
		$(".btn").click(function (e) {
			e.preventDefault();
			var btnSend = $(this);
			if(!btnSend.hasClass('disable')){
				var formCont = $(this).closest("form");				
				var loader = $("#loader").find(".loader").clone();
				formCont.append(loader);
				loader = formCont.find(".loader");
				btnSend.addClass('disable');

				$.ajax({
					type:'POST',
					url: formCont.attr("action"),
					data: formCont.serialize(),
					headers:{
						'X-CSRFToken':$("[name='csrfmiddlewaretoken']").val()
					}
				})
				.done(function(data,textStatus,jqXHR){
					if(jqXHR.status==200){
						if(data.success){
							console.log(data.success);
                        }
                        else{
                            //popup error
                            $('#popupNotification').addClass('active');
                            $('body').css('overflow', 'hidden');
                        }
					}
				})
				.fail(function (jqXHR,textStatus,errorTrhown){
					console.log(jqXHR.status);
					console.log(errorTrhown);
				})
				.always(function (){
					loader.remove();
				});
			}
		});
	}

	function closePopup(e){
		$('body').css('overflow', 'visible');
		$("#popupNotification").removeClass('active');
	}

	function start(){
		send();
		$(".closeNotification").on('click', closePopup);
	}
	return{
		start:start,
	}
}();

$(function(){
	senOrder.start();
});