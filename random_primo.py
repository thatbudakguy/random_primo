#!/usr/bin/env python

'''
random_primo.py - simple tool to return random items from primo as JSON
'''

import urllib
import urllib2
import sys
import random
import json
import argparse

parser = argparse.ArgumentParser(description='Return random Primo records as JSON.', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('-p', metavar='url', type=str, help='url of primo instance', default='http://primo.lclark.edu/')
parser.add_argument('-i', metavar='code', type=str, help='institution code', default='LCC')
parser.add_argument('-n', metavar='number', type=int, help='number of items to return', default=100)
parser.add_argument('-r', metavar='type', type=str, default='book', help='resource type to return', choices=['book','ebook','article'])
args = parser.parse_args()
args.k = random.randint(1,10000)

def main():
    '''perform cURL to Primo and process results'''
    webservices_url = 'PrimoWebServices/xservice/search/brief?'
    params = {
        'institution': args.i,
        'query': 'any,contains,' + args.r,
        'indx': args.k,
        'bulkSize': args.n,
        'lang': 'eng',
        'json': 'true'
    }
    url = args.p + webservices_url + urllib.urlencode(params)
    response = urllib2.urlopen(url).read()
    response_json = json.loads(response)
    docset = response_json['SEGMENTS']['JAGROOT']['RESULT']['DOCSET']['DOC']
    results = []
    for doc in docset:
        results.append(doc['PrimoNMBib']['record']['display'])
    filename = '_'.join([args.r, str(args.n), str(args.k)]) + '.json'
    output = open(filename, 'w')
    output.write(json.dumps(results))
    print "wrote " + filename
    sys.exit(0)

if __name__ == '__main__':
    main()
