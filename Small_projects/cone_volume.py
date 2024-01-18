# this program will calculate the volume of a cone using an input radius

# radius and height from user
R = float(input("What is the radius of the cone (in): "))
H = float(input("What is the height of the cone (in): "))
# calculating the volume of a cone
V = 3.14159 * (R**2) * (H / 3)

# Displaying the results
print( "A cone with a radius of", R, "inches and a height of", H, "inches, it will have a volume of", round(V, 2), "inches cubed.")
