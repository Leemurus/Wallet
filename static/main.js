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
        headers: {'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value},
        success: function (text) {
            response = {
                'responseText': text,
                'status': 200
            }
        },
        error: function (xhr, status, error) {
            response = xhr;
        }
    });
    return response
}

// AJAX ==========================================================================================

// OPEN AND CLOSE DIVS ===========================================================================

$('.create_wallet').click(function () {
    $('.dark_background').show();
    $('.create_wallets_inputs').show();
});

$('.close_wallets_inputs_button').click(function () {
    $('.dark_background').hide();
    $('.create_wallets_inputs').hide();
});

$('.wallets .edit_wallet').click(function (event) {
    $('.dark_background').show();
    $('.edit_wallets_inputs').show();
    $('.edit_wallets_inputs').attr('value', $(this).parent().attr('value'));
});

$('.close_wallets_editing_inputs_button').click(function () {
    $('.dark_background').hide();
    $('.edit_wallets_inputs').hide();
});

$('.create_transaction').click(function () {
    $('.dark_background').show();
    $('.create_transactions_inputs').show();
});

$('.close_transaction_inputs_button').click(function () {
    $('.dark_background').hide();
    $('.create_transactions_inputs').hide();
});

// OPEN AND CLOSE DIVS ===========================================================================


// OPERATIONS ===========================================================================

$('.create_transactions_inputs_form').on('submit', function () {
    const data = {
        'wallet_title': $('.create_transactions_inputs_form .wallet_title_input').val(),
        'amount': $('.create_transactions_inputs_form .amount_input').val(),
        'comment': $('.create_transactions_inputs_form .comment_input').val()
    };
    var response = postAjaxInformation('/api/add_transaction', data);

    if (response.status != 200) {
        alert(response.responseText);
        return false;
    }
    return true;
});

$('.create_wallets_inputs_form').on('submit', function () {
    const data = {
        'title': $('.create_wallets_inputs_form .title_input').val()
    };
    var response = postAjaxInformation('/api/create_wallet', data);

    if (response.status != 200) {
        alert(response.responseText);
        return false;
    }
    return true;
});

$('.edit_wallets_inputs_form').on('submit', function () {
    const data = {
        'id': parseInt($('.edit_wallets_inputs').attr('value')),
        'title': $('.edit_wallets_inputs_form .title_input').val()
    };
    var response = postAjaxInformation('/api/edit_wallet', data);

    if (response.status != 200) {
        alert(response.responseText);
        return false;
    }
    return true;
});

$('.wallets .li_wallets').click(function () {
    const id = parseInt($(this).attr('value'));
    var response = postAjaxInformation('/api/get_transactions_by_wallet', {'id': id});

    if (response.status != 200) {
        alert('Some problems');
    }

    $('.transactions_table tbody').empty();
    const transactions = response.responseText;
    for (let i = 0; i < transactions.length; i++) {
        const element =
            '<tr value=\"' + transactions[i].id + '\">' +
            '<td>' + transactions[i].id + '</td>' +
            '<td>' + transactions[i].amount + '</td>' +
            '<td>' + transactions[i].date + '</td>' +
            '<td>' +
            transactions[i].comment +
            '    <button type="button" class="close delete_transaction" aria-label="Close">' +
            '        <span aria-hidden="true">&times;</span>' +
            '    </button>' +
            '</td>' +
            '</tr>';
        $(element).appendTo($('.transactions_table tbody'));
    }
});

$('.wallets .delete_wallet').click(function (event) {
    event.stopPropagation();  // Because after button click will call li click

    const id = $(this).parent().attr('value');
    var response = postAjaxInformation('/api/delete_wallet', {'id': parseInt(id)});

    if (response.status != 200) {
        alert('Some problems');
    } else {
        location.reload();
    }
});

$('.transactions_table .delete_transaction').click(function () {
    const id = $(this).parent().parent().attr('value');

    var response = postAjaxInformation('/api/delete_transaction', {'id': parseInt(id)});

    if (response.status != 200) {
        alert('Some problems');
    } else {
        location.reload();
    }
});




