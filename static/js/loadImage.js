$('#image_url_button').on({
    'click': function(){
        var image_url = $("#image_url").val()
        try {
            $('#render').attr('src', image_url);

        } catch(err) {
            return null
        }
    }
});

$('.render-image').on({
    'change': function(){
        try {
            $("img").remove()
            $('#add-image').prepend('<img class="card-img-top" id="render" src="' + this.value + '" alt="Vacancy image" />')

        } catch(err) {
            return null
        }
    }
});