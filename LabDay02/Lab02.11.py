# 11. Given three points (x1,y1), (x2,y2) and (x3,y3), check if all the three points fall on one straight line. (check points are Collinear or not.)

def check_points_collinear(x1, y1, x2, y2, x3, y3):

    return (y2 - y1) * (x3 - x2) == (y3 - y2) * (x2 - x1)

x1, y1 = map(float, input("Enter coordinates of point 1 (x1 y1): ").split())
x2, y2 = map(float, input("Enter coordinates of point 2 (x2 y2): ").split())
x3, y3 = map(float, input("Enter coordinates of point 3 (x3 y3): ").split())

if check_points_collinear(x1, y1, x2, y2, x3, y3):
    print("\nAll the three points are fall on one straight line (Points are Collinear).")
else:
    print("\nAll the three points are not fall on one straight line (Points are not Collinear).")


