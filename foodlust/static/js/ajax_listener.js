// json_data = json.dumps({'new_rating': '78'})
// HTTPRsponse(json_data, content_type='application/json')

$('.liked').on('click', function(e) {
  e.preventDefault();
  var id = e.target.href.split('meals')[1].split('/')[1];
  $.get('http://localhost:8000/meals/' + id + '/liked').done(function(data){
    $('.rating span.'+id).html(data)

  })
})

$('.disliked').on('click', function(e) {
  e.preventDefault();
  var id = e.target.href.split('meals')[1].split('/')[1];
  $.get('http://localhost:8000/meals/' + id + '/disliked').done(function(data) {
      $('.rating span.'+id).html(data)

  })
})
