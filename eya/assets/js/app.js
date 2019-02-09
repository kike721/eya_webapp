import base from './base/base';
import sendOrder from './forms/sendOrder';
import search from './forms/search';
import popupDetail from './products/popup_detail';
import productCarousel from './owl-carousel/products-carousel';

import toggle from './users/toggle';

import owl from './plugins/owl.carousel.min.js';

base();
sendOrder();
search();
productCarousel();
popupDetail();

toggle();

owl();