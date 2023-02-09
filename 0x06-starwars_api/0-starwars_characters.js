#!/usr/bin/node

const request = require('request');

const id = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/';
request(url + id, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    JSON.parse(body).characters.forEach((people) => {
      request(people, (err, res, body) => {
        if (err) {
          console.log(err);
        } else {
          console.log(JSON.parse(body).name);
        }
      });
    });
  }
});
