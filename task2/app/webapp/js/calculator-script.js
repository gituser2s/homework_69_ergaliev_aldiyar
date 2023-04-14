let xhr = new XMLHttpRequest();
xhr.onload = function(){
    console.log(xhr.status);
    console.log(xhr.response);
};
xhr.open('GET', 'http://127.0.0.1:8000/add/');
xhr.send()