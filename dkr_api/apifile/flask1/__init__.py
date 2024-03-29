from flask import Flask
from os import environ
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
convar = 'mysql+pymysql://root:{}@{}/{}'.format(environ.get('db_root_password'),environ.get('MYSQL_SERVICE_HOST'),environ.get('db_name'))
app.config['SQLALCHEMY_DATABASE_URI']= convar
print(convar)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True
app.config['SECRET_KEY'] = '9b3eeae24ff5b6a5ca11c479'
db = SQLAlchemy(app)

from flask1 import routes
