import csv
from matplotlib import pyplot as plt
import numpy as py
filename = 'activity.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Generate Dictionary of dates : steps/interval
    daysDict = {}
    for row in reader:
        if row[1] not in daysDict:
            if not row[0] == 'NA':
                daysDict[row[1]] = [int(row[0])]
        else:
            if not row[0] == 'NA':
                daysDict[row[1]].append(int(row[0]))

    daysSum = daysDict
    # Using previous dictionary, make dictionary of dates : total steps
    for key in daysSum:
            daysSum[key] = sum(daysSum[key])
    print(daysSum.values(), daysSum.keys())

    dates, steps = [],[]
    for key in daysSum:
        dates.append(key)
        steps.append(daysSum[key])
    # Generate histogram from data gathered
    plt.plot(dates,steps,'b-')
    plt.plot(dates,steps,'r.')
    plt.xlabel('Dates')
    plt.ylabel('Steps')
    plt.show()

