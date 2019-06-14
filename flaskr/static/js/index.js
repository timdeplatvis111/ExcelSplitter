$("#partcolumn1").on("input", function(e) 
{
    //$("#output").text( $(e.target).val())
    //console.log($("#output").text( $(e.target).val())
    if ($("#partcolumn1").val() != '')
    {
        //$("#output").text( $(e.target).val() )
        //console.log('YEETICUS')
        //console.log($("#output").text( $(e.target).val().length))

        yeet = document.getElementById("partcolumn1").value;
        //console.log(yeet)
        yeeticus = Number(yeet)
        var koi = 'KOI489204760284859020306'
        
        for (i = 0; i < yeeticus; i++) 
        { 
            console.log(yeeticus)
            //document.getElementById("output").classList.add(i);
            //var newtext = document.createTextNode('-');
            //document.getElementById("output").appendChild(newtext);
            //document.getElementById("output").innerHTML = yeeticus
        }

        var lol = document.createTextNode(koi)
        document.getElementById("texticus").appendChild(lol);

        //var upArrow = document.createTextNode('↑');
        //document.getElementById("output").appendChild(upArrow);
    }
    else
    {
        i = 0;
        $("#output").text('')
        $('body').find('#output').addClass('Yeet');
        $('body').find('#output').removeClass();

        //$("#texticus").text('')
        //$('body').find('#texticus').removeClass();
    }
});

$("#partcolumn1").val("This is a test");
$("#partcolumn1").trigger("input");

//Validatie toevoegen dat de 2e value niet hoger kan zijn dan de eerste

//$("#testArea").on("input", function(e) {
    //$("#outputArea").text( $(e.target).val() )
//    if (($e.target).val() = 'yeet')
//    {
//        $("#outputArea").text( $(e.target).val() )
//    }
//});
  
//$("#testArea").val("This is a test");
//$("#testArea").trigger("input");
