$(document).ready(function(){
  $('.selector').on('click', '.liked-blue', function(e) {
    e.preventDefault();
    var liked = $(e.target)
    var disliked = liked.parent().find('a.disliked-gray');
    var href = e.target.href;
    if (href) {
      var id = e.target.href.split('meals')[1].split('/')[1];
      $.get('/meals/' + id + '/liked').done(function(data){
        liked.removeAttr('href');
        liked.addClass('liked-gray');
        liked.removeClass('liked-blue');
        liked.css('color', 'gray');
        disliked.attr('href', ("/meals/" + id + "/disliked"));
        disliked.removeAttr('style');
        disliked.addClass('disliked-blue');
        disliked.removeClass('disliked-gray');
        $('.rating span.'+id).html(data);
      });
    }
  });

  $('.selector').on('click', '.disliked-blue', function(e) {
    e.preventDefault();
    var href = e.target.href;
    var disliked = $(e.target)
    var liked = disliked.parent().find('a.liked-gray')
    if (href) {
      var id = e.target.href.split('meals')[1].split('/')[1];
      $.get('/meals/' + id + '/disliked').done(function(data) {
        disliked.removeAttr('href');
        disliked.addClass('disliked-gray');
        disliked.removeClass('disliked-blue');
        disliked.css('color', 'gray');
        liked.attr('href', ("/meals/" + id + "/disliked"));
        liked.removeAttr('style');
        liked.addClass('liked-blue');
        liked.removeClass('liked-gray');
        $('.rating span.'+id).html(data);

      });
    }
  });
});
