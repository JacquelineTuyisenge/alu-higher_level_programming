#!/usr/bin/node
$('document').ready(function () {
    const URL = 'https://www.fourtonfish.com/hellosalut/?';
    $('input#btn_translate').click(function () {
      $.get(URL + $.param({ lang: $('input#language_code').val() }), function (data) {
        $('div#hello').html(data.hello);
      });
    });
  });
