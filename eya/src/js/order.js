var ContactForm = function(){
	function sendForm() {
		$(".btnContact").click(function (e) {
			e.preventDefault();
			var btnSend = $(this);
			if(!btnSend.hasClass('disable')){
				var forma = validarForma($(this));
				var formCont = $(this).closest("form");
				if(forma){
					var loader = $("#loader").find(".loader").clone();
					formCont.append(loader);
					loader = formCont.find(".loader");
					var parent = formCont.parent();
					var formMessage = parent.find(".backResponse");
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
                                //popup éxito
                                $('#popupContactSuccess').addClass('active');
                                $('body').css('overflow', 'hidden');
                            }
                            else{
                                //popup error
                                $('#popupError').addClass('active');
                                $('body').css('overflow', 'hidden');
                            }
						}
					})
					.fail(function (jqXHR,textStatus,errorTrhown){
						console.log(jqXHR.status);
						console.log(errorTrhown);
					})
					.always(function (){
						clearForm(formCont);
						loader.remove();
					});

				}
			}
		});
	}

	function clearForm(form){
		form.find('input[type="text"],input[type="email"],textarea').each(function(){
			$(this).val('');
		});
	}

	function start(){
		sendForm();
	}
	return{
		start:start,
		clearForm:clearForm
	}
}();

$(function(){
	ContactForm.start();
});