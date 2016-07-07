import matplotlib.pyplot as plt
import matplotlib
import json

import datetime
import dateutil

import argparse

import ipdb

filename = "all.json"


argparser = argparse.ArgumentParser()

argparser.add_argument("--jsonfile", help="json file to display, format is datestamp and sig_count",
        default="all.json")
argparser.add_argument("--from", help="optional field to display from specified datetime", 
        default=False)
argparser.add_argument("--to", help="optional field to display to specified datetime",
        default=False)

args = argparser.parse_args()

timestamps = []
sig_counts = []

with open(args.jsonfile, "r") as f:
    for jsonline in f:
        timestamp, sig_count = json.loads(jsonline).popitem()
        
        timestamps.append(dateutil.parser.parse(timestamp))
        sig_counts.append(int(sig_count.replace(",","")))


matplotlibtimestamps = matplotlib.dates.date2num(timestamps)

fig, ax = plt.subplots()

plt.plot_date(x=matplotlibtimestamps, y=sig_counts, xdate=True, ydate=False,
        markersize=1)
plt.ylim(ymin=0, ymax=4500000)

# major_formatter = matplotlib.dates.DateFormatter('%d/%m/%y %h:%m:%s')
major_formatter = matplotlib.dates.DateFormatter('%d/%m/%y')
minor_formatter = matplotlib.dates.DateFormatter('%H')

ax.xaxis.set_major_locator(matplotlib.dates.DayLocator(
    bymonthday=range(1,32), interval=1, tz=None))
ax.xaxis.set_minor_locator(matplotlib.dates.HourLocator(
    byhour=[6,12,18]))

ax.xaxis.set_major_formatter(major_formatter)
ax.xaxis.set_minor_formatter(minor_formatter)

# labels = ax.get_xticklabels()
# plt.setp(labels, rotation=30, fontsize=10)

plt.xticks(rotation='vertical')

plt.show()





