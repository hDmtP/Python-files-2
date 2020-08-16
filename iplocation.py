
# import requests

# res = requests.get('https://ipinfo.io/')
# data = res.json()
# print(data)

import geoip2.database
import socket as s
import winsound
print("Enter the targeted website url:\n")
host = input()
print(f"IP address of {host} is: {s.gethostbyname(host)}\n")
reader = geoip2.database.Reader(r'C:\Users\user\Downloads\GeoLite2-City_20200814\GeoLite2-City.mmdb')
response = reader.city(s.gethostbyname(host))

fr=4500
d=1500
winsound.Beep(fr, d)
print("Fetching Resources......\n")
fr=1500
d=2000
winsound.Beep(fr, d)
print("Fetching Targated database.......\n")
fr=8500
d=2500
winsound.Beep(fr, d)
print("*****FORKED SUCCESSFULLY*****\n")


print("Country iso code:",response.country.iso_code)
print("Country:",response.country.name)
print("Zip Code:",response.postal.code)
print("State:",response.subdivisions.most_specific.name) 
print("City:",response.city.name)
print("Latitude:",response.location.latitude)
print("Longitude:",response.location.longitude)



