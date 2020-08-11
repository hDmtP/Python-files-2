import time
from covid import Covid
starTime=time.time()
covid = Covid()   
cases1=covid.get_status_by_country_name("india")
for x in cases1:
    print(x, ":", cases1[x])

    
cases2=covid.get_status_by_country_name("us")
for x in cases2:
    print(x, ":", cases2[x])

endTime=time.time()    

timelapsed = endTime - starTime

print("timelapsed:", timelapsed)


