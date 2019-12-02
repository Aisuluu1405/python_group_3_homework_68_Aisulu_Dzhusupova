function successResult(data) {
  let answer = `<p style="color:green">${data.answer}</p>`;
  $('.result').append(answer);
  }

function errorResult(data) {
    text = JSON.parse(data.responseText);
    error_message = text.error;
    let answer = `<p style="color:red">${text.error}</p>`;
    $('.result').append(answer);
}

function add() {
  A = document.getElementById('first_number');
  B = document.getElementById('second_number');
  $.ajax({
    url: "http://localhost:8000/api/add/",
    method: 'post',
    dataType: "json",
    contentType: "application/json",
    data: JSON.stringify({"A":A.value,  "B":B.value}),
    success: successResult,
    error: errorResult
  });
}

function subtract() {
  A = document.getElementById('first_number');
  B = document.getElementById('second_number');
  $.ajax({
    url: "http://localhost:8000/api/subtract/",
    method: 'post',
    dataType: "json",
    contentType: "application/json",
    data: JSON.stringify({"A":A.value,  "B":B.value}),
    success: successResult,
    error: errorResult
  });
}

function multiply() {
  A = document.getElementById('first_number');
  B = document.getElementById('second_number');
  $.ajax({
    url: "http://localhost:8000/api/multiply/",
    method: 'post',
    dataType: "json",
    contentType: "application/json",
    data: JSON.stringify({"A":A.value,  "B":B.value}),
    success: successResult,
    error: errorResult
  });
}

function divide() {
  A = document.getElementById('first_number');
  B = document.getElementById('second_number');
  $.ajax({
    url: "http://localhost:8000/api/divide/",
    method: 'post',
    dataType: "json",
    contentType: "application/json",
    data: JSON.stringify({"A":A.value,  "B":B.value}),
    success: successResult,
    error: errorResult
  });
}




