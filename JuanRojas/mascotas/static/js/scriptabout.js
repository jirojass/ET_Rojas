//on page load
$(document).ready(function(){
function fadeInSlideOnScroll() {
    var elements = document.querySelectorAll('.fade-in-slide');
  
    function fadeIn(element) {
      element.style.opacity = 1;
      element.style.transform = 'translateY(0)';
    }
  
    function isElementInViewport(el) {
      var rect = el.getBoundingClientRect();
      return (
        rect.top >= 0 &&
        rect.left >= 0 &&
        rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
        rect.right <= (window.innerWidth || document.documentElement.clientWidth)
      );
    }
  
    function handleScroll() {
      for (var i = 0; i < elements.length; i++) {
        var element = elements[i];
        if (isElementInViewport(element)) {
          if (!element.classList.contains('fade-in-slide-active')) {
            element.classList.add('fade-in-slide-active');
            fadeIn(element);
          }
        }
      }
    }
  
    window.addEventListener('scroll', handleScroll);
    handleScroll(); // Check on page load
  }
  
  fadeInSlideOnScroll();
  
  });