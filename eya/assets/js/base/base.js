var OpenSearch = function() {
	
	function open(e){
		e.preventDefault();
		$('#popupSearch').addClass('active');
		$('body').css('overflow', 'hidden');
	}

	function close(e){
		e.preventDefault();
		$('#popupSearch').removeClass('active');
		$('body').css('overflow', 'visible');
	}

	function start(){
		$('.openSearch').on('click', open);
		$('.closeSearch').on('click', close);
	}
	return{
		open:open,
		close:close,
		start:start
	};
}();

var IsMobile = function() {
	function checkMobile(){
		if(/Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent)) {
			return true;
		}
		else {
			return false;
		}
	}
	function start(){
		if(!checkMobile()){
			$('body').addClass('desktop');
		}
	}
	return{
		checkMobile:checkMobile,
		start:start
	};
}();

$(function(){
	OpenSearch.start();
	IsMobile.start();
});
