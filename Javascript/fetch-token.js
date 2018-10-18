var request = require('request')

var postData = {
  'username': '<Username>',
  'password': '<Password>'
}

var url = "<Your_URL>"
var options = {
  method: 'post',
  body: postData,
  json: true,
  rejectUnauthorized: false,
  url: url
}
request(options, function (err, res, body) {
  if (err) {
    console.error('error posting json: ', err)
    throw err
  }
  var headers = res.headers
  var statusCode = res.statusCode
  console.log(JSON.stringify(body));
})
