# this program will estimate the population of the US based
# off a specific number of births/deaths/immigrations in the coming years.

# asking the user for a number of years
Y = int(input("how many years away would you like to estimate population? "))

# converting years to seconds
D = Y * 365
H = D * 24
M = H * 60
S = M * 60

# Calculating population based of seconds and variables given by Angstat
Pop = 328000000 + (S / 8) - (S / 12) + (S / 33)

# Printing out the data
print("After", Y, "years, the population of the United States will be", int(Pop), "people.")

