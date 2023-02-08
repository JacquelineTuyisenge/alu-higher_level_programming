#!/usr/bin/node
$('document').ready(function () {
    $('input#btn_translate').click(translate);
    $('input#language_code').focus(function () {
      $(this).keydown(function (e) {
        if (e.keyCode === 13) {
          translate();
        }
      });
    });
  });
  
  function translate () {
    const url = 'https://www.fourtonfish.com/hellosalut/?';
    $.get(url + $.param({ lang: $('input#language_code').val() }), function (data) {
      $('div#hello').html(data.hello);
    });
  }
