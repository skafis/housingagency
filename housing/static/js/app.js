// Input Lock
$('textarea').blur(function () {
    $('#hire textarea').each(function () {
        $this = $(this);
        if (this.value != '') {
            $this.addClass('focused');
            $('textarea + label').css({
                'opacity': 1
            });
        } else {
            $this.removeClass('focused');
            $('textarea + label').css({
                'opacity': 0
            });
        }
    });
});

$('#hire .field:first-child input').blur(function () {
    $('#hire .field:first-child input').each(function () {
        $this = $(this);
        if (this.value != '') {
            $this.addClass('focused');
            $('.field:first-child input + label').css({
                'opacity': 1
            });
        } else {
            $this.removeClass('focused');
            $('.field:first-child input + label').css({
                'opacity': 0
            });
        }
    });
});

$('#hire .field:nth-child(2) input').blur(function () {
    $('#hire .field:nth-child(2) input').each(function () {
        $this = $(this);
        if (this.value != '') {
            $this.addClass('focused');
            $('.field:nth-child(2) input + label').css({
                'opacity': 1
            });
        } else {
            $this.removeClass('focused');
            $('.field:nth-child(2) input + label').css({
                'opacity': 0
            });
        }
    });
});