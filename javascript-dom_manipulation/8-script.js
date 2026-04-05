window.onload = function() {
  fetch("https://hellosalut.stefanbohacek.com/?lang=fr")
  .then(res => res.json())
  .then(data => {
    document.getElementById("hello").innerHTML = data.hello;
  })
}
