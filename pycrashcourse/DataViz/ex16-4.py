import csv
import matplotlib.pyplot as plt
from datetime import datetime

with open('sitka_weather_2014.csv') as f:
    reader = csv.reader(f)
    header_row = next(reader)
    #for index, header in enumerate(header_row):
     #   print(index, header)

    dates, highs, lows = [], [], []
    for row in reader: 
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[7])
            low = int(row[9])
        except ValueError:
            print(current_date, 'No Data')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

fig = plt.figure(dpi = 128, figsize = (10,6))
plt.plot(dates, highs, c='blue', alpha = 0.5)
plt.plot(dates, lows, c= 'red', alpha = 0.5)
plt.fill_between(dates, highs, lows, facecolor ='blue', alpha = 0.1)

plt.title('Humidity Highs and Lows \n Sitka, Alaska, 2014', fontsize =24)
plt.xlabel('')
plt.ylabel('Humidity %', fontsize = 16)

plt.show()