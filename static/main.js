$(document).ready(function () {
});

// AJAX ==========================================================================================

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

// AJAX ==========================================================================================

// OPEN AND CLOSE DIVS ===========================================================================

$('.create_wallet').click(function () {
    $('.dark_background').show();
    $('.wallets_inputs').show();
});

$('.close_wallets_inputs_button').click(function () {
    $('.dark_background').hide();
    $('.wallets_inputs').hide();
});

$('.create_transaction').click(function () {
    $('.dark_background').show();
    $('.transactions_inputs').show();
});

$('.close_transaction_inputs_button').click(function () {
    $('.dark_background').hide();
    $('.transactions_inputs').hide();
});

// OPEN AND CLOSE DIVS ===========================================================================


// OPERATIONS ===========================================================================

$('.transactions_inputs_form').on('submit', function () {
   alert('WOw');
});

$('.wallets_inputs_form').on('submit', function () {
    alert('WOW2');
});

