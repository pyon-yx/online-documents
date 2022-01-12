function show_notification(type, message, width=400, delay=5000) {
    /**
     * type: ['success', 'warning', 'info', 'error']
     */
    Lobibox.notify(type, {
        showClass: 'fadeInDown',
        hideClass: 'fadeUpDown',
        position: 'top right',
        width: width,
        delay: delay,
        msg: message
    });
}

function check_client_code() {
    let client_code = $('#client_code').val();
    $.ajax({
        type: 'GET',
        url: '/check_client_code',
        data: {
            client_code: client_code
        },
        success: function(res) {
            if (res === 'success') {
                window.location.href = '/dashboard';
            }
            else {
                show_notification('error', 'Invalid code');
            }
        }
    })
}

$(document).on('keyup', '#client_code', function(e) {
    if (e.which === 13) {
        check_client_code();
    }
});

$(document).on('click', '.btn-check-code', function(e) {
    check_client_code();
});

$(document).on('click', '.download-file-content', function() {
    let element = document.createElement('a');
    element.href = $(this).attr('data-url');
    element.download = $(this).attr('data-title');
    element.style.display = 'none';
    document.body.appendChild(element);
    element.click();
    element.remove();
});