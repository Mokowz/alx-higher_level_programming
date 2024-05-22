#!/usr/bin/node
const request = require('request');

const url = 'https://swapi-api.alx-tools.com/api/films';
const id = process.argv[2];

request(`${url}/${id}/`, (err, response, body) => {
  if (err) {
    console.log(err);
  }

  const film = JSON.parse(body);
  const characters = film.characters;

  characters.forEach(character => {
    request(character, (err, response, body) => {
      if (err) {
        console.log(err);
      }

      const char = JSON.parse(body);
      console.log(char.name);
    });
  });
});
