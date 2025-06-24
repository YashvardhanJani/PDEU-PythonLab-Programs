# 12. Given the coordinates (x,y) of center of a circle and its radius, determine whether a point lies inside the circle, on the circle or outside the circle. (Hint: Use sqrt( ), pow( ) )

import math

# Function to check point position relative to the circle
def point_circle_position(h, k, r, x_p, y_p):
   
    distance = math.sqrt((x_p - h)**2 + (y_p - k)**2)
    
    if distance < r:
        return "\nThe point lies inside the circle."
    elif distance == r:
        return "\nThe point lies on the circle."
    else:
        return "\nThe point lies outside the circle."
    

h, k = map(float, input("Enter the coordinates of the circle's center (h k) : ").split())
r = float(input("Enter the radius of the circle : "))
x_p, y_p = map(float, input("Enter the coordinates of the point (x y) : ").split())

result = point_circle_position(h, k, r, x_p, y_p)
print(result)