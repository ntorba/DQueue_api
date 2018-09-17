#src/models/SongsModel.py

from marshmallow import fields, Schema
import datetime
from . import db, bcrypt

class SongModel(db.Model):
    """
    Songs Model
    """

    __tablename__ = 'songs'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    party_id = db.Column(db.Integer, db.ForeignKey('parties.id'), nullable=False)
    vote_count = db.Column(db.Integer)
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    created_at = db.Column(db.DateTime)
    modified_at = db.Column(db.DateTime)


    def __init__(self, data):
        """
        Class constructor
        """
        self.name = data.get('name')
        self.email = data.get('email')
        self.party_id = data.get('party_id')
        self.vote_count = data.get('vote_count')
        self.owner_id = data.get('owner_id')
        self.created_at = datetime.datetime.utcnow()
        self.modified_at = datetime.datetime.utcnow()


    def save(self):
        db.session.add(self)
        db.session.commit()

    """
    I need a vote count update method.
    and I guess a general update method
    """
    #def update(self, data):
    #    for key, item in data.items():
    #        if key == 'password':

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_all_songs():
        return SongModel.query.all()

    @staticmethod
    def get_one_song(id):
        return SongModel.query.get(id)

    @staticmethod
    def get_party_songs(id):
        return SongModel.query.filter_by(party_id=id).all()

    def __repr__(self):
        return '<name {}>'.format(self.id)

class SongSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    vote_count = fields.Int(required = True)
    party_id = fields.Int(required = True)
    owner_id = fields.Int(required = True)
    created_at = fields.DateTime(dump_only=True)
    modified_at = fields.DateTime(dump_only=True)
