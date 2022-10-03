
# ******************************
# Make your Code
# ******************************


# Requirement
# No need to use list
# All input values are taken one by one separatively.
###
long = "a"
shor = "asdiugfqowudiqyhvwpfiquwjhdihv"
while True:
 string = str(input()) 
 if string == "stop" or string == "STOP":
    break
 if len(string)> len(long):
    long = string
 if len(string)< len(shor):
    shor = string
print(long+" " +shor)