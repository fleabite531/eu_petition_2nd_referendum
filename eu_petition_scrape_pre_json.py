import requests
from bs4 import BeautifulSoup
import time
import datetime

import argparse

import ipdb


PATH = "https://petition.parliament.uk/petitions/131215"


parser = argparse.ArgumentParser()
parser.add_argument("output_file", help="file to output to")
args = parser.parse_args()


while True:
    
    webpage = requests.get(PATH).text
    soup = BeautifulSoup(webpage)

    timestamp = datetime.datetime.now()

    sig_count = soup.find(class_="signature-count-number").get_text(strip=True)

    print("%s : %s" % (timestamp, sig_count))

    with open(args.output_file, 'a') as logfile:
        logfile.write("%s : %s \n" % (timestamp, sig_count))


    time.sleep(30)


