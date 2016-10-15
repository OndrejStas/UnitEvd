 Request ={
    GetDataFromUrl:function (url,target)
    {
       
      var xhttp = new XMLHttpRequest();
      xhttp.onreadystatechange = function() 
      {
      if (this.readyState == 4 && this.status == 200) 
      {
        //alert(this.responseText);
        target.innerHTML=  this.responseText;
      }
     
     };
     xhttp.open("GET",url,true);
     xhttp.send();
    }  ,
     Test:function ()
     {
     alert('Test');
     return 1;
     }
}