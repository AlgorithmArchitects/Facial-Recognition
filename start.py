import PersonInfo
from pip._vendor.distlib.compat import raw_input
stop = False
while not stop:
    arguments = raw_input("Enter your command now:")
    arguments = set(arguments.split(' '))
    if(arguments == {"exit"} or arguments == {"quit"} or arguments == {"stop"}):
        print ("Thank you for using Algorithm-Architects' Facial Recognition System!")
        stop = True
    else:
        #process command
        raise NotImplementedError("process command")
    