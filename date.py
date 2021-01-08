from datetime import datetime

date_string = "21 June, 2018"
print("date_string =", date_string)

date_object = datetime.strptime(date_string, "%d %B, %Y")
print("date_object =", date_object)


date_object = datetime.strptime('Nov 16, 2020', "%b %d, %Y")
print("date_object =", date_object)