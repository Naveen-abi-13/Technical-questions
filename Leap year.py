Year=int(input("Enter a year need to check:"))
if (Year%4==0 and Year%100!=0 ) or (Year%400==0):
    print(Year,"is a leep year")
else:
    print(Year,"is not a leep year")