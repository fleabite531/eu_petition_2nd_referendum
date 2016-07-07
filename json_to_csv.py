
import json
import argparse

import ipdb

def main():
    
    argparser = argparse.ArgumentParser()

    argparser.add_argument("json_file", help="json file to import from")
    argparser.add_argument("csv_file", help="csv file to export to")

    args = argparser.parse_args()

    json_file = open(args.json_file, "r")
    csv_file = open(args.csv_file, "w")


    for jsonline in json_file:
        line = json.loads(jsonline).popitem()
        datestamp, sig_count = line
        sig_count = sig_count.replace(",", "")
        csv_file.write(datestamp + "," + sig_count + "\n")

    json_file.close()
    csv_file.close()




if __name__ == "__main__":
    main()
