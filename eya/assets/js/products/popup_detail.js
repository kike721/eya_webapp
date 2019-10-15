var popUpDetail = function(){
	
	function closePopup(e){
		$('body').css('overflow', 'visible');
		$("#popupDetail").css('display', 'none');
	}

	function openDetail(e) {
		e.preventDefault();
		var btn = $(this);
		var parent = btn.parent('.detail-product__product');
		var text = parent.find('#code_eyamex').clone();
		var desc = parent.find('#description__eyamex').clone();
		var id_product = parent.find('#id_product').val();
		var img = parent.find('#image_eyamex').attr('src');

		$('body').css('overflow', 'hidden');
		$("#popupDetail").css('display', 'flex');

		$("#code").html(text);
		$("#description").html(desc);
		$("#popup_id_product").val(id_product);
		$("#image").attr("src", img);
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


