#!/usr/bin/python3.8
# coding=utf-8
"""
Icinga API Client
"""
import requests
import pprint

API_AUTH = ('root', 'icinga')

def get_object(object: str, basicauth: bool, host: str):
    API_URI = "https://{0}:5665/v1".format(host)
    if basicauth:
        r = requests.get(f'{API_URI}/objects/{object}', auth=API_AUTH)
    else:
        API_CERT = ("/var/lib/icinga2/certs/{0}.crt".format(host), "/var/lib/icinga2/certs/{0}.key".format(host))
        r = requests.get(f'{API_URI}/objects/{object}', cert=API_CERT)
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
    pprint.pprint(get_object('hosts'), width=200)
    pprint.pprint(get_object('services'), width=200)
    # /v1/actions/reschedule-check -d '{ "type": "Service", "filter": "service.name==\"$1\"" }'

