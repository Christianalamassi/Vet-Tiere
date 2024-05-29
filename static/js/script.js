var messages = document.getElementById('message_alert');

//for notification message
setTimeout(function () {
    var alert = new bootstrap.Alert(messages);
    alert.close();
}, 4000);