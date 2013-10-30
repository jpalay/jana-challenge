#!/usr/bin/env python
import json
import os
import urllib2
import xml.etree.ElementTree as ET
from twilio.rest import TwilioRestClient

import settings

def update_xml():
    # reddit top story
    html = urllib2.urlopen('http://reddit.com/.json').read()
    d = json.loads(html)
    headline =  d['data']['children'][0]['data']['title']

    x = ET.parse(settings.XML_LOC)

    # Get all Say elements with id headline (xpath wouldn't work)
    say = [elt for elt in x.findall('.//Say') if elt.attrib.get('id', None) == 'headline']
    for elt in say:
        elt.text = headline
    # edit xml file
    x.write(settings.XML_LOC, encoding='UTF-8')

def make_call():
    client = TwilioRestClient(settings.ACCOUNT_SID, settings.AUTH_TOKEN)
    call = client.calls.create(url=settings.XML_URL, to=settings.NUM, from_='415-723-4236', IfMachine='Continue')

update_xml()
make_call()
