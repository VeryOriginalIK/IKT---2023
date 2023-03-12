window.addEventListener('scroll', function() {
    var scrollPosition = window.pageYOffset || document.documentElement.scrollTop || document.body.scrollTop || 0;
    if (scrollPosition > 10) {
      document.getElementById('back-to-top-btn').classList.add('show');
    } else {
      document.getElementById('back-to-top-btn').classList.remove('show');
    }
  });
  
  document.getElementById('back-to-top-btn').addEventListener('click', function() {
    window.scrollTo({
      top: 0,
      behavior: 'smooth'
    });
  });
  