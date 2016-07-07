import ipdb

from dateutil import parser
import time
import datetime

import json

import re


inputfile = open("data/outputstruct", "r")
outputfile = open("data/outputstruct.json", "a")

sig_count_re = re.compile("[0-9,]+signatures")


for inputline in inputfile:
    if len(inputline) < 1:
        continue

    sig_count_raw = sig_count_re.search(inputline)
    sig_count = sig_count_raw.string[sig_count_raw.start():sig_count_raw.end()-10]
    sig_count = sig_count.replace(",", "")
    sig_count = sig_count.replace("signatures", "")

    datestring = sig_count_raw.string[:sig_count_raw.start()]

    numbers_re = re.compile("[0-9]+")
    
    time_list = numbers_re.findall(datestring)
    
    timestamp = datetime.datetime(*map(int, time_list[:-3]))

    outputfile.write(json.dumps({
        timestamp.isoformat() : sig_count
    }) + "\n")



inputfile.close()
outputfile.close()
    
    

