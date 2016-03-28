from flask import jsonify, request, abort

from . import api
from .. import db
from ..models.spaces import Spaces
from ..schemas.spaces import space_schema, spaces_schema

@api.route('/spaces', methods=['GET'])
def get_spaces():
  spaces = Spaces.query.all()
  return jsonify(spaces=spaces_schema.dump(spaces).data)


@api.route('/spaces/<int:id>', methods=['GET'])
def get_space(id):
  space = Spaces.query.get(id)
  if not space:
    abort(404)
  return jsonify(space_schema.dump(space).data)


@api.route('/spaces', methods=['POST'])
def create_spaces():
  space = Spaces(name=request.form['name'])
  db.session.add(space)
  db.session.commit()
  return '', 201


@api.route('/spaces/<int:id>', methods=['PUT'])
def update_spaces(id):
  space = Spaces.query.get(id)
  space.name = request.form['name']
  db.session.commit()
  return '', 204


@api.route('/spaces/<int:id>', methods=['DELETE'])
def delete_spaces(id):
  if not id:
    abourt(400)

  space = Spaces.query.get(id)
  if not space:
    abort(404)

  db.session.delete(space)
  db.session.commit()
  return '', 204