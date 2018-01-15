#!/usr/bin/env python

import os

import httplib

import socket

KEY_FILE = os.getcwd() + '/CA/private/client.key'

CERT_FILE = os.getcwd() + '/CA/client.crt'

GET = "GET"

conn = httplib.HTTPSConnection('0.0.0.0', '4444', cert_file=CERT_FILE)

conn.request(GET, "/this.txt")

response = conn.getresponse()

print response.status, response.reason, response.read()

conn.close()