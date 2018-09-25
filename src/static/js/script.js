$(function() {
  $('button').click(function () {
    $.ajax({
      url:'/api/v1/users/',
      data: $('form').serialize(),
      type:'POST',
      success: function(response){
        console.log('IT WORKED')
        console.log(response);
      },
      error: function(error) {
        console.log('ERROR BITCH')
        console.log(error);
      }
    });
  });
});
