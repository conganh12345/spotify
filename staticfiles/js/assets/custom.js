/*
=========================================
|                                       |
|       Multi-Check checkbox            |
|                                       |
=========================================
*/

window.checkall = function (clickchk, relChkbox) {

    var checker = $('#' + clickchk);
    var multichk = $('.' + relChkbox);

    checker.click(function () {
        multichk.prop('checked', $(this).prop('checked'));
    });
}


/*
=========================================
|                                       |
|           MultiCheck                  |
|                                       |
=========================================
*/

/*
    This MultiCheck Function is recommanded for datatable
*/

window.multiCheck = function (tb_var) {
    tb_var.on("change", ".chk-parent", function () {
        var e = $(this).closest("table").find("td:first-child .child-chk"), a = $(this).is(":checked");
        $(e).each(function () {
            a ? ($(this).prop("checked", !0), $(this).closest("tr").addClass("active")) : ($(this).prop("checked", !1), $(this).closest("tr").removeClass("active"))
        })
    }),
        tb_var.on("change", "tbody tr .new-control", function () {
            $(this).parents("tr").toggleClass("active")
        })
}


/*
=========================================
|                                       |
|           ReloadWithTableOrPage       |
|                                       |
=========================================
*/

/*
    This ReloadWithTableOrPage Function is reload for datatable or page
*/

window.reloadWithTableOrPage = function (tableId) {
    if (tableId) {
        $(tableId).DataTable().ajax.reload(null, false);
    } else {
        location.reload();
    }
}
