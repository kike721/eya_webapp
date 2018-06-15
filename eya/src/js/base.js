var Header = function(){
	function scrollHeader(){
		var $header = $("#header");
		var $phone = $("#phone");
		var $popupsMenu = $("#popupsMenu");
		var safeTop = 110;
		var scrollBefore = 0;

		$(window).scroll(function (e) {
			if(scrollBefore > $(this).scrollTop()){
				$header.addClass("scroll-reverse");
				$phone.addClass("scroll-reverse");
				$popupsMenu.addClass("scroll-reverse");
			}
			else{
				$header.removeClass("scroll-reverse");
				$phone.removeClass("scroll-reverse");
				$popupsMenu.removeClass("scroll-reverse");
			}
			if ($(this).scrollTop() > safeTop){
				$header.addClass("scroll");
				$popupsMenu.addClass("scroll");
				$phone.addClass("scroll");
				$phone.removeClass("active");
			}
			else{
				$header.removeClass("scroll");
				$header.removeClass("scroll-reverse");
				$phone.removeClass("scroll");
				$phone.removeClass("scroll-reverse");
				$popupsMenu.removeClass("scroll");
				$popupsMenu.removeClass("scroll-reverse");
			}
			scrollBefore = $(this).scrollTop();
		});
	}
	
	function start(){
		scrollHeader();
	}
	
	return{
		start:start
	}
}();

var Menu = function(){
	function toggleMenu(event) {
		typeof event !== 'undefined' && event.preventDefault();
		if( $('#menu').hasClass('open') ) {
			closeMenu();
		}
		else {
			openMenu();
		}
	}

	function openMenu() {
		$('body').css('overflow', 'hidden');
		$('#menu').addClass('open');
		$('#header').addClass('open');
	}

	function closeMenu() {
		$('#menu').removeClass('open');
		$('#header').removeClass('open');
		$('body').css('overflow', 'visible');
	}

	function start(){
		$('.toggleMenu').on('click', toggleMenu);
	}
	return{
		toggleMenu:toggleMenu,
		start:start
	};

}();

var TogglePhone = function(){

	function toggleActive(event) {
		typeof event !== 'undefined' && event.preventDefault();
		$('.phone').toggleClass('active');
	}

	function start(){
		$('.togglePhone').on('click', toggleActive);
	}

	return{
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

var OpenLogin = function() {
	
	function open(e){
		e.preventDefault();
		$('#popupLogin').addClass('active');
		$('#popupPasswordRecover').removeClass('active');
		$('body').css('overflow', 'hidden');
	}

	function close(e){
		e.preventDefault();
		$('#popupLogin').removeClass('active');
		$('body').css('overflow', 'visible');
	}

	function openPassword(){
		$('#popupLogin').removeClass('active');
		$('#popupPasswordRecover').addClass('active');
		$('body').css('overflow', 'visible');
	}

	function closePassword(){
		$('#popupPasswordRecover').removeClass('active');
		$('body').css('overflow', 'visible');
	}

	function start(){
		$('.openLogin').on('click', open);
		$('.closeLogin').on('click', close);
		$('.openPasswordRecover').on('click', openPassword);
		$('.closeRecover').on('click', closePassword);
	}
	return{
		open:open,
		close:close,
		openPassword:openPassword,
		start:start
	};
}();

$(function(){
	IsMobile.start();
	Menu.start();
	TogglePhone.start();
	Header.start();
	OpenLogin.start();
});
