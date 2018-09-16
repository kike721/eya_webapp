var popUpDetail = function(){
	
	function closePopup(e){
		$('body').css('overflow', 'visible');
		$("#popupDetail").css('display', 'none');
	}

	function openDetail() {
		$(".btnId").click(function(e) {
			document.getElementById("code").innerText = "{{ item.code_eyamex }}";
			document.getElementById("description").innerHTML = "{{ item.description }}";
			document.getElementById("image").innerHTML = "{{ item.image }}";

			$('body').css('overflow', 'hidden');
			$("#popupDetail").css('display', 'flex');
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
