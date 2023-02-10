#!/usr/bin/node
$('DIV#add_item').click(function () {
  $('UL.my_list').addTag('<li>Item</li>');
});
