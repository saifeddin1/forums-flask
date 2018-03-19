$(function ()
{
	$("form").submit(function (event)
	{
		event.preventDefault();    
			
		var topicTitle = $("input[name='title']").val();
		var topicContent = $("#myContent").val();
		var topicData = {
						"title": topicTitle,
						"content": topicContent
						};

		$.ajax({
			type: "POST",
			url: "/api/topic/add",
			data: JSON.stringify(topicData),
			contentType: "application/json; charset=utf-8",
			dataType: "json",
			success: function (response)
			{
				alert("Topic added succussfuly !");
				window.location.href = '/';
			}
		});        	
	});
});
