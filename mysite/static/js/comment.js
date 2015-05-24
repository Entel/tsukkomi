$(".subtitle").click(function(){
	$(this).next().toggle();
	var full_id = $(this).next().attr('id');
	console.log(full_id);
	var id = full_id.replace("comment_area_", "");
	console.log(id);
	
	//ajax
	if (id){
		$.get("showComment");
	}
	
})

