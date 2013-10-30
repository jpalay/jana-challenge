#!/usr/bin/env python
import json
import os
import urllib2
import xml.etree.ElementTree as ET
from twilio.rest import TwilioRestClient

from settings import XML_LOC, XML_URL, ACCOUNT_SID, AUTH_TOKEN, NUM

def edit_xml():
    html = urllib2.urlopen('http://reddit.com/.json').read()
    d = json.loads(html)
    headline =  d['data']['children'][0]['data']['title']

    x = ET.parse(XML_LOC)
    x.findall('.//Say')[0].text = headline
    x.write(XML_LOC, encoding='UTF-9', xml_declaration=True)

def make_call():
    client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
    call = client.calls.create(url=XML_URL, to=NUM, IfMachine='Continue')

edit_xml()
make_call()
