var productsCarousel = function(){

	function start(){

		var $carousel = $(this);
		var items = $carousel.data("items");
		var options = {};
			options.autoWidth = false;
			options.nav = false;
			options.margin = 10;
			options.loop = false;
			options.rtl = false;

			if(typeof items !== "undefined"){
				options.items = items;
			}

			options.responsive = {};
			options.responsive[0] = {};
			options.responsive[600] = {};
			options.responsive[1000] = {};

			options.responsive[0].items = 1;
			options.responsive[600].items = 3;
			options.responsive[1000].items = 4;
			
			$('.productsCarousel').owlCarousel(options);
	}

	return{
		start:start
	};

}();

$(function(){
	productsCarousel.start();
});
