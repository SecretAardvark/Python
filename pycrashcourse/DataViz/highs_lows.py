import csv
from matplotlib import pyplot as plt
from datetime import datetime

#Opens the datafile and reads the header row
filename = 'death_valley_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
   
    #Makes lists of the data we want to display.
    dates, highs, lows = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high =int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, 'missing data')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)
   
    """for row in reader:
        current_date = datetime.strptime(row[0], "%Y-%m-%d")
        dates.append(current_date)

        high = int(row[1])
        highs.append(high)

        low = int(row[3])
        lows.append(low)"""

#Sets the window size and plots our data. 
fig = plt.figure(dpi = 128, figsize = (10,6))
plt.plot( dates, highs, c='red', alpha = 0.5)
plt.plot(dates, lows, c= 'blue', alpha =0.5)
plt.fill_between(dates, highs, lows, facecolor = 'blue', alpha =0.1)

#Sets the title and axis labels for the graph
plt.title("Daily high and low temperatures - 2014\nDeath Valley, CA", fontsize = 20)
plt.xlabel('', fontsize = 16)
#Formats the dates to display diagonally on the x axis
fig.autofmt_xdate()
plt.ylabel("Temperature(F)", fontsize =16)
plt.tick_params(axis = 'both', which = 'major', labelsize = 16)

#Builds and displays the finished graph
plt.show()