import threading

def myFun():
    print("Time starts now")
    
    print("Time ends now")

timer = threading.Timer(15.0, myFun)

timer.start()
