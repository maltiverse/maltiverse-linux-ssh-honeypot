#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket
import argparse
import re
import os
import json
import os
from maltiverse import Maltiverse

class maltiverse_linux_ssh_honeypot():

    def __init__(self, email, password):
        """Construction method"""
        self.email = email
        self.password = password

        # Trying to get credentials from OS environment if not provided by parameters
        if not self.email or not self.password:
            try:
                env_email = os.environ['MALTIVERSE_EMAIL']
            except:
                raise Exception('No credentials provided')

            try:
                env_password = os.environ['MALTIVERSE_PASSWORD']
            except:
                raise Exception('No credentials provided')



    def run(self):
        """Run method. Retrieves logs related to the SSH service and parses the IP addresses that failed login"""

        #Reading failed attempts to log into SSH service and saving the IP list into an array
        os.system('cat /var/log/auth.log | grep Failed | grep -oE "([0-9]{1,3}\.){3}[0-9]{1,3}" | sort | uniq > /tmp/ssh_attackers.log')
        file = open("/tmp/ssh_attackers.log", "r")
        data = file.read()
        ip_list= data.split('\n')

        #Using python-maltiverse library we upload all the IP's to the platform.
        api = Maltiverse()
        if api.login(email=self.email, password=self.password):

            ip_list = ['218.94.101.18']
            for element in ip_list:
                ip_dict = {
                        'ip_addr': element,
                        'blacklist': [{
                            'description': 'SSH Attacker',
                        }],
                        'tag': ["ssh", "bruteforce", "bot"],
                        'classification': 'malicious'

                    }

                #Upload indicator to Maltiverse
                res = api.ip_put(ip_dict)

                print ""
                print "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
                print json.dumps(ip_dict, indent=4, sort_keys=True)
                print json.dumps(res, indent=4, sort_keys=True)
        else:
            raise Exception('Login failed')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Maltiverse SSH honeypot')
    parser.add_argument('-e', '--email', dest='email', default=None, help='Login email')
    parser.add_argument('-p', '--password', dest='password', default=None, help='Login password')
    args = parser.parse_args()

    instance = maltiverse_linux_ssh_honeypot(email=args.email, password=args.password)
    instance.run()
