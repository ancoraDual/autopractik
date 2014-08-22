// jQuery PopUp Plugin by AncoraDual
//
// Version 6/3/2014
//

(function ($) {

    $.aDualPopUp = {

        options: {
            id: -1,
            title: '',
            titleIcon: 'icon-util-form',
            contentBody: '',
            width: 500,
            height: 200,
            hideClose: false,
            draggable: false,
            activeTabs: false,
            hideFooter: false,
            buttonsFooter: {
                removeBtn: false,
                removeEvent: '',
                cancelBtn: true,
                saveBtn: false,
                saveEvent: '',
                saveAndCloseEventBtn: false,
                saveAndCloseEvent: ''
            },
            afterEvents: '',
            cancelEvents: ''
        },

        // Public methods
        show: function (params) {
            $.extend($.aDualPopUp.options, params);
            $.aDualPopUp._show();
        },
        setData: function (data) {
            $("body").append(data);
            $('#mask').html("");
        },
        close: function () {
            $.aDualPopUp._hide();
        },
        loading: function () {

            var maskHeight = $(document).height();
            var maskWidth = $(window).width();

            $('#mask').html("<img src='img/progress.gif' style='position:fixed;top:40px;left:45%'>");
            $('#mask').css({ 'width': maskWidth, 'height': maskHeight });
            $('#mask').fadeTo("fast", 0.9);
            $('#mask').fadeIn();
            $('#mask').show();

        },
        showLoading: function () {
            $('#mask').html("<img src='img/progress.gif'>");
        },
        hideLoading: function () {
            $('#mask').html("");
            $('#mask').hide();
        },
        // Private methods
        _show: function () {

            var close = "<span class='configure'>" +
                            "<span class='close glyphicon glyphicon-remove' title='Cerrar panel' onclick=\"$.aDualPopUp.close();" + $.aDualPopUp.options.cancelEvents + "\"></span>" +
                        "</span>";

            if ($.aDualPopUp.options.hideClose)
                close = "";

            // --------

            var id = "<span>(Id:" + $.aDualPopUp.options.id + " ) </span>";
            if ($.aDualPopUp.options.id <= 0)
                id = "";

            // -----

            $('#popUpContenido').remove();

            $("body").append(
			  '<div id="popUpContenido">' +
			    '<div class="panel_PopUp">' +

                    '<div class="cabecera">' +
			            '<span class="titulo">' +
                            '<span class="icon icon-left ' + $.aDualPopUp.options.titleIcon + '">&nbsp;</span>' + $.aDualPopUp.options.title + " " + id +
                         '</span>' +
                         close +
				    '</div>' +

                    '<div class="panelPopUp_content">' +
			            $.aDualPopUp.options.contentBody +
				    '</div>' +

                    $.aDualPopUp._getFooter() +

				'</div>' +
             '</div>' +
             '<script type="text/javascript">$(document).ready(function() {' + $.aDualPopUp.options.afterEvents + '});</script>' +

             '');

            $.aDualPopUp._view();

        },
        _view: function () {

            $.aDualPopUp._draggable();

            $("#popUpContenido").css({
                zIndex: 99999,
                padding: 0,
                margin: 0
            });

            $('.panel_PopUp').css({ 'width': $.aDualPopUp.options.width });

            $('.panelPopUp_content').css({ 'height': $.aDualPopUp.options.height });
            $('.panelPopUp_content').css({ 'overflow-x': 'hidden' });
            $('.panelPopUp_content').css({ 'overflow-y': 'scroll' });

            $('#popUpContenido').css({ 'left': ($(window).width() - $("#popUpContenido").width()) / 2 });
            $('#popUpContenido').fadeIn("fast");
            $("#popUpContenido").css('position', 'fixed');

            window.onresize = function (event) {

                $('#popUpContenido').css({ 'left': ($(window).width() - $("#popUpContenido").width()) / 2 });
                $('#mask').css({ 'width': $(window).width() });

                //                if (($(".panelPopUp_content").height() + 150) > $("body").height()) {
                //                    $('.panelPopUp_content').css({ 'height': ($("body").height() - 100) });
                //                }
                //                else {
                //                    $('.panelPopUp_content').css({ 'height': $.aDualPopUp.options.height });
                //                }
            }

            if ($.aDualPopUp.options.activeTabs) {

                $(".tab_content").hide();
                $("ul.tabs li:first").addClass("active").show();
                $(".tab_content:first").show();

                $("ul.tabs li").click(function () {
                    $("ul.tabs li").removeClass("active");
                    $(this).addClass("active");
                    $(".tab_content").hide();

                    var activeTab = $(this).find("a").attr("href");
                    $(activeTab).fadeIn();
                    return false;
                });
            }

        },
        _hide: function () {
            $('#popUpContenido, #mask, #loading').fadeOut("slow");
            $('#popUpContenido').remove();
        },
        _draggable: function () {
            if ($.aDualPopUp.options.draggable) {
                try {
                    $("#popUpContenido").draggable({ handle: '.panel_PopUp .cabecera', containment: 'parent' });
                    $(".panelPopUp_PopUp > .cabecera").css({ cursor: 'move' });
                } catch (e) { /* requires jQuery UI draggables */ }
            }
        },

        // Footer ////////////////////////////////////////////////
        // ------------------------------------------------------

        _footerData: '',
        _getFooter: function () {

            var footer = "";
            footer += "<div class='panelPopUp_footer'>";

            if ($.aDualPopUp.options.buttonsFooter.cancelBtn) {

                footer += "<div class='btn btn-primary pull-left' onclick=\"$.aDualPopUp.close();" + $.aDualPopUp.options.cancelEvents + "\">";
                footer += "  <span class='glyphicon glyphicon-remove pull-left color-white'></span>cancelar";
                footer += "</div>";
            }

            if ($.aDualPopUp.options.buttonsFooter.saveBtn) {

                footer += "     <div class='btn btn-primary pull-right' onclick=\"" + $.aDualPopUp.options.buttonsFooter.saveEvent + "\">";
                footer += "         <span class='glyphicon glyphicon-floppy-save pull-left color-white'></span>guardar";
                footer += "     </div>";
            }

            if ($.aDualPopUp.options.buttonsFooter.removeBtn) {

                footer += "     <div class='buttonPnl buttonPnl-right' onclick=\"" + $.aDualPopUp.options.buttonsFooter.removeEvent + "\">";
                footer += "         <span>suprimir</span><span class='icon-right icon-pnl-remove'>&nbsp</span>";
                footer += "     </div>";
            }

            if ($.aDualPopUp.options.buttonsFooter.saveAndCloseEventBtn) {

                footer += "     <div class='btn btn-primary pull-right' onclick=\"" + $.aDualPopUp.options.buttonsFooter.saveAndCloseEvent + "\">";
                footer += "         <span class='glyphicon glyphicon-floppy-save pull-left color-white'></span>guardar y salir";
                footer += "     </div>";
            }

            footer += "</div>";
            if ($.aDualPopUp.options.hideFooter)
                footer = "";

            return footer;
        }
    }
})(jQuery);