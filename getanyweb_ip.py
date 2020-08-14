
import socket as s
print("Enter the targeted website url\n")
host = input()
print(f"IP address of {host} is: {s.gethostbyname(host)}")

# gethostname ---> to know your ip address
'''
host = s.gethostname()
YourIPadd = s.gethostbyname(host)
print(YourIPadd)
'''