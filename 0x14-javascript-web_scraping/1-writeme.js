#!/usr/bin/node
// reads file passed as arg.
const fs = require('fs');

fs.appendFile(process.argv[2], process.argv[3], function (err) {
  if (err) {
    console.log(err);
  }
});
