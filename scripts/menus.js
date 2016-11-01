$(document).ready(function () {
dialog = $( "#dialog-form" );       
	$(function() {
        $.contextMenu({
            selector: 'div.cell', 
            callback: function(key, options) {
                var m = "clicked: " + key;
		var idt = options.$trigger;
		var ddr = idt.parent().html();
		var originalElement = $('.context-menu-active');
		if (key=='edit')  dialog.dialog( "open" );
            },
            items: {
                "edit": {name: "Otevři", icon: "edit"}
                }
           
        });

        $('.context-menu-one').on('click', function(e){
            console.log('clicked', this);
        })    

    }



);
 

    });
    
    function dropFunction() {
        document.getElementById("myDropdown").classList.toggle("show");
    }

 function DropDown0() {
        document.getElementById("myDropdown0").classList.toggle("show");
    }



function UnitDetail(inp)
{
    $('#container').load('/detail/1');
}
    
    function myFunction() {
    var x = document.getElementById("myTopnav");
    if (x.className === "topnav") {
        x.className += " responsive";
    } else {
        x.className = "topnav";
    }
}