(function ($) {
    "use strict";

    // Spinner
    var spinner = function () {
        setTimeout(function () {
            if ($('#spinner').length > 0) {
                $('#spinner').removeClass('show');
            }
        }, 1);
    };
    spinner();
    
    
    // Initiate the wowjs
    new WOW().init();


    // Sticky Navbar
    $(window).scroll(function () {
        if ($(this).scrollTop() > 300) {
            $('.sticky-top').addClass('shadow-sm').css('top', '0px');
        } else {
            $('.sticky-top').removeClass('shadow-sm').css('top', '-100px');
        }
    });
    
    
    // Back to top button
    $(window).scroll(function () {
        if ($(this).scrollTop() > 300) {
            $('.back-to-top').fadeIn('slow');
        } else {
            $('.back-to-top').fadeOut('slow');
        }
    });
    $('.back-to-top').click(function () {
        $('html, body').animate({scrollTop: 0}, 1500, 'easeInOutExpo');
        return false;
    });


    // Facts counter
    $('[data-toggle="counter-up"]').counterUp({
        delay: 10,
        time: 2000
    });


    // Header carousel
    $(".header-carousel").owlCarousel({
        autoplay: true,
        smartSpeed: 1500,
        loop: true,
        nav: false,
        dots: true,
        items: 1,
        dotsData: true,
    });


    // Testimonials carousel
    $(".testimonial-carousel").owlCarousel({
        autoplay: true,
        smartSpeed: 1000,
        center: true,
        dots: false,
        loop: true,
        nav : true,
        navText : [
            '<i class="bi bi-arrow-left"></i>',
            '<i class="bi bi-arrow-right"></i>'
        ],
        responsive: {
            0:{
                items:1
            },
            768:{
                items:2
            }
        }
    });


    // Portfolio isotope and filter
    var portfolioIsotope = $('.portfolio-container').isotope({
        itemSelector: '.portfolio-item',
        layoutMode: 'fitRows'
    });
    $('#portfolio-flters li').on('click', function () {
        $("#portfolio-flters li").removeClass('active');
        $(this).addClass('active');

        portfolioIsotope.isotope({filter: $(this).data('filter')});
    });
    
})(jQuery);


// Force refresh when user returns via back button
window.addEventListener("pageshow", function (event) {
    if (event.persisted || (window.performance && window.performance.navigation.type === 2)) {
      window.location.reload();
    }
  });

  
  // JSON Form Submission Script
  document.getElementById("contact-form").addEventListener("submit", async function(e) {
    e.preventDefault();

    const form = e.target;
    const formData = new FormData(form);

    try {
      const response = await fetch("send-mail.php", {
        method: "POST",
        body: formData
      });

      const result = await response.text();

      if (response.ok) {
        // Show success message
        document.getElementById("form-success").innerText = result;
        document.getElementById("form-success").classList.remove("d-none");
        form.reset();
      } else {
        // Show error message from PHP
        alert("Error: " + result);
      }
    } catch (error) {
      alert("⚠️ Network error. Please try again later.");
    }
  });

  // Refresh the page if user returns via back button
  window.addEventListener("pageshow", function (event) {
    if (event.persisted || (window.performance && window.performance.navigation.type === 2)) {
      window.location.reload();
    }
  });

