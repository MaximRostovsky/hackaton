function UploadPhoto() {
    file = document.getElementById('Photo').files[0];
    var output = [];
    output.push("File ", file.name, " was uploaded successfully");
    document.getElementById('FileChosen').innerHTML = '<ul>' + output.join('') + '</ul>';
}

function sendToServ() {
    alert("Sending to server");
    var objectToSend = {
        FIO: document.getElementById('FIO').value,
        Phone: document.getElementById('Phone').value,
        Photo: file
    };

    var xhr = new XMLHttpRequest();
    xhr.open("POST", "http://127.0.0.1:5000/json", true);
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.onreadystatechange = function () {
        if (xhr.readyState == 4 && xhr.status == 200) {
            var json = xhr.responseText;
            console.log(json);
        }
    }
    
    xhr.send(objectToSend);
}

var file;
window.onload = function () {
    var photo = document.getElementById('Photo');
    document.getElementById('Photo').addEventListener('change', UploadPhoto, false);
}
