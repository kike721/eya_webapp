var popUpDetail = function(){
	
	function closePopup(e){
		$('body').css('overflow', 'visible');
		$("#popupDetail").css('display', 'none');
	}

	function openDetail(e) {
		e.preventDefault();
		var btn = $(this);
		var text = btn.find('#code_eyamex').clone();
		var desc = btn.find('#description__eyamex').clone();

		var img = btn.find('#image_eyamex').attr('style');
		console.log(img)

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


