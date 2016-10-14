$('.selector').on('click', '.liked-blue', function(e) {
  e.preventDefault();
  var id = e.target.href.split('meals')[1].split('/')[1];
  $.get('/meals/' + id + '/liked').done(function(data){
    $('.liked-blue').removeAttr('href');
    $('.liked-blue').addClass('liked-gray');
    $('.liked-blue').removeClass('liked-blue');
    $('.liked-gray').css('color', 'gray');
    $('.disliked-gray').attr('href', ("/meals/" + id + "/disliked"));
    $('.disliked-gray').removeAttr('style');
    $('.disliked-gray').addClass('unliked-blue');
    $('.disliked-gray').removeClass('unliked-gray');
    $('.rating span.'+id).html(data);
  })
})

$('.selector').on('click', '.disliked-gray', function(e) {
  e.preventDefault();
  var id = e.target.href.split('meals')[1].split('/')[1];
  $.get('/meals/' + id + '/disliked').done(function(data) {
        $('.disliked-blue').removeAttr('href');
        $('.disliked-blue').addClass('liked-gray');
        $('.disliked-blue').removeClass('liked-blue');
        $('.disliked-gray').css('color', 'gray');
        $('.liked-gray').attr('href', ("/meals/" + id + "/disliked"));
        $('.liked-gray').removeAttr('style');
        $('.liked-gray').addClass('unliked-blue');
        $('.liked-gray').removeClass('unliked-gray');
        $('.rating span.'+id).html(data);

  })
})
