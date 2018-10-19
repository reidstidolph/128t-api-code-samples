var request = require('request')


var url = "<Your_URL>"
var options = {
  method: 'post',
  headers: {'Authorization': 'Bearer <Your_Token>'
},
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
