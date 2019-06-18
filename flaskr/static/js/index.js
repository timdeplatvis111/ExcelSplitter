//$("#partcolumn1").on("input", function(e) 


// Het moet nog laten zien van welke character tot welke character het matched, om het duidelijker te maken.
// Misschien in plaats van een random getal kan ik gewoon een iteration gebruiken, dus dan wordt het
// gewoon KOI1234567890s

$("#dingetje :input").change(function() 
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
        flokken = ($('#texticus').text());
        var koi = 'KOI'

        var lolol = document.createTextNode(koi);
        document.getElementById("texticus").append(lolol);
        
        for (i = 0; i < yeeticus; i++) 
        { 
            console.log(yeeticus)
            //document.getElementById("output").classList.add(i);
            //var newtext = document.createTextNode('-');
            //document.getElementById("output").appendChild(newtext);
            //document.getElementById("output").innerHTML = yeeticus
            holyshit = Math.floor((Math.random() * $("#partcolumn1").val() * + 10) + $("#partcolumn1").val() + 10);

            if (flokken.length < $("#partcolumn1").val())
            {
                var holyshit = document.createTextNode(holyshit)
                document.getElementById("texticus").appendChild(holyshit);
            }
        }

        $("input").keyup(function()
        {
            $("#texticus").text('');
            $('body').find('#texticus').removeClass();
        });

        //var upArrow = document.createTextNode('↑');
        //document.getElementById("output").appendChild(upArrow);
    }
    else
    {
        i = 0;
        //$("#output").text('')
        //$('body').find('#output').addClass('Yeet');
        //$('body').find('#output').removeClass();

        $("#texticus").text('')
        $('body').find('#texticus').removeClass();
    }
});

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
