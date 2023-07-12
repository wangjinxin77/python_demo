import flask

from flask import Response

from api_utils import json_response

# ========= HTTP CODE ===========
HTTP_OK = 200
HTTP_POST_OK = 201
HTTP_DEL_OK = 204
HTTP_REDIRECT = 300
HTTP_FORBIDDEN = 403
HTTP_NOT_FOUND = 404
HTTP_BAD_REQUEST = 400
HTTP_SERVER_ERROR = 500

bp = flask.Blueprint('module_name', __name__, url_prefix="/v1")


@bp.route("/info", methods=["GET"])
def info_get():
    """
    @apiGroup CmdbExporterFull
    @apiVersion 1.0.0
    @api {get} /v1/info  01. 获取info

    @apiSuccessExample {json} Success-Response:
    {
        "OPT_STATUS": "SUCCESS"
        "DESCRIPTION": "",
        "DATA": {
            "info": "welcome to call info api"
        }
    }
    """
    data = json_response(data={"info": "welcome to call info api"})
    return Response(data, content_type='application/json; charset=utf-8'), HTTP_OK
