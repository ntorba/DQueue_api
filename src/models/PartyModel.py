from . import db
import datetime
from marshmallow import fields, Schema
from . import db, bcrypt
from .SongModel import SongSchema

class PartyModel(db.Model):
    """
    Party Model
    """
    __tablename__ = 'parties'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), nullable=False)
    #queue_content = db.Column(db.Dict, nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    created_at = db.Column(db.DateTime)
    modified_at = db.Column(db.DateTime)
    songs = db.relationship('SongModel', backref='users', lazy=True)


    def __init__(self, data):
        self.title = data.get('title')
        self.contents = data.get('queue_content')
        self.owner_id = data.get('owner_id')
        self.created_at = datetime.datetime.utcnow()
        self.modified_at = datetime.datetime.utcnow()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self, data):
        for key, item in data.items():
            setattr(self, key, item)
        self.modified_at = datetime.datetime.utcnow()
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_all_parties():
        return PartyModel.query.all()

    @staticmethod
    def get_one_party(id):
        return PartyModel.query.get(id)

    def __repr__(self):
        return '<id {}>'.format(self.id)

class PartySchema(Schema):
    """
    Party Schema
    """
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    #contents = fields.Dict(required=True)
    owner_id = fields.Int(required=True)
    created_at = fields.DateTime(dump_only=True)
    modified_at = fields.DateTime(dump_only=True)
