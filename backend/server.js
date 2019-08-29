const express = require('express');
const bodyParser = require('body-parser')
const path = require('path');
const app = express();
app.use(express.static(path.join(__dirname, 'build')));

app.get('/ping', function (req, res) {
 return res.send('pong');
});

app.get('/', function (req, res) {
  res.sendFile(path.join(__dirname, 'build', 'index.html'));
});

app.get('/getMessage', function (req, res) {
  let randomNumber = Math.floor((Math.random() * 10) + 1);
  let realTweet = false;
  if(randomNumber >= 0 && randomNumber <= 5){
    realTweet = false;
  }
  else{
    realTweet = true;
  }
  return res.send(String(realTweet));
});

app.listen(process.env.PORT || 8080);