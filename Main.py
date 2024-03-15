years = input("Please enter number of years: ")
months = input("Please enter number of months: ")

days = int(years) * 365 + int(months) * 30

result = years + " years and " + months + " months are equal with " + str(days) + " days"

print(result)