# coding: utf-8
# Your code here!

import json
import requests


def get_api():
    url = 'URL'

    r = requests.get(url, {})

    return r.text


     

