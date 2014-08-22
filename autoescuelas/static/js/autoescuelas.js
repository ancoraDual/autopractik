
function get_csrf_token()
{
    return $("input[name='csrfmiddlewaretoken']").val();
}

// ------

function buscar()
{
  val = $(".input-search").val();
  location.href="?search=" + val;
}

function editFicha(tipo, id)
{
	$(".popup").removeClass("new-popup");
	$(".popup").css("z-index", "8000");

	$.get( "/autoescuelas/"+ tipo + "/edit/" + id + "/", function( data ) {
  		$(".content").append(data);
	});
}


function guardarFicha(tipo, id)
{

  if(id == "None")
    id = 0;

  var f = $('form').serialize()

  $.ajax({
       beforeSend: function(xhr, settings) {
          if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
              // Only send the token to relative URLs i.e. locally.
              xhr.setRequestHeader("X-CSRFToken",
                                   $("input[name='csrfmiddlewaretoken']").val());
          }
      },    
      type:"POST",
      url:"/autoescuelas/" + tipo + "/save/" + id + "/",
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

jQuery.extend( jQuery.fn.dataTableExt.oSort, {
    "date-euro-pre": function ( a ) {
        var x;
 
        if ( $.trim(a) !== '' ) {
            var frDatea = $.trim(a).split(' ');
            var frTimea = frDatea[1].split(':');
            var frDatea2 = frDatea[0].split('/');
            x = (frDatea2[2] + frDatea2[1] + frDatea2[0] + frTimea[0] + frTimea[1] + frTimea[2]) * 1;
        }
        else {
            x = Infinity;
        }
 
        return x;
    },
 
    "date-euro-asc": function ( a, b ) {
        return a - b;
    },
 
    "date-euro-desc": function ( a, b ) {
        return b - a;
    }
} );

// Old


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