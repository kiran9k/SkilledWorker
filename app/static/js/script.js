function isChrome() {
    if ((!!window.chrome && !!window.chrome.webstore))
    {
        var x = document.getElementById("ChromeOnly");
        x.style.display = "none";
    }
    
}

//isChrome();