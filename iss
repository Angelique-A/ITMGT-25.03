import json
import pandas as pd
import matplotlib.pyplot as plt
import requests
import time

interval = 10
points = 0
data = []

while points < 100:
    api = requests.get("http://api.open-notify.org/iss-now.json")
    
    if api.status_code == 200:
        apijson = api.json()
        long = float(apijson['iss_position']['longitude'])
        lat = float(apijson['iss_position']['longitude'])
        timeS = apijson['timestamp']
        
        data.append({'Time':timeS, 'Longitude':long, 'Latitude':lat})
        points += 1
        time.sleep(interval)
        
    else:
        print("error")
    
dataTable = pd.DataFrame(data)

plt.plot(dataTable['Latitude'], dataTable['Longitude'], marker = '.')
plt.title('International Space Station Location')
plt.xlabel('Latitude')
plt.ylabel('Longitude')
plt.grid(True)
plt.show()
