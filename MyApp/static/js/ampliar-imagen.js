
function expandImage(img) {
    img.style.width = "auto"; // Anchura fija de 700px
    img.style.height = "auto"; // Altura fija de 500px
    img.style.maxWidth = "40vw"; // Anchura máxima del 90% del viewport width
    img.style.maxHeight = "90vh";  
    img.style.position = "fixed";
    img.style.left = "0";
    img.style.right = "0";
    img.style.top = "0";
    img.style.bottom = "0";
    img.style.margin = "auto";
    img.style.zIndex = "9999";
    img.style.backgroundColor = "rgba(0, 0, 0, 0.8)";
    img.style.cursor = "zoom-out";
    img.onclick = function () {
        img.style.width = "100%";
        img.style.height = "auto";
        img.style.position = "static";
        img.style.zIndex = "0";
        img.style.backgroundColor = "";
        img.onclick = function () { expandImage(this); };
    };
}
