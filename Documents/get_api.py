# coding: utf-8
# Your code here!

import json
import requests


def get_api():
    url = 'http://hack1.dstn.club/dataspider/trigger/path'

    r = requests.get(url, {})

    return r.text


     

