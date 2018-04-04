import urllib.request
import datetime
from xml.etree import ElementTree
import matplotlib.pyplot as plt
import matplotlib.dates as dates

url = 'http://www.eurometeo.ru/belarus/minskaya-oblast/minsk/export/xml/data/'

r = urllib.request.urlopen(url)
data = r.read()
tree = ElementTree.fromstring(data)
temp_list, time_list = [], []

for step in tree.findall('./city/step'):
    time = step.find('datetime').text
    temp = step.find('temperature').text
    temp_list.append(temp)
    time_list.append(time)
    print(time, temp)

fig, ax = plt.subplots(figsize=(15, 10))
fmt = '%Y-%m-%d %H:%M:%S'
time_list = [datetime.datetime.strptime(i, fmt) for i in time_list]
ax.xaxis.set_major_formatter(dates.DateFormatter(fmt))
ax.plot_date(time_list, temp_list, linestyle='solid')
plt.xticks(time_list, rotation=30, ha='right')
ax.set_xlabel('time')
ax.set_ylabel('temperature')
plt.savefig('weather_history.png')
