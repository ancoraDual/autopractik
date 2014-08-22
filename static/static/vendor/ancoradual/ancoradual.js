jQuery.ancoraDual = {

    m_boxActivo: "",
    m_despliegaAcciones: function (idBox) {


        if (this.m_boxActivo != idBox) {
            
            if (this.m_boxActivo == "") {
                this.m_boxActivo = idBox;
                $("#" + idBox).addClass("row-table-select");
                $("#AccionBox_" + idBox).slideDown("fast");
                return;
            }
            else {
                $("#" + this.m_boxActivo).removeClass("row-table-select");
                $("#" + this.m_boxActivo).addClass("row-table");
                $("#AccionBox_" + this.m_boxActivo).fadeOut("fast");

                $("#AccionBox_" + idBox).slideDown("fast");
                $("#" + idBox).addClass("row-table-select");
                this.m_boxActivo = idBox;
                return;
            }

        }
        else {
            $("#" + this.m_boxActivo).removeClass("row-table-select");
            $("#" + this.m_boxActivo).addClass("row-table");
            $("#AccionBox_" + this.m_boxActivo).fadeOut("fast");
            this.m_boxActivo = "";
            return;

        }
    }
};




