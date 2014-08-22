function editAlumno(id)
{
	$(".popup").removeClass("new-popup");
	$(".popup").css("z-index", "8000");

	$.get( "/autoescuelas/alumnos/edit/" + id + "/", function( data ) {
  		$(".content").append(data);
	});
}

function get_csrf_token(){
    return $("input[name='csrfmiddlewaretoken']").val();
}

function buscar()
{
  val = $(".input-search").val();
  location.href="?search=" + val;
}

function guardarAlumno(id)
{

  if(id == "None")
    id = 0;

	var f = $('form').serialize()
	//alert(f);
	//return;

    $.ajax({
         beforeSend: function(xhr, settings) {
            if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
                // Only send the token to relative URLs i.e. locally.
                xhr.setRequestHeader("X-CSRFToken",
                                     $("input[name='csrfmiddlewaretoken']").val());
            }
        },   	
        type:"POST",
        url:"/autoescuelas/alumnos/save/" + id + "/",
        data: f,
       	// or ...
       	// data: 
       	// {
        //     id: $('#id').val(),
        //     nombre: $('#nombre').val(),
        //     direccion: $('#direccion').val()
        // },
        success: function(data) {
            location.reload();
        },
        error: function(ts) {
            alert(ts.responseText);
        }
    });
}

function getAlumnosHtml(){

	$.get( "/autoescuelas/alumnos/getallhtml/", function( data ) {
  		$( ".resultHtml" ).html( data );
	});
}

function getAlumnosJson(){

	$.get( "/autoescuelas/alumnos/getalljson/", function( data ) {
  		$( ".resultJson" ).html( data );
	});
}