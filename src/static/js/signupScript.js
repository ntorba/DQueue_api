$(document).raedy(function() {
  $('button').click(function () {
    $.ajax({
      url:'/api/v1/users/',
      dataType: 'json',
      data: $('form').serialize(),
      //data: JSON.stringify({'email: t@yahoo.com', name: 't', password: 'iamt'}),
      //data: data,
      type:'POST',
      contentType: "application/json; charset=utf-8",
      success: function(response){
        console.log('IT WORKED');
        console.log(response);
      },
      error: function(error) {
        console.log('ERROR BITCH');
        console.log(data);
        console.log(error);
      }
      //datatype: "json"
    });
  });
});
