var header = document.getElementsByClassName('header');
var uploader = document.getElementsByClassName('uploader');
var footer = document.getElementsByClassName('footer');

uploader[0].style.height = (screen.availHeight - header[0].clientHeight - footer[0].clientHeight) + "px";


// console.log(screen.availHeight);
// console.log(header[0].clientHeight);
// console.log(footer[0].clientHeight);
// console.log(screen.availHeight - header[0].clientHeight - footer[0].clientHeight);


var loadFile = function (event) {
    var reader = new FileReader();
    reader.onload = function () {
        var outputbox = document.getElementById('input_img_box');
        var output = document.getElementById('input_img');
        output.src = reader.result;
        outputbox.style.opacity = 1;
        outputbox.style.zIndex = 1;
        output.style.opacity = 1;
        var f = document.getElementById('fileInput');
        f.style.opacity = 0;
        f.style.zIndex = 2;
    };
    reader.readAsDataURL(event.target.files[0]);
};