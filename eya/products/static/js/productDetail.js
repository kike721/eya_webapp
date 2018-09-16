var popUpDetail = function(){
	
	function closePopup(e){
		$('body').css('overflow', 'visible');
		$("#popupDetail").removeClass('active');
	}

	function openDetail() {
		$(".btnId").click(function (e) {
			$("#code").text(data.code_eyamex);
			$("#description").text(data.description);
			$("#image").attr('src',data.image);
		
			$('body').css('overflow', 'hidden');
			$("#popupDetail").css('display', 'block');
		});
	}	

	function start(){
		openDetail();
		$(".closeDetail").on('click', closePopup);
	}

	return{
		start:start
	};

}();

$(function(){
	popUpDetail.start();
});
