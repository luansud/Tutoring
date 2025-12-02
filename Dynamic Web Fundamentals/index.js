
test = document.getElementById("test");
button = document.getElementById("change");
button.addEventListener("click", () => {
    if (test.style.display == "flex"){
        test.style.display = "none";
        button.innerText = "Show";
    }

    else{
        test.style.display = "flex";
        button.innerText = "Hide";
    }

});








