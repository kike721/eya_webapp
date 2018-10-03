var popUpDetail = function(){
	
	function closePopup(e){
		$('body').css('overflow', 'visible');
		$("#popupDetail").css('display', 'none');
	}

	function openDetail(e) {
		e.preventDefault();
		var btn = $(this);
		var parent = btn.parent('.card');
		var text = parent.find('#code_eyamex').clone();
		var desc = parent.find('#description__eyamex').clone();
		var img = parent.find('#image_eyamex').attr('style');

		$('body').css('overflow', 'hidden');
		$("#popupDetail").css('display', 'flex');

		$("#code").html(text);
		$("#description").html(desc);
		$("#image").attr("style", img);
	}	

	function start(){
		$(".btnId").on('click', openDetail);
		$(".closeDetail").on('click', closePopup);
	}

	return{
		start:start
	};

}();

$(function(){
	popUpDetail.start();
});


