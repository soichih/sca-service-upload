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

products = []

if config["type"] == "bio/fasta":
    #create different products for each fasta file
    #also, for each file, "guess" data type (nucl, or prot)
    for file in config["files"]:
        print file["filename"]
        with open(file["filename"], "r") as f:
            count=0
            prot_count=0
            while True:
                line = f.readline()
                if line == '':
                    break
                if line[0] == '>':
                    continue 
                count+=1
                if count > 100:
                    break
                prots = set('BDEFHIJKLMNOPQRSUVWXYZ')
                if any((c in prots) for c in line.upper()):
                    prot_count+=1

            per=prot_count/count*100
            print "chance of this sequence being protein sequence: ",per
            if per > 99.9:
                file["type"] = "prot"
            else:
                file["type"] = "nucl"
            
        #just store all files as input
        products.append({'type': config["type"], 'fasta': file})
else:
    #just store all files as input
    products.append({'type': config["type"], 'files': config["files"]})

with open('products.json', 'w') as out:
    json.dump(products, out)


