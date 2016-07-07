"""
Displays data of timestamp against number of signatures


TODO:
    prettify graph:
        add title and stuff [ ]
        tidy up x axis labels [ ]
        sort out whitespace around graph [ ]
        add pointer and citation to when sigs got removed [ ]

    add date range options [*]

    investigate seaborn wrapper to make prettier [ ]


"""

import matplotlib.pyplot as plt
import matplotlib
import json

import datetime
import dateutil

import argparse

import ipdb


argparser = argparse.ArgumentParser()

argparser.add_argument("--jsonfile", help="json file to display, format is datestamp and sig_count",
        default="data/all.json")
argparser.add_argument("--from-time", help="optional field to display from specified datetime", 
        default=False)
argparser.add_argument("--to-time", help="optional field to display to specified datetime",
        default=False)

args = argparser.parse_args()

from_time = to_time = None

if args.from_time:
    from_time = dateutil.parser.parse(args.from_time)
if args.to_time:
    to_time = dateutil.parser.parse(args.to_time)


timestamps = []
sig_counts = []

with open(args.jsonfile, "r") as f:
    for jsonline in f:
        rawtimestamp, sig_count = json.loads(jsonline).popitem()
        
        timestamp = dateutil.parser.parse(rawtimestamp)

        if from_time and timestamp < from_time:
            continue

        if to_time and timestamp > to_time:
            continue

        timestamps.append(timestamp)
        sig_counts.append(int(sig_count.replace(",","")))




matplotlibtimestamps = matplotlib.dates.date2num(timestamps)

fig, ax = plt.subplots()

plt.plot_date(x=matplotlibtimestamps, y=sig_counts, xdate=True, ydate=False,
        markersize=1)
plt.ylim(ymin=0, ymax=4500000)

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





