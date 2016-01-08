#!/usr/bin/env python

import logging
#logging.basicConfig(filename='run.log',level=logging.DEBUG)
#logging.debug('This message should go to the log file')
#logging.info('So should this')
#logging.warning('And this, too')

import json
import sys
import os

#load config.json
config_json=open("config.json").read()
config=json.loads(config_json)

#TODO..

product = {'type': config["type"], 'whaterver': 'test'}
with open('products.json', 'w') as out:
    json.dump([product], out)


