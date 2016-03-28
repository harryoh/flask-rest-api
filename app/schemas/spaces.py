from .. import ma
from ..models.spaces import Spaces


class SpacesSchema(ma.ModelSchema):

    class Meta:
        model = Spaces


space_schema = SpacesSchema()
spaces_schema = SpacesSchema(many=True)
