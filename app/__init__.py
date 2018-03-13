from flask import Flask
from app import stores, models, dummy_data
from app import api 
app = Flask(__name__)

member_store = stores.MemberStore()
post_store = stores.PostStore()
dummy_data.seed_stores(member_store, post_store)

from app import views

