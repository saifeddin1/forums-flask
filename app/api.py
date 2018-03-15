from flask import request,jsonify, abort 
from app import models
from app import app, member_store, post_store


@app.route("/api/topic/all")
def topic_get_all():
    posts = [post.__dict__() for post in post_store.get_all()]
    return jsonify(posts)

@app.route("/api/topic/add", methods = ["POST"])
def topic_create():
	request_data = request.get_json()
	try:
	    new_post = models.Post(request_data["title"], request_data["content"])
	    post_store.add(new_post)
	    result = jsonify(new_post.__dict__())
	except KeyError:
		result = abort(400, f"Couldn't parse the request data !")
	return result		


@app.route("/api/topic/show/<int:id>")
def api_topic_show(id):
	post = post_store.get_by_id(id)
	try:
		result = jsonify(post.__dict__())
	except AttributeError:
		result = abort(404, f"topic with id: {id} doesn't exist!")
	return result
		
@app.route("/api/topic/edit/<int:id>", methods = ["POST"])
def api_topic_edit(id):
	request_data = request.get_json()
	post = post_store.get_by_id(id)
	try:
		post.title = request_data["title"]
		post.content = request_data["content"]
		post_store.update(post)
		return jsonify(post.__dict__())
	except AttributeError:
		result = abort(404, f"topic with id: {id} doesn't exist!")
	except KeyError:
		result = abort(400, f"Couldn't parse the request data !")
	return result	

@app.route("/api/topic/delete/<int:id>", methods = ["DELETE"])
def topic_delete_api(id):
    try:
        result = post_store.delete(id)
        result = jsonify(result.__dict__())
    except ValueError:
        result = abort(404, f"topic with id: {id} doesn't exist")

    return result

