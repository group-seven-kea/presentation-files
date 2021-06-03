$("#buy-btn").click((e) => {
    e.preventDefault()
    data = $("form").serialize()

    $.ajax({
        url: "/dashboard/cryptocurrency/buy",
        type: "POST",
        data: data,
        dataType: "json",
        success: (res) => {
            window.location.href = "/dashboard/cryptocurrency"
        },
        error: (err) => {
            alert(err.responseJSON.error)
        }
    })
})

$("#sell-btn").click((e) => {
    e.preventDefault()
    data = $("form").serialize()

    $.ajax({
        url: "/dashboard/cryptocurrency/sell",
        type: "POST",
        data: data,
        dataType: "json",
        success: (res) => {
            window.location.href = "/dashboard/cryptocurrency"
        },
        error: (err) => {
            alert(err.responseJSON.error)
        }
    })
})