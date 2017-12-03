// main.js

function POSTEmployee(data) {
    console.log(data);
    var xhr = new XMLHttpRequest();

    xhr.open("POST", "http://student04.cse.nd.edu:51076/employees/", true);

    xhr.onload = function() {
        console.log(xhr.responseText);
    }

    xhr.onerror = function() {
        console.error(xhr.statusText);
    }

    data['Id'] = parseFloat(data['Id'])
    data['BasePay'] = parseFloat(data['BasePay'])
    data['TotalPay'] = parseFloat(data['TotalPay'])
    data['Year'] = parseFloat(data['Year'])
    var json = JSON.stringify(data);

    xhr.send(json);
}

function AddEmployee() {
    var fields = document.forms["AddForm"].getElementsByTagName("input");
    var length = fields.length;
    var data = {};
    var all_filled = true;
    for (var i = 0; i < length; i++) {
        if (fields[i].value == "") {
            all_filled = false;
        } else if (fields[i].value != "Submit"){
            data[fields[i].name] = fields[i].value;
        }
    }

    console.log(data);

    if (!all_filled) {
        alert("Please fill in all the fields for adding employee");
    } else {
        POSTEmployee(data);
        alert("Sending request to add employee...");
    }
}

function DELETEEmployee(id) {
    var xhr = new XMLHttpRequest();

    xhr.open("DELETE", "http://student04.cse.nd.edu:51076/employees/" + id, true);

    xhr.onload = function() {
        console.log(xhr.responseText);
        alert("hi");
    }

    xhr.onerror = function() {
        console.error(xhr.statusText);
    }

    data = {};
    xhr.send(JSON.stringify(data));
}

function DropEmployee() {
    var fields = document.forms["DropForm"].getElementsByTagName("input");
    if (fields[0].value == "") {
        alert("Please fill id for deleting employee");
    } else {
        DELETEEmployee(fields[0].value);
        alert("Sending request to drop employee...");
    }
}

function GetIDS(JobTitle) {
    var xhr = new XMLHttpRequest();

    xhr.open("GET", "http://student04.cse.nd.edu:51076/jobs/" + JobTitle, true);

    xhr.onload = function() {
        var text_field = document.getElementById("JobIdList");
        text_field.innerHTML = xhr.responseText;
    }

    xhr.onerror = function() {
        console.error(xhr.statusText);
    }

    xhr.send(null);
}

function JobQuery() {
    var JobTitle = document.forms["JobForm"].getElementsByTagName("input")[0].value;
    if (JobTitle != "") {
        JobTitle = encodeURI(JobTitle);
        var text_field = document.getElementById("JobIdList");
        GetIDS(JobTitle);
        alert("Sending request to get Ids for specified job...");
    }
}
