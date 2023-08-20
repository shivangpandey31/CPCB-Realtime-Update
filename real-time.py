import requests
import urllib.parse

def realtime_aqi(state, city, limit, string):

    limit = str(limit)
    string = urllib.parse.quote(string)

    req = requests.get('https://api.data.gov.in/resource/3b01bcb8-0b14-4abf-b6f2-c1bfd384ba69?api-key=579b464db66ec23bdd00000133cd04648bab44736a512df444a3cf72&format='+file_type+'&limit='+limit+'&filters%5Bstate%5D='+state+'&filters%5Bcity%5D='+city+'&filters%5Bstation%5D='+string)

    #req = requests.get('https://api.data.gov.in/resource/3b01bcb8-0b14-4abf-b6f2-c1bfd384ba69?api-key=579b464db66ec23bdd00000133cd04648bab44736a512df444a3cf72&format=csv&limit=100&filters%5Bstate%5D=Bihar&filters%5Bcity%5D=Patna&filters%5Bstation%5D=IGSC%20Planetarium%20Complex%2C%20Patna%20-%20BSPCB')
    url_content = req.content

    csv_file = open('real-time.csv', 'wb')
    csv_file.write(url_content)
    csv_file.close()

    print(string)

file_type  = 'csv'
state = 'Bihar'
city = 'Patna'
limit = '100'	
string = "IGSC Planetarium Complex, Patna - BSPCB"

realtime_aqi(state, city, limit, string)