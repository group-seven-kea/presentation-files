$("#submit-btn").click((e) => {
    e.preventDefault()
    data = $("form").serialize()

    $.ajax({
        url: "/user/login",
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