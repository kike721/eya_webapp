var Loader = function(){
  var loader;
  var overflow;
  function show(container){
    var cont = container ? container : $('body');
    overflow = container ? false : true;

    loader = $('#loader .loader').clone();
    loader.addClass('active');

    if(overflow){
      $('body, html').css('overflow', 'hidden');
    } else{
      loader.addClass('absolute');
    }

    cont.append(loader);
  }

  function hide(){
    loader.remove();
    if(overflow) $('body, html').css('overflow', 'visible');
  }
  
  return{
    show:show,
    hide:hide
  }
}();