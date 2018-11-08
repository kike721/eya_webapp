import base from './base/base';
import popupDetail from './products/popup_detail';
import productCarousel from './owl-carousel/products-carousel';

import toggle from './users/toggle';

import owl from './plugins/owl.carousel.min.js';

base();
productCarousel();
popupDetail();

toggle();

owl();