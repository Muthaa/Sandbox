from flask import Blueprint

blueprint = Blueprint(
    'recorder_blueprint',
    __name__,
    url_prefix=''
)
