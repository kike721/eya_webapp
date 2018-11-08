var Header = function(){
  function scrollHeader(){
    var $header = $("#header");
    var $menu = $("#menu");
    var $popupsMenu = $("#popupsMenu");
    var safeTop = 110;

    $(window).scroll(function (e) {
      if ($(this).scrollTop() > safeTop){
        $header.addClass("scroll");
        $menu.addClass("scroll");
        $popupsMenu.addClass("scroll");
      }
      else{
        $header.removeClass("scroll");
        $menu.removeClass("scroll");
        $popupsMenu.removeClass("scroll");
      }
    });
  }
  
  function start(){
    scrollHeader();
  }
  
  return{
    start:start
  }
}();

$(function(){
  Header.start();
});