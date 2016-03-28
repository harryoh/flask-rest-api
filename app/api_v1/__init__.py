from flask import Blueprint


api = Blueprint('api_v1', __name__)


# Import any endpoints here to make them available
#from . import dis_endpoint, dat_endpoint

from . import spaces
