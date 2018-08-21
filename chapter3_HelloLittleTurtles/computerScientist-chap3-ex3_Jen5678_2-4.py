months = ["January", "Febuary", "March",
          "April", "May", "June", 
          "July", "August", "September",
          "November", "December"]

msg = months
for i in range(len(months)):
    if(not(i is 0)):
        msg =+ ","
    msg += i 
    print(msg  + "months")