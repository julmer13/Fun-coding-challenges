#call in things
from fractions import Fraction
import math
import os

#def things
def is_decimal(num):
    #Check if a number is a decimal.
    return isinstance(num, float) and num % 1 != 0

def convert_to_fraction(num):
    #Convert a decimal to a fraction if needed
    return Fraction(num).limit_denominator() if is_decimal(num) else num

#clear screen
os.system('cls' if os.name == 'nt' else 'clear')

#make it loop
while True:

#housekeeeping
    start = "n"


    while start.lower() != "y":
        #get the points
        x1 = input("\n" + "what is the x of the first point: ")
        y1 = input("what is the y of the first point: ")
        x2 = input("what is the x of the second point: ")
        y2 = input("what is the y of the second point: ")
        x3 = input("what is the x of the third point: ")
        y3 = input("what is the y of the third point: ")

        #print points
        start = input( "\n" + "are these the three points you want to use:" + "\n" + "(" + x1 + "," + y1 + ")" + "\n" + "(" + x2 + "," + y2 + ")" + "\n" + "(" + x3 + "," + y3 + ")" + "\n" + "\n" +  "y/n: " )

    #turn all points to ints
    x1 = int(x1)
    x2 = int(x2)
    x3 = int(x3)
    y1 = int(y1)
    y2 = int(y2)
    y3 = int(y3)

    #find circucenter
    find_circumcentrer = input("\n" + "do you what to find the circucenter y/n: ")
    if find_circumcentrer.lower() == "y":
        # Calculate midpoints
        midpoint1_x = (x1 + x2) / 2
        midpoint1_y = (y1 + y2) / 2
        midpoint2_x = (x2 + x3) / 2
        midpoint2_y = (y2 + y3) / 2

        # Find slopes of sides
        slope_AB = (y2 - y1) / (x2 - x1) if (x2 - x1) != 0 else None
        slope_BC = (y3 - y2) / (x3 - x2) if (x3 - x2) != 0 else None

        # Find perpendicular slopes
        perp_slope_1 = -1 / slope_AB if slope_AB is not None else None
        perp_slope_2 = -1 / slope_BC if slope_BC is not None else None

        # Line 1 equation
        if perp_slope_1 is not None:
            b1 = midpoint1_y - perp_slope_1 * midpoint1_x
        else:
            b1 = midpoint1_x  # Vertical line x = b1

        # Line 2 equation
        if perp_slope_2 is not None:
            b2 = midpoint2_y - perp_slope_2 * midpoint2_x
        else:
            b2 = midpoint2_x  # Vertical line x = b2

        # Find intersection of the two lines
        if perp_slope_1 is not None and perp_slope_2 is not None:
            # Solve for x and y
            x_circumcenter = (b2 - b1) / (perp_slope_1 - perp_slope_2)
            y_circumcenter = perp_slope_1 * x_circumcenter + b1
        elif perp_slope_1 is None:
            # Line 1 is vertical
            x_circumcenter = b1
            y_circumcenter = perp_slope_2 * x_circumcenter + b2
        elif perp_slope_2 is None:
            # Line 2 is vertical
            x_circumcenter = b2
            y_circumcenter = perp_slope_1 * x_circumcenter + b1

        #find faction
        x_circumcenter = convert_to_fraction(x_circumcenter)
        y_circumcenter = convert_to_fraction(y_circumcenter)

        #print the product
        print("\n" + "the circucenter is:" + "(" + str(x_circumcenter) + "," + str(y_circumcenter) + ")")

    find_incenter = input("\n" + "do you want to find the incenter y/n: ")
    #find incenter
    if find_incenter.lower() == "y" :
        #find the distance for all the sides
        distance_a = math.sqrt((x2 - x3) ** 2 + (y2 - y3) ** 2)
        distance_b = math.sqrt((x1 - x3) ** 2 + (y1 - y3) ** 2)
        distance_c = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

        #find incenter_x
        incenter_x = ((distance_a * x1) + (distance_b * x2) + (distance_c * x3)) / (distance_a + distance_b + distance_c)

        #find incenter_y
        incenter_y = ((distance_a * y1) + (distance_b * y2) + (distance_c * y3)) / (distance_a + distance_b + distance_c)

        #find faction
        incenter_x = convert_to_fraction(incenter_x)
        incenter_y = convert_to_fraction(incenter_y)
        #print the product
        print("\n" + "the incenter is:" + "(" + str(incenter_x) + "," + str(incenter_y) + ")")

    #find the centroid
    find_centriod = input("\n" + "do you want to know the centriod y/n: ")
    if find_centriod == "y":
        #find totals
        total_x = x1 + x2 + x3
        total_y = y1 + y2 + y3
        final_x = (total_x / 3)
        final_y = (total_y / 3)
        final_x = convert_to_fraction(final_x)
        final_y = convert_to_fraction(final_y)

        #print the product
        print("\n" + "the centroid is:" + "(" + str(final_x) + "," + str(final_y) + ")")

    find_orthocenter = input("\n" + "Do you want to find the orthocenter y/n: ")  
    
    if find_orthocenter.lower() == "y":  
        # Calculate the slope of line AB and AC
        slope_AB = (y2 - y1) / (x2 - x1) if x2 != x1 else float('inf')
        slope_AC = (y3 - y1) / (x3 - x1) if x3 != x1 else float('inf')

        # Calculate the slopes of the altitudes
        if slope_AB != 0:
            slope_altitude_C = -1 / slope_AB
        else:
            slope_altitude_C = float('inf')
            
        if slope_AC != 0:
            slope_altitude_B = -1 / slope_AC
        else:
            slope_altitude_B = float('inf')
        
        # Calculate the intercepts of the altitudes
        if slope_altitude_C != float('inf'):
            intercept_C = y3 - slope_altitude_C * x3
        else:
            intercept_C = None  # The altitude from C is a vertical line
        
        if slope_altitude_B != float('inf'):
            intercept_B = y2 - slope_altitude_B * x2
        else:
            intercept_B = None  # The altitude from B is a vertical line
        
        # Find the orthocenter by solving the equations of two altitudes
        if slope_altitude_C == float('inf'):
            # Altitude from C is vertical
            x_orthocenter = x3
            y_orthocenter = slope_altitude_B * x_orthocenter + intercept_B
        elif slope_altitude_B == float('inf'):
            # Altitude from B is vertical
            x_orthocenter = x2
            y_orthocenter = slope_altitude_C * x_orthocenter + intercept_C
        else:
            # Solve for intersection point
            x_orthocenter = (intercept_B - intercept_C) / (slope_altitude_C - slope_altitude_B)
            y_orthocenter = slope_altitude_C * x_orthocenter + intercept_C

        x_orthocenter = convert_to_fraction(x_orthocenter)
        y_orthocenter = convert_to_fraction(y_orthocenter)
    
        # Print the result  
        print("\n" + "The orthocenter is: (" + str(x_orthocenter) + ", " + str(y_orthocenter) + ")" + "\n")
