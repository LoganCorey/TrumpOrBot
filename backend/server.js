const express = require('express');
const bodyParser = require('body-parser')
const path = require('path');
const app = express();
const spawn = require('child_process').spawn;

app.use(express.static(path.join(__dirname, 'build')));

app.get('/ping', function (req, res) {
 return res.send('pong');
});

app.get('/', function (req, res) {
  res.sendFile(path.join(__dirname, 'build', 'index.html'));
});

/**
 * Generates a 'tweet' and sends it back as a resposne
 */
app.get('/getMessage', function (req, res) {
  const ls = spawn('pipenv run python', ['./TrumpOrBotPython/main.py'])
  ls.stdout.on.on('data', (data) =>{
    return res.send(data);
  });

  ls.stderr.on('data', (data) =>{
    return res.send(data);
  });

  ls.on('close', (code) =>{
    console.log(`child process excited with code ${code}`);
  })
  
});

app.listen(process.env.PORT || 8080);