import csv 
from matplotlib import pyplot as plt
from datetime import datetime

filename = '538impeachment.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    dates, yes, no = [], [], [],
    for row in reader: 
        current_date = datetime.strptime(row[1],'%m/%d/%Y'  )
        dates.append(current_date)
        dates = sorted(dates)
        for datetime in dates: 
            this_year = []
            if datetime.year == 2019:
                this_year.append(datetime)

                Yes = float(row[10])
                yes.append(Yes)

                No = float(row[11])
                no.append(No)
            this_year = sorted(this_year)


plt.plot(this_year, yes, color ='blue', alpha = 0.5)
plt.plot(this_year, no, color='red', alpha = 0.5)
plt.show()
