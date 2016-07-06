import requests
from bs4 import BeautifulSoup
import time
import datetime

import json

import argparse

import ipdb


PATH = "https://petition.parliament.uk/petitions/131215"

SLEEPTIME = 30


parser = argparse.ArgumentParser()
parser.add_argument("output_file", help="file to output to")
args = parser.parse_args()


while True:
    
    timestamp = datetime.datetime.now()

    try:
        webpage = requests.get(PATH).text
    except requests.ConnectionError:
        print("Network error. Retyring...")
        time.sleep(SLEEPTIME)
        continue

    soup = BeautifulSoup(webpage)

    sig_count = soup.find(class_="signature-count-number")

    # check if not None type ie has found tag in webpage otherwise would throw exception
    if sig_count is not None:
        sig_count = sig_count.get_text(strip=True)
    else:
        print("signature-count-number tag not found in webpage. retrying")
        time.sleep(SLEEPTIME)
        continue


    sig_count = sig_count.replace("signatures","")

    print("%s : %s" % (timestamp, sig_count))

    with open(args.output_file, 'a') as logfile:
        logfile.write(json.dumps({
            timestamp.isoformat() : sig_count
        }) + "\n")

        # logfile.write("%s : %s \n" % (timestamp, sig_count))


    time.sleep(SLEEPTIME)


