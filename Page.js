function UploadPhoto() {
    file = document.getElementById('Photo').files[0];
    var output = [];
    output.push("File ", file.name, " was uploaded successfully");
    document.getElementById('FileChosen').innerHTML = '<ul>' + output.join('') + '</ul>';
}

function sendToServ() {

    document.getElementById('Result').value = null;

    var FIO = document.getElementById('FIO').value;
    var Phone = document.getElementById('Phone').value;
    var Birthday = document.getElementById('Birthday').value;


    if (FIO == '' || Phone == '' || Birthday == '') {
        alert("Some of the fields are empty! Please fill them up");
        return;
    }

    var formData = new FormData();
    formData.append("FIO", FIO);
    formData.append("Phone", Phone);
    formData.append("Birthday", Birthday);
    formData.append("Photo", file, );

    var xhr = new XMLHttpRequest();
    xhr.open("POST", "http://127.0.0.1:5000/json", true);
    xhr.onreadystatechange = function () {
        if (xhr.readyState == 4 && xhr.status == 200) {
            var json = xhr.responseText;
            document.getElementById('Result').value = json;
            document.getElementById('Result').style.display = "block";
        }
    }

    xhr.send(formData);
}

var file;
window.onload = function () {
    var photo = document.getElementById('Photo');
    document.getElementById('Photo').addEventListener('change', UploadPhoto, false);
}
