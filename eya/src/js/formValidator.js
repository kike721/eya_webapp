
/* -- js para validar que no haya campos mal llenados en alguna forma --  */

function validarForma(element,single){
	single = typeof single !== 'undefined' ? single : false;
	var elem = $(element);
	var form;
	if(!single){
		form = elem.closest("form");
	}
	else{
		form = $(element);
	}

	var error=false;

	function addError(element){
		var parent = element.closest('.input');
		if(!element.hasClass("error")){
			element.addClass("error");
			parent.addClass("error");
		}
		error=true;
	}

	function removeError(element){
		var parent = element.closest('.input');
		element.removeClass("error");
		parent.removeClass("error");
	}
	form.find('input').removeClass("error");
	form.find('.input').removeClass("error");

	//Input text & email
	form.find('input[type="text"]:not(.form-no-obligatorio),input[type="email"]:not(.form-no-obligatorio),input[type="tel"]:not(.form-no-obligatorio),input[type="number"]:not(.form-no-obligatorio)').each(function(){
		if(!$(this).val().length>0 && !$(this).hasClass("form-email")){
			addError($(this));
		}
		else if ($(this).hasClass("form-email")){
			var mailRegex = /^([A-Za-z0-9_\-\.])+\@([A-Za-z0-9_\-\.])+\.([A-Za-z]{2,4})$/;
			if(!mailRegex.test($(this).val())){
				addError($(this));
			}
			else{
				removeError($(this));
			}
		}
		else{
			removeError($(this));
		}
	});

	//Textarea
	form.find('textarea:not(.form-no-obligatorio)').each(function(){
		if(!$(this).val().length>0){
			addError($(this));
		}
		else{
			removeError($(this));
		}
	});

	// Campos con longitud específica
	form.find(".form-minMax:not(.form-no-obligatorio)").each(function(){
		var $this = $(this);
		var actual = $this.val().length;
		var ext = parseInt($this.attr("maxlength"));
		if(actual != ext){
			addError($(this));
		}
	});

	//Input password
	form.find('input[type="password"]').each(function(){
		if(!$(this).val().length>0){
			addError($(this));
		}
		else if(!$(this).hasClass('form-no-secure')){
			var passRegex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{7,}.+$/; //verificar si el pasword tiene, letras mayúsculas y minpusculas y más de 7 caracteres
			if(!passRegex.test($(this).val())){
				error = true;
				addError($(this));
			}
			else{
				removeError($(this));
			}
		}
	});

	// Campos que se comparan
	form.find('.form-comparar:not(.error)').each(function(){
		var id2 = $(this).data("comparar");
		if(!$(this).hasClass("form-no-obligatorio")){
			if($(this).val() != $("#"+id2).val() || !$(this).val().length > 0){
				addError($(this));
				addError($("#" + id2));
			}
			else{
				if($(this).val() == $("#"+id2).val()){
					removeError($(this));
					removeError($("#" + id2));
				}
			}
		}
		else{
			if($(this).hasClass("form-validar-no-vacio")){
				if($(this).val().length > 0){
					if($(this).val() != $("#"+id2).val() || !$(this).val().length>0){
						addError($(this));
						addError($("#" + id2));
					}
				}
			}
		}
	});

	// Campos con longitud mínima
	form.find(".form-min").each(function(){
		var $this = $(this);
		var actual = $this.val().length;
		var ext = parseInt($this.data("length"));
		if(!$(this).hasClass("form-no-obligatorio")){
			if(actual < ext){
				addError($(this));
			}
		}
		else{
			if($(this).hasClass("form-validar-no-vacio")){
				if(actual > 0){
					if(actual < ext){
						addError($(this));
					}
				}
			}
		}
	});

	// Campos siempre inválidos
	form.find('.form-always-invalid').each(function(){
		addError($(this));
	});

	// Un checkbox obligatorio
	form.find('input[type="checkbox"]').each(function(){
		if($(this).hasClass('form-obligatorio')){
			var label = 'label[for=' + $(this).attr('id') +']';
			if($(this).is(':checked')){
				removeError($(label));
			}
			else{
				addError($(label));
			}
		}
	});

	// Conjunto de checkbox con al menos uno seleccionado
	form.find('.form-check-obligatorio').each(function(){
		var $this = $(this);
		var isValid = false;
		$this.find('input[type="checkbox"]').each(function(){
			if($(this).is(':checked')){
				isValid=true;
			}
		});
		if(!isValid){
			addError($this);
		}
		else{
			removeError($this);
		}
	});


	return !error;
}

//RESTRINGIR CAMPOS DE TEXTO A SÓLO NÚMEROS
function soloNumeros(){
	var inputs = $(".form-solo-numeros");
	if(inputs.length > 0){
		inputs.keypress(function (e) {
			if (e.which != 8 && e.which != 0 && (e.which < 46 || e.which > 57)) {
				return false;
			}
		});
	}
}

//VALIDAR TARJETAS
function creditCards(){
	var checkPayment = false;
	if($('.cc-number').length > 0){
		checkPayment = true;
		$('.cc-number').payment('formatCardNumber');
	}
	if(checkPayment){
		//amex 378645128306814
		//visa 4716953786621380
		//mc 5507281219738120

		var cardType = $.payment.cardType($('.cc-number').val());


		//NÚMERO DE TARJETA
		$(".tarjeta-icon").removeClass("active");
		if(cardType=="amex"){
			$(".icon-amex").addClass("active");
			$("#input-amex").prop('checked', true);
		}else if(cardType=="mastercard"){
			$(".icon-mastercard").addClass("active");
			$("#input-mastercard").prop('checked', true);
		}else if(cardType=="visa"){
			$(".icon-visa").addClass("active");
			$("#input-visa").prop('checked', true);
		}else{
			turnOffCards();
		}

		//CVC

		if($.payment.validateCardCVC($('.cc-cvc').val(), cardType)){
			$('.cc-cvc').removeClass("error");
		}else{
			$('.cc-cvc').addClass("error");
		}

		//FECHA EXPIRACIÓN
		if($.payment.validateCardExpiry($('.cc-exp').payment('cardExpiryVal'))){
			$('.cc-exp').removeClass("error");
		}else{
			$('.cc-exp').addClass("error");
		}
	}
}
function turnOffCards(){
	$(".tarjeta-icon").removeClass("active");
	$("#input-amex").prop('checked', false);
	$("#input-mastercard").prop('checked', false);
	$("#input-visa").prop('checked', false);
}
