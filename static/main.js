$(document).ready(function () {
    alert('Loaded');
});

function getAjaxInformation(url) {
    let response = null;
    $.ajax({
        type: "GET",
        url: url,
        async: false,
        success: function (text) {
            response = text;
        }
    });
    return response;
}

function postAjaxInformation(url, data) {
    let response = null;
    $.ajax({
        type: "POST",
        url: url,
        async: false,
        data: JSON.stringify(data),
        contentType: 'application/json;charset=UTF-8',
        success: function (text) {
            response = text;
        },
        error: function (xhr, status, error) {
            response = xhr.responseText;
        }
    });
    return response
}