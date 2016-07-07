import matplotlib.pyplot as plt
import matplotlib
import json

import datetime
import dateutil

import ipdb

filename = "all.json"


jsonList = []

with open(filename, "r") as f:
    for line in f:
        jsonList.append(json.loads(line))


timestamps = []
sig_counts = []

for jsonDict in jsonList:
    timestamp , sig_count = jsonDict.popitem()

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





