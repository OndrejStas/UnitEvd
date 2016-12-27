<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<html xmlns="http://www.w3.org/1999/xhtml">
<head>

<style>

body{
    background-color: #294F77;
    color:#EEE
}

div.rightPart{
 	background-color: #4CAF50;    
 	width:20%;	
	height:100%;
	/*height:100vh;*/
	display: inline-block;
	float:left;
}

div.leftPart{
    
	background-color:#f44336;
	width:80%;
	/*height:100vh;*/
	position:absolute;
	display: inline-block;
}



div.detailLabel {
    height: 50px;
    width: 100%;
    background-color: #294F77;
    color:#EEE;
    /*border-style: solid;*/
/*    border-bottom: thick #EEE;*/
    
	
}
div.detailHodnota
{
	font-size: 200%;
	position: relative;
    	left:10%;
}
div.detailPopis
{
	/*position: relative;*/
    	left:0px;
	top:0px;
}
div.Button
{
      width:100%;
    height: 50px;
    background-color: #294F77;
    color:#EEE;
    border-style: solid;
    border-bottom: thick #EEE;
    font-size: 150%;
    display: block;
    position: relative;
    padding: 0px 0px;
    margin: 0px 0;
    text-align: center;
    vertical-align: middle;
}
div.buttonMenu0
{
	
	
	width:inherit;
	position: absolute;
    	/*left:0px;*/
	bottom:0px;

}

.Button:hover {
    background-color: #3e8e41;
}


</style>
</head>
<body>
<div class="rightPart">


<div class="detailLabel" > <div  class="detailPopis" > nazev </div > <div  class="detailHodnota"  > {{title}} </div > </div>
<div class="detailLabel" > <div  class="detailPopis" > cislo </div > <div  class="detailHodnota"  >  {{content}}</div >  </div>
<div class="detailLabel" > <div  class="detailPopis" > typ </div > <div  class="detailHodnota"  > TYP </div >  </div>
<div class="detailLabel" > <div  class="detailPopis" > kod </div > <div  class="detailHodnota"  > KOD </div >  </div>


<div class="buttonMenu0">
<div class="Button" >  Pűidat úkol  </div>
<div class="Button" >   </div>
<div class="Button" >   </div>
<div class="Button" >  Odstranit jednotku  </div>
</div>
</div>
<div class="leftPart">
</div>
</body>
</html>
