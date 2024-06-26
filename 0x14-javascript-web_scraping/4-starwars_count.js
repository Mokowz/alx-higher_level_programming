#!/usr/bin/node
const request = require('request');

//  first argument is the API URL
const URL = process.argv[2];

request(URL, (error, response, body) => {
  if (error) {
    console.log(error);
  } else if (body) {
    const json = JSON.parse(body);
    const films = json.results.filter(
      x => x.characters.find(y => y.match(/\/people\/18\/?$/))
    );
    console.log(films.length);
  }
});
