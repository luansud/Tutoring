

button = document.querySelector("#change");
button = document.getElementById("change");
button.onclick = function() {
    about = document.querySelector("#about_me");
    about.style.border = "10px solid black";
    about.style.padding = "10px";
    about.style.backgroundColor = "black";
    about.innerText = "About me Luã Felizola";

    const description = document.createElement("h4");
    about.appendChild(description);
    description.innerHTML = "I am a tutor at BYU and I love coding!";

    full_page = document.querySelector("#FULL_about_me"); 
    full_page.style.backgroundColor = "black";
    full_page.style.color = "white";
    full_page.style.margin = "20px";
}

Luã Felizola 





// #  = Id 
// .  = Class 
// "" = Tag Name