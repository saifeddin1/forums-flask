from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
import os

app = Flask(__name__)

folder_path = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ['DATABASE_URL']
db = SQLAlchemy(app)

from app import stores, dummy_data

member_store = stores.MemberStore()
post_store = stores.PostStore()
#dummy_data.seed_stores(member_store, post_store)

from app import api
from app import views

