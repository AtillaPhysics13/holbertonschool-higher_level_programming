fetch("https://swapi-api.hbtn.io/api/films/?format=json")
.then(res => res.json())
.then(data => {

  data.results.forEach(element => {

    let li = document.createElement("li")
    li.innerText = element.title

    document.getElementById("list_movies").appendChild(li)

  })

})
