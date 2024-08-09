#!/usr/bin/node
const request = require('request');

function fetchCharacter (urls) {
  if (urls.length === 0) return;
  request.get(urls[0], (_error, _response, body) => {
    console.log(JSON.parse(body).name);
    fetchCharacter(urls.slice(1));
  });
}

request.get(
  'https://swapi-api.alx-tools.com/api/films/' + process.argv[2],
  (_error, _response, body) => {
    const characters = JSON.parse(body).characters;
    fetchCharacter(characters);
  }
);
