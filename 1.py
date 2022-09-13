
print("Welcome to Tip Calculator")

total_bil=input("What was the total bill:")
total_bill=float(total_bil)
tip_percent=input("What percentage tip would you like to give? 10, 12 or 15:\n")
tip_percent_as_int=int(tip_percent)
tip_percentage= tip_percent_as_int/100
num_of_sharehold=input("How many people to split the bill: ")
no_of_shares= int(num_of_sharehold)

tips= round((total_bill / no_of_shares)*tip_percentage,2)
#rounding off to two decimal points
tips1="{:.2f}".format(tips)


print("Each person should pay: Rs. " + str(tips1))
