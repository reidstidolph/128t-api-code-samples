var request = require('request')

var patchData = {"<Your_Mod>": "<Your_Mod>"}
var url = "<Your_URL>"
var options = {
  method: 'patch',
  body: patchData,
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
