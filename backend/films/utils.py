import json
from http.client import HTTPException

import requests
import re

HTTP_GET = "get"


def call_url(url, method=HTTP_GET):
    response = getattr(requests, method)(url)
    if response.status_code != 200:
        raise HTTPException(f"External API responded with {response.status_code}")
    data_dict = json.loads(response.content)
    return data_dict


def extract_uuid_v4(text):
    re_uuid = re.compile(
        "[0-9A-F]{8}-[0-9A-F]{4}-[4][0-9A-F]{3}-[89AB][0-9A-F]{3}-[0-9A-F]{12}", re.I
    )
    uuids = re_uuid.findall(text)
    if len(uuids) != 1:
        raise ValueError(f"Expected 1 uuid in text found {uuids}. Input: {text}")
    return uuids[0]
