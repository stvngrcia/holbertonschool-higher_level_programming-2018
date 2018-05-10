$(function () {
  let url = 'https://swapi.co/api/films/?format=json';
  let listMovies = $('#list_movies');
  $.get(url, function (data, status) {
    let results = data['results'];
    $.each(results, function (i, result) {
      listMovies.append('<li>' + result['title'] + '</li>');
    });
  });
});
