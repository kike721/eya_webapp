var ToggleRow = function(){

  function toggleStatus(e){
    e.preventDefault();
    var button = $(e.target);
    var parent = button.parent('.toggleRow');
    parent.toggleClass('active');
  }

  function start(){
    $('.toggleBtn').on('click', toggleStatus);
  }


  return{
    start:start
  }
}();

$(function(){
  ToggleRow.start();
});