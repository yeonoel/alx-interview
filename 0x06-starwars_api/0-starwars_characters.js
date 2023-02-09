#!/usr/bin/node

const request = require('request');

const id = process.argv[2];
// let test = 0;
const url = 'https://swapi-api.alx-tools.com/api/films/' + id;
request(url, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }
  if (response.statusCode === 200) {
    const itemCharacters = JSON.parse(body).characters;
    printName(0, itemCharacters[0], itemCharacters);
  }
});

function printName (index, url, characters) {
  if (characters.length === index) {
    return;
  }
  request(url, (err, res, body) => {
    if (err) {
      console.log(err);
    }
    console.log(JSON.parse(body).name);
    index++;
    printName(index, characters[index], characters);
  });
}
