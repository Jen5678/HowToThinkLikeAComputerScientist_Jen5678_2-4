months = ["January", "Febuary", "March",
          "April", "May", "June", 
          "July", "August", "September",
          "November", "December"]

msg = ""
for i in range(len(months)):
    if (i != 0 ):
        msg += "One month of the year is "
    msg += str(months[i])
print(msg + "") 