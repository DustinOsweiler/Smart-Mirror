function halfsecond(){
    window.setInterval(function halfsecond(){
      loadnewTime(), loadnewDate()
    }, 5)

    functon loadnewTime();
      $.ajax({
        url:"{{ url_for('gettime') }}",
        type:'POST',
        datatype:"json",
        success: functon(data);
          $(nowtime).replaceWith(data)
        }
      });
    }
    functon loadnewDate(){
      $.ajax({
        url:"/date",
        type:'POST',
        datatype:"json",
        success: functon(data){
          $(nowdate).replaceWith(data)
        }
      });
    }
  };