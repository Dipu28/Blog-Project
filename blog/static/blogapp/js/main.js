$(document).ready(function(){
    // Owl-crousel for blog
    $('.owl-carousel').owlCarousel({
        loop:true,
        autoplay:true,
        autoplayTimeout:4000,
        dots:false,
        nav:true,
        navText:[$('.owl-navigation.owl-nav-prev'),$('.owl-navigation.owl-nav-next')]
    });

});