from flask import request, json, Response, Blueprint, g
from ..models.SongModel import SongModel, SongSchema
from ..shared.Authentication import Auth
from .UserView import custom_response
from ..models.PartyModel import PartyModel

song_api = Blueprint('song_api', __name__)
song_schema = SongSchema()

#songs must be added with a party id
#no point of a song without one
#this may be a good way to do it, Ill see
#when I get to frontend work i guess
@song_api.route('/<int:party_id>', methods=['POST'])
@Auth.auth_required
def create(party_id):
    """
    Create Party
    """
    party = PartyModel.get_one_party(party_id)
    if not party:
        return custom_response({'error': 'party not found'}, 404)

    req_data = request.get_json()
    req_data['party_id'] = party_id
    req_data['owner_id'] = g.user.get('id')
    #req_data['owner_id'] = g.user.get('id')
    data, error = song_schema.load(req_data)
    if error:
        return custom_response(error, 400)
    print('LOOOOKKKK')
    print(data)
    song = SongModel(data)
    song.save()
    data=song_schema.dump(song).data
    return custom_response(data, 201)

@song_api.route('/<int:party_id>', methods=['GET'])
def get_party_queue(party_id):
    """
    Get songs for one party
    """
    songs = SongModel.get_party_songs(party_id)
    ser_songs = song_schema.dump(songs,many=True).data
    return custom_response(ser_songs, 200)
