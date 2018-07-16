$(document).ready(function(){

    $('#toss-action').click(function() {
        getResults()
    });

});

function getResults() {
    $.ajax({
        type: 'GET',
        url: '/api/v1/cointoss',
        dataType: 'json',
        success: function (data) {
            if (data) {
                if (data.result) {
                    $('#toss-result').text("Heads!");
                }
                else {
                    $('#toss-result').text("Tails!");
                }

            }
        }
    });
}
