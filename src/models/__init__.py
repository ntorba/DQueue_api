#src/models/__init__.py

from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
#initial our db

db = SQLAlchemy()
bcrypt = Bcrypt()


#from .PartyModel import PartyModel,PartySchema
#from .UserModel import UserModel, UserSchema
