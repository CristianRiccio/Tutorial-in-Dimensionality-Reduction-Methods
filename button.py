%%javascript

$('#maintoolbar-container').children('#toggleButton').remove()

var toggle_button = ("<button id='toggleButton' type='button'>Show Code</button>");
$('#maintoolbar-container').append(toggle_button);

var code_shown = false;

function code_toggle()
{

    if (code_shown)
    {
        console.log("code shown")
        $('div.input').hide('500');
        $('#toggleButton').text('Show Code');
    }
    else
    {
        console.log("code not shown")
        $('div.input').show('500');
        $('#toggleButton').text('Hide Code');
    }

    code_shown = !code_shown;
}

$(document).ready(function()
{
    code_shown=false;
    $('div.input').hide();
});

$('#toggleButton').on('click', code_toggle);
