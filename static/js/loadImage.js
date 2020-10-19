$('#image_url_button').on({
    'click': function(){
        var image_url = $("#image_url").val()
        try {
            $('#blah').attr('src', image_url);

        } catch(err) {
            return null
        }
    }
});