from flask import Flask

app = Flask(__name__)


# we are doing this to avoid the circular import
from app import views
from app import admin_views