#!/usr/bin/python3.8
# coding=utf-8
"""
Icinga API Client
"""
import requests
import pprint

API_URI = "https://icinga:5665/v1"
API_AUTH = ('root', 'icinga')


def get_status(object: str):
    r = requests.get(API_URI + '/objects/' + object, auth=API_AUTH)
    result_json = r.json()['results']
    return_dict = {}
    for result in result_json:
        status_json = result['attrs']
        name = status_json['name']
        state = int(status_json['last_check_result']['state'])
        output = status_json['last_check_result']['output']
        return_dict[name] = {'state': state, 'output': output}
    return return_dict


if __name__ == "__main__":
    pprint.pprint(get_status('hosts'), width=200)
    pprint.pprint(get_status('services'), width=200)
