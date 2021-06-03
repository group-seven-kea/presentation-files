$("#submit-btn").click((e) => {

    e.preventDefault()
    data = $("form").serialize()

    $.ajax({
        url: "/user/register",
        type: "POST",
        data: data,
        dataType: "json",
        success: (res) => {
            window.location.href = "/dashboard/cryptocurrency"
        },
        error: (err) => {
            console.log(err)
        }
    })
})