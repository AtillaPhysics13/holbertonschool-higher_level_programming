document.querySelector("#toggle_header").onclick = function() {

    if(document.querySelector("header").classList.contains("red"))
    {
        document.querySelector("header").classList.remove("red");
        document.querySelector("header").classList.add("green");
    }
    else
    {
        document.querySelector("header").classList.remove("green");
        document.querySelector("header").classList.add("red");
    }

}
