document.querySelector("#add_item").onclick = function() {
 let li = document.createElement("li")

li.innerText = "Item"

document.querySelector(".my_list").appendChild(li)
}
