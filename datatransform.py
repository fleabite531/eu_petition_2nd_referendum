import ipdb

from dateutil import parser

import json

import re


inputfile = open("output", "r")
outputfile = open("first_few_days.json", "a")

sig_count_re = re.compile("[0-9,]+signatures")


for inputline in inputfile:
    if len(inputline) < 1:
        continue

    sig_count_raw = sig_count_re.search(inputline)
    sig_count = sig_count_raw.string[sig_count_raw.start():sig_count_raw.end()-10]
    sig_count = sig_count.replace(",", "")
    sig_count = sig_count.replace("signatures", "")

    datestring = sig_count_raw.string[:sig_count_raw.start() - 3]

    timestamp = parser.parse(datestring)

    outputfile.write(json.dumps({
        timestamp.isoformat() : sig_count
    }) + "\n")


inputfile.close()
outputfile.close()
    
    

