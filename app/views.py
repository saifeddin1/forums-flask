from flask import render_template, request, redirect, abort, url_for
from app import models
from app import app, member_store, post_store



@app.route("/")
@app.route("/index")
def home():
    return render_template("index.html", posts = post_store.get_all())


@app.route("/topic/add", methods = ["GET", "POST"])
def topic_add():
    if request.method == "POST":
        new_post = models.Post(title=request.form["title"], content=request.form["content"])
        post_store.add(new_post)
        return redirect(url_for("home"))

    else:
        return render_template("topic_add.html")

@app.route("/topic/delete/<int:id>")
def topic_delete(id):
    if post_store.get_by_id(id) is None:
        abort(404)
    else:
        post_store.delete(id)
    return redirect(url_for("home"))

@app.route("/topic/edit/<int:id>", methods = ["GET", "POST"])
def topic_edit(id):
    post = post_store.get_by_id(id)
    if request.method == "POST":
        
        if post is None:
            abort(404)
        else:
            post.title = request.form['title']
            post.content = request.form['content']
            post_store.update(post)
            return render_template("topic_show.html", post = post)
        return redirect(url_for("home"))
    else:

        return render_template("topic_edit.html", post = post_store.get_by_id(id))

@app.route("/topic/show/<int:id>")
def topic_show(id):
    if post_store.get_by_id(id) is None:
        abort(404)
    else:
        return render_template("topic_show.html", post = post_store.get_by_id(id))
    return redirect(url_for("home"))

#Credits: Mr.Yassser Al-najjar
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html', message = error.description)



