from flask import request, json, Response, Blueprint, g
from ..models.PartyModel import PartyModel, PartySchema
from ..shared.Authentication import Auth
from .UserView import custom_response

party_api = Blueprint('party_api', __name__)
party_schema = PartySchema()

@party_api.route('/', methods=['POST'])
@Auth.auth_required
def create():
    """
    Create Party
    """
    req_data = request.get_json()
    req_data['owner_id'] = g.user.get('id')
    data, error = party_schema.load(req_data)

    if error:
        return custom_response(error, 400)

    party = PartyModel(data)
    party.save()
    data = party_schema.dump(party).data
    return custom_response(data, 201)

@party_api.route('/', methods=['GET'])
def get_all():
    """
    Get all partys
    """
    posts = PartyModel.get_all_parties()
    ser_posts = party_schema.dump(posts, many=True).data
    return custom_response(ser_posts,200)

@party_api.route('/<int:party_id>', methods=['GET'])
def get_one(party_id):
    """
    get one party by id
    """
    #post = BlogpostModel.get_one_blogpost(blogpost_id)
    party = PartyModel.get_one_party(party_id)
    if not party:
        return custom_response({'error': 'party not found'}, 404)
    data = party_schema.dump(post).data
    return custom_response(data, 200)

@party_api.route('/<int:party_id>', methods=['PUT'])
@Auth.auth_required
def update_party(party_id):
    """
    Update a blogpost
    """
    req_data = request.get_json()
    post = PartyModel.get_one_party(party_id)
    if not post:
        return custom_response({'error': 'post not found'},404)
    data = party_schema.dump(post).data

    #this makes it so only the owner_id of the blog can edit
    if data.get('owner_id') != g.user.get('id'):
        return custom_response({'error': 'permission denied'}, 400)

    data, error = party_schema.load(req_data, partial=True)
    if error:
        return custom_response(error, 400)
    post.update(req_data)
    return custom_response(data, 200)


@party_api.route('/<int:party_id>', methods=['DELETE'])
@Auth.auth_required
def delete_party(party_id):
    """
    Delete a party
    """
    post = PartyModel.get_one_party(party_id)
    if not post:
        return custom_response({'error': 'post not found'}, 404)
    data = party_schema.dump(post).data

    if data.get('owner_id') != g.user.get('id'):
        return custom_response({'error': 'permission denied'}, 400)

    post.delete()
    return custom_response({'message': 'deleted'}, 204)
