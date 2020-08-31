const responsive={
    0:{
        items:1
    },
    320:{
        items:1
    },
    560:{
        items:2
    },
    960:{
        items:3
    }
}

$(document).ready(function(){
    // Owl-crousel for blog
    $('.owl-carousel').owlCarousel({
        loop:true,
        autoplay:true,
        autoplayTimeout:4000,
        dots:true,
        // nav:true,
        // navText:[$('.owl-navigation.owl-nav-prev'),$('.owl-navigation.owl-nav-next')]
        responsive:responsive
    });
    
    // Click to scroll top
    $('.move-up.my').click(function(){
        $('html,body').animate({
            scrollTop:0
        },1);
    });
    // $(window).scroll(function(){
    //     if ($(window).scrollTop()>0){
    //         $('.dipu')
    //     }
    // })
});



