var Menu = function(){
  function toggleMenu(event) {
    if( $('#menu').hasClass('open') ) {
      closeMenu();
    }
    else {
      openMenu();
    }
  }

  function openMenu() {
    $('body, html').css('overflow', 'hidden');
    $('#menu').addClass('open');
  }

  function closeMenu() {
    $('#menu').removeClass('open');
    $('body, html').css('overflow', 'visible');
  }

  function start(){
    $('.toggleMenu').on('click', toggleMenu);
  }
  
  return {
    start:start
  };

}();

$(function(){
  Menu.start();
});