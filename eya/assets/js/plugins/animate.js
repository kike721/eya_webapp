var AnimatedBlock = function(){
    var scrollPosition;
    var blocks;
    var windowHeight;


    function turnOnBlocks(e){
        scrollPosition = $(this).scrollTop();

        blocks.each(function(){
            var offsetValues = $(this).offset();

            if( scrollPosition >= (offsetValues.top - windowHeight) ) {
                $(this).addClass("active");

            }
        });

        blocks = $(".animatedBlock:not(.active)");
        if(!blocks.length){
            $(window).off('scroll', turnOnBlocks);
        }
    }

    function start(){
        blocks = $(".animatedBlock:not(.active)");
        windowHeight = $(window).height() - 50;
        turnOnBlocks(null);
        $(window).on('scroll', turnOnBlocks);
    }
    
    return{
        start:start
    }
}();

$(function(){
    AnimatedBlock.start();
});