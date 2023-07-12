import datetime
import logging
import threading

import json

log = logging.getLogger()

uuid_lock = threading.Lock()
STATUS_SUCCESS = "SUCCESS"
DATE_PATTEN = '%Y-%m-%d %H:%M:%S'


class LCJSONEncoder(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime(DATE_PATTEN)
        else:
            return json.JSONEncoder.default(self, obj)


def dict_response(
    data=None,
    status=STATUS_SUCCESS,
    description=None,
    mtype=None,
    wait_callback=True,
    task=None,
    page=None,
    flag=None
):
    if not description:
        description = ''

    if status != STATUS_SUCCESS or not task:
        wait_callback = False

    if mtype is None and data is not None:
        if isinstance(data, list):
            if data:
                mtype = data[0].__class__.__name__
            else:
                mtype = None
        else:
            mtype = data.__class__.__name__

    info = {'DATA': data, 'TYPE': mtype, 'OPT_STATUS': status, 'DESCRIPTION': description}
    if wait_callback:
        info['WAIT_CALLBACK'] = True
        info['TASK'] = task

    if page:
        info['PAGE'] = page
    if flag:
        info['FLAG'] = flag
    return info


def json_response(
    data=None,
    status="SUCCESS",
    description=None,
    type=None,
    wait_callback=False,
    task=None,
    page=None,
    flag=None
):
    return LCJSONEncoder().encode(dict_response(data, status, description, type, wait_callback, task, page, flag))
