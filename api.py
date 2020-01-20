#!/usr/bin/python2ve
# coding=utf-8
"""
Icinga API Client
"""
import requests
import pprint
import socket

FQDN = socket.getfqdn()
API_URI = "https://{0}:5665/v1".format(FQDN)
API_AUTH = ('root', 'icinga')
API_CERT = ("/var/lib/icinga2/certs/{0}.crt".format(FQDN), "/var/lib/icinga2/certs/{0}.key".format(FQDN))


def get_status(object: str):
    r = requests.get(API_URI + '/objects/' + object, cert=API_CERT)
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
    # /v1/actions/reschedule-check -d '{ "type": "Service", "filter": "service.name==\"$1\"" }'

