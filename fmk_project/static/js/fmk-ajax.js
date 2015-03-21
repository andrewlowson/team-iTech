$('#suggestion').keyup(function(){
        var query;
        query = $(this).val();
        $.get('/fmk/suggest_celebrity/', {suggestion: query}, function(data){
         $('#celebrities').html(data);
        });
});