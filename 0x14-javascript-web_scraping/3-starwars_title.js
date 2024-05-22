#!/usr/bin/node
const request = require('request');

const url = 'https://swapi-api.alx-tools.com/api/films';
const id = process.argv[2];

request(`${url}/${id}/`, (error, response, body) => {
  if (error) {
    console.log(error);
  }
  const film = JSON.parse(body);
  console.log(film.title);
});
