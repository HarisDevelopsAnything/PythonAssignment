import datetime
def ds(date_str1, date_str2):
    dateformat = '%d-%m-%Y'
    date1 = datetime.datetime.strptime(date_str1, dateformat)
    date2 = datetime.datetime.strptime(date_str2, dateformat)
    date_diff = date2 - date1
    return date_diff
date_str1 = input("Enter the from date in DD-MM-YYYY: ")
date_str2 = input("Enter the to date in DD-MM-YYYY: ")
sub= ds(date_str1, date_str2)
print("Difference between the dates:", sub.days, "days")