$(function ()
{
    $(".delete_topic").click(function(event){
        var id = event.target.id;
        alert("Deleted");
        window.location.href = '/';
        $.ajax({
            type: "DELETE",
            url: "/api/topic/delete/"+id,
            dataType: "json",
            success: function (response)
            {
                alert("Added topic successfully !");
            }
        });
    });
});