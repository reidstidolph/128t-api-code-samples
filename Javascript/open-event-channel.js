var EventSource = require('eventsource');

var authToken = '<Your_Token>';
var eventUrl = `<Your_URL>`;

var es = new EventSource(eventUrl, {https: {rejectUnauthorized: false}});

es.onmessage = (event)=>{
  console.log(event.data);
};

es.onerror = (err)=>{
  if (err) {
    console.log(err);
    if (err.status === 401 || err.status === 403) {
      console.log('not authorized');
    }
  }
};

es.onopen = ()=>{
  console.log('eventstream opened!');
};
