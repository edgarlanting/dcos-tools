#!/usr/bin/env python3
import sys
import os
import subprocess
import json
import requests

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def get_dcos_url_from_cli():
    res = subprocess.run(["dcos", "config", "show", "core.dcos_url"], shell=False, stdout=subprocess.PIPE)
    return res.stdout.strip().decode("utf-8")

def get_dcos_token_from_cli():
    res = subprocess.run(["dcos", "config", "show", "core.dcos_acs_token"], shell=False, stdout=subprocess.PIPE)
    return res.stdout.strip().decode("utf-8")

if __name__ == "__main__":
    url = get_dcos_url_from_cli()
    token = get_dcos_token_from_cli()
    combined_json = list()
    for app_filename in sys.argv[1:]:
        with open(app_filename) as app_file:
            data = app_file.read()
            app_def = json.loads(data)
            combined_json.append(app_def)
    response = requests.put(url + "/service/marathon/v2/apps", json=combined_json, headers={"Authorization": "token=%s" % token}, verify=False)
    if not response.ok:
        print(response.text)
    print(response.json())
