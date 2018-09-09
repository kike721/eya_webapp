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
  
	function addError(element, input){
    input = typeof input !== 'undefined' ?  input : true;
    if(input){
      var parent = element.closest('.input');
    }
    else{
      var parent = element.closest('label');
    }
    
    element.addClass("error");
    parent.addClass("error");
    parent.find('input').addClass("error");

	  error=true;
	}
  
	function removeError(element, input){
    input = typeof input !== 'undefined' ?  input : true;
    if(input){
      var parent = element.closest('.input');
    }
    else{
      var parent = element.closest('label');
    }

    element.removeClass("error");
    parent.removeClass("error");
    parent.find('input').removeClass("error");
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
  
	// Select obligatorio
	form.find('.form-select-obligatorio').each(function(){
	  var $this = $(this);
	  if($this[0].value === null || $this[0].value === 'null'){
		  addError($(this));
	  }
	  else{
		  removeError($this);
	  }
	});
  
	// File obligatorio
	form.find('.form-file-obligatorio').each(function(){
		var $this = $(this);
	  if($this[0].files.length){
			removeError($this, false);
	  }
	  else{
			addError($this, false);
	  }
	});
  
	// numéricos con valor mínimo y máximo
	form.find('.form-min-max-value').each(function(){
	  var $this = $(this);
	  if(!$(this).val().length>0){
		addError($(this));
	  }
	  else {
		var min = parseInt($this.data('min'));
		var max = parseInt($this.data('max'));
		var value = parseInt($this.val());
		if(value >= min && value <= max){
		  removeError($this);
		}
		else{
		  addError($this);
		}
	  }
	});
  
	return !error;
  }
  
  //RESTRINGIR CAMPOS DE TEXTO A SÓLO NÚMEROS
  function soloNumeros(){
	var inputs = $(".form-solo-numeros");
	if(inputs.length > 0){
	  inputs.keypress(function (e) {
		if (e.which != 8 && e.which != 0 && (e.which < 48 || e.which > 57)) {
		  return false;
		}
	  });
	}
  }