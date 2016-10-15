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
                "edit": {name: "Otevøi", icon: "edit"}
                }
           
        });

        $('.context-menu-one').on('click', function(e){
            console.log('clicked', this);
        })    

    }



);
 

    });
    
    
    function myFunction() {
    var x = document.getElementById("myTopnav");
    if (x.className === "topnav") {
        x.className += " responsive";
    } else {
        x.className = "topnav";
    }
}