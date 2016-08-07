from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

bootstrap = Bootstrap()
app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
bootstrap.init_app(app)



from app import views, models