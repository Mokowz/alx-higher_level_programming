#!/usr/bin/node
const request = require('request');

const url = 'http://swapi.co/api/films/';
let id = parseInt(process.argv[2], 10);

let charList = [];

request(url, function (err, response, body) {
  if (err == null) {
    const films = JSON.parse(body);
    const results = films.results;
    if (id < 4) {
      id += 3;
    } else {
      id -= 3;
    }
    for (let i = 0; i < results.length; i++) {
      if (results[i].episode_id === id) {
        charList = results[i].characters;
        break;
      }
    }
    for (let j = 0; j < charList.length; j++) {
      request(charList[j], function (err, response, body) {
        if (err == null) {
          console.log(JSON.parse(body).name);
        }
      });
    }
  }
});
