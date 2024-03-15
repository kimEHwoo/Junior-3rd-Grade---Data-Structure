years = input("Please enter number of years: ")
months = input("Please enter number of months: ")

days = int(years) * 365 + int(months) * 30

result = "{} years and {} months is equal with {}".format(years, months, str(days))
print(result)