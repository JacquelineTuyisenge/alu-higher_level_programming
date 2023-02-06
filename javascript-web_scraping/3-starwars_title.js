#!/usr/bin/node
const req = require('request');
const URL = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;
req.get(URL, (err, res) => {
  err ? console.log(err) : console.log(JSON.parse(res.body).title);
});
