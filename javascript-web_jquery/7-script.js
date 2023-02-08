#!/usr/bin/node
$.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', function(data) {
  $('UL#list_movies').text(data.name);
});
