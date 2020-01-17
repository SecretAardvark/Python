import csv
import matplotlib.pyplot as plt
from datetime import datetime

with open('sitka_weather_2014.csv') as f:
    reader = csv.reader(f)
    header_row = next(reader)
    #for index, header in enumerate(header_row):
     #   print(index, header)

    dates, rain = [], []
    for row in reader: 
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            Rain = float(row[19])
        except ValueError:
            print(current_date, 'No Data')
        else:
            dates.append(current_date)
            rain.append(Rain)

fig = plt.figure(dpi = 128, figsize = (10,6))
plt.plot(dates, rain, c='green')

plt.title('Rain in Sitka, Alaska, 2014', fontsize =24)
plt.xlabel('')
plt.ylabel('Rain in inches', fontsize = 16)

plt.show()