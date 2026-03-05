var OwlMixin = {
    initOwlCarousel: function (
        cls,
        margin,
        responsive,
        loop,
        items,
        dots,
        nav,
        navText,
        carouselInterval,
        mouseDrag,
        touchDrag,
        pullDrag,
        center,
        autoplay,
        rewind
    ) {
        var owl_rtl = false;
        if ($("#wrapwrap").hasClass("o_rtl")) {
            owl_rtl = true;
        }
        var margin = margin ? margin : 10;
        var owlCarousel = cls ? $(cls) : $(".owl-carousel");
        owlCarousel.owlCarousel({
            loop,
            margin,
            lazyLoad: true,
            nav,
            navText,
            autoplay,
            center,
            dots,
            rtl: owl_rtl,
            items,
            rewind,
            autoplayHoverPause: true,
            autoplayTimeout: carouselInterval,
            mouseDrag,
            touchDrag,
            pullDrag,
            responsive,
        });
    },
};
export default OwlMixin;
